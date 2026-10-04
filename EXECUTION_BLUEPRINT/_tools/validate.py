#!/usr/bin/env python3
"""
Independent quality audit for the Sketch Design execution blueprint.

Checks the twelve conditions of PHASE 9 of the master prompt mechanically,
so the audit is reproducible rather than asserted:

  1. every declared file exists
  2. prompt IDs are unique
  3. a prompt's ID prefix matches the phase file it lives in
  4. every prereq references a prompt that exists
  5. the prompt dependency graph is acyclic
  6. the phase dependency graph is acyclic and consistent with prompt prereqs
  7. every requirement ID a prompt cites exists in requirements.tsv
  8. every requirement in requirements.tsv is covered by >= 1 prompt
  9. every phase has an entry condition and an exit condition
 10. every prompt carries the five Arabic explanation questions
 11. every prompt carries exactly one English executable code block binding to
     the operating contract, with all seven required sections
 12. no artifact claims READY / DONE / PRODUCTION-READY for the platform

Exit code 0 = clean. Non-zero = findings, listed on stderr.

Usage:  python3 EXECUTION_BLUEPRINT/_tools/validate.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASES_DIR = ROOT / "PHASES"
REGISTRY = ROOT / "_registry"

REQUIRED_DOCS = [
    "00-START-HERE.md",
    "01-DEEP-ANALYSIS.md",
    "02-EXECUTION-ROADMAP.md",
    "03-MASTER-EXECUTION-PROMPTS.md",
    "04-REQUIREMENTS-TRACEABILITY.md",
    "05-QUALITY-AND-VERIFICATION.md",
    "06-OPEN-DECISIONS.md",
]

REQUIRED_REGISTRY = [
    "requirements.tsv",
    "phases.tsv",
    "AGENT-OPERATING-CONTRACT.md",
]

ARABIC_QUESTIONS = [
    "ماذا سينفذ هذا الأمر؟",
    "لماذا نحتاجه؟",
    "ما المتطلبات السابقة؟",
    "ما النتيجة المتوقعة؟",
    "كيف نتحقق من نجاحه؟",
]

# Section names rather than letters: PHASE-16's conditional prompt legitimately
# inserts a STOP CONDITION section, shifting the letters.
REQUIRED_SECTIONS = [
    "IDENTITY",
    "OBJECTIVE",
    "CONTEXT",
    "EXECUTION INSTRUCTIONS",
    "DELIVERABLES",
    "VERIFICATION",
    "COMPLETION CONTRACT",
]

CONTRACT_BINDING = "EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md"

# Forbidden readiness claims about the platform. The source's own status
# vocabulary (DEFINED / DESIGNED / SPEC / UNVERIFIED / NOT RUN / ...) is fine;
# these words are not, because sheet 02 row 9 (ADR-008) forbids claiming
# readiness without evidence.
FORBIDDEN_CLAIMS = [
    r"\bis production[- ]ready\b",
    r"\bplatform is ready\b",
    r"\bfully (?:built|tested|implemented|verified)\b",
    r"\bPDPL[- ]compliant\b",
    r"\bZATCA[- ]compliant\b",
    r"\bcertified survey\b(?!\s*(?:\.|,)?\s*(?:disclaimer|declaration))",
]

findings: list[str] = []
notes: list[str] = []


def finding(msg: str) -> None:
    findings.append(msg)


def note(msg: str) -> None:
    notes.append(msg)


def read_tsv(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open(encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.lstrip().startswith("#") and ln.strip()]
    reader = csv.DictReader(lines, delimiter="\t")
    for row in reader:
        rows.append({(k or "").strip(): (v or "").strip() for k, v in row.items()})
    return rows


def parse_meta(block: str) -> dict[str, object]:
    meta: dict[str, object] = {}
    for line in block.strip().splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [x.strip() for x in inner.split(",") if x.strip()]
        else:
            meta[key] = val
    return meta


def main() -> int:
    # ---- 1. required files -------------------------------------------------
    for name in REQUIRED_DOCS:
        if not (ROOT / name).is_file():
            finding(f"[files] missing required document: {name}")
    for name in REQUIRED_REGISTRY:
        if not (REGISTRY / name).is_file():
            finding(f"[files] missing required registry file: _registry/{name}")

    if not (REGISTRY / "requirements.tsv").is_file() or not (REGISTRY / "phases.tsv").is_file():
        print("FATAL: registries missing; cannot continue", file=sys.stderr)
        for f in findings:
            print(f, file=sys.stderr)
        return 2

    requirements = read_tsv(REGISTRY / "requirements.tsv")
    phases = read_tsv(REGISTRY / "phases.tsv")

    req_ids = {r["req_id"] for r in requirements}
    if len(req_ids) != len(requirements):
        seen: set[str] = set()
        for r in requirements:
            if r["req_id"] in seen:
                finding(f"[requirements] duplicate req_id: {r['req_id']}")
            seen.add(r["req_id"])

    phase_ids = [p["phase_id"] for p in phases]
    phase_set = set(phase_ids)
    if len(phase_set) != len(phase_ids):
        finding("[phases] duplicate phase_id in phases.tsv")

    # ---- 9. every phase has entry + exit ----------------------------------
    for p in phases:
        if not p.get("entry_condition"):
            finding(f"[phases] {p['phase_id']} has no entry_condition")
        if not p.get("exit_condition"):
            finding(f"[phases] {p['phase_id']} has no exit_condition")
        for dep in [d.strip() for d in p.get("depends_on", "").split(",") if d.strip() and d.strip() != "-"]:
            if dep not in phase_set:
                finding(f"[phases] {p['phase_id']} depends_on unknown phase {dep}")

    # ---- phase dependency graph acyclic -----------------------------------
    phase_deps = {
        p["phase_id"]: [
            d.strip()
            for d in p.get("depends_on", "").split(",")
            if d.strip() and d.strip() != "-"
        ]
        for p in phases
    }
    if cycle := find_cycle(phase_deps):
        finding(f"[phases] dependency cycle: {' -> '.join(cycle)}")

    # ---- parse phase files -------------------------------------------------
    phase_files = sorted(PHASES_DIR.glob("PHASE-*.md"))
    if not phase_files:
        finding("[files] no PHASES/PHASE-*.md files found")

    prompts: dict[str, dict] = {}
    order: list[str] = []
    file_phase: dict[str, str] = {}

    for pf in phase_files:
        text = pf.read_text(encoding="utf-8")
        pm = re.search(r"<!--\s*phasemeta\s*(.*?)-->", text, re.S)
        if not pm:
            finding(f"[{pf.name}] missing <!-- phasemeta --> block")
            continue
        phase_meta = parse_meta(pm.group(1))
        pid = str(phase_meta.get("id", ""))
        if pid not in phase_set:
            finding(f"[{pf.name}] phasemeta id {pid!r} is not in phases.tsv")
        if pid != pf.stem:
            finding(f"[{pf.name}] phasemeta id {pid!r} does not match filename")
        file_phase[pf.name] = pid

        blocks = list(re.finditer(r"<!--\s*meta\s*(.*?)-->", text, re.S))
        if not blocks:
            finding(f"[{pf.name}] contains no prompt <!-- meta --> blocks")
        for i, mb in enumerate(blocks):
            meta = parse_meta(mb.group(1))
            prid = str(meta.get("id", ""))
            if not prid:
                finding(f"[{pf.name}] a meta block has no id")
                continue
            # body = from end of this meta block to the start of the next, or EOF
            start = mb.end()
            end = blocks[i + 1].start() if i + 1 < len(blocks) else len(text)
            body = text[start:end]

            if prid in prompts:
                finding(f"[prompts] duplicate prompt id {prid} (also in {prompts[prid]['file']})")
                continue

            prompts[prid] = {
                "file": pf.name,
                "phase": str(meta.get("phase", "")),
                "prereq": meta.get("prereq", []) or [],
                "requirements": meta.get("requirements", []) or [],
                "title_en": str(meta.get("title_en", "")),
                "body": body,
            }
            order.append(prid)

            # ---- 3. ID prefix matches its phase ---------------------------
            m = re.match(r"^P(\d{2})-(\d{2})$", prid)
            if not m:
                finding(f"[prompts] {prid} does not match the P<NN>-<NN> pattern")
            else:
                if f"PHASE-{m.group(1)}" != pid:
                    finding(f"[prompts] {prid} lives in {pid} but its prefix says PHASE-{m.group(1)}")
            if meta.get("phase") and str(meta["phase"]) != pid:
                finding(f"[prompts] {prid} meta phase {meta['phase']!r} != file phase {pid}")

            # ---- 10. Arabic explanation questions -------------------------
            for q in ARABIC_QUESTIONS:
                if q not in body:
                    finding(f"[prompts] {prid} is missing the Arabic question: {q}")

            # ---- 11. English executable block ----------------------------
            code_blocks = re.findall(r"```text\n(.*?)```", body, re.S)
            if len(code_blocks) != 1:
                finding(
                    f"[prompts] {prid} has {len(code_blocks)} ```text executable "
                    "blocks; expected exactly 1"
                )
            else:
                cb = code_blocks[0]
                if CONTRACT_BINDING not in cb:
                    finding(f"[prompts] {prid} executable block does not bind to the operating contract")
                for sec in REQUIRED_SECTIONS:
                    if not re.search(rf"^[A-Z]\.\s+{re.escape(sec)}", cb, re.M):
                        finding(f"[prompts] {prid} executable block is missing section: {sec}")
                if f"TASK {prid}" not in cb:
                    finding(f"[prompts] {prid} executable block does not open with 'TASK {prid}'")
                # the block must be English-dominant: flag stray Arabic prose
                arabic_chars = len(re.findall(r"[؀-ۿ]", cb))
                if arabic_chars > 40:
                    finding(
                        f"[prompts] {prid} executable block contains {arabic_chars} Arabic "
                        "characters; executable prompts must be English"
                    )

            # ---- 7. cited requirements exist ------------------------------
            for rid in prompts[prid]["requirements"]:
                if rid not in req_ids:
                    finding(f"[prompts] {prid} cites unknown requirement {rid}")

    # ---- 4 + 5. prereqs exist, graph acyclic ------------------------------
    prompt_deps: dict[str, list[str]] = {}
    for prid, p in prompts.items():
        deps = []
        for d in p["prereq"]:
            if d not in prompts:
                finding(f"[prompts] {prid} prereq {d} does not exist")
            else:
                deps.append(d)
        prompt_deps[prid] = deps
    if cycle := find_cycle(prompt_deps):
        finding(f"[prompts] dependency cycle: {' -> '.join(cycle)}")

    # ---- 6. a prereq must not point forward across phase dependencies -----
    for prid, p in prompts.items():
        own_phase = p["phase"]
        for d in prompt_deps[prid]:
            dep_phase = prompts[d]["phase"]
            if dep_phase == own_phase:
                continue
            if not phase_reachable(own_phase, dep_phase, phase_deps):
                finding(
                    f"[prompts] {prid} ({own_phase}) depends on {d} ({dep_phase}) "
                    f"but {own_phase} does not declare {dep_phase} as a transitive dependency"
                )

    # ---- 8. requirement coverage ------------------------------------------
    covered: dict[str, list[str]] = {rid: [] for rid in req_ids}
    for prid, p in prompts.items():
        for rid in p["requirements"]:
            if rid in covered:
                covered[rid].append(prid)
    uncovered = sorted(r for r, v in covered.items() if not v)
    for rid in uncovered:
        row = next((r for r in requirements if r["req_id"] == rid), {})
        finding(
            f"[coverage] requirement {rid} ({row.get('domain','?')}) is not cited "
            f"by any prompt; its registry phase is {row.get('phase','?')}"
        )

    # requirement phase vs covering prompt phase (consistency, not fatal)
    for rid, prids in covered.items():
        if not prids:
            continue
        row = next((r for r in requirements if r["req_id"] == rid), {})
        want = row.get("phase", "")
        got = {prompts[p]["phase"] for p in prids}
        if want and want not in got:
            note(
                f"[coverage] {rid} registry phase {want} but covered only in "
                f"{sorted(got)} — intentional for cross-cutting requirements"
            )

    # ---- 12. forbidden readiness claims -----------------------------------
    scan_files = (
        [ROOT / n for n in REQUIRED_DOCS if (ROOT / n).is_file()]
        + list(PHASES_DIR.glob("*.md"))
        + [REGISTRY / n for n in REQUIRED_REGISTRY if (REGISTRY / n).is_file()]
    )
    for f in scan_files:
        text = f.read_text(encoding="utf-8")
        for pat in FORBIDDEN_CLAIMS:
            for m in re.finditer(pat, text, re.I):
                ctx = text[max(0, m.start() - 320) : m.end() + 120].replace("\n", " ")
                # allow it when it appears as something the blueprint forbids
                if re.search(r"never|not\b|forbid|prohibit|must not|cannot|do not|refus|without", ctx, re.I):
                    continue
                finding(f"[claims] {f.name}: unevidenced readiness claim {m.group(0)!r} — {ctx.strip()}")

    # ---- report ------------------------------------------------------------
    print("=" * 72)
    print("SKETCH DESIGN EXECUTION BLUEPRINT — INDEPENDENT QUALITY AUDIT")
    print("=" * 72)
    print(f"phase files      : {len(phase_files)}")
    print(f"phases declared  : {len(phases)}")
    print(f"prompts          : {len(prompts)}")
    print(f"requirements     : {len(requirements)}")
    print(f"requirements cov.: {len(req_ids) - len(uncovered)}/{len(req_ids)}")
    print(f"prompt order     : {', '.join(order[:6])} ... {', '.join(order[-3:])}")
    print("-" * 72)

    if notes:
        print(f"NOTES ({len(notes)}):")
        for n in notes:
            print("  ·", n)
        print("-" * 72)

    if findings:
        print(f"FINDINGS ({len(findings)}):", file=sys.stderr)
        for f in findings:
            print("  ✗", f, file=sys.stderr)
        print("-" * 72, file=sys.stderr)
        print("AUDIT RESULT: FAIL", file=sys.stderr)
        return 1

    print("AUDIT RESULT: PASS — all twelve structural conditions satisfied.")
    print("Note: this audit verifies the blueprint's internal integrity.")
    print("It does not and cannot verify that the target platform works.")
    return 0


def find_cycle(graph: dict[str, list[str]]) -> list[str] | None:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    stack: list[str] = []

    def visit(n: str) -> list[str] | None:
        color[n] = GREY
        stack.append(n)
        for m in graph.get(n, []):
            if m not in color:
                continue
            if color[m] == GREY:
                return stack[stack.index(m) :] + [m]
            if color[m] == WHITE:
                if res := visit(m):
                    return res
        stack.pop()
        color[n] = BLACK
        return None

    for n in list(graph):
        if color[n] == WHITE:
            if res := visit(n):
                return res
    return None


def phase_reachable(src: str, target: str, deps: dict[str, list[str]]) -> bool:
    seen: set[str] = set()
    frontier = list(deps.get(src, []))
    while frontier:
        n = frontier.pop()
        if n == target:
            return True
        if n in seen:
            continue
        seen.add(n)
        frontier.extend(deps.get(n, []))
    return False


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Generates the two derived deliverables from the phase files and the registries,
so they can never drift from the prompts they describe:

  03-MASTER-EXECUTION-PROMPTS.md   every prompt, in dependency order
  04-REQUIREMENTS-TRACEABILITY.md  source ref -> requirement -> phase -> prompt
                                   -> acceptance criteria

Both files carry a generated-file banner. Edit the phase files or the
registries, then re-run this script. Never hand-edit the generated files.

Usage:  python3 EXECUTION_BLUEPRINT/_tools/build.py
"""

from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASES_DIR = ROOT / "PHASES"
REGISTRY = ROOT / "_registry"

BANNER = (
    "<!-- GENERATED FILE — DO NOT EDIT BY HAND.\n"
    "     Produced by EXECUTION_BLUEPRINT/_tools/build.py from\n"
    "     EXECUTION_BLUEPRINT/PHASES/*.md and EXECUTION_BLUEPRINT/_registry/*.tsv.\n"
    "     Edit those sources and re-run the script. -->\n"
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.lstrip().startswith("#") and ln.strip()]
    return [
        {(k or "").strip(): (v or "").strip() for k, v in row.items()}
        for row in csv.DictReader(lines, delimiter="\t")
    ]


def parse_meta(block: str) -> dict[str, object]:
    meta: dict[str, object] = {}
    for line in block.strip().splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            meta[key] = [x.strip() for x in val[1:-1].split(",") if x.strip()]
        else:
            meta[key] = val
    return meta


def collect() -> tuple[list[dict], dict[str, dict]]:
    """Returns (prompts in file order, phase metadata by phase id)."""
    prompts: list[dict] = []
    phase_info: dict[str, dict] = {}

    for pf in sorted(PHASES_DIR.glob("PHASE-*.md")):
        text = pf.read_text(encoding="utf-8")

        pm = re.search(r"<!--\s*phasemeta\s*(.*?)-->", text, re.S)
        phase_id = str(parse_meta(pm.group(1)).get("id", pf.stem)) if pm else pf.stem

        # the phase heading and the Arabic preamble, i.e. everything before the
        # first prompt heading
        first_prompt = re.search(r"^### ", text, re.M)
        preamble = text[: first_prompt.start()] if first_prompt else text
        phase_info[phase_id] = {"file": pf.name, "preamble": preamble.rstrip()}

        blocks = list(re.finditer(r"<!--\s*meta\s*(.*?)-->", text, re.S))
        headings = list(re.finditer(r"^###\s+(.*)$", text, re.M))

        for i, mb in enumerate(blocks):
            meta = parse_meta(mb.group(1))
            start = mb.end()
            end = blocks[i + 1].start() if i + 1 < len(blocks) else len(text)
            body = text[start:end]

            # the Arabic heading immediately preceding this meta block
            heading = ""
            for h in headings:
                if h.start() < mb.start():
                    heading = h.group(1).strip()
                else:
                    break
            # the phase-file heading already carries the prompt id; the master
            # file renders the id separately, so strip the duplicate prefix
            heading = re.sub(r"^P\d{2}-\d{2}\s*[—–-]\s*", "", heading)

            # trim a trailing horizontal rule and any trailing next-prompt heading
            body = re.sub(r"\n---\s*$", "\n", body.rstrip()) + "\n"
            body = re.sub(r"\n###\s+[^\n]*\n?$", "\n", body)

            prompts.append(
                {
                    "id": str(meta.get("id", "")),
                    "phase": str(meta.get("phase", phase_id)),
                    "title_ar": heading,
                    "title_en": str(meta.get("title_en", "")),
                    "prereq": meta.get("prereq", []) or [],
                    "requirements": meta.get("requirements", []) or [],
                    "body": body.strip() + "\n",
                    "file": pf.name,
                }
            )
    return prompts, phase_info


def build_master(prompts: list[dict], phases: list[dict], phase_info: dict[str, dict]) -> str:
    today = dt.date.today().isoformat()
    out: list[str] = [BANNER]
    out.append("# 03 — مكتبة أوامر التنفيذ الكاملة\n")
    out.append(
        "> هذا هو المُخرَج الأساسي. يحتوي **كل** أوامر التنفيذ بالترتيب الصحيح.\n"
        "> كل أمر مستقل بذاته وقابل للتنفيذ في جلسة Claude Code جديدة، بشرط توفر\n"
        "> ملفات المشروع المذكورة فيه.\n"
    )
    out.append(
        f"\n**تاريخ التوليد:** {today} · "
        f"**عدد المراحل:** {len(phases)} · "
        f"**عدد الأوامر:** {len(prompts)}\n"
    )
    out.append(
        "\n## كيف تستخدم هذا الملف\n\n"
        "1. اقرأ `EXECUTION_BLUEPRINT/00-START-HERE.md` أولاً.\n"
        "2. تأكد من أن المتطلبات السابقة لكل أمر مُستوفاة قبل تنفيذه.\n"
        "3. انسخ **النص الإنجليزي داخل كتلة الكود** كما هو إلى Claude Code.\n"
        "4. لا تنفّذ أمراً قبل أن يُسجّل الأمر السابق نتيجته في "
        "`docs/EXECUTION-LOG.md`.\n"
        "5. عند انقطاع السياق، اقرأ سجل التنفيذ ثم أعد التحقق من حالة المشروع "
        "الفعلية قبل الوثوق بأي ادعاء سابق.\n"
    )

    # ---- index -------------------------------------------------------------
    out.append("\n## الفهرس\n")
    cur_phase = None
    for p in prompts:
        if p["phase"] != cur_phase:
            cur_phase = p["phase"]
            row = next((x for x in phases if x["phase_id"] == cur_phase), {})
            out.append(
                f"\n**{cur_phase} — {row.get('name_ar','')}** "
                f"(`{row.get('criticality','')}`)\n"
            )
        pre = ", ".join(f"`{x}`" for x in p["prereq"]) or "—"
        out.append(f"- `{p['id']}` — {p['title_ar']} · المتطلب السابق: {pre}\n")

    # ---- the prompts -------------------------------------------------------
    cur_phase = None
    for p in prompts:
        if p["phase"] != cur_phase:
            cur_phase = p["phase"]
            out.append("\n\n---\n\n")
            info = phase_info.get(cur_phase, {})
            # reuse the phase file's own Arabic preamble verbatim: one source of truth
            preamble = info.get("preamble", "")
            preamble = re.sub(r"<!--\s*phasemeta.*?-->\n?", "", preamble, flags=re.S)
            out.append(preamble.strip() + "\n")
        out.append("\n---\n\n")
        out.append(f"### `{p['id']}` — {p['title_ar']}\n\n")
        out.append(f"**Phase:** `{p['phase']}` · **EN title:** {p['title_en']}\n\n")
        pre = ", ".join(f"`{x}`" for x in p["prereq"]) or "—"
        reqs = ", ".join(f"`{x}`" for x in p["requirements"]) or "—"
        out.append(f"**المتطلبات السابقة:** {pre}\n\n")
        out.append(f"**المتطلبات المغطاة:** {reqs}\n\n")
        out.append(p["body"])

    out.append("\n\n---\n\n")
    out.append(
        "## نهاية المكتبة\n\n"
        "آخر أمر في المكتبة هو `P16-02`، وهو مشروط بتفويض مكتوب من المالك.\n"
        "إن بقي تأجيل التجارة قائماً (وهو الوضع المسجَّل في المصدر، الورقة 68\n"
        "الصف 8)، فإن نطاق التنفيذ ينتهي عند `PHASE-15`، ويستمر التشغيل عبر\n"
        "دورة الحكومة في `PHASE-14`.\n"
    )
    return "".join(out)


def build_traceability(
    prompts: list[dict], requirements: list[dict], phases: list[dict]
) -> str:
    today = dt.date.today().isoformat()
    cover: dict[str, list[str]] = {}
    for p in prompts:
        for rid in p["requirements"]:
            cover.setdefault(rid, []).append(p["id"])

    by_class: dict[str, int] = {}
    by_crit: dict[str, int] = {}
    for r in requirements:
        by_class[r["class"]] = by_class.get(r["class"], 0) + 1
        by_crit[r["criticality"]] = by_crit.get(r["criticality"], 0) + 1

    uncovered = [r["req_id"] for r in requirements if not cover.get(r["req_id"])]

    out: list[str] = [BANNER]
    out.append("# 04 — مصفوفة تتبع المتطلبات\n")
    out.append(
        "> تربط هذه المصفوفة كل متطلب بمرجعه في المصدر، وبمرحلته، وبالأوامر التي\n"
        "> تغطيه، وبضابط قبوله. المصفوفة **مُولَّدة** من `_registry/requirements.tsv`\n"
        "> ومن كتل `meta` في ملفات المراحل، فلا يمكن أن تنحرف عنها.\n"
    )
    out.append(
        "\n## اصطلاح اللغة\n\n"
        "محتوى الجدول بالإنجليزية لأنه معرّفات ومراجع قابلة للقراءة آلياً "
        "(`source_ref`, `req_id`, `phase`, `prompt_id`). الشرح العربي الكامل لكل "
        "نطاق موجود في `01-DEEP-ANALYSIS.md`.\n"
    )

    out.append("\n## قراءة `source_ref`\n\n")
    out.append(
        "الصيغة `<رقم الورقة>:<صف Excel>`. مثال: `02:r2` تعني الورقة\n"
        "`02_قرارات_معمارية` الصف 2. وكل المراجع تشير إلى المصدر الوحيد:\n"
        "`Sketch_Design_Model_Gateway_Observability_v11.md`.\n"
    )

    out.append(f"\n## ملخص التغطية (تاريخ التوليد {today})\n\n")
    out.append("| المقياس | القيمة |\n|---|---|\n")
    out.append(f"| إجمالي المتطلبات | {len(requirements)} |\n")
    out.append(f"| متطلبات مُغطاة بأمر واحد على الأقل | {len(requirements) - len(uncovered)} |\n")
    out.append(f"| متطلبات غير مُغطاة | {len(uncovered)} |\n")
    out.append(f"| إجمالي الأوامر | {len(prompts)} |\n")
    out.append(f"| إجمالي المراحل | {len(phases)} |\n")

    out.append("\n### التوزيع بحسب درجة الإثبات (`class`)\n\n")
    out.append("| class | العدد | المعنى |\n|---|---|---|\n")
    meaning = {
        "CONFIRMED": "منصوص عليه في المصدر",
        "DERIVED": "نتيجة منطقية لازمة",
        "PROPOSED": "توصية هندسية ليست في المصدر",
        "UNKNOWN": "لا يمكن إثباته من المصدر",
    }
    for k in ("CONFIRMED", "DERIVED", "PROPOSED", "UNKNOWN"):
        if k in by_class:
            out.append(f"| {k} | {by_class[k]} | {meaning[k]} |\n")

    out.append("\n### التوزيع بحسب الأهمية (`criticality`)\n\n")
    out.append("| criticality | العدد |\n|---|---|\n")
    for k in ("P0", "P1", "P2", "DEFERRED"):
        if k in by_crit:
            out.append(f"| {k} | {by_crit[k]} |\n")

    if uncovered:
        out.append("\n### متطلبات غير مُغطاة — يجب معالجتها\n\n")
        for rid in uncovered:
            row = next(r for r in requirements if r["req_id"] == rid)
            out.append(f"- `{rid}` ({row['domain']}) — {row['statement_en'][:120]}\n")
    else:
        out.append(
            "\n**لا يوجد متطلب غير مُغطى.** كل متطلب في السجل تغطيه أمر تنفيذي واحد "
            "على الأقل، أو هو مُعلَّم `DEFERRED` ومُغطى في `PHASE-16` خلف بوابة تفويض.\n"
        )

    # ---- the matrix, grouped by phase -------------------------------------
    out.append("\n---\n\n## المصفوفة\n")
    for ph in phases:
        pid = ph["phase_id"]
        rows = [r for r in requirements if r["phase"] == pid]
        if not rows:
            continue
        out.append(f"\n### {pid} — {ph['name_ar']} · `{ph['criticality']}`\n\n")
        out.append(
            "| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |\n"
            "|---|---|---|---|---|---|---|\n"
        )
        for r in rows:
            prids = ", ".join(f"`{x}`" for x in sorted(cover.get(r["req_id"], []))) or "**—**"
            acc = r["acceptance_ref"].replace("|", "\\|")
            out.append(
                f"| `{r['source_ref']}` | `{r['req_id']}` | {r['class']} | "
                f"{r['source_state']} | {r['criticality']} | {prids} | {acc} |\n"
            )

    # ---- reverse view: prompt -> requirements -----------------------------
    out.append("\n---\n\n## العرض المعاكس: أمر ← متطلبات\n\n")
    out.append("| prompt_id | phase | prereq | requirements covered |\n|---|---|---|---|\n")
    for p in prompts:
        pre = ", ".join(f"`{x}`" for x in p["prereq"]) or "—"
        reqs = ", ".join(f"`{x}`" for x in p["requirements"]) or "—"
        out.append(f"| `{p['id']}` | `{p['phase']}` | {pre} | {reqs} |\n")

    # ---- acceptance test index --------------------------------------------
    out.append("\n---\n\n## فهرس اختبارات القبول في المصدر (الورقة 16)\n\n")
    out.append(
        "الاختبارات الثلاثة عشر `AT-*` هي ضوابط القبول المُسمّاة في المصدر. "
        "كل واحد منها يُنفَّذ في أمر محدد:\n\n"
    )
    out.append("| test_id | الأمر الذي ينفّذه | المرحلة |\n|---|---|---|\n")
    at_map = [
        ("AT-SEC-001", "P01-02", "PHASE-01"),
        ("AT-FILE-001", "P02-01", "PHASE-02"),
        ("AT-WF-002", "P03-01", "PHASE-03"),
        ("AT-WF-001", "P03-02", "PHASE-03"),
        ("AT-RAG-001", "P06-01", "PHASE-06"),
        ("AT-REV-001", "P07-04", "PHASE-07"),
        ("AT-REV-002", "P07-03", "PHASE-07"),
        ("AT-DEL-001", "P07-05", "PHASE-07"),
        ("AT-PRICE-001", "P08-01", "PHASE-08"),
        ("AT-PAY-001", "P08-03", "PHASE-08"),
        ("AT-PAY-002", "P08-03", "PHASE-08"),
        ("AT-PRIV-001", "P11-02", "PHASE-11"),
        ("AT-EVAL-001", "P14-03", "PHASE-14"),
    ]
    for tid, prid, ph in at_map:
        out.append(f"| `{tid}` | `{prid}` | `{ph}` |\n")
    out.append(
        "\nوالاختبار المركّب `AT-VILLA-v1` (الورقة 07 الصف 2) يُعرَّف ويُنفَّذ في "
        "`P09-03`، وهو دليل البند `G01` في دفتر الأدلة.\n"
    )

    out.append(
        "\n---\n\n## تحذير\n\n"
        "تغطية المتطلب بأمر تنفيذي تعني أن **خطة** تنفيذه موجودة. ولا تعني أنه\n"
        "مُنفَّذ أو مُختبَر. حالة التنفيذ الحقيقية تُقرأ من دفتر الأدلة الذي يبنيه\n"
        "`P14-04`، وفقاً للقرار `ADR-008`.\n"
    )
    return "".join(out)


def main() -> int:
    requirements = read_tsv(REGISTRY / "requirements.tsv")
    phases = read_tsv(REGISTRY / "phases.tsv")
    prompts, phase_info = collect()

    if not prompts:
        print("FATAL: no prompts parsed from PHASES/", file=sys.stderr)
        return 2

    master = build_master(prompts, phases, phase_info)
    trace = build_traceability(prompts, requirements, phases)

    (ROOT / "03-MASTER-EXECUTION-PROMPTS.md").write_text(master, encoding="utf-8")
    (ROOT / "04-REQUIREMENTS-TRACEABILITY.md").write_text(trace, encoding="utf-8")

    print(f"wrote 03-MASTER-EXECUTION-PROMPTS.md  ({len(master):,} chars, {len(prompts)} prompts)")
    print(f"wrote 04-REQUIREMENTS-TRACEABILITY.md ({len(trace):,} chars, {len(requirements)} requirements)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

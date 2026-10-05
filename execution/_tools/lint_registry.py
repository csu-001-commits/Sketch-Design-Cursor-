# -*- coding: utf-8 -*-
"""Linter for the P00_DISCOVERY registry deliverables.

Implements the three tests P00 names in its AUTOMATED TESTS section:
  1. a TSV row with the wrong column count, an empty required field, or a
     source_state outside the ledger's allowed set, fails;
  2. a source marked AVAILABLE with no sha256 fails;
  3. a source marked NOT_SUPPLIED with no gap-report entry fails.

It is written to be able to fail: each check asserts something a plausible
authoring mistake would break.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REG = os.path.join(ROOT, "_registry")

SOURCES = os.path.join(REG, "source-register.tsv")
LEDGER = os.path.join(REG, "decision-ledger.tsv")
INVENTORY = os.path.join(REG, "environment-inventory.md")
GAPS = os.path.join(REG, "gap-report.md")

SOURCE_COLS = ["source_id", "title", "format", "supplied", "sha256", "role", "coverage_notes"]
LEDGER_COLS = ["decision_id", "statement", "source_state", "owner_role", "blocks_prompts"]

# "supplied" values this register is allowed to use. A new value must be added
# here deliberately, so a typo cannot silently become a new category.
SUPPLIED_STATES = {
    "AVAILABLE", "PARTIAL", "NOT_SUPPLIED",
    "EXCLUDED_BY_INSTRUCTION", "AVAILABLE_AS_REPOSITORY",
}

# Decision states the reference actually uses, verbatim. Anything else means a
# state was paraphrased or invented during transcription.
LEDGER_STATES = {
    "Approved direction",
    "Needs procurement/validation",
    "Needs legal/engineering review",
    "Unverified",
    "تم اعتماده",
}

SHA256 = re.compile(r"^[0-9a-f]{64}$")

errors = []


def err(msg):
    errors.append(msg)


def read_tsv(path, cols):
    rows = []
    if not os.path.isfile(path):
        err("missing deliverable: %s" % os.path.relpath(path, ROOT))
        return rows
    with open(path, encoding="utf-8") as fh:
        header_seen = False
        for n, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("\t")
            if not header_seen:
                header_seen = True
                if parts != cols:
                    err("%s: header is %r, expected %r"
                        % (os.path.basename(path), parts, cols))
                continue
            if len(parts) != len(cols):
                err("%s line %d: %d columns, expected %d"
                    % (os.path.basename(path), n, len(parts), len(cols)))
                continue
            row = dict(zip(cols, parts))
            for c in cols:
                if not row[c].strip():
                    err("%s line %d: empty required field %r" % (os.path.basename(path), n, c))
            rows.append(row)
    return rows


def gap_sections(text):
    """The body of each '### GAP-..' block, so a source_id mentioned only in the
    summary table cannot satisfy the NOT_SUPPLIED requirement."""
    out = []
    for block in re.split(r"\n#{3}\s+", text)[1:]:
        if block.startswith("GAP-"):
            out.append(block)
    return out


def check_sources(rows, gap_text, repo_root):
    seen = set()
    for r in rows:
        sid = r["source_id"]
        if sid in seen:
            err("source-register.tsv: duplicate source_id %s" % sid)
        seen.add(sid)

        state = r["supplied"]
        if state not in SUPPLIED_STATES:
            err("%s: supplied state %r is not in the allowed set" % (sid, state))

        digest = r["sha256"]
        # Test 2: AVAILABLE requires a real digest.
        if state in ("AVAILABLE", "PARTIAL", "EXCLUDED_BY_INSTRUCTION"):
            if not SHA256.match(digest):
                err("%s is %s but sha256 is %r — a source is described only if it was hashed"
                    % (sid, state, digest))
        elif state == "AVAILABLE_AS_REPOSITORY":
            if digest != "-":
                err("%s is AVAILABLE_AS_REPOSITORY but carries a digest %r; a hashable "
                    "file belongs in AVAILABLE" % (sid, digest))
            paths = re.findall(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]*", r["coverage_notes"])
            if not any(os.path.exists(os.path.join(repo_root, p.rstrip("/.")))
                       for p in paths):
                err("%s is AVAILABLE_AS_REPOSITORY but its coverage_notes name no path "
                    "that exists in this repository" % sid)
        elif state == "NOT_SUPPLIED":
            if digest != "-":
                err("%s is NOT_SUPPLIED but carries a digest %r" % (sid, digest))
            # Test 3: NOT_SUPPLIED requires a GAP section naming it. A mention
            # in the summary table does not count.
            if not any(sid in b for b in gap_sections(gap_text)):
                err("%s is NOT_SUPPLIED but no '### GAP-' section names it" % sid)
    return seen


def known_prompt_ids():
    d = os.path.join(ROOT, "prompts")
    if not os.path.isdir(d):
        return set()
    return {f.split("_", 1)[0] for f in os.listdir(d)
            if f.endswith(".md") and f != "README.md"}


def check_ledger(rows):
    prompts = known_prompt_ids()
    seen = set()
    for r in rows:
        did = r["decision_id"]
        if did in seen:
            err("decision-ledger.tsv: duplicate decision_id %s" % did)
        seen.add(did)
        # Test 1: states must be verbatim from the reference.
        if r["source_state"] not in LEDGER_STATES:
            err("%s: source_state %r was paraphrased; it must be the reference's own wording"
                % (did, r["source_state"]))
        blocks = r["blocks_prompts"]
        if blocks != "-" and prompts:
            for pid in blocks.split(","):
                pid = pid.strip()
                if pid and pid not in prompts:
                    err("%s: blocks_prompts names %r, which is not a prompt in "
                        "execution/prompts/" % (did, pid))


def main():
    for p in (INVENTORY, GAPS):
        if not os.path.isfile(p):
            err("missing deliverable: %s" % os.path.relpath(p, ROOT))

    gap_text = open(GAPS, encoding="utf-8").read() if os.path.isfile(GAPS) else ""

    sources = read_tsv(SOURCES, SOURCE_COLS)
    ledger = read_tsv(LEDGER, LEDGER_COLS)
    check_sources(sources, gap_text, os.path.dirname(ROOT))
    check_ledger(ledger)

    if sources and not any(r["supplied"] == "AVAILABLE" for r in sources):
        err("source-register.tsv lists no AVAILABLE source at all")

    print("sources   : %d" % len(sources))
    print("decisions : %d" % len(ledger))
    print("not supplied: %d" % sum(1 for r in sources if r["supplied"] == "NOT_SUPPLIED"))
    print("")
    if errors:
        for e in errors:
            print("FAIL  %s" % e)
        print("")
        print("REGISTRY LINT: FAIL (%d)" % len(errors))
        return 1
    print("REGISTRY LINT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

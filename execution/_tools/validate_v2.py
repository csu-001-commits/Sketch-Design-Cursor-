# -*- coding: utf-8 -*-
"""Structural audit of the Sketch Design V2 execution package.

This audit is written to be able to fail. Every check asserts a condition that a
plausible authoring mistake would break.
"""
import os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(ROOT)
PROMPTS = os.path.join(ROOT, "prompts")

MANDATORY = [
    "SKETCH_DESIGN_PRODUCTION_EXECUTION_MASTER_V2.md",
    "execution/ARCHITECTURE_DECISIONS.md",
    "execution/SERVICE_CATALOG.md",
    "execution/API_AND_EVENT_CONTRACTS.md",
    "execution/AGENT_RUNTIME_CONTRACTS.md",
    "execution/MODEL_GATEWAY_SPEC.md",
    "execution/ADMIN_CONTROL_PLANE.md",
    "execution/FRONTEND_FIDELITY_SPEC.md",
    "execution/SKETCH_SCAN_IMPLEMENTATION.md",
    "execution/REQUIREMENTS_TRACEABILITY.md",
    "execution/SECURITY_AND_COMPLIANCE.md",
    "execution/PRODUCTION_READINESS_GATES.md",
    "execution/EXECUTION_ROADMAP.md",
]

ELEMENTS = [
    "1. OBJECTIVE", "2. DEPENDENCIES", "3. EXACT SCOPE",
    "4. FILES AND MODULES AFFECTED", "5. REQUIRED CONTRACTS",
    "6. IMPLEMENTATION INSTRUCTIONS", "7. SECURITY REQUIREMENTS",
    "8. AUTOMATED TESTS", "9. ACCEPTANCE CRITERIA", "10. REQUIRED EVIDENCE",
    "11. ROLLBACK INSTRUCTIONS", "12. DEFINITION OF DONE",
]

ARABIC_QUESTIONS = [
    "ماذا ينفذ هذا الأمر؟", "لماذا نحتاجه؟", "ما المتطلبات السابقة؟",
    "ما النتيجة المتوقعة؟", "كيف نتحقق من نجاحه؟",
]

BINDING = "execution/OPERATING_RULES.md"
VALID_STATUS = {"DESIGNED", "IMPLEMENTED", "TESTED", "VERIFIED", "BLOCKED"}

# Readiness language that must not appear as an unqualified claim.
FORBIDDEN = [
    "production-ready", "production ready", "fully tested", "fully verified",
    "battle-tested", "certified", "10/10", "perfect score", "guaranteed",
    "جاهز للإنتاج", "مُختبَر بالكامل", "مضمون", "معتمد رسميًا",
]
NEGATION_WINDOW = 320
NEGATORS = [
    "not ", "never", "no ", "without", "cannot", "must not", "do not", "لا ", "لم ",
    "ليس", "غير ", "دون", "يُمنع", "محظور", "BLOCKED", "NOT_ASSESSED", "لا يُدّعى",
    "لا تُدّعى", "ولا يُدّعى", "لا يُعلن", "ممنوع", "يحجب", "بلا",
    # prohibition verbs: the phrase appears inside a rule that forbids it
    "fails on", "reject", "refuse", "prohibit", "forbid", "blocks the",
]

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def check_deliverables():
    for rel in MANDATORY:
        p = os.path.join(REPO, rel)
        if not os.path.isfile(p):
            err("missing mandatory deliverable: %s" % rel)
        elif os.path.getsize(p) < 500:
            err("mandatory deliverable suspiciously small: %s" % rel)
    if not os.path.isdir(PROMPTS):
        err("missing execution/prompts/")


def parse_meta(text, path):
    m = re.search(r"<!-- promptmeta\n(.*?)\n-->", text, re.S)
    if not m:
        err("%s: no promptmeta block" % path)
        return {}
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            err("%s: malformed promptmeta line %r" % (path, line))
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta


def check_prompts():
    files = sorted(f for f in os.listdir(PROMPTS) if f.endswith(".md") and f != "README.md")
    if not files:
        err("no prompt files found")
        return {}, []
    metas = {}
    order = []
    for f in files:
        path = os.path.join(PROMPTS, f)
        text = open(path, encoding="utf-8").read()
        meta = parse_meta(text, f)
        for k in ("id", "file", "stage", "title_en", "prereq", "requirements", "status"):
            if k not in meta:
                err("%s: promptmeta missing key %r" % (f, k))
        if meta.get("file") != f:
            err("%s: promptmeta file field is %r" % (f, meta.get("file")))
        if meta.get("status") not in VALID_STATUS:
            err("%s: invalid status %r" % (f, meta.get("status")))
        # stray comment terminator inside the body would break the parser
        if text.count("-->") != 1:
            err("%s: expected exactly one '-->' (found %d)" % (f, text.count("-->")))
        # the twelve elements, in order
        pos = -1
        for e in ELEMENTS:
            i = text.find("\n" + e + "\n")
            if i < 0:
                err("%s: missing element %r" % (f, e))
            elif i < pos:
                err("%s: element %r out of order" % (f, e))
            else:
                pos = i
        for q in ARABIC_QUESTIONS:
            if q not in text:
                err("%s: missing Arabic question %r" % (f, q))
        if BINDING not in text:
            err("%s: not bound to %s" % (f, BINDING))
        if "STOP CONDITION" not in text:
            err("%s: missing STOP CONDITION" % f)
        if text.count("```text") != 1 or text.count("```") != 2:
            err("%s: expected exactly one fenced executable block" % f)
        metas[meta.get("id")] = meta
        order.append(meta.get("id"))
    return metas, order


def check_chain(metas, order):
    expected = ["P%02d" % i for i in range(len(order))]
    if order != expected:
        err("prompt ids are not a complete sequence: %s" % order)
    for pid, meta in metas.items():
        pre = meta.get("prereq", "")
        if pre == "-":
            if pid != "P00":
                err("%s: only P00 may have no prereq" % pid)
            continue
        if pre not in metas:
            err("%s: prereq %r does not exist" % (pid, pre))
        elif int(pre[1:]) >= int(pid[1:]):
            err("%s: prereq %r is not earlier" % (pid, pre))


def check_requirements(metas):
    reg = os.path.join(ROOT, "_registry", "v2-requirements.tsv")
    known, mapped_to = set(), {}
    with open(reg, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if parts[0] == "req_id":
                continue
            if len(parts) != 8:
                err("v2-requirements.tsv: row %r has %d columns, expected 8" % (parts[0], len(parts)))
                continue
            known.add(parts[0])
            mapped_to[parts[0]] = parts[7]
    referenced = set()
    for pid, meta in metas.items():
        for r in meta.get("requirements", "").split(","):
            r = r.strip()
            if not r:
                continue
            referenced.add(r)
            if r not in known:
                err("%s: references unknown requirement %r" % (pid, r))
    for r in sorted(known - referenced):
        err("requirement %s (registry says %s) is referenced by no prompt" % (r, mapped_to[r]))
    # registry prompt_ref must agree with at least one prompt's own meta
    for r, p in mapped_to.items():
        if p in metas and r not in metas[p].get("requirements", ""):
            err("registry maps %s to %s but %s does not list it" % (r, p, p))


def check_index(metas):
    idx = os.path.join(PROMPTS, "README.md")
    if not os.path.isfile(idx):
        err("missing execution/prompts/README.md")
        return
    text = open(idx, encoding="utf-8").read()
    for pid, meta in metas.items():
        if meta.get("file", "")[:-3] not in text:
            err("README.md does not list %s" % pid)


def check_claims():
    scanned = 0
    for base, _dirs, files in os.walk(ROOT):
        if "_tools" in base:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            scan_file(os.path.join(base, f))
            scanned += 1
    scan_file(os.path.join(REPO, MANDATORY[0]))
    return scanned + 1


def scan_file(path):
    text = open(path, encoding="utf-8").read()
    low = text.lower()
    for phrase in FORBIDDEN:
        start = 0
        while True:
            i = low.find(phrase.lower(), start)
            if i < 0:
                break
            start = i + 1
            ctx = text[max(0, i - NEGATION_WINDOW): i + len(phrase) + 60]
            if not any(n.lower() in ctx.lower() for n in NEGATORS):
                err("%s: unqualified readiness claim %r" % (os.path.relpath(path, REPO), phrase))


def check_traceability_fresh():
    out = os.path.join(ROOT, "REQUIREMENTS_TRACEABILITY.md")
    before = open(out, encoding="utf-8").read() if os.path.isfile(out) else None
    r = subprocess.run([sys.executable, os.path.join(HERE, "gen_traceability.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        err("gen_traceability.py failed: %s" % r.stderr.strip())
        return
    after = open(out, encoding="utf-8").read()
    if before != after:
        err("REQUIREMENTS_TRACEABILITY.md was stale; regenerate before committing")
    m = re.search(r"<!-- coverage: total=(\d+) covered=(\d+) deferred=(\d+) uncovered=(\d+) -->", after)
    if not m:
        err("REQUIREMENTS_TRACEABILITY.md has no machine-readable coverage marker")
    elif int(m.group(4)) != 0:
        err("traceability reports %s uncovered requirements" % m.group(4))
    elif int(m.group(1)) != int(m.group(2)) + int(m.group(3)):
        err("coverage marker does not balance: %s != %s + %s" % m.group(1, 2, 3))


def main():
    check_deliverables()
    metas, order = check_prompts()
    if metas:
        check_chain(metas, order)
        check_requirements(metas)
        check_index(metas)
    n = check_claims()
    check_traceability_fresh()

    print("prompts audited : %d" % len(metas))
    print("markdown scanned: %d" % n)
    print("")
    if warnings:
        for w in warnings:
            print("WARN  %s" % w)
    if errors:
        for e in errors:
            print("FAIL  %s" % e)
        print("")
        print("AUDIT RESULT: FAIL (%d)" % len(errors))
        return 1
    print("AUDIT RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

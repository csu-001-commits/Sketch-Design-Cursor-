# -*- coding: utf-8 -*-
"""Prove check_governance_contracts.py can fail.

A checker that has never failed proves nothing. This harness copies the package
to a temporary tree, injects one defect at a time, and requires the checker to
report FAIL for each. It exits non-zero if any injected defect goes unnoticed,
or if the unmodified baseline does not pass.

Run: python3 execution/_tools/test_governance_contracts_can_fail.py
"""
import io, os, shutil, subprocess, sys, tempfile

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

C = "API_AND_EVENT_CONTRACTS.md"
P = os.path.join("prompts", "P-GOV_GOVERNANCE_ENTITIES.md")
G = os.path.join("_registry", "governance-additions.tsv")
GAP = os.path.join("_registry", "gap-report.md")
REQ = os.path.join("_registry", "v2-requirements.tsv")
OD = "OPEN_DECISIONS.md"


def drop(path, needle):
    def f(root):
        p = os.path.join(root, path)
        t = io.open(p, encoding="utf-8").read()
        assert needle in t, "needle absent: %r" % needle
        io.open(p, "w", encoding="utf-8").write(t.replace(needle, "", 1))
    return f


def swap(path, a, b):
    def f(root):
        p = os.path.join(root, path)
        t = io.open(p, encoding="utf-8").read()
        assert a in t, "needle absent: %r" % a
        io.open(p, "w", encoding="utf-8").write(t.replace(a, b, 1))
    return f


def drop_line(path, needle):
    def f(root):
        p = os.path.join(root, path)
        lines = io.open(p, encoding="utf-8").read().split("\n")
        keep = [l for l in lines if needle not in l]
        assert len(keep) < len(lines), "no line holds %r" % needle
        io.open(p, "w", encoding="utf-8").write("\n".join(keep))
    return f


CASES = [
    ("C-01 Request cardinality constraint removed",
     drop(C, "`UNIQUE (converted_project_id) WHERE converted_project_id IS NOT NULL`")),
    ("C-02 public_code non-derivation rule weakened",
     swap(C, "ولا base32/base58/base64 للبايتات", "ولا base32/base58 للبايتات")),
    ("C-03 BLOCKED smuggled into the status enumeration",
     swap(C, "`completed` · `failed`", "`completed` · `failed` · `BLOCKED`")),
    ("C-04 a blocking attribute row removed",
     drop_line(C, "| `next_action` | text \\| null |")),
    ("C-05 Accreditation type widened past INTERIM/OFFICIAL",
     swap(C, "**`INTERIM` أو `OFFICIAL` فقط**", "`INTERIM` أو `OFFICIAL` أو `PROVISIONAL`")),
    ("C-06 DeliveryManifest review-decision reference removed",
     drop_line(C, "`required_review_decision_ids`")),
    ("C-07 outbox atomic-write rule removed",
     swap(C, "يُكتبان **في المعاملة نفسها**", "يُكتبان بالترتيب")),
    ("C-08 outbox idempotency key removed",
     drop_line(C, "| `idempotency_key` | text | `UNIQUE` |")),
    ("C-09 tenant isolation test removed from P-GOV",
     drop_line(P, "Tenant isolation holds for all ten new entities")),
    ("registry: a governance item attributed to a supplied source",
     swap(G, "GOV-04\tRequest is a standalone", "GOV-04\tSRC-01 requires that Request is a standalone")),
    ("registry: a contract_ref pointing at a section that does not exist",
     swap(G, "API_AND_EVENT_CONTRACTS.md#7.6", "API_AND_EVENT_CONTRACTS.md#7.99")),
    ("registry: the provenance warning removed",
     swap(G, "NEW USER DIRECTIVE / GOVERNANCE ADDITION", "governance note")),
    ("traceability: the GAP-07 section removed",
     drop_line(GAP, "### GAP-07")),
    ("traceability: the RC-02 section removed",
     drop_line(GAP, "### RC-02")),
    ("traceability: OD-V2-12 removed from OPEN_DECISIONS.md",
     drop_line(OD, "OD-V2-12")),
    ("UR-009 silently amended to mention a blocked status",
     swap(REQ, "human-review, completed and failed.", "human-review, completed, failed and blocked.")),
]


def run(root):
    r = subprocess.run([sys.executable, os.path.join(root, "_tools",
                                                     "check_governance_contracts.py")],
                       capture_output=True, text=True)
    fails = [l for l in r.stdout.splitlines() if l.startswith("FAIL")]
    return r.returncode, fails


base = tempfile.mkdtemp()
clean = os.path.join(base, "execution")
shutil.copytree(SRC, clean, ignore=shutil.ignore_patterns("__pycache__"))
rc, fails = run(clean)
print("baseline (unmodified): exit=%d fails=%d" % (rc, len(fails)))
if rc != 0:
    for f in fails:
        print("   ", f)
    sys.exit("baseline must pass before injection means anything")
print("")

bad = 0
for i, (name, mutate) in enumerate(CASES, 1):
    d = os.path.join(base, "case%02d" % i)
    shutil.copytree(clean, os.path.join(d, "execution"))
    mutate(os.path.join(d, "execution"))
    rc, fails = run(os.path.join(d, "execution"))
    ok = rc != 0 and fails
    if not ok:
        bad += 1
    print("%-2d %-62s %s  (%d FAIL line%s)"
          % (i, name[:62], "CAUGHT " if ok else "MISSED!", len(fails),
             "" if len(fails) == 1 else "s"))
    if ok:
        print("      -> %s" % fails[0][6:][:150])

print("")
print("injections: %d  caught: %d  missed: %d" % (len(CASES), len(CASES) - bad, bad))
shutil.rmtree(base)
sys.exit(1 if bad else 0)

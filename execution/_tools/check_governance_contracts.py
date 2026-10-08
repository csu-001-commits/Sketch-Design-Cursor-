# -*- coding: utf-8 -*-
"""Conformance checker for the operational governance entity contracts.

WHAT THIS PROVES AND WHAT IT DOES NOT.

Section 7 of execution/API_AND_EVENT_CONTRACTS.md is a specification. No
database, service or migration exists for it. This checker therefore verifies
that the CONTRACT IS COMPLETE AS WRITTEN, and that each of the nine required
tests is named in P-GOV. It does not execute a system, and a PASS here is
DESIGN PRESENT, never IMPLEMENTATION VERIFIED.

It is written to be able to fail: remove any required field, constraint or test
statement and the matching check reports FAIL.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REG = os.path.join(ROOT, "_registry")

CONTRACTS = os.path.join(ROOT, "API_AND_EVENT_CONTRACTS.md")
GOVREG = os.path.join(REG, "governance-additions.tsv")
GAPS = os.path.join(REG, "gap-report.md")
V2REQ = os.path.join(REG, "v2-requirements.tsv")
OPEN_DEC = os.path.join(ROOT, "OPEN_DECISIONS.md")
PROMPT = os.path.join(ROOT, "prompts", "P-GOV_GOVERNANCE_ENTITIES.md")

GOV_COLS = ["gov_id", "statement_en", "origin", "status", "contract_ref", "prompt_ref", "linked"]
GOV_ORIGINS = {"USER_DIRECTIVE"}
GOV_STATUSES = {"ADOPTED", "PROPOSED", "RECONCILIATION_REQUIRED"}

# The seven task statuses the approved source fixes. Not six, not eight.
SEVEN = ["queued", "validating", "running", "waiting-for-input",
         "human-review", "completed", "failed"]

BLOCK_ATTRS = ["blocked", "block_code", "block_reason", "blocked_owner",
               "blocked_at", "expected_resolution_at", "next_action"]

# entity -> (section number, required field names)
ENTITIES = [
    ("Request", "7.1", [
        "id", "tenant_id", "submitted_by", "request_type", "raw_summary",
        "context_json", "status", "converted_project_id", "created_at"]),
    ("Project", "7.2", [
        "id", "public_code", "tenant_id", "owner_id", "source_request_id",
        "title", "summary", "context_json", "lifecycle", "blocker_code",
        "created_at", "updated_at", "closed_at"]),
    ("Task", "7.3", [
        "id", "project_id", "kind", "title", "status", "priority",
        "assignee_id", "depends_on", "is_idempotent", "created_at",
        "started_at", "completed_at"] + BLOCK_ATTRS),
    ("Evidence", "7.4", [
        "id", "project_id", "task_id", "kind", "source", "version",
        "author_id", "storage_ref", "content_sha256", "metadata_json",
        "state", "created_at"]),
    ("ReviewDecision", "7.5", [
        "id", "project_id", "task_id", "reviewer_id",
        "reviewer_accreditation_id", "decision", "scope", "evidence_refs",
        "document_digest_sha256", "covered_finding_ids", "supersedes_id",
        "audit_event_id", "created_at"]),
    ("DeliveryManifest", "7.6", [
        "id", "project_id", "version", "recipient_id", "included_task_ids",
        "included_evidence_ids", "required_review_decision_ids",
        "included_file_refs", "manifest_digest_sha256", "state",
        "created_at", "sent_at", "acknowledged_at"]),
    ("Accreditation", "7.7", [
        "id", "account_id", "type", "specialty", "membership_ref", "status",
        "decision_ref", "provider_ref", "valid_from", "expires_at", "events"]),
    ("AuditEvent", "7.8", [
        "event_id", "occurred_at", "actor_type", "actor_id", "action",
        "target_type", "target_id", "before_ref", "after_ref", "request_id",
        "trace_id", "outcome"]),
    ("UsageRecord", "7.9", [
        "invocation_id", "tenant_id", "project_id", "workflow_run_id",
        "agent_version_id", "model_candidate_id", "input_tokens",
        "output_tokens", "cost_sar", "cost_source", "recorded_at"]),
    ("OutboxEvent", "7.10", [
        "id", "aggregate_type", "aggregate_id", "event_type", "payload",
        "idempotency_key", "occurred_at", "published_at", "publish_attempts",
        "last_error", "status"]),
]

# The nine required tests from the governance directive. Each is checked twice:
# the contract element must be present in its section, and the test must be
# named in P-GOV's AUTOMATED TESTS section.
#   (check id, section, contract fragments, prompt fragments)
CHECKS = [
    ("C-01", "7.1",
     ["UNIQUE (converted_project_id)", "IS NOT NULL"],
     ["cannot be linked to more than one Project"]),
    ("C-02", "7.2",
     ["UNIQUE (tenant_id, public_code)", "base32", "base64",
      "مفتاحًا داخليًا"],
     ["public_code is unique per tenant", "not a reversible encoding"]),
    ("C-03", "7.3",
     SEVEN,
     ["accepts exactly the seven values and rejects BLOCKED"]),
    ("C-04", "7.3",
     BLOCK_ATTRS + ["ليست قيمة مسموحة في `status`"],
     ["blocked=true without block_code"]),
    ("C-05", "7.7",
     ["`INTERIM` أو `OFFICIAL` فقط", "CAPTCHA", "provider_ref"],
     ["INTERIM accreditation cannot be displayed or exported"]),
    ("C-06", "7.6",
     ["recipient_id", "included_task_ids", "included_evidence_ids",
      "required_review_decision_ids", "included_file_refs", "version",
      "sent_at"],
     ["reaching READY with any dangling reference"]),
    ("C-07", "7.10",
     ["في المعاملة نفسها"],
     ["written atomically"]),
    ("C-08", "7.10",
     ["idempotency_key", "UNIQUE"],
     ["publication is idempotent"]),
    ("C-09", "7.0",
     ["tenant_id"],
     ["Tenant isolation holds for all ten new entities"]),
]

errors = []
checks_run = 0


def err(msg):
    errors.append(msg)


def read(path):
    if not os.path.isfile(path):
        err("missing file: %s" % os.path.relpath(path, ROOT))
        return ""
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def sections(text):
    """Body of each '## 7.x' subsection, keyed by its number."""
    out = {}
    parts = re.split(r"\n##\s+(7(?:\.\d+)?)([^\n]*)\n", "\n" + text)
    for i in range(1, len(parts) - 2, 3):
        out[parts[i]] = parts[i + 1] + "\n" + parts[i + 2]
    return out


def table_fields(body):
    """Field names declared in the first cell of a table row. A field mentioned
    only in prose is not a declared field, so removing its row is caught."""
    out = set()
    for line in body.splitlines():
        if not line.startswith("|"):
            continue
        cells = line.split("|")
        if len(cells) < 3:
            continue
        for tok in re.findall(r"`([A-Za-z0-9_]+)`", cells[1]):
            out.add(tok)
    return out


def check_entities(secs):
    global checks_run
    for name, num, fields in ENTITIES:
        body = secs.get(num)
        if body is None:
            err("%s: section %s is missing from API_AND_EVENT_CONTRACTS.md" % (name, num))
            continue
        if "`%s`" % name not in body and name not in body:
            err("%s: section %s does not name the entity" % (name, num))
        declared = table_fields(body)
        for f in fields:
            checks_run += 1
            if f not in declared:
                err("%s (section %s): field %r is not declared in the contract's "
                    "field table" % (name, num, f))


def check_required(secs, prompt):
    global checks_run
    tests_block = ""
    m = re.search(r"\n8\. AUTOMATED TESTS\n(.*?)\n9\. ACCEPTANCE CRITERIA\n",
                  prompt, re.S)
    if m:
        tests_block = m.group(1)
    elif prompt:
        err("P-GOV: no AUTOMATED TESTS section found")

    for cid, num, contract_frags, prompt_frags in CHECKS:
        body = secs.get(num, "")
        if not body:
            err("%s: section %s is missing, so the contract element cannot be verified" % (cid, num))
            continue
        for frag in contract_frags:
            checks_run += 1
            if frag not in body:
                err("%s: section %s does not state %r" % (cid, num, frag))
        for frag in prompt_frags:
            checks_run += 1
            if frag not in tests_block:
                err("%s: P-GOV names no automated test matching %r" % (cid, frag))


def check_seven_states(secs):
    """UR-009 fixes seven statuses. The contract must list all seven and must
    not admit BLOCKED as an eighth."""
    global checks_run
    body = secs.get("7.3", "")
    line = ""
    for l in body.splitlines():
        if all(("`%s`" % s) in l for s in SEVEN):
            line = l
            break
    checks_run += 1
    if not line:
        err("section 7.3 has no line enumerating all seven task statuses")
        return
    checks_run += 1
    if "BLOCKED" in line:
        err("section 7.3 admits BLOCKED into the status enumeration: %r" % line.strip())
    # and no eighth backticked token smuggled into the same line
    tokens = set(re.findall(r"`([a-z-]+)`", line))
    extra = tokens - set(SEVEN)
    checks_run += 1
    if extra:
        err("section 7.3 enumerates status values beyond the seven: %s" % sorted(extra))


def check_ur009_untouched():
    """The directive forbids changing UR-009 silently. Its registry row must
    still carry the seven states and must not mention a blocked status."""
    global checks_run
    text = read(V2REQ)
    row = None
    for line in text.splitlines():
        if line.startswith("UR-009\t"):
            row = line
            break
    checks_run += 1
    if row is None:
        err("UR-009 is no longer in v2-requirements.tsv")
        return
    low = row.lower()
    for s in SEVEN:
        checks_run += 1
        if s not in low:
            err("UR-009 no longer states the status %r" % s)
    checks_run += 1
    if "blocked" in low:
        err("UR-009 was amended to mention a blocked status; that needs Product Owner approval (RC-02)")


def check_registry(secs):
    global checks_run
    text = read(GOVREG)
    rows, header_seen, ids = [], False, set()
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if not header_seen:
            header_seen = True
            if parts != GOV_COLS:
                err("governance-additions.tsv: header is %r, expected %r" % (parts, GOV_COLS))
            continue
        if len(parts) != len(GOV_COLS):
            err("governance-additions.tsv line %d: %d columns, expected %d"
                % (n, len(parts), len(GOV_COLS)))
            continue
        row = dict(zip(GOV_COLS, parts))
        for c in GOV_COLS:
            if not row[c].strip():
                err("governance-additions.tsv line %d: empty required field %r" % (n, c))
        rows.append(row)

    if not rows:
        err("governance-additions.tsv holds no rows")
        return

    for r in rows:
        gid = r["gov_id"]
        checks_run += 1
        if gid in ids:
            err("governance-additions.tsv: duplicate gov_id %s" % gid)
        ids.add(gid)
        checks_run += 1
        if r["origin"] not in GOV_ORIGINS:
            err("%s: origin %r is not an allowed provenance value" % (gid, r["origin"]))
        checks_run += 1
        if r["status"] not in GOV_STATUSES:
            err("%s: status %r is not in the allowed set" % (gid, r["status"]))
        # provenance: these items must never be attributed to a supplied source
        checks_run += 1
        if re.search(r"SRC-0[12]", "\t".join(r.values())):
            err("%s: attributes a governance addition to a supplied source" % gid)
        # the contract reference must resolve to a section that exists
        ref = r["contract_ref"]
        checks_run += 1
        if not ref.startswith("API_AND_EVENT_CONTRACTS.md#"):
            err("%s: contract_ref %r does not point at the contracts document" % (gid, ref))
        else:
            anchor = ref.split("#", 1)[1]
            if anchor not in secs:
                err("%s: contract_ref %r names section %r, which does not exist"
                    % (gid, ref, anchor))
        checks_run += 1
        if r["prompt_ref"] != "P-GOV":
            err("%s: prompt_ref is %r; these items belong to P-GOV" % (gid, r["prompt_ref"]))

    # the registry must carry the provenance warning, not only the rows
    for frag in ("NEW USER DIRECTIVE", "GOVERNANCE ADDITION"):
        checks_run += 1
        if frag not in text:
            err("governance-additions.tsv carries no %r provenance warning" % frag)
    checks_run += 1
    if "v2-requirements.tsv" not in text:
        err("governance-additions.tsv does not state its separation from v2-requirements.tsv")


def check_traceability(secs):
    """P-GOV, the entity contracts, RC-02, GAP-07 and OD-V2-12 must be linked,
    each in the file that owns it."""
    global checks_run
    gaps = read(GAPS)
    decisions = read(OPEN_DEC)
    for token, text, where in (
            ("RC-02", gaps, "gap-report.md"),
            ("GAP-07", gaps, "gap-report.md"),
            ("OD-V2-12", decisions, "OPEN_DECISIONS.md")):
        checks_run += 1
        # (?<![A-Z]) so that SRC-02 cannot satisfy a search for RC-02
        if not re.search(r"(?<![A-Z])" + re.escape(token), text):
            err("%s is not recorded in %s" % (token, where))
    # GAP-07 must name the unsupplied document it is about, inside its own section
    checks_run += 1
    blocks = [b for b in re.split(r"\n#{3}\s+", gaps)[1:] if b.startswith("GAP-07")]
    if not blocks:
        err("gap-report.md has no '### GAP-07' section")
    elif "engineering-project-governance" not in blocks[0]:
        err("GAP-07 does not name engineering-project-governance")
    # RC-02 must state that the seven states stand and that BLOCKED is deferred
    checks_run += 1
    rc = [b for b in re.split(r"\n#{3}\s+", gaps)[1:] if b.startswith("RC-02")]
    if not rc:
        err("gap-report.md has no '### RC-02' section")
    else:
        for frag in ("UR-009", "RECONCILIATION_REQUIRED", "BLOCKED"):
            checks_run += 1
            if frag not in rc[0]:
                err("RC-02 does not mention %r" % frag)
    # OD-V2-12 must record Manus API as recorded-not-adopted
    checks_run += 1
    od = [l for l in decisions.splitlines() if "OD-V2-12" in l]
    if od and not any("Manus" in l for l in od):
        err("OD-V2-12 does not name the Manus API")
    # section 7.11 must carry the traceability chain
    body = secs.get("7.11", "")
    for frag in ("P-GOV", "governance-additions.tsv", "RC-02", "GAP-07", "OD-V2-12"):
        checks_run += 1
        if frag not in body:
            err("section 7.11 does not link %r" % frag)


def main():
    contracts = read(CONTRACTS)
    prompt = read(PROMPT)
    secs = sections(contracts)

    if "7" not in secs:
        err("API_AND_EVENT_CONTRACTS.md has no section 7")

    check_entities(secs)
    check_required(secs, prompt)
    check_seven_states(secs)
    check_ur009_untouched()
    check_registry(secs)
    check_traceability(secs)

    print("entities checked : %d" % len(ENTITIES))
    print("directive checks : %d" % len(CHECKS))
    print("assertions run   : %d" % checks_run)
    print("")
    if errors:
        for e in errors:
            print("FAIL  %s" % e)
        print("")
        print("GOVERNANCE CONTRACTS: FAIL (%d)" % len(errors))
        return 1
    print("GOVERNANCE CONTRACTS: PASS — design present, not implementation verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())

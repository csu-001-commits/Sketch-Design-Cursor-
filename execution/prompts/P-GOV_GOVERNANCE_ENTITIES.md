<!-- promptmeta
id: P-GOV
file: P-GOV_GOVERNANCE_ENTITIES.md
stage: 1 — Foundation
title_en: Operational governance entities — field, relation and constraint contracts
prereq: P03
requirements: UR-009,UR-011,UR-018,UR-040,UR-047
status: DESIGNED
-->

# P-GOV_GOVERNANCE_ENTITIES — Operational governance entities — field, relation and constraint contracts

**كيانات الحوكمة التشغيلية — عقود الحقول والعلاقات والقيود**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 1 — Foundation |
| المتطلب السابق | P03 |
| المتطلبات المغطّاة | UR-009، UR-011، UR-018، UR-040، UR-047 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يثبّت عقدًا كاملًا على مستوى الحقل والعلاقة والقيد لعشرة كيانات حوكمة تشغيلية، ويضيف صندوق الصادر المعامِلي عقدًا حقيقيًا لا ملاحظة معمارية.

**لماذا نحتاجه؟**  
قائمة أسماء كيانات لا تمنع عيبًا. الطلب الذي يُنتج مشروعين، والمعرّف العام الذي يكشف الـUUID، والاعتماد المؤقت الذي يُطبَع رسميًا، والحدث الذي يُنشَر دون تثبيت تغييره — كلها تمر من ثغرة «الكيان مذكور والعقد غائب».

**ما المتطلبات السابقة؟**  
اكتمال P03 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
عقود الحقول والقيود في `execution/API_AND_EVENT_CONTRACTS.md` القسم 7، وسجل مصدرية `governance-additions.tsv`، ومدقّق نصي يفشل عند نقص أي بند من العقد.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا قُبل طلب مرتبط بأكثر من مشروع، أو إذا دخلت `BLOCKED` قائمة حالات المهمة، أو إذا عُرض `INTERIM` بوصفه `OFFICIAL`، أو إذا كُتب حدث الصادر في معاملة غير معاملة تغيير النطاق.

## EXECUTABLE PROMPT

```text
You are executing P-GOV_GOVERNANCE_ENTITIES of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Fix the field-, relation- and constraint-level contracts for the ten operational governance entities — Request, Project, Task, Evidence, ReviewDecision, DeliveryManifest, Accreditation, AuditEvent, UsageRecord, OutboxEvent — and make the transactional outbox a first-class contract rather than an architectural note.

2. DEPENDENCIES
P03 — the project and evidence domain and the Evidence Package contract exist and are tenant-scoped. This prompt specifies contracts; it does not re-implement P03's entities.

3. EXACT SCOPE
IN SCOPE:
- Field tables for the ten entities named above, each field carrying a type and its binding constraint.
- Request as a standalone intake entity: one Request converts to zero or exactly one Project, enforced by a unique partial index rather than by application convention.
- Project.public_code as a public identifier that does not reveal the internal UUID, is unique per tenant, and is never used as an internal or foreign key.
- Project.lifecycle as a state machine with a vocabulary wholly separate from Task.status.
- Task blocking as an orthogonal attribute set — blocked, block_code, block_reason, blocked_owner, blocked_at, expected_resolution_at, next_action — alongside, not inside, the seven task statuses.
- DeliveryManifest referential completeness: project, recipient, tasks, evidence, review decisions, files, version and delivery timestamps.
- Accreditation type restricted to INTERIM or OFFICIAL, with the display and export rules that keep the two apart.
- OutboxEvent with id, aggregate_type, aggregate_id, event_type, payload, idempotency_key, occurred_at, published_at, publish_attempts, last_error and status, plus the atomic-write, retry and de-duplication rules.
- A text-level conformance checker that fails when any of these contract elements is missing from the specification.
- Provenance: every item recorded in execution/_registry/governance-additions.tsv as a USER_DIRECTIVE governance addition.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not add BLOCKED as an eighth value of Task.status. UR-009 fixes seven, and amending it is an open decision — see RC-02.
- Do not edit execution/_registry/v2-requirements.tsv. Its rows carry source-derived provenance; these items are a user directive and belong in governance-additions.tsv.
- Do not attribute any item here to SRC-01 or SRC-02, and do not cite the unsupplied engineering-project-governance document — see GAP-07.
- Do not implement the Manus API integration. OD-V2-12 records the decision and its limits; adoption is not granted.
- Do not write migrations, services or database code. This prompt fixes contracts; P03 and P04 implement them.

4. FILES AND MODULES AFFECTED
- execution/API_AND_EVENT_CONTRACTS.md — section 7, the ten entity contracts
- execution/_registry/governance-additions.tsv — the provenance registry for these items
- execution/_registry/gap-report.md — GAP-07 and RC-02
- execution/OPEN_DECISIONS.md — OD-V2-12
- execution/_tools/check_governance_contracts.py — the conformance checker

5. REQUIRED CONTRACTS
- Request: UNIQUE (converted_project_id) WHERE converted_project_id IS NOT NULL, and status='converted' if and only if converted_project_id IS NOT NULL.
- Project: UNIQUE (tenant_id, public_code); public_code is not a reversible encoding of id, is never a key, and carries no ordinal meaning.
- Project.lifecycle and Task.status share no value and are never derived from one another.
- Task.status is exactly queued, validating, running, waiting-for-input, human-review, completed, failed. BLOCKED is not a member.
- Task: blocked=true implies block_code, block_reason, blocked_owner, blocked_at and next_action are all non-empty.
- DeliveryManifest: state READY requires every reference — project, recipient, tasks, evidence, review decisions, files, version — to resolve to an existing record; a SENT manifest is immutable and a correction is a new version.
- Accreditation: type is INTERIM or OFFICIAL; OFFICIAL requires a non-empty provider_ref and a recorded provider accreditation decision; INTERIM is never displayed, exported or printed as OFFICIAL.
- OutboxEvent: the domain change and its OutboxEvent are written in one transaction; idempotency_key is UNIQUE; status=PUBLISHED if and only if published_at is non-null.

6. IMPLEMENTATION INSTRUCTIONS
- Enforce the Request-to-Project cardinality in the schema. A unique partial index holds under concurrency; an application check does not.
- Generate public_code from a source independent of the UUID. Any encoding of the id bytes — hex, base32, base58, base64 — is a reveal, not an identifier.
- Keep the two vocabularies physically separate: separate enum types, separate columns, no shared constant.
- Model blocking as attributes and leave the seven statuses untouched. A blocked task may sit in any of the seven; blocking describes an obstacle, not a position.
- Write the domain change and the outbox row in the same transaction, and publish from a separate reader of PENDING rows. Publishing before commit is the defect this contract exists to prevent.
- On publish failure, increment publish_attempts, record last_error, and leave the row claimable. Past the limit, move it to DEAD_LETTER where an operator can see it.
- Record every item's provenance as NEW USER DIRECTIVE / GOVERNANCE ADDITION. Do not back-date it onto a supplied source.

7. SECURITY REQUIREMENTS
- tenant_id is non-nullable on all ten entities and its scope is enforced in the data layer, not in application code alone.
- public_code must not leak tenant size, creation order or internal identifiers; it is a public surface and is treated as one.
- AuditEvent and UsageRecord are append-only, with UPDATE and DELETE withdrawn from the application role by database privilege.
- An INTERIM accreditation shown or exported as OFFICIAL is a misrepresentation of professional standing, not a display bug. Describing a login page, a CAPTCHA or a public search as government verification or official accreditation is prohibited.
- The outbox payload carries references, not secrets, and never a credential or a full evidence body.

8. AUTOMATED TESTS
- A Request cannot be linked to more than one Project: inserting a second Request pointing at the same project is rejected.
- public_code is unique per tenant and is not a reversible encoding of the project UUID.
- Task.status accepts exactly the seven values and rejects BLOCKED.
- blocked=true without block_code, block_reason, blocked_owner, blocked_at or next_action is rejected, one test per field.
- An INTERIM accreditation cannot be displayed or exported with the word OFFICIAL on any surface.
- A DeliveryManifest reaching READY with any dangling reference is rejected.
- The domain change and its OutboxEvent are written atomically: a failure after the domain write leaves no outbox row, and a failure after the outbox write leaves no domain change.
- Outbox publication is idempotent: re-publishing the same idempotency_key produces no second effect.
- Tenant isolation holds for all ten new entities: a principal outside the tenant reads zero rows.

9. ACCEPTANCE CRITERIA
- Every field, relation and constraint named in section 7 is present in the specification, proven by a checker that fails when one is removed.
- The seven task statuses are unchanged and BLOCKED is absent from them.
- Every item carries USER_DIRECTIVE provenance and none is attributed to a supplied source.
- RC-02, GAP-07 and OD-V2-12 are registered and linked to this prompt.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- check_governance_contracts.py output listing each entity and each required element with its result.
- A transcript showing the checker failing on an injected defect for each of its checks, so a PASS means something.
- The governance-additions.tsv rows, with their contract references resolving to section 7.
- The RC-02, GAP-07 and OD-V2-12 entries, each naming its owner and what it blocks.

11. ROLLBACK INSTRUCTIONS
Revert the specification commit. No database object, service or migration is created by this prompt, so there is nothing to un-apply. Do not remove the RC-02, GAP-07 or OD-V2-12 entries on a rollback: a recorded conflict survives the revert of the change that found it.

12. DEFINITION OF DONE
- The ten entity contracts are complete at field, relation and constraint level.
- The transactional outbox is a contract with all eleven fields and its atomicity, retry and de-duplication rules.
- BLOCKED is an attribute and not a status, and UR-009 is unchanged.
- The checker is wired into execution/_tools/validate_v2.py and proven able to fail.
- Status recorded as DESIGNED. No implementation is claimed.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


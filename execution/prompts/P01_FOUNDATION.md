<!-- promptmeta
id: P01
file: P01_FOUNDATION.md
stage: 1 — Foundation
title_en: Repository, environments, CI and audited change control
prereq: P00
requirements: UR-012,UR-027,UR-048,UR-054
status: DESIGNED
-->

# P01_FOUNDATION — Repository, environments, CI and audited change control

**المستودع والبيئات والتكامل المستمر وضبط التغيير المدقق**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 1 — Foundation |
| المتطلب السابق | P00 |
| المتطلبات المغطّاة | UR-012، UR-027، UR-048، UR-054 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينشئ الهيكل البرمجي والبيئات الثلاث وخط التكامل المستمر وسياسة التغيير المدققة التي تحكم كل ما يليها.

**لماذا نحتاجه؟**  
المرجع يشترط في المرحلة صفر: مستودع، أسرار، بنية نظيفة، واختبار استرجاع. وبدون بوابة تغيير مدققة لا يمكن إثبات أن أي نشر لاحق مُصرّح به.

**ما المتطلبات السابقة؟**  
اكتمال P00 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
مستودع واحد ببيئات dev/staging/prod منفصلة، وخط CI يمنع الدمج عند فشل الفحص، وسجل تدقيق لكل تغيير في الإعدادات.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا نجح دمج فرع يخالف الفحوص، أو إذا أمكن تغيير إعداد إنتاجي دون قيد في سجل التدقيق.

## EXECUTABLE PROMPT

```text
You are executing P01_FOUNDATION of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Stand up the repository, the three isolated environments, the continuous integration pipeline and the audited change-control path, so that every later prompt lands in a system where unreviewed change is impossible.

2. DEPENDENCIES
P00 — the environment inventory establishes what already occupies the target accounts.

3. EXACT SCOPE
IN SCOPE:
- Monorepo or polyrepo layout with an explicit service boundary per the service catalog.
- Three isolated environments: development, staging, production. Separate credentials, separate data stores, no shared secrets.
- CI pipeline: dependency install, lint, format check, type check, unit tests, build, and a secret scan. Every step blocking.
- Branch protection requiring CI pass and at least one human review before merge to the default branch.
- Secret management: a vault or managed secret store with references in configuration and no literal secrets in the repository.
- Structured logging, trace context propagation and a health endpoint convention shared by all services.
- An audit log table and write path that records actor, action, target, before-state reference, after-state reference and timestamp.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not provision production infrastructure that incurs paid usage without explicit authorization.
- Do not configure DNS or any public ingress.
- Do not implement any business domain service. Those begin at P02.

4. FILES AND MODULES AFFECTED
- Repository root configuration (package manifests, lockfiles, formatter and linter configuration)
- ci/ pipeline definition
- infra/ environment definitions as code
- packages/platform-core/ — logging, tracing, config loading, error taxonomy
- packages/audit/ — audit event schema and write path

5. REQUIRED CONTRACTS
- AuditEvent: { event_id, occurred_at, actor_type, actor_id, action, target_type, target_id, before_ref, after_ref, request_id, trace_id, outcome }.
- Every service exposes GET /healthz (liveness) and GET /readyz (readiness including dependency checks).
- Configuration is loaded from environment with a typed schema; an unknown or missing required key fails startup rather than defaulting.

6. IMPLEMENTATION INSTRUCTIONS
- Fail startup on missing configuration. A service that starts with a silently defaulted secret is a security defect, not a convenience.
- Make the audit write path append-only at the database level. Revoke UPDATE and DELETE on the audit table from the application role.
- Propagate a trace identifier from the edge through every service call and into every model invocation record.
- Make the CI secret scan blocking. A detected secret fails the build; it does not warn.
- Keep the environments genuinely isolated: a staging credential must not authenticate against production.

7. SECURITY REQUIREMENTS
- No secret literal in the repository, in CI logs, or in any committed configuration file. Only secret references.
- The production deployment path requires an approval that a single actor cannot grant to themselves.
- Audit rows are immutable to the application role, enforced by database grant, not by application convention.
- CI runs with least-privilege credentials scoped to the environment it targets.

8. AUTOMATED TESTS
- Unit: configuration loader rejects a missing required key and rejects an unknown key.
- Unit: audit event serialisation round-trips and rejects a row missing actor or action.
- Integration: an attempt to UPDATE or DELETE an audit row with the application role is rejected by the database.
- Integration: a staging credential fails to authenticate against the production data store.
- CI self-test: a branch containing a planted dummy secret fails the pipeline.

9. ACCEPTANCE CRITERIA
- CI blocks merge on any failing step.
- A commit containing a planted test secret is rejected by the pipeline.
- Audit rows cannot be mutated by the application role.
- The three environments authenticate independently.
- A restore of the primary data store from backup succeeds in a non-production environment and the restored data is verified, not merely reported.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- A CI run URL showing all steps green on the merge commit.
- A CI run URL showing the planted-secret branch failing, with the failing step named.
- A database transcript showing the rejected UPDATE and DELETE on the audit table.
- A restore rehearsal transcript showing the backup identifier, the restore command, and a row-count or checksum comparison against the source.

11. ROLLBACK INSTRUCTIONS
Revert the commit and re-run the pipeline. Infrastructure defined as code is rolled back by applying the previous revision; record the applied revision identifier before and after. No data migration occurs in this prompt, so no data rollback is required.

12. DEFINITION OF DONE
- CI is blocking and green on the default branch.
- The restore rehearsal is evidenced, not merely documented.
- Audit immutability is proven by a rejected write, not asserted.
- Status recorded as TESTED once all automated tests pass in CI and the restore rehearsal transcript is attached.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


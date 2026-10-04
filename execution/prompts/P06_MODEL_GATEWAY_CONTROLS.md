<!-- promptmeta
id: P06
file: P06_MODEL_GATEWAY_CONTROLS.md
stage: 2 — Model Gateway
title_en: Budgets, fallback, prompt cache, output validation and usage ledger
prereq: P05
requirements: UR-030,UR-034,UR-035,UR-036
status: DESIGNED
-->

# P06_MODEL_GATEWAY_CONTROLS — Budgets, fallback, prompt cache, output validation and usage ledger

**الميزانيات والبدائل وذاكرة التلقين والتحقق من المخرجات وسجل الاستهلاك**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 2 — Model Gateway |
| المتطلب السابق | P05 |
| المتطلبات المغطّاة | UR-030، UR-034، UR-035، UR-036 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يضيف إلى البوابة ضوابط التكلفة والبدائل المعتمدة وذاكرة التلقين والتحقق من المخرجات وسجل استهلاك قابل للتدقيق.

**لماذا نحتاجه؟**  
المرجع يشترط الحفاظ على التنفيذ الدائم وسجل الاستهلاك ومحاسبة التكلفة والبدائل كخدمات جديدة مُختبَرة مستقلة، وكفاءة الرموز دون تدهور الجودة.

**ما المتطلبات السابقة؟**  
اكتمال P05 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
ميزانيات ملزمة، وبدائل لا تخرج عن قائمة السماح، وذاكرة تلقين تُبطَل بالإصدار، وسجل استهلاك بالريال السعودي لكل وكيل ومشروع.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا تجاوز استدعاء ميزانية ملزمة، أو إذا أعادت ذاكرة التلقين نتيجة من إصدار تلقين مُبطَل.

## EXECUTABLE PROMPT

```text
You are executing P06_MODEL_GATEWAY_CONTROLS of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Complete the Model Gateway with the cost, resilience, efficiency and accountability controls the reference requires, implemented as new independently tested services rather than reused legacy components.

2. DEPENDENCIES
P05 — the router and adapters must exist before budgets and fallback can constrain them.

3. EXACT SCOPE
IN SCOPE:
- Budget controller: per-tenant, per-project and per-agent budgets with hard and soft limits; a hard limit blocks, a soft limit alerts.
- Fallback controller: an ordered, approved fallback chain per task type, with no fallback outside the allowlist.
- Prompt cache keyed by prompt version plus input digest, invalidated by version, never by time alone.
- Context compiler: task-scoped retrieval and provenance-preserving compression into structured facts.
- Output validator: schema validation, required citation presence for critical findings, and refusal on validation failure.
- Usage ledger: tokens and SAR cost attributed to agent, project, tenant and workflow run.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not implement customer-facing pricing or invoicing. The ledger is an internal accounting record.
- Do not implement the knowledge base itself. The context compiler consumes P09's retrieval interface.
- Do not set a cost threshold without a recorded authorization; an unset threshold blocks rather than defaults.

4. FILES AND MODULES AFFECTED
- services/model-gateway/budget/
- services/model-gateway/fallback/
- services/model-gateway/cache/
- services/model-gateway/context/
- services/model-gateway/validation/
- services/model-gateway/ledger/
- db/migrations/ — budget, usage_record, prompt_version, cache_entry

5. REQUIRED CONTRACTS
- Budget check runs before execution and after estimation. An invocation whose estimated cost would breach a hard limit is refused with BUDGET_EXCEEDED naming the breached scope.
- A budget whose limit has never been set returns BUDGET_NOT_CONFIGURED and blocks. It must never be treated as unlimited.
- Cache key = hash(prompt_version_id, normalised_inputs, model_candidate_id, policy_version). A change to any component is a miss.
- UsageRecord: { invocation_id, tenant_id, project_id, workflow_run_id, agent_version_id, model_candidate_id, input_tokens, output_tokens, cost_sar, cost_source, recorded_at }. cost_source names where the rate came from.
- Where a rate card entry is absent, cost_sar is recorded as RATE_CARD_INCOMPLETE rather than as zero.
- Output validation failure returns a typed refusal to the caller. A failed validation never returns the unvalidated output with a warning.

6. IMPLEMENTATION INSTRUCTIONS
- Make budget enforcement synchronous and pre-execution. A post-hoc budget report is accounting, not a control.
- Invalidate the cache on prompt version change by key construction, not by a scheduled sweep. A stale entry must be unreachable, not merely eventually removed.
- Compress context into structured facts that retain a provenance reference to the original artifact. Never discard the original.
- Deduplicate near-identical work only within the same authorized project context. A cache hit across tenants is a tenancy breach, so include tenant in the key.
- Record the usage ledger entry even when the invocation fails, so failed spend is visible.
- Where a safety-critical task's validation fails, escalate to human review rather than retrying with a weaker model.

7. SECURITY REQUIREMENTS
- The cache must not permit cross-tenant or cross-project reads. Prove it by including tenant and project in the key and by an explicit test.
- Compressed context is still customer data and carries the same access control and retention as the original.
- Budget overrides require an authorization that is audited and cannot be granted by the requesting principal.
- The usage ledger is append-only to the application role.
- Validation refusals and their reasons are logged without logging the rejected content verbatim where that content may be sensitive.

8. AUTOMATED TESTS
- Unit: a hard-limit breach refuses before execution; the adapter is never called, proven by a call spy.
- Unit: an unset budget returns BUDGET_NOT_CONFIGURED and does not execute.
- Unit: a missing rate card entry yields RATE_CARD_INCOMPLETE and never 0.
- Unit: changing prompt_version, policy_version, candidate or inputs each independently produces a cache miss.
- Integration: a cache lookup under tenant B never returns an entry written under tenant A, across a generated tenant matrix.
- Integration: fallback never selects an endpoint outside the allowlist, across a generated failure matrix.
- Integration: a failed invocation still writes a usage record.
- Integration: a safety-critical validation failure escalates to human review and does not retry on a weaker candidate.

9. ACCEPTANCE CRITERIA
- No invocation executes past a breached hard limit, proven by an adapter call spy.
- No cache entry crosses a tenant or project boundary.
- No fallback reaches an unapproved endpoint under any injected failure.
- Unset budgets and missing rates block or mark themselves; they never silently default.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- Adapter call-spy output for the budget-breach test.
- The cross-tenant cache matrix test output.
- The fallback failure-matrix test output.
- A usage ledger extract showing cost_source on each row and at least one RATE_CARD_INCOMPLETE row where rates are genuinely absent.

11. ROLLBACK INSTRUCTIONS
Revert the deployment. Flush the prompt cache on rollback, because a cache written under a newer key construction may be unreadable or, worse, readable with different semantics. Usage ledger rows are append-only and are never removed by a rollback; they remain as the record of what was spent.

12. DEFINITION OF DONE
- Budgets block before execution, proven by a spy rather than by a log line.
- The cache is proven tenant-safe by a generated matrix, not by inspection.
- RATE_CARD_INCOMPLETE appears wherever rates are genuinely absent, and no zero cost is recorded in its place.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


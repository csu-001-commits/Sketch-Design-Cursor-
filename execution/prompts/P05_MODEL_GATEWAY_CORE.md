<!-- promptmeta
id: P05
file: P05_MODEL_GATEWAY_CORE.md
stage: 2 — Model Gateway
title_en: Model Gateway: capability registry, routing sequence and provider adapters
prereq: P04
requirements: UR-015,UR-029,UR-031,UR-032,UR-033,UR-034
status: DESIGNED
-->

# P05_MODEL_GATEWAY_CORE — Model Gateway: capability registry, routing sequence and provider adapters

**بوابة النماذج: سجل القدرات وتسلسل التوجيه ومحوّلات المزوّدين**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 2 — Model Gateway |
| المتطلب السابق | P04 |
| المتطلبات المغطّاة | UR-015، UR-029، UR-031، UR-032، UR-033، UR-034 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يبني بوابة النماذج كخدمة إنتاجية مشتركة بتسلسل توجيه ثابت لا يُتجاوَز، ومحوّلات مزوّدين خلف واجهة واحدة.

**لماذا نحتاجه؟**  
المرجع يعلن تقاعد AI Core القديم، ويمنع التوجيه الصامت إلى نقطة غير معتمدة، ويشترط أن يسبق التحقق من أهلية الأدوات الحتمية أي استدعاء لنموذج.

**ما المتطلبات السابقة؟**  
اكتمال P04 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
بوابة واحدة تمر عبرها كل استدعاءات النماذج، بتسلسل توجيه مُنفَّذ ومُختبَر، وسجل قدرات لكل مهمة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا أمكن استدعاء أي مزوّد خارج البوابة، أو إذا أعاد الموجّه مسارًا إلى نقطة غير مدرجة في قائمة السماح.

## EXECUTABLE PROMPT

```text
You are executing P05_MODEL_GATEWAY_CORE of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Build the Model Gateway as the single shared production service through which every model invocation passes, with the reference's ten-step routing sequence implemented in order and no path that bypasses it.

2. DEPENDENCIES
P04 — model invocations are made from tasks the orchestrator owns, and must carry its trace context.

3. EXACT SCOPE
IN SCOPE:
- Capability registry: per-task capability declarations with a per-task quality score. A single global model score is prohibited.
- The routing sequence implemented in order: task classification, data sensitivity and residency gate, deterministic-tool eligibility, modality and Arabic proficiency, candidate allowlist, quality and latency SLO, price and capacity aware choice, execution, output validation, approved fallback or human escalation.
- Provider adapters behind one internal interface, one adapter per provider, with no provider type leaking into caller code.
- The four provider tiers with their entry requirements recorded as registry metadata: direct enterprise, approved aggregation gateway, deterministic engines, embedding and retrieval.
- A ModelInvocation record for every call, successful or not.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not select, procure or contract any vendor. The registry holds candidates whose approval state is recorded, and an unapproved candidate is not routable.
- Do not implement budgets, caching, fallback execution or the usage ledger. Those are P06.
- Do not incur paid API usage without explicit written authorization recorded in the run.

4. FILES AND MODULES AFFECTED
- services/model-gateway/
- services/model-gateway/routing/ — the ordered router
- services/model-gateway/adapters/ — one module per provider
- services/model-gateway/registry/ — capability and candidate registry
- db/migrations/ — model_candidate, capability, model_invocation

5. REQUIRED CONTRACTS
- invoke(task_descriptor, inputs, policy_context) -> { output, invocation_id, route, validations } or a typed refusal.
- task_descriptor carries { task_type, sensitivity_class, residency_requirement, required_modalities[], language_requirements, risk_action_class, professional_consequence_class }.
- A candidate is routable only when approval_state is APPROVED and its data-policy and benchmark gate records are present. Otherwise it is not a candidate.
- When no candidate satisfies the constraints, the gateway returns NO_ELIGIBLE_ROUTE with the failing constraint named. It never relaxes a constraint to produce an answer.
- Quality scores are per task_type. The registry schema has no column for a global score, so one cannot be recorded.

6. IMPLEMENTATION INSTRUCTIONS
- Implement the routing steps as an ordered, individually testable chain. Each step either narrows the candidate set or refuses. A step must not be skippable by configuration.
- Check deterministic-tool eligibility before any model is considered. If a deterministic engine can answer, the gateway routes there and records that it did.
- Enforce the allowlist at the adapter boundary as well as in the router, so a routing bug cannot reach an unapproved endpoint.
- Record the full route decision on every invocation: which candidates were considered, which constraint eliminated each, and why the winner won.
- Never automatically downgrade a safety-critical task to a cheaper or less capable model. Where the task's risk class forbids downgrade, the gateway refuses rather than substitutes.
- Keep the gateway free of agent logic. It routes and executes; it does not decide what the engineering task means.

7. SECURITY REQUIREMENTS
- Provider credentials live only in the gateway's secret references and are never passed to callers, logged, or returned in any response.
- The sensitivity and residency gate runs before candidate selection and cannot be bypassed by a caller-supplied override.
- Caller input is never interpolated into a provider request without the gateway's own boundary handling; untrusted document content carries no instruction authority.
- Every invocation records the principal, the tenant, the trace identifier and the policy version that permitted it.
- An invocation to an endpoint not on the allowlist is a security event: blocked, audited and alertable.

8. AUTOMATED TESTS
- Unit: each routing step tested in isolation for narrowing and for refusal.
- Unit: a candidate with approval_state other than APPROVED is never selected, for every non-approved state value.
- Unit: a task whose constraints no candidate satisfies returns NO_ELIGIBLE_ROUTE naming the failing constraint.
- Unit: the registry schema rejects an attempt to record a score not bound to a task_type.
- Integration: an adapter configured with an off-allowlist endpoint is blocked at the adapter boundary and the attempt is audited.
- Integration: a safety-critical task descriptor never routes to a candidate marked as downgrade-ineligible, across a generated matrix of risk classes.
- Integration: a sensitive-residency task refuses rather than routing to a candidate outside the required residency.
- Contract: a code search proves no service other than the gateway imports a provider SDK.

9. ACCEPTANCE CRITERIA
- Every model invocation in the system passes through the gateway, proven by a dependency check that fails if any other service imports a provider SDK.
- The routing steps execute in the reference's order, proven by an ordering test.
- No unapproved candidate can be selected under any input.
- NO_ELIGIBLE_ROUTE is returned rather than a relaxed route, proven across the constraint matrix.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The dependency-check output showing provider SDK imports confined to the gateway.
- The routing ordering test output.
- The risk-class matrix test output showing no downgrade of safety-critical tasks.
- An audit extract showing a blocked off-allowlist attempt.
- A written statement of which provider calls, if any, were executed against live endpoints, with the authorization reference. If none were executed, say so.

11. ROLLBACK INSTRUCTIONS
Revert the gateway deployment to the previous image. Because the gateway is a shared dependency, roll back only after draining in-flight invocations or allowing them to fail into the orchestrator's retry path; record the count. Registry rows are additive, so no data rollback is required; mark candidates inactive rather than deleting them.

12. DEFINITION OF DONE
- No service outside the gateway can reach a provider, proven mechanically.
- Refusal is the proven default when constraints cannot be met.
- No live paid provider call was made without a recorded authorization reference, and the evidence states explicitly which calls were and were not executed.
- Status recorded as TESTED for the routing logic. Any claim about a specific provider's behavior remains DESIGNED until that provider is approved and benchmarked.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


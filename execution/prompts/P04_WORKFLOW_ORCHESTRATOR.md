<!-- promptmeta
id: P04
file: P04_WORKFLOW_ORCHESTRATOR.md
stage: 1 — Foundation
title_en: Durable workflow orchestration, idempotency and the event feed
prereq: P03
requirements: UR-009,UR-010,UR-019,UR-023,UR-027
status: DESIGNED
-->

# P04_WORKFLOW_ORCHESTRATOR — Durable workflow orchestration, idempotency and the event feed

**محرك مسارات العمل الدائم وعدم التكرار وبث الأحداث**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 1 — Foundation |
| المتطلب السابق | P03 |
| المتطلبات المغطّاة | UR-009، UR-010، UR-019، UR-023، UR-027 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ المنسّق الذي يملك الحالة، ومفاتيح عدم التكرار، وقوائم الانتظار الدائمة، وبث الأحداث الحقيقي إلى الواجهة.

**لماذا نحتاجه؟**  
المرجع يمنع أي تقدم تمثيلي أو زمن إنجاز مُختلق، ويشترط إعادة محاولة آمنة بلا ازدواج في الآثار المُحاسَبة. هذا لا يُحقَّق إلا بمنسّق يملك الحالة.

**ما المتطلبات السابقة؟**  
اكتمال P03 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
محرك مسارات دائم بحالات محددة، وبث أحداث مصادق عليه، وإعادة محاولة لا تُكرر أثرًا قابلًا للفوترة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا أنتجت إعادة المحاولة أثرًا مزدوجًا، أو إذا ظهرت في الواجهة أي حالة غير مشتقة من حالة الخادم.

## EXECUTABLE PROMPT

```text
You are executing P04_WORKFLOW_ORCHESTRATOR of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement the durable orchestrator that owns workflow state, guarantees idempotent retry without duplicated billable side effects, and feeds the frontend only states that actually exist on the server.

2. DEPENDENCIES
P03 — workflows operate on projects and evidence packages that must already exist.

3. EXACT SCOPE
IN SCOPE:
- WorkflowRun and TaskRun entities with durable persisted state.
- The seven workflow states: queued, validating, running, waiting-for-input, human-review, completed, failed. No other state may be displayed.
- Idempotency keys on every externally triggered mutation and on every billable side effect.
- Durable queues with visibility timeouts, bounded retries, exponential backoff and a dead-letter queue.
- Circuit breakers around every outbound dependency.
- Compensating actions for side effects that cannot be made idempotent.
- An authenticated server-sent event feed emitting state transitions as they are persisted.
- Cancellation: a running workflow can be cancelled, and cancellation propagates to in-flight tasks.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not implement agent logic. The orchestrator schedules tasks; P07 implements what runs inside them.
- Do not implement model calls. Those go through P05.
- Do not emit any progress estimate, percentage or ETA that is not computed from completed task counts against a declared task plan.

4. FILES AND MODULES AFFECTED
- services/workflow/ — orchestrator, state machine, scheduler
- services/workflow/events/ — event store and SSE endpoint
- packages/idempotency/
- db/migrations/ — workflow_run, task_run, workflow_event, idempotency_key

5. REQUIRED CONTRACTS
- POST /v1/workflows: body carries { project_id, workflow_type, inputs, idempotency_key }. A repeat with the same key returns the original run, not a new one.
- GET /v1/workflows/{id}: returns durable state plus trace_id. Never a computed guess.
- GET /v1/workflows/{id}/events: authenticated SSE. Each event carries { event_id, workflow_id, task_id|null, state, occurred_at, trace_id }. Events are ordered and resumable via a Last-Event-ID.
- A billable side effect is recorded with its idempotency key before it is executed, so a crash between execution and recording cannot cause a second charge.
- Progress, where shown, is { completed_tasks, total_planned_tasks }. If total_planned_tasks is not yet determined, the API returns PLAN_NOT_ESTABLISHED and the frontend must not render a percentage.

6. IMPLEMENTATION INSTRUCTIONS
- Persist state transitions before emitting events. An event the client sees must correspond to committed state.
- Write the idempotency record in the same transaction as the side effect wherever the store permits; where it does not, write the intent first and reconcile on recovery.
- Make retry bounded and audited. Unbounded retry against a failing provider is an outage amplifier.
- Dead-letter entries are visible to operators and carry the full failure context, including the trace identifier.
- Never synthesise a time-to-completion. If the system cannot compute one from recorded data, it returns that it cannot.
- Cancellation must be honoured by long-running tasks at defined checkpoints; a task that cannot be cancelled must declare so in its definition.

7. SECURITY REQUIREMENTS
- The event feed is authenticated and authorized per workflow; a principal without read access to the project receives no events and no existence signal.
- Workflow inputs are validated against a schema before scheduling; an unvalidated input must never reach a task.
- The orchestrator runs under its own identity and cannot assume a user's privileges beyond the scoped task identity it mints.
- Idempotency keys are scoped per tenant and per principal to prevent cross-principal replay.

8. AUTOMATED TESTS
- Unit: the state machine rejects every illegal transition, driven by an exhaustive transition matrix.
- Unit: a repeated idempotency key returns the original run identifier.
- Integration: a task killed mid-execution and retried produces exactly one billable side-effect record.
- Integration: a crash injected between side-effect execution and record write is reconciled on recovery without a second charge.
- Integration: the SSE feed resumes from Last-Event-ID without gaps or duplicates.
- Integration: a principal without project access receives 404 rather than 403 from the event feed.
- Integration: cancellation terminates in-flight tasks and transitions the run to a terminal state.
- Failure injection: a dependency returning 5xx trips the circuit breaker and the run moves to failed with the dependency named.

9. ACCEPTANCE CRITERIA
- Retry after an injected crash produces exactly one billable side effect, proven by a ledger count.
- No API surface exposes a state outside the seven defined states.
- No progress percentage is emitted when the task plan is not established.
- The event feed is resumable and gap-free under an injected disconnect.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The duplicate-side-effect test output showing a ledger count of exactly one across injected crash points.
- The exhaustive state-transition matrix test output.
- An SSE resumption transcript showing Last-Event-ID continuity across a forced disconnect.
- A failure-injection report showing the circuit breaker opening and the run failing with the dependency named.

11. ROLLBACK INSTRUCTIONS
Revert the orchestrator deployment to the previous image. In-flight workflow runs must be drained or explicitly failed before rollback; never roll back with runs in a state the previous version cannot interpret. Record the count of drained and failed runs. Schema changes roll back by down migration rehearsed in staging.

12. DEFINITION OF DONE
- Exactly-once billable side effects are proven under injected crash, not argued.
- The in-flight drain procedure is written and rehearsed before the first production deployment.
- No fabricated progress exists anywhere in the API surface.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


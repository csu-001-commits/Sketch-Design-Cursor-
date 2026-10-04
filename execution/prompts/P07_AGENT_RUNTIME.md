<!-- promptmeta
id: P07
file: P07_AGENT_RUNTIME.md
stage: 2 — Model Gateway
title_en: Agent runtime: definitions, versions, tool allowlist and scoped task identity
prereq: P06
requirements: UR-014,UR-020,UR-021,UR-024,UR-025,UR-026
status: DESIGNED
-->

# P07_AGENT_RUNTIME — Agent runtime: definitions, versions, tool allowlist and scoped task identity

**تشغيل الوكلاء: التعريفات والإصدارات وقائمة الأدوات المسموحة وهوية المهمة المحصورة**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 2 — Model Gateway |
| المتطلب السابق | P06 |
| المتطلبات المغطّاة | UR-014، UR-020، UR-021، UR-024، UR-025، UR-026 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ زمن تشغيل الوكلاء: تعريف مُصدَّر لكل وكيل، وقائمة أدوات مسموحة، وهوية مهمة محصورة، وترقية بإصدار مُقيَّم ومُعتمَد بشريًا.

**لماذا نحتاجه؟**  
المرجع يعرّف الوكيل كحزمة قدرة مُصدَّرة بأحد عشر عنصرًا إلزاميًا، ويمنع الوكيل من منح نفسه صلاحية أو إحداث أثر غير قابل للتراجع.

**ما المتطلبات السابقة؟**  
اكتمال P06 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
سجل وكلاء بإصدارات مثبتة لكل تشغيل، وأدوات تعمل بأقل امتياز وبمهلة وحصة وإمكانية إلغاء، وحدود مراجعة مهنية لكل عائلة قدرة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا استدعى وكيل أداة خارج قائمته، أو إذا رُقّي إصدار إلى الإنتاج دون تقييم مرحلي واعتماد بشري.

## EXECUTABLE PROMPT

```text
You are executing P07_AGENT_RUNTIME of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement the agent runtime so that every agent is a versioned capability bundle executing under a scoped task identity and a tool allowlist, with promotion gated by staged evaluation and human approval.

2. DEPENDENCIES
P06 — agents invoke models only through the completed gateway, under its budgets and validation.

3. EXACT SCOPE
IN SCOPE:
- AgentDefinition and AgentVersion entities carrying all eleven required attributes: purpose, input schema, output schema, allowed tools, evidence policy, validation rules, escalation threshold, model policy, evaluation suite reference, cost and latency budget, rollback target.
- The seven capability families, each carrying its review boundary as data on the definition, not as documentation.
- A scoped task identity minted per TaskRun, carrying only the permissions that agent version declares.
- Tool execution with per-tool timeout, quota, cancellation support and an audit trace.
- Version pinning: a WorkflowRun records the exact AgentVersion identifier it executed and cannot be reinterpreted later under a different version.
- Promotion pipeline: a version moves to production only after its evaluation suite runs and a human approver records a decision.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not implement the engineering tool logic itself. That is P08.
- Do not implement retrieval. That is P09.
- Do not allow an agent to create an irreversible side effect. Irreversible actions belong to an authorized human path.

4. FILES AND MODULES AFFECTED
- services/agent-runtime/
- services/agent-runtime/registry/ — definitions, versions, promotion
- services/agent-runtime/sandbox/ — tool invocation under scoped identity
- db/migrations/ — agent_definition, agent_version, agent_promotion, task_identity

5. REQUIRED CONTRACTS
- AgentVersion is immutable once published. A change produces a new version; it never edits a published one.
- A TaskRun references exactly one agent_version_id and one scoped task identity. Both are recorded before the first tool call.
- Tool invocation: invoke_tool(task_identity, tool_name, args) checks tool_name against the agent version's allowlist before anything else, and refuses with TOOL_NOT_ALLOWED otherwise.
- Critical findings require typed output plus at least one source attribution. An output failing this is refused, not downgraded to a non-critical finding.
- Each capability family declares review_boundary: who must validate before the output can be relied upon. The boundary is enforced by P11, not optional.
- An agent version whose evaluation suite has not run returns EVALUATION_NOT_RUN and cannot be promoted.

6. IMPLEMENTATION INSTRUCTIONS
- Check the allowlist first, before argument validation, before any side effect. A tool not on the list must never be constructed.
- Mint the task identity from the agent version's declared permissions. Never from the invoking user's permissions, which are broader.
- Make agent versions immutable at the database level, not by convention.
- Record which agent version produced each finding, so a later regression can be attributed.
- Enforce the escalation threshold in the runtime: when confidence or risk crosses it, the task transitions to human-review rather than completing.
- Give every tool a timeout and a quota. A tool without a declared timeout fails registration.
- Honour cancellation at tool boundaries and declare any tool that cannot be cancelled.

7. SECURITY REQUIREMENTS
- Least privilege: the scoped task identity is the only credential available inside tool execution. Platform credentials are never reachable from agent code.
- An agent cannot modify its own definition, its allowlist, or any policy. Attempts are denied and audited as security events.
- Tool arguments derived from untrusted documents are validated against the tool's schema; document content never selects which tool runs.
- Every tool call is audited with task identity, tool name, argument digest and outcome.
- Resource limits (wall clock, memory, outbound calls) are enforced by the sandbox, not requested politely of the agent.

8. AUTOMATED TESTS
- Unit: every one of the eleven AgentVersion attributes is required; one rejection test per attribute, generated from the schema.
- Unit: an attempt to mutate a published AgentVersion is rejected at the database level.
- Unit: a tool registered without a timeout fails registration.
- Integration: a tool call outside the allowlist is refused before construction, proven by a constructor spy that is never reached.
- Integration: a critical finding without a source attribution is refused and never silently reclassified.
- Integration: an agent attempting to alter its own allowlist is denied and a security audit row is written.
- Integration: crossing the escalation threshold transitions the task to human-review, across a generated threshold matrix.
- Integration: promotion is blocked when the evaluation suite has not run.
- Integration: a scoped task identity cannot read a resource outside its agent version's declared permissions.

9. ACCEPTANCE CRITERIA
- No tool outside the allowlist can be constructed, proven by an unreached constructor spy.
- Published agent versions are immutable, enforced by the database.
- Every critical finding carries a source attribution or is refused.
- Promotion without evaluation and human approval is impossible.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The generated per-attribute rejection test output.
- A database transcript showing the rejected mutation of a published version.
- The allowlist constructor-spy test output.
- An audit extract showing a denied self-modification attempt.
- A promotion record showing the evaluation run reference and the named human approver.

11. ROLLBACK INSTRUCTIONS
Each agent version declares a rollback_target. Rolling back means repinning the workflow definition to the target version; it never means editing the failing version. In-flight runs continue on their pinned version and are not retargeted mid-run. Record the repinned version identifier and the count of runs still on the previous version.

12. DEFINITION OF DONE
- All eleven attributes are enforced individually.
- Allowlist refusal is proven before construction, not after.
- Every agent version has a reachable rollback_target, verified by a test that resolves each one.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


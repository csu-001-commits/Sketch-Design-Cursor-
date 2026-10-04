<!-- promptmeta
id: P16
file: P16_ADMIN_CONTROL_PLANE.md
stage: 6 — Launch readiness
title_en: Admin Control Plane: roles, capability matrix and authorized destructive actions
prereq: P15
requirements: UR-013,UR-037,UR-042,UR-043,UR-007
status: DESIGNED
-->

# P16_ADMIN_CONTROL_PLANE — Admin Control Plane: roles, capability matrix and authorized destructive actions

**لوحة التحكم الإدارية: الأدوار ومصفوفة الصلاحيات والإجراءات الحساسة المصرّح بها**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 6 — Launch readiness |
| المتطلب السابق | P15 |
| المتطلبات المغطّاة | UR-013، UR-037، UR-042، UR-043، UR-007 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ لوحة التحكم الإدارية كواجهة مدققة فوق Control Plane API، بمصفوفة صلاحيات صريحة وإجراءات حساسة تتطلب تصريحًا وتدقيقًا.

**لماذا نحتاجه؟**  
المرجع يشترط أن تكون الإدارة واجهة تحكم منفصلة لا واجهة قاعدة بيانات مباشرة، وأن يتطلب كل إجراء مدمّر أو مالي تصريحًا صريحًا وتدقيقًا.

**ما المتطلبات السابقة؟**  
اكتمال P15 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
سبعة أدوار منفصلة، ومصفوفة صلاحيات مُنفَّذة لا موصوفة، وكل إجراء حساس خلف تصريح مزدوج وسجل تدقيق.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا نفّذ أي دور إجراءً خارج مصفوفته، أو إذا تم إجراء مدمّر دون تصريح مسجّل.

## EXECUTABLE PROMPT

```text
You are executing P16_ADMIN_CONTROL_PLANE of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement the Admin Control Plane as a policy-checked frontend over a Control Plane API, with the reference's capability matrix enforced in code and every destructive or financial action behind explicit authorization and audit.

2. DEPENDENCIES
P15 — the console administers systems that must already exist to be administered.

3. EXACT SCOPE
IN SCOPE:
- The seven separated roles from P02, now exercised: founder, platform admin, security, support, engineering reviewer, finance, read-only auditor.
- The eight-capability matrix enforced: agent version release, provider and route configuration, connector and API key management, project and task trace inspection, pause and retry of failed execution, engineering evidence review, billing and budget controls, security incident and audit export.
- Dashboard actions: inspect trace, compare model versions, disable route, roll back configuration, pause queue, retry idempotent tasks only, rotate secret references, acknowledge incidents.
- Connector lifecycle: proposal, scope, sandbox test, security approval, vault storage, deploy, health monitor, rotate and revoke.
- Break-glass access with approval, expiry and full audit.
- Support views with masked personal data by default.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not provide any direct database query surface.
- Do not allow retry of a non-idempotent task; the reference limits retry to idempotent tasks and support to limited safe retry.
- Do not display raw provider secrets anywhere in the interface.

4. FILES AND MODULES AFFECTED
- apps/admin/
- services/control-plane/
- services/control-plane/connectors/
- services/control-plane/breakglass/

5. REQUIRED CONTRACTS
- Every control-plane action declares its required capability and its risk class. An action without both fails registration.
- A destructive or financial action requires a second authorized approver who is not the requester, recorded before execution.
- Retry endpoint accepts only tasks whose definition declares idempotency; a non-idempotent task returns RETRY_NOT_PERMITTED.
- Connectors store secret references only; the API never returns a secret value, and the response schema has no field capable of carrying one.
- Break-glass grants are time-boxed, scoped and automatically revoked; an active grant is visible on the security dashboard.

6. IMPLEMENTATION INSTRUCTIONS
- Derive the interface from the capability matrix rather than hand-coding each screen's permissions, so the matrix is the single source and drift is impossible.
- Enforce authorization server-side for every action; hiding a button is presentation, not security.
- Make the two-person rule structural: the approval record is a foreign key the execution path requires, not a check it performs.
- Mask personal data by default in support views and require a recorded, expiring unmask with a stated reason.
- Make configuration rollback a first-class action with a recorded previous-state reference, so rollback is one authorized click rather than a manual reconstruction.
- Never expose a secret value. Build the response schema so a secret cannot be carried even by mistake.

7. SECURITY REQUIREMENTS
- The console is a client of the Control Plane API with no privileged database access.
- Every action is audited with actor, approver, before-state reference, after-state reference and outcome.
- Break-glass requires approval, is time-boxed, and alerts the security role on grant and on use.
- Session handling for administrative roles uses stronger requirements than customer sessions, including re-authentication for destructive actions.
- Audit export is itself an audited action and is restricted to the roles the matrix permits.

8. AUTOMATED TESTS
- Matrix: a generated test asserts, for every role and every capability in the matrix, that permitted actions succeed and non-permitted actions are denied. The matrix is read from the same definition the application uses.
- Integration: a destructive action without a second approver is refused at the service layer.
- Integration: the requester cannot be the approver.
- Integration: a non-idempotent task returns RETRY_NOT_PERMITTED.
- Contract: a schema test proves no control-plane response type can carry a secret value.
- Integration: break-glass expires automatically and the expiry is audited.
- Integration: support views mask personal data by default and unmasking requires a recorded reason.

9. ACCEPTANCE CRITERIA
- The full role-by-capability matrix passes, generated from the same definition the application enforces.
- No destructive or financial action can execute without a distinct second approver.
- No response schema can carry a secret.
- Break-glass is time-boxed, alerting and audited.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The generated matrix test output showing every role-capability cell and its result.
- The two-person rule test output, including the self-approval refusal.
- The schema test output proving no secret-bearing response type exists.
- An audit extract for one break-glass grant, use and automatic expiry.

11. ROLLBACK INSTRUCTIONS
Control-plane rollback is a deployment revert plus a configuration revert using the recorded previous-state reference. Because the console can itself roll back configuration, ensure the rollback action is available in the previous version too; never ship a rollback capability that only exists in the version being rolled back.

12. DEFINITION OF DONE
- The capability matrix is enforced from a single definition and fully tested.
- Two-person control is structural, not procedural.
- No secret can traverse the API by construction.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


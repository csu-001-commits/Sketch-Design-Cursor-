<!-- promptmeta
id: P02
file: P02_IDENTITY_AND_TENANCY.md
stage: 1 — Foundation
title_en: Identity, organizations, tenancy boundary and RBAC
prereq: P01
requirements: UR-006,UR-008,UR-017,UR-042,UR-045,UR-046,UR-047
status: DESIGNED
-->

# P02_IDENTITY_AND_TENANCY — Identity, organizations, tenancy boundary and RBAC

**الهوية والمنظمات وحدود العزل وصلاحيات الأدوار**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 1 — Foundation |
| المتطلب السابق | P01 |
| المتطلبات المغطّاة | UR-006، UR-008، UR-017، UR-042، UR-045، UR-046، UR-047 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ الهوية والأدوار وحدود العزل بين المشاريع والمستأجرين، مع إبقاء عقود B2B جاهزة دون فتح البيع الذاتي.

**لماذا نحتاجه؟**  
المرجع يحجز كيان Tenant من اليوم الأول ويمنع أي تقاطع بين المستأجرين في البيانات والسجلات والملفات والفوترة. فتح هذا لاحقًا يعني إعادة كتابة طبقة التصريح بالكامل.

**ما المتطلبات السابقة؟**  
اكتمال P01 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
نموذج هوية وأدوار منفصلة، وعزل مُثبَت باختبار، ومسار تسجيل ذاتي للأفراد والمهندسين، ومسار مبيعات للمؤسسات.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا نجح أي استعلام في قراءة بيانات مستأجر آخر، بما في ذلك عبر السجلات أو الملفات أو ذاكرة التخزين المؤقت.

## EXECUTABLE PROMPT

```text
You are executing P02_IDENTITY_AND_TENANCY of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement identity, the organization and tenant model, the seven separated roles and the authorization boundary that no later service may cross, while keeping B2B contracts present and self-service commerce closed.

2. DEPENDENCIES
P01 — audit log and configuration loading must exist before any authorization decision can be recorded.

3. EXACT SCOPE
IN SCOPE:
- Entities: Tenant, Organization, User, Role, and the membership relations between them.
- Seven separated roles: founder, platform admin, security, support, engineering reviewer, finance, read-only auditor. Plus the customer-facing roles: individual, engineer.
- Self-registration for individuals and engineers, subject to verification rules; engineer accounts carry a verification state that gates professional actions.
- Institutional path: a Contact Sales lead capture that creates a lead record and a managed onboarding task. No agent seat purchase.
- A single authorization decision point that every service calls; services never implement their own rules.
- Tenant scoping enforced at the data layer, not only in application code.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not implement subscriptions, entitlements, billing or a self-service marketplace. Those are deferred by the reference.
- Do not implement white-label branding configuration.
- Do not grant any role the ability to approve its own privileged change.

4. FILES AND MODULES AFFECTED
- services/identity/ — registration, verification, session, role assignment
- services/policy/ — the authorization decision point and policy definitions
- packages/tenancy/ — tenant context propagation and data-layer scoping
- db/migrations/ — tenant, organization, user, role, membership, lead

5. REQUIRED CONTRACTS
- Every authenticated request carries a resolved principal: { user_id, tenant_id, organization_id, roles[], verification_state }.
- Authorization decision: decide(principal, action, resource) -> { allow: boolean, reason, policy_version }. A denial always carries a reason and is audited.
- Every tenant-scoped table carries a non-nullable tenant_id, and row-level security or an equivalent enforced predicate restricts access to the request's tenant.
- Lead: { lead_id, organization_name, contact, requested_capabilities[], source, state, created_at }.

6. IMPLEMENTATION INSTRUCTIONS
- Enforce tenant scoping in the database with row-level security or an equivalent mandatory predicate. Application-side filtering alone is insufficient and must not be the only control.
- Make the authorization decision point the single source of truth. A service that embeds its own role check is a defect.
- Keep the Tenant entity present and populated from day one even though only one tenant exists at launch. Do not add it later.
- Record every allow and every deny in the audit log with the policy version that decided it.
- Engineer verification is a state, not a boolean flag on a profile: unverified, pending, verified, revoked. Professional sign-off requires verified.
- Institutions route to Contact Sales. Do not build a purchase flow and disable it; do not build it at all.

7. SECURITY REQUIREMENTS
- Default deny. An action with no matching policy is denied and audited, never allowed.
- Session tokens are short-lived with rotation; revocation takes effect at the decision point, not only at token expiry.
- No role may approve its own privileged change. Enforce separation of duties in the policy, not in a runbook.
- Cross-tenant access attempts are a security event: audited, counted and alertable.
- Password and credential handling follows current practice for hashing and rate limiting; never store a recoverable credential.

8. AUTOMATED TESTS
- Unit: decide() returns deny with a reason for an unmapped action.
- Unit: engineer verification state transitions reject illegal transitions.
- Integration: a query issued under tenant A's context returns zero rows from tenant B, for every tenant-scoped table, driven by a table-enumerating test rather than a hand-written list.
- Integration: a direct database query with the application role and a forged tenant_id predicate is rejected by row-level security.
- Integration: an attempt by a role to approve its own privileged change is denied and audited.
- Integration: a revoked session is denied at the decision point before token expiry.

9. ACCEPTANCE CRITERIA
- No query under one tenant context can read another tenant's rows in any tenant-scoped table.
- Every authorization denial carries a reason and an audit row.
- Engineer professional actions are blocked unless verification_state is verified.
- The institutional path creates a lead and never a purchase.
- Self-approval of a privileged change is denied.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The cross-tenant isolation test output, listing every table it enumerated and asserting zero cross-tenant rows for each.
- A database transcript showing row-level security rejecting a forged predicate.
- Audit log extracts for one allow and one deny, each showing the policy version.
- The separation-of-duties test output.

11. ROLLBACK INSTRUCTIONS
Roll back by reverting the service deployment to the previous image and applying the down migration for the schema change. Because this prompt introduces tenant_id as non-nullable, the down migration must be rehearsed in staging and its data-loss behavior recorded before production is touched.

12. DEFINITION OF DONE
- The table-enumerating cross-tenant test passes with zero exceptions and its enumeration covers every tenant-scoped table present in the schema.
- Default deny is proven by a test, not asserted.
- The down migration has been rehearsed in staging with its outcome recorded.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


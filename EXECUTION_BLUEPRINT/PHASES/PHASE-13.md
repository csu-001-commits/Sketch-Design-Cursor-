# PHASE-13 — لوحة التحكم الإدارية والموصلات والدعم

<!-- phasemeta
id: PHASE-13
depends_on: [PHASE-01, PHASE-04, PHASE-12]
criticality: P0
-->

## الغرض من المرحلة

الورقة 68 الصف 4 تحدد المعمارية الحاكمة للإدارة بعبارة لا تقبل التأويل:
«Admin Console → authenticated Platform API → policy/approval → workflow/agent
runtime. Never direct browser-to-agent or database».

والورقة 57 الصف 3 (`A02`) تسجّل الفجوة بأولوية `CRITICAL`: «عمليات الإدارة تفتقر
إلى عقود تفويض وتدقيق كاملة»، والأثر «إساءة استخدام الصلاحية». والورقة 67 الصف 3
تضع المرحلة الأولى في خطة الإصدار: «لوحة تحكم إدارية للقراءة فقط + تدقيق».

## شروط الدخول

- اكتمال `PHASE-01` (الهوية والسياسة والتدقيق) و`PHASE-04` (البوابة).

## شروط الخروج

- عدم وجود أي مسار مباشر من المتصفح إلى وكيل أو قاعدة بيانات.
- مصفوفة RBAC الإدارية مفروضة باختبارات سلبية.
- تحكم مزدوج على أسرار وسياسات الإنتاج.
- تسجيل واختبار وتدوير وإبطال الموصلات مُثبت.
- انتهاء break-glass آلياً.

## المتطلبات المغطاة في هذه المرحلة

`REQ-GOV-03`, `REQ-ADM-01`..`REQ-ADM-07`, `REQ-API-09`, `REQ-SEC-01`,
`REQ-GW-12`, `REQ-OBS-04`

---

## الأوامر التنفيذية

### P13-01 — مستوى التحكم والحد المعماري

<!-- meta
id: P13-01
phase: PHASE-13
title_en: Admin control plane and the architectural boundary
prereq: [P12-03]
requirements: [REQ-GOV-03, REQ-ADM-03, REQ-ADM-06, REQ-API-09]
-->

**ماذا سينفذ هذا الأمر؟** يبني مستوى التحكم الإداري بوصفه طبقة أوامر خلف الـAPI
والسياسة، ويفرض الحد المعماري باختبار يفشل عند أي خرق.

**لماذا نحتاجه؟** الورقة 52 الصف 7 تحدد الشرط: «لا نداءات وكيل مباشرة من
المتصفح»، والورقة 52 الصف 7 تضيف «orchestrator via commands» — أي أن الإدارة
تُصدر أوامر لا تستدعي المحرك مباشرة. والورقة 67 الصف 3 تبدأ بقراءة فقط عن قصد:
عرض بلا تعريض.

**ما المتطلبات السابقة؟** `P12-03`.

**ما النتيجة المتوقعة؟** مستوى تحكم بأوامر مُنمَّطة، وقراءة مُحجَّبة، وحد معماري
مفروض.

**كيف نتحقق من نجاحه؟** اختبار معماري يفشل إن وُجد مسار من واجهة الإدارة إلى
الوكيل أو قاعدة البيانات مباشرة.

```text
TASK P13-01 — Admin control plane and the architectural boundary

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-01
   Phase: PHASE-13 (Admin control plane, connectors and support operations)
   Prerequisites: P12-03
   Requirements covered: REQ-GOV-03, REQ-ADM-03, REQ-ADM-06, REQ-API-09

B. OBJECTIVE
   Build the admin control plane as a command layer behind the authenticated
   platform API and the policy service, with read access masked by default, and
   enforce the architectural boundary with a test that fails on any violation.

   Why this is necessary: sheet 68 row 4 states the control path as console to
   platform API to policy and approval to runtime, and forbids
   browser-to-agent and browser-to-database. Sheet 52 row 7 requires the
   orchestrator be reached via commands and forbids direct browser agent calls.
   Sheet 57 row 3 (A02) records that admin operations currently lack complete
   authorization and audit contracts, with the impact of privilege abuse.
   Sheet 67 row 3 deliberately starts with a read-only console so staff can
   inspect without exposure.

   SCOPE BOUNDARY: the control plane, the command pattern, the read surface and
   the boundary test. The sixteen admin capabilities are P13-03. Connectors are
   P13-02.

C. CONTEXT
   Required inputs, sheet 52 rows 2-9, each as area / admin frontend action /
   backend authority / agent-layer relation / audit and security / acceptance:
     Organizations / create, approve, suspend / Org service / none direct /
       admin scoped plus audit / suspension blocks new runs
     Sales and contracts / lead to quote to contract / CRM and billing /
       entitlement provision only / dual approval / a signed contract gates
     Agent licenses / grant and revoke SKUs / Entitlement service / runtime
       checks policy / audit grants / an unlicensed run is denied
     Branding / review logo, theme, domain / Branding service / none / domain
       verification / theme scoped
     Knowledge / approve uploaded corpora / Knowledge service / RAG namespace
       by tenant / source license check / no tenant crossover
     Operations / view runs, errors, usage / Observability API / orchestrator
       via commands / RBAC plus redaction / no direct browser agent calls
     Quality / approve human review / Review service / agent output only /
       signed decisions / traceable signoff
     Billing / quotas, invoices, credits / Billing service / budget preflight /
       reconciliation / accurate usage
   Note: the Organizations, Sales, Agent licenses and Branding areas belong to
   the deferred commerce scope (sheet 68 row 8). Implement their read surfaces
   and the command contracts where they serve single-tenant operation, and
   leave the multi-tenant commercial behaviour to PHASE-16 without building it.

D. EXECUTION INSTRUCTIONS
   1. Implement the command pattern: every administrative mutation is a typed
      command with a name, a payload schema, a required authority, an approval
      requirement, an idempotency key and an audit contract. Commands are
      submitted to the platform API, authorized, policy-checked, recorded, and
      then dispatched to the owning service. A command's effect is never
      performed inline in a request handler that also renders a view.
   2. Implement the command log as part of the append-only audit store: who
      submitted, what, when, under which approval, with the before and after
      state and the correlation id. Sheet 58 marks nearly every admin action as
      audited, so this is the mechanism.
   3. Implement the read surface read-only and masked by default, per sheet 67
      row 3's exit criterion "staff can inspect without exposure":
        - personal data masked unless the role and the justification permit it;
        - secrets never returned, in any form, including partially;
        - cross-tenant reads denied through the P01-02 helper;
        - a justification required for any access to customer data, recorded
          with the read (sheet 58 row 3 requires a ticket and "scoped access
          plus justification").
   4. Implement the architectural boundary test, the central deliverable here:
        - assert no admin frontend asset makes a request to anything other than
          the platform API origin;
        - assert no admin backend route reaches the agent runtime or the
          database without passing the authorization and policy middleware —
          implement as a route-table or dependency-graph assertion, extending
          the P01-04 guard;
        - assert the browser bundle contains no database connection string, no
          provider credential and no direct runtime endpoint;
        - make the test fail when a violating path is introduced, and
          demonstrate it.
   5. Implement suspension semantics per sheet 52 row 2: suspending an
      organization blocks new runs immediately while leaving in-flight work and
      records intact. Add a test.
   6. Implement the operations read surface over the P10-01 traces and P10-02
      signals, with redaction, so support can diagnose without raw data access.
   7. Implement the admin API operations from sheet 65 that belong to this
      prompt: GET /v1/admin/health (ops:read, emits health.degraded) and GET
      /v1/admin/audit (audit:read, emits audit.accessed). Note that audit
      access itself emits an event — reading the audit trail is an audited act.
   8. Implement a session model for admin users with short lifetimes,
      re-authentication for sensitive reads, and no long-lived tokens.
   9. Tests:
        a. the architectural boundary test passes; then introduce a direct
           database call in an admin route and show it failing; restore it;
        b. the browser bundle scan finds no credential or direct endpoint;
        c. a customer-data read without a justification -> refused; with one ->
           permitted and the justification recorded;
        d. a secret is never returned by any admin read, including a masked
           form that would leak length or prefix;
        e. a cross-tenant admin read -> denied uniformly;
        f. suspending an organization -> new runs blocked, in-flight work
           untouched;
        g. every command produces an audit record with before and after state;
        h. reading the audit trail emits audit.accessed;
        i. a command submitted without its required approval -> refused;
        j. an admin session expires and a sensitive read requires
           re-authentication.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the typed command pattern with authority, approval, idempotency and audit
     contracts
   - the command log in the append-only store
   - the masked, justification-gated read surface
   - the architectural boundary test with its bundle scan
   - organization suspension semantics
   - the redacted operations read surface over traces and signals
   - GET /v1/admin/health and GET /v1/admin/audit with audit.accessed
   - short-lived admin sessions with re-authentication for sensitive reads
   - tests/admin/boundary-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the boundary test passing, then failing on the injected violation,
     then passing again.
   - Paste the bundle scan output.
   - Paste the case d result showing no secret is returned in any form.
   - Acceptance criterion: no path exists from the admin browser to an agent or
     the database, and the test proving it can fail.

G. COMPLETION CONTRACT
   Definition of Done: the command plane working, reads masked and justified,
   the boundary enforced and provably testable.
   Evidence to report: the three boundary test runs, the bundle scan, the
   masking proof, the command audit sample.
   Remaining blockers: the commerce-related admin areas remain deferred per
   sheet 68 row 8. Confirm you built only their single-tenant read surfaces.
   Next prompt: P13-02.
```

**المخرجات المتوقعة:** نمط أوامر مُنمَّط، سطح قراءة مُحجَّب، اختبار حد معماري قادر على الفشل.
**التحقق المطلوب:** لا مسار من المتصفح إلى وكيل أو قاعدة بيانات؛ لا سر يُرجَع بأي صورة.
**الاعتمادية التالية:** `P13-02`.

---

### P13-02 — دورة حياة الموصلات وخزانة الأسرار

<!-- meta
id: P13-02
phase: PHASE-13
title_en: Connector lifecycle and secrets vault
prereq: [P13-01]
requirements: [REQ-ADM-04, REQ-ADM-05, REQ-SEC-01, REQ-INT-04]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ مراحل الموصل الست في الورقة 60 — التسجيل
والمصادقة والتحقق والتنفيذ والفشل والإيقاف — مع خزانة أسرار وتدوير وإبطال.

**لماذا نحتاجه؟** الورقة 67 الصف 5 تضع «مدير الموصلات + خزانة الأسرار» مرحلة
`P0` بمعيار خروج: «Register/test/rotate/revoke». والورقة 58 الصف 8 تشترط «الأسرار
لا تُرجَع أبداً» وتحكماً مزدوجاً للتدوير. والورقة 60 الصف 4 تضيف ضابطاً أمنياً
محدداً: «حماية SSRF وTLS».

**ما المتطلبات السابقة؟** `P13-01`.

**ما النتيجة المتوقعة؟** مدير موصلات كامل الدورة، وخزانة أسرار لا تُرجِع قيمة
أبداً.

**كيف نتحقق من نجاحه؟** اختبار إبطال يُثبت توقف الموصل فوراً؛ واختبار SSRF يُحجَب؛
ولا قيمة سر تظهر في أي استجابة أو سجل.

```text
TASK P13-02 — Connector lifecycle and secrets vault

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-02
   Phase: PHASE-13
   Prerequisites: P13-01
   Requirements covered: REQ-ADM-04, REQ-ADM-05, REQ-SEC-01, REQ-INT-04

B. OBJECTIVE
   Implement the six-stage connector lifecycle with its security,
   observability and verification requirements, backed by a secrets vault that
   never returns a secret value.

   Why this is necessary: sheet 67 row 5 makes the connector manager and
   secrets vault a P0 phase whose exit criterion is register, test, rotate and
   revoke. Sheet 58 row 8 requires dual approval for credential rotation and
   states the secret is never returned. Sheet 60 row 4 requires SSRF protection
   and TLS at the validation stage. Sheet 57 row 5 (A04) requires per-provider
   credential, licensing and contract verification with provider sandbox
   success as evidence.

   SCOPE BOUNDARY: the connector manager and the vault integration. Do not
   onboard a provider that has no agreement — registration without a
   credential is a valid, reportable state.

C. CONTEXT
   Required inputs, sheet 60 rows 2-7, each as step / contract and behavior /
   security / observability / verification:
     Register / connector id, version, base URL, scopes, region, owner /
       allowlisted domains / audit registration / schema test
     Authenticate / OAuth2 client credentials or a signed service account /
       vault-managed keys with rotation / expiry alerts / no secrets in logs
     Validate / OpenAPI schema, test endpoint, quota / SSRF protection, TLS /
       synthetic probe / sandbox contract tests
     Execute / idempotency key, timeout, retry and backoff / least-privilege
       egress / trace and request id / provider response fixture
     Fail / circuit breaker, DLQ, fallback / no silent data transfer / error
       budget / failure injection
     Retire / disable, revoke, delete credentials / revoke token / audit trail
       / revocation test
   And sheet 65 rows 4-5: POST /v1/admin/connectors (integrations:write,
   idempotency required, emits connector.created) and POST
   /v1/admin/connectors/{id}/test (integrations:test, idempotency required,
   emits connector.tested) — note the test probe is described in sheet 65 as
   "credential-safe".

D. EXECUTION INSTRUCTIONS
   1. Implement the Connector entity with the register-stage fields: id,
      version, base URL, scopes, region, owner, plus its lifecycle state
      (REGISTERED, AUTHENTICATED, VALIDATED, ACTIVE, DEGRADED, DISABLED,
      RETIRED) and the contract and licensing references from P00-03.
   2. Enforce a domain allowlist at registration: a base URL outside the
      allowlist is rejected. The allowlist is itself a dual-approved,
      audited configuration change, not a free-text field on the connector.
   3. Integrate the secrets vault with a strict interface: write-only from the
      admin path, read-only at call time by the owning service, and no
      read-back path at all for a human or an API. The vault returns a handle
      to the admin surface, never a value. Add a test asserting no endpoint,
      log, trace, error or export returns a secret value or a prefix of one.
   4. Implement rotation with dual approval per sheet 58 row 8: two distinct
      approvers, overlapping validity so rotation is not an outage, and
      automatic revocation of the previous credential after the overlap. Record
      the rotation and emit an event. Implement expiry alerts per the
      authenticate stage's observability requirement.
   5. Implement validation with the source's three checks and two controls:
        - the connector's OpenAPI schema is fetched or supplied and validated;
        - a credential-safe test endpoint probe runs (one minimal, non-mutating
          call) and its result is recorded;
        - quota and rate limits are recorded;
        - SSRF protection: resolve and validate the target address, block
          private, loopback, link-local and metadata address ranges, re-validate
          after redirects, and pin the resolved address for the request;
        - TLS verification is mandatory and non-disableable.
      Add an explicit SSRF test suite, since a connector manager that accepts a
      base URL is the classic SSRF entry point.
   6. Implement execution through one connector client providing idempotency
      keys, timeouts, bounded retry with backoff, least-privilege egress
      (reusing the P04-04 allowlist), and trace and request id propagation.
   7. Implement the failure stage with the circuit breaker, DLQ and fallback,
      and the rule "no silent data transfer": a partial or failed transfer is
      recorded and surfaced, never dropped. Track an error budget per connector.
   8. Implement retirement: disable, revoke the token at the provider where the
      provider supports it, delete the vault entry, and keep the audit trail.
      Add the revocation test the source names: after retirement, a call attempt
      fails immediately and no cached credential works.
   9. Implement synthetic probes per the validate stage's observability
      requirement, running on a schedule and feeding the P10-02 reliability
      dashboard, so a connector that silently stopped working is detected
      before a customer finds out.
  10. Record, per connector, the A04 evidence: the agreement reference, the
      licensing basis, the credential status and the sandbox probe result.
      Report how many connectors have all four and how many do not.
  11. Tests:
        a. registration with a base URL outside the allowlist -> rejected;
        b. no path returns a secret value or prefix — assert across endpoints,
           logs, traces, errors and exports;
        c. rotation with one approver -> refused; with two -> succeeds with an
           overlap, then the old credential stops working;
        d. an expiring credential -> an alert fires;
        e. the SSRF suite: private, loopback, link-local and cloud metadata
           addresses all blocked, including after a redirect;
        f. TLS verification cannot be disabled by configuration;
        g. a schema-invalid connector -> not promoted to VALIDATED;
        h. the credential-safe probe performs exactly one non-mutating call;
        i. a connector failure -> circuit opens, DLQ records it, no silent
           drop;
        j. retirement -> immediate call failure, vault entry gone, audit trail
           intact;
        k. a synthetic probe failure -> the reliability dashboard reflects it
           and an alert fires.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the Connector entity with its seven-state lifecycle
   - the dual-approved domain allowlist
   - vault integration with no read-back path
   - dual-approved rotation with overlap and automatic old-credential
     revocation, plus expiry alerts
   - validation with schema check, credential-safe probe, quota, SSRF
     protection and mandatory TLS
   - the single connector client with idempotency, timeouts, retries and egress
     control
   - circuit breaker, DLQ, error budget and no-silent-drop handling
   - retirement with provider revocation and the revocation test
   - scheduled synthetic probes feeding the dashboard
   - the per-connector A04 evidence table
   - tests/admin/connector-*.* covering cases a through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eleven tests.
   - Paste the full SSRF suite results naming each blocked address class.
   - Paste the secret non-disclosure assertion across all five surfaces.
   - Paste the A04 evidence table with the counts.
   - Acceptance criterion: register, test, rotate and revoke all work and are
     tested; no secret is ever returned; SSRF is blocked including after
     redirects.

G. COMPLETION CONTRACT
   Definition of Done: the six stages implemented with their controls, the
   vault read-back-free, rotation and revocation proven, SSRF blocked.
   Evidence to report: the eleven test outputs, the SSRF results, the secret
   non-disclosure proof, the A04 table.
   Remaining blockers: connectors without an agreement or credential cannot
   reach VALIDATED. That is the correct state; list them and name the owner.
   Next prompt: P13-03.
```

**المخرجات المتوقعة:** دورة موصل بسبع حالات، خزانة بلا مسار قراءة، حماية SSRF، اختبار إبطال.
**التحقق المطلوب:** التسجيل والاختبار والتدوير والإبطال كلها مُختبَرة؛ لا سر يُرجَع.
**الاعتمادية التالية:** `P13-03`.

---

### P13-03 — القدرات الإدارية الست عشرة ومصفوفة الصلاحيات

<!-- meta
id: P13-03
phase: PHASE-13
title_en: The sixteen admin capabilities, RBAC matrix and dual control
prereq: [P13-02]
requirements: [REQ-ADM-01, REQ-ADM-02, REQ-ADM-07, REQ-GW-12]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ القدرات الست عشرة في الورقة 58 ومصفوفة الصلاحيات
في الورقة 59، بتحكم مزدوج وbreak-glass منتهي الصلاحية.

**لماذا نحتاجه؟** الورقة 58 تحدد لكل قدرة دورها وموافقتها وAPIها وحدها الآمن
وأولويتها. والورقة 59 تضع مصفوفة تسعة أدوار × ثمانية أفعال بقيم دقيقة مثل
`Scoped`, `Redacted`, `Ticketed`, `Policy`, `Emergency`, `Draft`, `Approve` —
وهذه ليست نعم/لا، بل حالات وسطى يجب تنفيذها كما هي.

**ما المتطلبات السابقة؟** `P13-02`.

**ما النتيجة المتوقعة؟** ست عشرة قدرة مُنفَّذة بحدودها، ومصفوفة مفروضة باختبارات
سلبية، وbreak-glass ينتهي آلياً.

**كيف نتحقق من نجاحه؟** لكل خلية في الورقة 59 اختبار؛ وتعديل نموذج في الإنتاج
بموافقة واحدة يُرفض.

```text
TASK P13-03 — The sixteen admin capabilities, RBAC matrix and dual control

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-03
   Phase: PHASE-13
   Prerequisites: P13-02
   Requirements covered: REQ-ADM-01, REQ-ADM-02, REQ-ADM-07, REQ-GW-12

B. OBJECTIVE
   Implement the sixteen admin capabilities with their roles, approval
   requirements, APIs, safety boundaries and launch priorities, and enforce the
   nine-role by eight-action authorization matrix with its intermediate states
   — plus dual control and auto-expiring break-glass.

   Why this is necessary: sheet 58 specifies each capability's exact approval
   requirement and safety boundary. Sheet 59's matrix uses graded values —
   Scoped, Redacted, Ticketed, Policy, Emergency, Draft, Approve, Project,
   Summary — which are distinct authorization states, not yes-or-no. Sheet 70
   row 13 requires four-eyes control for production secrets and policies.
   Sheet 57 row 3 (A02) requires RBAC plus ABAC with dual control and
   append-only audit.

   SCOPE BOUNDARY: the capabilities and the matrix. The underlying services
   already exist from earlier phases; here you expose them as authorized,
   approved, audited commands and enforce the matrix.

C. CONTEXT
   Required inputs, sheet 58 rows 2-17, each as area / action / role /
   approval / API / audit / safety boundary / launch:
     Dashboard / inspect system health / Support L1 / no / GET /admin/health /
       read access / redact PII / P0
     Tenants / view own organization and projects / Support L2 / ticket / GET
       /admin/tenants/{id} / yes / scoped access plus justification / P0
     Agents / enable or disable an agent version / Platform operator / dual
       approval in production / POST /admin/agents/{id}/rollouts / yes /
       canary plus rollback / P0
     Agents / edit prompt or tool policy / AI engineer / peer approval / POST
       /admin/agent-versions / yes / version immutable after publish / P0
     Models / change model route and budget / AI operator / dual approval /
       POST /admin/model-policies / yes / shadow eval plus rollback / P0
     Integrations / register an API connector / Integration engineer / security
       approval / POST /admin/connectors / yes / secret vault, no raw secrets
       in UI / P0
     Integrations / rotate or revoke a credential / Security admin / dual
       approval / POST /admin/connectors/{id}/rotate / yes / the secret is
       never returned / P0
     Workflows / pause or resume the queue / SRE / incident / POST
       /admin/workflows/pause / yes / idempotent, drain in-flight / P0
     Execution / retry a failed task / Support L2 / policy / POST
       /admin/executions/{id}/retry / yes / no duplicate side effects / P0
     Execution / cancel an unsafe task / SRE / incident / POST
       /admin/executions/{id}/cancel / yes / compensating action / P0
     Knowledge / publish a code or standard revision / Knowledge steward /
       reviewer approval / POST /admin/knowledge/releases / yes / license plus
       source version / P0
     Support / view traces and sanitized logs / Support L2 / ticket / GET
       /admin/traces/{id} / yes / no cross-tenant access / P0
     Security / manage staff roles / Security admin / dual approval / POST
       /admin/role-assignments / yes / break-glass expires / P0
     Billing / view token spend and invoices / Finance / no / GET /admin/usage
       / yes / immutable usage ledger / P0
     Scan / inspect evidence and scan quality / Qualified reviewer / project
       authorization / GET /projects/{id}/evidence / yes / consent and
       retention / P0
     Commerce / provision a partner agent package / Sales ops / contract
       approval / POST /admin/entitlements / yes / FUTURE FEATURE / P2
   And sheet 59 rows 2-10, the matrix of nine roles against eight actions:
   view health, view customer PII, edit agent, edit API, change model, retry
   jobs, billing, approve release — with values including Yes, No, Scoped,
   Redacted, Policy, Emergency, Draft, Approve, Ticketed, Summary, Project.

D. EXECUTION INSTRUCTIONS
   1. Implement each of the sixteen capabilities as a command or a scoped read
      per P13-01, carrying exactly the role, approval requirement, API path and
      safety boundary the source assigns. Do not simplify an approval
      requirement, and do not merge two capabilities whose approvals differ
      (enabling an agent version needs dual approval in production, while
      editing a prompt needs peer approval — these are different gates).
   2. Implement the approval types as distinct mechanisms:
        - none;
        - ticket: a referenced support ticket plus a justification;
        - policy: the action is permitted only within a configured policy
          envelope, checked by the policy service;
        - incident: an open incident reference;
        - peer approval: one other qualified person, not the author;
        - dual approval: two distinct approvers, neither the author;
        - security approval: a security-role approver;
        - reviewer approval: a qualified reviewer in scope;
        - project authorization: authorization on that specific project;
        - contract approval: a signed contract reference (deferred scope).
   3. Implement the matrix from sheet 59 with its graded values as a
      data-driven policy, extending the P01-03 decision point. Each graded
      value has precise semantics you must implement:
        - Scoped: limited to the records within the actor's assignment, plus a
          justification;
        - Redacted: the data is returned with sensitive fields masked;
        - Ticketed: requires a ticket reference;
        - Policy: permitted within the configured envelope only;
        - Emergency: permitted only with an open incident, time-boxed and
          audited (SRE changing a model route);
        - Draft: may create or modify a draft but may not publish;
        - Approve: may approve another actor's draft but, per the peer and dual
          rules, not their own;
        - Project: limited to an authorized project;
        - Summary: aggregate figures only, no record-level data.
   4. Implement the separation that makes Draft and Approve meaningful: an AI
      engineer drafts an agent version and a model policy change but cannot
      approve either; a Security admin approves but, where they also drafted,
      cannot approve their own draft. Add tests for both directions.
   5. Implement break-glass per sheet 58 row 14's boundary "break-glass
      expires": dual-approved, time-boxed, scoped to named resources,
      automatically expiring without any revocation call, non-renewable
      silently, and audited to a separate stream. Reuse and verify the P01-03
      implementation.
   6. Implement the production-specific gates: enabling or disabling an agent
      version requires dual approval in production specifically, with canary
      and rollback available (reusing P05-02). A model policy change requires
      dual approval and a shadow evaluation plus rollback (reusing P04-02 and
      P04-03).
   7. Implement the safety boundaries as enforced behaviour, not notes:
      idempotent pause with in-flight drain; retry with no duplicate side
      effects (reusing P03-03); cancel with a compensating action; immutability
      after publish; license and source version checks on knowledge publication
      (reusing P06-01); no cross-tenant trace access; consent and retention
      checks on evidence inspection.
   8. Mark the Commerce capability as the source does — FUTURE FEATURE, P2 —
      and leave it unimplemented behind the PHASE-16 gate. Implement nothing of
      its behaviour.
   9. Write the negative authorization suite covering the full matrix: for
      every one of the seventy-two role-action cells, a test asserting the
      implemented behaviour matches the source's value, including the graded
      semantics. This is the A02 evidence and the sheet 59 enforcement proof.
  10. Tests:
        a. the seventy-two-cell matrix suite;
        b. an AI engineer attempting to approve their own agent version draft
           -> refused; a Security admin approving it -> permitted;
        c. a production agent rollout with one approver -> refused; with two
           distinct non-author approvers -> permitted with canary available;
        d. a model policy change without a shadow evaluation reference ->
           refused;
        e. an SRE emergency model change without an open incident -> refused;
           with one -> permitted, time-boxed and audited;
        f. break-glass expires with no revocation call and cannot be silently
           renewed;
        g. a Support L2 customer-data read without a ticket -> refused; with
           one -> Scoped and justified;
        h. a Finance billing read returns Summary-level data for roles limited
           to Summary;
        i. pause applied twice -> idempotent with in-flight drained;
        j. a knowledge publication without a license check -> refused;
        k. the Commerce entitlement endpoint -> returns a clear not-available
           response, implements nothing.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the sixteen capabilities as commands or scoped reads with their exact
     approvals and boundaries
   - the ten distinct approval mechanisms
   - the data-driven sheet 59 matrix with all nine graded value semantics
   - Draft and Approve separation enforced in both directions
   - verified auto-expiring, scoped, dual-approved break-glass
   - production-specific dual approval with canary, shadow eval and rollback
   - enforced safety boundaries reusing the earlier phases' guarantees
   - the Commerce capability left unimplemented behind the PHASE-16 gate
   - tests/admin/rbac-matrix-72.* and cases b through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the seventy-two-cell suite summary and the full cell-by-cell result
     table.
   - Paste cases b, c, e and f in full.
   - State the count: sixteen capabilities implemented or deliberately not
     implemented, and seventy-two matrix cells asserted.
   - Acceptance criterion: every matrix cell behaves exactly as the source
     specifies, no actor approves their own draft, and break-glass expires on
     its own.

G. COMPLETION CONTRACT
   Definition of Done: sixteen capabilities with correct approvals, the full
   matrix enforced and tested cell by cell, break-glass expiry verified.
   Evidence to report: the matrix result table, the named test outputs, the
   capability implementation status list.
   Remaining blockers: the Commerce capability stays deferred. Confirm it is
   inert.
   Next prompt: P13-04.
```

**المخرجات المتوقعة:** ست عشرة قدرة بموافقاتها، مصفوفة 72 خلية مفروضة، break-glass منتهٍ آلياً.
**التحقق المطلوب:** كل خلية مُختبَرة؛ لا أحد يعتمد مسودته؛ الصلاحية الطارئة تنتهي بنفسها.
**الاعتمادية التالية:** `P13-04`.

---

### P13-04 — سطح الدعم والتشخيص المُحجَّب

<!-- meta
id: P13-04
phase: PHASE-13
title_en: Support surfaces, masked diagnostics and the ops API
prereq: [P13-03]
requirements: [REQ-OBS-04, REQ-ADM-01, REQ-API-09, REQ-TEN-07]
-->

**ماذا سينفذ هذا الأمر؟** يبني سطح الدعم: تذاكر وتشخيص مُحجَّب ووصول JIT وإعادة
محاولة عبر runbook، ويُكمل عمليات الـAPI الإدارية في الورقة 65.

**لماذا نحتاجه؟** الورقة 03 الصف 9 تحدد بوابة الدعم: «بيانات حساسة JIT»،
و«Masking وapproval للـbreak-glass»، وحدها: «لا يغيّر قرار مراجعة أو دفع». وهذا
الحد الأخير جوهري: الدعم يُشخّص ولا يُقرّر.

**ما المتطلبات السابقة؟** `P13-03`.

**ما النتيجة المتوقعة؟** سطح دعم فعّال بلا تعريض، وحدود صلبة تمنع تغيير قرارات
المراجعة والدفع.

**كيف نتحقق من نجاحه؟** محاولة `SUPPORT_L2` تغيير قرار مراجعة أو حالة دفع تُرفض؛
والوصول JIT ينتهي آلياً.

```text
TASK P13-04 — Support surfaces, masked diagnostics and the ops API

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-04
   Phase: PHASE-13
   Prerequisites: P13-03
   Requirements covered: REQ-ADM-01, REQ-API-09, REQ-OBS-04, REQ-TEN-07

B. OBJECTIVE
   Build the support surface — tickets, masked diagnostics, JIT access to
   sensitive data, and runbook-driven retry — and complete the admin operations
   API, with the source's hard boundary that support can diagnose but never
   change a review decision or a payment status.

   Why this is necessary: sheet 03 row 9 defines the support portal with JIT
   sensitive data, masking and break-glass approval, and the access limit "does
   not change a review decision or payment". Sheet 04 row 9 repeats it for
   SUPPORT_L2, forbidding manually setting a reviewer decision or payment
   status. That boundary is what keeps professional and financial
   accountability intact, and it is easy to erode through a well-meaning
   support tool.

   SCOPE BOUNDARY: the support surface and the remaining sheet 65 operations.
   The runbooks themselves are P10-03; here they are exposed to support with
   the right authorization and masking.

C. CONTEXT
   Required inputs:
     - sheet 03 row 9: users L1, L2 and SRE; functions tickets, diagnosis and
       retry via runbook; sensitive data JIT; identity masking and break-glass
       approval; limit "does not change a review decision or payment"
     - sheet 04 row 9: SUPPORT_L2 may see limited logs and retry; data scope
       temporary JIT; forbidden from manually setting a reviewer decision or
       payment status; MFA plus JIT; monthly access review
     - sheet 61 rows 2-8, the seven support scenarios from P10-03
     - sheet 65 rows 2-9, the eight admin operations, of which P13-01 and
       P13-02 covered health, audit and connectors; this prompt completes:
       POST /v1/admin/agents/{id}/deployments (agents:deploy, idempotency
       required, emits agent.deployed); POST /v1/admin/executions/{id}/retry
       (executions:retry, idempotency required, emits
       execution.retry_requested); POST /v1/admin/model-policies (models:write,
       idempotency required, emits model.policy_changed); GET
       /v1/projects/{id}/scan-sessions (scan:read, emits
       scan.quality_changed)

D. EXECUTION INSTRUCTIONS
   1. Implement the ticket linkage: a support action requiring a ticket
      validates the reference against the ticketing source of truth, or, where
      none is integrated, against an internal ticket record created by a
      support lead. A free-text ticket string is not a reference — make the
      validation real or state plainly that no ticketing integration exists and
      that the internal record is the control.
   2. Implement masked diagnostics as the default and only view: a support user
      sees run state, step outcomes, error classes, timings, policy and routing
      decisions, and sanitized logs and traces — never raw customer documents,
      raw prompts, personal data beyond identifiers, or secrets. Reuse the
      P10-01 redaction so masking is applied at the data layer.
   3. Implement JIT elevation for genuinely necessary sensitive access:
      requested with a reason and a ticket, approved per the matrix,
      time-boxed, scoped to named records, auto-expiring, and audited with
      every record accessed under it recorded individually. An elevation that
      logs only its grant and not its use is insufficient for the monthly
      access review sheet 04 row 9 requires.
   4. Implement the hard boundary as a structural prohibition, which is the
      central deliverable: there is no code path, endpoint, command or script
      by which a support identity can set a reviewer decision, alter a finding
      status, set a payment state, change an invoice amount or alter a delivery
      hash. Implement it as an architectural test over the command registry and
      the route table, and demonstrate it failing when a violating command is
      introduced. Sheet 04 row 8 adds the related prohibition that FINANCE
      cannot change a delivery hash — assert that too.
   5. Implement runbook-driven retry: support invokes the P10-03 safe actions
      within its policy envelope. A retry is idempotent, records the
      justification, and cannot bypass a business gate — retrying a payment
      verification does not verify a payment, it re-runs the verification
      against the provider.
   6. Implement the remaining four sheet 65 operations with their scopes,
      idempotency requirements and events, wiring them to the existing
      capabilities: agent deployment to P05-02, execution retry to P03-03 and
      P10-03, model policy change to P04-02 and P04-03, and scan session read
      to P12-02 with consent and retention checks.
   7. Implement the monthly access review per sheet 04 row 9: a report of every
      JIT elevation, every record accessed under it, every break-glass grant,
      and every support action taken, for review by the security owner. Make it
      generated, not manual.
   8. Implement the support view of the seven scenarios from sheet 61: for each
      scenario, the surface shows the trigger, the current state, the available
      safe action within the user's authority, the escalation path and the
      evidence to capture, so the runbook is followed in the tool rather than
      from memory.
   9. Tests:
        a. a support action requiring a ticket without a valid reference ->
           refused;
        b. a diagnostic view contains no raw document, prompt, secret or
           personal data beyond identifiers — assert field-by-field against an
           allowlist;
        c. JIT elevation -> time-boxed, scoped, auto-expiring, and every record
           accessed under it individually audited;
        d. the structural prohibition test: no support path can set a reviewer
           decision, a finding status, a payment state, an invoice amount or a
           delivery hash; introduce a violating command, show the test failing,
           remove it;
        e. FINANCE cannot change a delivery hash;
        f. a support retry is idempotent and does not bypass a business gate —
           retrying payment verification re-queries the provider rather than
           marking it paid;
        g. the four sheet 65 operations enforce their scopes, idempotency and
           events;
        h. a scan session read without consent or past retention -> refused;
        i. the monthly access review report is generated and includes
           elevations, accessed records, break-glass grants and actions.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - validated ticket linkage, or an honest statement of its absence
   - data-layer masked diagnostics with an allowlisted field set
   - JIT elevation with per-record access auditing
   - the architectural prohibition on support changing review, finance or
     delivery state, with its failing demonstration
   - runbook-driven idempotent retry that cannot bypass a business gate
   - the four remaining sheet 65 operations
   - the generated monthly access review report
   - the scenario-guided support surface for sheet 61's seven cases
   - tests/admin/support-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - Paste the case d prohibition test passing, failing on the injected
     command, and passing again.
   - Paste the masked diagnostic view beside its field allowlist.
   - Paste a sample monthly access review report.
   - Acceptance criterion: support can diagnose everything it needs and change
     nothing it must not, and the test proving that can fail.

G. COMPLETION CONTRACT
   Definition of Done: support surfaces working under masking and JIT, the
   structural prohibition enforced and provably testable, the ops API complete,
   access review generated.
   Evidence to report: the nine test outputs, the three prohibition test runs,
   the allowlist comparison, the review report sample.
   Remaining blockers: a ticketing integration may be absent; say so if the
   internal record is the only control. SLO targets for support response
   remain unestablished per sheet 61's "SLO pending".
   Next prompt: P14-01. PHASE-13 exit requires the boundary test green, the
   seventy-two-cell matrix green, dual control on production secrets and
   policies, connector revocation proven, and break-glass expiry verified.
```

**المخرجات المتوقعة:** تشخيص مُحجَّب، JIT بتدقيق لكل سجل، حظر بنيوي على تغيير المراجعة والدفع والتسليم.
**التحقق المطلوب:** الدعم يُشخّص ولا يُقرّر — مُثبت باختبار معماري قادر على الفشل.
**الاعتمادية التالية:** `P14-01`.

# PHASE-01 — الأساسات: الهوية والعزل والسياسة والتدقيق

<!-- phasemeta
id: PHASE-01
depends_on: [PHASE-00]
criticality: P0
-->

## الغرض من المرحلة

بناء العمود الفقري الذي يستحيل إضافته لاحقاً: اشتقاق `tenant_id` من الهوية
وفرضه في كل طبقة، وأدوار محددة بصلاحيات ومنع صريح، ومحرك سياسة يفشل مُغلقاً،
وسجل تدقيق لا يقبل التعديل.

الورقة 02 الصف 4 (ADR-003) تجعل العزل قراراً معتمداً: «`tenant_id` مشتق من
الهوية ويُطبَّق في IAM وDB والتخزين والطوابير وRAG». والورقة 27 الصف 2 تصنّفه
`CRITICAL`. أما الورقة 68 الصف 3 فتحدد نطاق الإطلاق: «تشغيل أحادي المستأجر
مملوك الآن، مع بدائيات واعية بالمستأجر للمستقبل» — أي أننا نبني المخطط واعياً
بالمستأجر من اليوم الأول، لكننا لا نبني تجارة متعددة المستأجرين.

## شروط الدخول

- اكتمال `PHASE-00`.
- إجابة `OD-07` (هدف النشر وقاعدة البيانات) و`OD-02` (التسلسل المعتمد) من المالك.

## شروط الخروج

- نجاح `AT-SEC-001`: محاولة مستأجر A الوصول إلى معرفات وملفات ومتجهات مستأجر B
  تُرفض بـ403/404 بلا تسريب أي بيانات وصفية، مع تنبيه.
- اختبارات سلبية لكل دور من الأدوار العشرة.
- سجل تدقيق مُثبت أنه كاشف للتلاعب.
- ترحيل المخطط الأساسي بقيوده.

## المتطلبات المغطاة في هذه المرحلة

`ADR-003`, `REQ-GOV-01`, `REQ-TEN-01`..`REQ-TEN-09`, `REQ-SEC-03`, `REQ-SEC-04`,
`REQ-DAT-01`, `REQ-DAT-02`, `REQ-API-03`, `REQ-INT-03`

## تحذير مهم

العزل ليس ميزة تُضاف لاحقاً. كل جدول وكل مفتاح تخزين وكل طابور وكل فهرس متجهات
يُنشأ في هذه المرحلة أو بعدها يجب أن يحمل نطاق المستأجر من لحظة إنشائه. إضافة
العزل بأثر رجعي على بيانات قائمة هي من أكثر الهجرات خطورة.

---

## الأوامر التنفيذية

### P01-01 — هيكل المنصة والمخطط الأساسي وقيوده

<!-- meta
id: P01-01
phase: PHASE-01
title_en: Platform skeleton and core schema with constraints
prereq: [P00-04]
requirements: [REQ-DAT-01, REQ-DAT-02, REQ-SEC-03, REQ-GOV-01, REQ-TEN-02, REQ-TEN-04]
-->

**ماذا سينفذ هذا الأمر؟** يثبّت اختيار المنصة وقاعدة البيانات في ADR جديد، ثم
ينشئ الهيكل الأولي وترحيلات المخطط للكيانات الأساسية مع القيود والفهارس المحددة
في الورقة 39.

**لماذا نحتاجه؟** الورقة 28 تحدد عشرين كياناً أساسياً، والورقة 39 تحدد لكل جدول
حقوله الإلزامية وقيد التفرد وفهارسه والثابت المنطقي وسياسة الحفظ. هذه ليست
تفاصيل لاحقة: قيد `UNIQUE (tenant_id, idempotency_key)` هو ما يمنع الشحن
المزدوج، وقيد `UNIQUE (artifact_id, review_version)` هو ما يحمي سلامة المراجعة.

**ما المتطلبات السابقة؟** `P00-04`، وإجابة `OD-07`.

**ما النتيجة المتوقعة؟** مشروع يبنى ويختبر، وترحيلات تُطبَّق وتُسترجع على قاعدة
بيانات مؤقتة، وقيود مُثبتة بالاختبار.

**كيف نتحقق من نجاحه؟** لكل قيد تفرد في الورقة 39 اختبار يُدخل تكراراً ويتوقع
الرفض. الترحيل يُطبَّق ويُرجَع بلا فقدان.

```text
TASK P01-01 — Platform skeleton and core schema with constraints

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-01
   Phase: PHASE-01 (Foundations)
   Prerequisites: P00-04 complete; open decisions OD-02 and OD-07 answered by
                  the owner and recorded in docs/OPEN-DECISIONS.md
   Requirements covered: REQ-DAT-01, REQ-DAT-02, REQ-SEC-03, REQ-GOV-01

B. OBJECTIVE
   Stand up the project skeleton and the core database schema with the exact
   integrity constraints the source specifies, so that every later phase builds
   on enforced invariants rather than on convention.

   Why this is necessary: sheet 28 defines 20 core entities; sheet 39 defines,
   per table, the required fields, the uniqueness constraint, the suggested
   indexes, the invariant and the retention rule. Those constraints are the
   mechanism behind several P0 controls — UNIQUE (tenant_id, idempotency_key)
   is what prevents a double charge, and UNIQUE (artifact_id, review_version)
   is what protects review integrity.

   SCOPE BOUNDARY: schema, migrations, constraints and the minimum application
   skeleton needed to run them. No business logic, no endpoints beyond a health
   check, no AI, no payment code.

C. CONTEXT
   Required inputs:
     - config/registries/data-entities.json (sheet 28, 20 entities)
     - config/registries/data-constraints.json (sheet 39, 9 tables)
     - docs/OPEN-DECISIONS.md — OD-07 names the chosen datastore
     - docs/discovery/RUNTIME-INVENTORY.md — what already exists
   Constraint from the source: sheet 39 row 3 states these are proposed
   relational constraints and that migration review is required before
   implementation. Treat the constraint set as specified, but review it against
   your chosen engine and report any incompatibility rather than silently
   changing it.
   Constraint: launch scope is single-tenant owned operation with tenant-aware
   primitives (sheet 68 row 3). Every table carries tenant_id from the start
   even though only one tenant exists at launch.

D. EXECUTION INSTRUCTIONS
   1. If a platform or datastore decision is not already an accepted ADR, write
      docs/adr/ADR-011-platform-and-datastore.md as PROPOSED, capturing the
      owner's answer to OD-07, the alternatives considered, and the
      consequences. Do not proceed past step 2 if OD-07 is unanswered.
   2. Create or extend the project skeleton so that install, build, lint,
      typecheck and test all run and pass on an empty-but-valid project. Match
      whatever the repository already uses; if the repository is empty, choose a
      stack consistent with the ADR and justify it there.
   3. Write forward migrations for the 20 entities of sheet 28. Every table:
        - has tenant_id, not nullable, on every tenant-scoped table;
        - has created_at and updated_at in UTC;
        - uses the exact uniqueness constraints from
          config/registries/data-constraints.json where that table appears
          there (projects, workflow_runs, agent_executions, evidence_assets,
          review_decisions, boq_items, usage_ledger, outbox_events,
          idempotency_keys);
        - creates the suggested indexes from that same register.
   4. Implement the invariants from sheet 39 that are expressible in the
      database, as constraints rather than as application checks:
        - idempotency_keys conflicts when the request hash differs for the same
          (tenant_id, key);
        - review_decisions is append-only (no UPDATE, no DELETE) — enforce with
          a rule, trigger or permission, not with a code comment;
        - evidence_assets.sha256 is not nullable;
        - usage_ledger.execution_id is unique, enabling exactly-once posting.
   5. Encryption at rest and in transit per sheet 27 row 6: configure TLS for
      client connections and document the at-rest mechanism (engine-level,
      volume-level or cloud-managed) with the key custodian named. If you cannot
      enable it in the local environment, state that explicitly and record what
      production must configure.
   6. Write a migration test script that, on a throwaway database:
        - applies every migration from empty;
        - asserts every expected table, column, constraint and index exists;
        - for each uniqueness constraint, inserts a duplicate and asserts the
          write is rejected;
        - asserts review_decisions rejects UPDATE and DELETE;
        - rolls back or tears down cleanly.
   7. Wire that script into the repository's test or validation command.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - docs/adr/ADR-011-platform-and-datastore.md
   - migration files for the 20 entities
   - a migration and constraint test script, wired into the test command
   - updated README section describing how to run migrations locally
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Run the full migration from empty on a throwaway database. Paste the real
     output and exit code.
   - Paste the output of the constraint test showing each duplicate insert
     being rejected, naming the constraint.
   - Paste the output showing UPDATE and DELETE rejected on review_decisions.
   - Confirm build, lint, typecheck and test all pass; paste exit codes.
   - Acceptance criterion: every table in data-constraints.json has its stated
     uniqueness constraint proven by a failing duplicate insert. A table whose
     constraint you could not implement is reported as NOT VERIFIED with the
     engine limitation that caused it.

G. COMPLETION CONTRACT
   Definition of Done: migrations apply from empty, every specified constraint
   is proven by test, the project's own checks pass.
   Evidence to report: migration output, constraint test output, the table of
   entity -> constraint -> PROVEN / NOT VERIFIED.
   Remaining blockers: any constraint from sheet 39 that is incompatible with
   the chosen engine — report it, propose the equivalent, and do not silently
   drop it.
   Next prompt: P01-02.
```

**المخرجات المتوقعة:** ترحيلات الكيانات العشرين، سكربت اختبار القيود، `ADR-011`.
**التحقق المطلوب:** كل قيد تفرد مُثبت برفض إدخال مكرر؛ `review_decisions` يرفض التعديل والحذف.
**الاعتمادية التالية:** `P01-02`.

---

### P01-02 — عزل المستأجرين في كل الطبقات

<!-- meta
id: P01-02
phase: PHASE-01
title_en: Tenant isolation across every layer
prereq: [P01-01]
requirements: [ADR-003, REQ-TEN-01, REQ-TEN-03, REQ-TEN-06, REQ-API-03]
-->

**ماذا سينفذ هذا الأمر؟** يفرض العزل في قاعدة البيانات (RLS أو تقسيم)، وفي مفاتيح
التخزين، وفي الطوابير، وفي فلاتر المتجهات، ويبني اختبار `AT-SEC-001` السلبي.

**لماذا نحتاجه؟** هذا هو الضابط `CTRL-001` بأولوية `CRITICAL` (الورقة 15 الصف 2)،
والمؤشر الوحيد في الورقة 30 الذي هدفه صفر مطلق مع إجراء «Stop-the-line». كما أن
الورقة 33 الصف 7 تضيف شرطاً دقيقاً: «لا تكشف أبداً وجود كيان لمستأجر آخر» — أي أن
الرد على طلب غير مصرح به يجب ألا يفرّق بين «غير موجود» و«موجود لكن ممنوع».

**ما المتطلبات السابقة؟** `P01-01`.

**ما النتيجة المتوقعة؟** عزل مفروض في أربع طبقات، واختبار سلبي آلي في مجموعة
الاختبارات، وتنبيه عند محاولة الاختراق.

**كيف نتحقق من نجاحه؟** `AT-SEC-001`: مستأجر A يحاول قراءة وكتابة معرفات وملفات
ومتجهات مستأجر B، فيحصل على 403/404 بلا تسريب بيانات وصفية، ويُسجَّل تنبيه.

```text
TASK P01-02 — Tenant isolation across every layer

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-02
   Phase: PHASE-01
   Prerequisites: P01-01 (schema and constraints in place)
   Requirements covered: ADR-003, REQ-TEN-01, REQ-TEN-03, REQ-TEN-06,
                         REQ-API-03

B. OBJECTIVE
   Enforce tenant isolation in all four layers the source names — database,
   object storage, queues and vector indexes — with tenant_id always derived
   from the authenticated identity and never accepted from a client, and prove
   it with the negative test AT-SEC-001.

   Why this is necessary: this is CTRL-001 at CRITICAL priority (sheet 15
   row 2), it is ADR-003 (sheet 02 row 4), and it is the only KPI in the source
   with an absolute target of zero and a Stop-the-line action (sheet 30 row 2).
   Sheet 33 row 7 adds a precise requirement: cross-tenant existence must never
   be revealed, so an unauthorized read must not let the caller distinguish
   "does not exist" from "exists but forbidden".

   SCOPE BOUNDARY: isolation enforcement and its tests. Do not build product
   endpoints. Do not build the AI gateway. Add only the minimal routes needed
   to exercise the isolation test.

C. CONTEXT
   Required inputs:
     - the migrations from P01-01
     - config/registries/data-entities.json
     - config/registries/acceptance-tests.json, entry AT-SEC-001: "Tenant A
       attempts B's IDs, files and vectors" -> expected "403/404 with no
       metadata leak plus alert"
   Constraint: launch is single-tenant (sheet 68 row 3), so the test must
   provision at least two tenants in the test fixture even though production
   runs one. Isolation that is never exercised is isolation that does not work.

D. EXECUTION INSTRUCTIONS
   1. Database layer:
      - Enable row-level security (or the engine's equivalent) on every
        tenant-scoped table, with a default-deny policy.
      - Derive the tenant context from the authenticated session on every
        connection or transaction. Never read tenant_id from a request body,
        query parameter or header.
      - Add a test that asserts a query without a tenant context returns zero
        rows rather than all rows.
   2. Object storage layer:
      - Namespace every object key with the tenant prefix.
      - Scope credentials or signed URLs so a token for tenant A cannot
        construct a readable URL for tenant B's prefix.
   3. Queue layer:
      - Carry tenant_id in every message envelope and assert it on consume.
      - Reject a message whose tenant does not match the consumer's scope, and
        route it to the dead-letter queue with an alert rather than processing
        it.
   4. Vector or search layer:
      - If a vector store exists at this point, enforce a mandatory tenant
        filter at the query-construction layer so a query cannot be issued
        without it. If no vector store exists yet, write the enforcement
        interface and a failing-by-default stub, and record that PHASE-06 will
        complete it.
   5. Response shaping:
      - Implement a single authorization helper that returns an identical
        response shape for "not found" and "forbidden" on cross-tenant access,
        so no metadata, existence hint, ID echo or timing difference leaks.
   6. Alerting:
      - Emit a structured security event on every cross-tenant attempt, with
        actor, target, decision and correlation id, into the audit path that
        P01-05 will harden. Never put the attempted payload in the event.
   7. Implement AT-SEC-001 as an automated test that, for tenants A and B:
        - attempts a cross-tenant read by ID on every tenant-scoped entity;
        - attempts a cross-tenant write;
        - attempts a cross-tenant object fetch;
        - attempts a cross-tenant vector or search query;
        - asserts 403 or 404 with an identical body shape in every case;
        - asserts no response contains B's identifiers or counts;
        - asserts a security event was emitted for each attempt.
   8. Wire AT-SEC-001 into the test command and mark it non-skippable.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - RLS or equivalent policies in migrations
   - tenant-context derivation middleware
   - object key namespacing and scoped credential issuance
   - queue envelope tenant assertion with DLQ routing
   - vector or search mandatory tenant filter (or enforced stub)
   - the uniform not-found/forbidden authorization helper
   - tests/security/at-sec-001.* implementing the full negative suite
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Run AT-SEC-001. Paste the real output showing every assertion.
   - Demonstrate the test actually catches a regression: temporarily disable
     one isolation layer, show the test failing, restore it, show it passing.
     Paste both outputs.
   - Confirm no response body differs between forbidden and missing.
   - Acceptance criterion: AT-SEC-001 passes, and its deliberate-regression
     run fails. Both are required — a test that cannot fail proves nothing.

G. COMPLETION CONTRACT
   Definition of Done: isolation enforced in all four layers, AT-SEC-001
   passing and proven able to fail, security events emitted.
   Evidence to report: AT-SEC-001 output, the deliberate-regression output, and
   a table of layer -> mechanism -> test that covers it.
   Remaining blockers: any layer not yet present in the project (for example a
   vector store before PHASE-06) — name it and name the prompt that completes
   it.
   Next prompt: P01-03.
```

**المخرجات المتوقعة:** سياسات RLS، وسيط سياق المستأجر، اختبار `AT-SEC-001`.
**التحقق المطلوب:** الاختبار ينجح، ويفشل عند تعطيل طبقة عزل متعمداً.
**الاعتمادية التالية:** `P01-03`.

---

### P01-03 — الهوية والمصادقة ومصفوفة الأدوار

<!-- meta
id: P01-03
phase: PHASE-01
title_en: Identity, authentication strength and the role matrix
prereq: [P01-02]
requirements: [REQ-TEN-05, REQ-TEN-07, REQ-TEN-08, REQ-TEN-09, REQ-INT-03]
-->

**ماذا سينفذ هذا الأمر؟** يبني الهوية (OIDC)، ودرجات المصادقة المطلوبة لكل دور
(MFA، step-up، JIT، break-glass)، ومصفوفة الأدوار العشرة بما تسمح وما تحظر وما
نطاق بياناتها.

**لماذا نحتاجه؟** الورقة 04 لا تكتفي بتسمية الأدوار، بل تحدد لكل دور عموداً
«يحظر» — وهذا هو الجزء الذي يُنسى عادة. مثال: `EXECUTION_ENGINEER` يُحظر عليه
«مراجعة مستقلة لعمله»، و`FINANCE` يُحظر عليه «تغيير delivery hash»،
و`SUPPORT_L2` يُحظر عليه «قرار reviewer أو payment status يدوياً». هذه محظورات
يجب أن تكون مفروضة بالكود ومُختبرة سلبياً.

**ما المتطلبات السابقة؟** `P01-02`.

**ما النتيجة المتوقعة؟** مصادقة عاملة بدرجات، ومصفوفة أدوار مفروضة، واختبار سلبي
لكل محظور في الورقة 04.

**كيف نتحقق من نجاحه؟** لكل صف في الورقة 04 اختبار يحاول الفعل المحظور ويتوقع
الرفض مع تسجيل تدقيقي.

```text
TASK P01-03 — Identity, authentication strength and the role matrix

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-03
   Phase: PHASE-01
   Prerequisites: P01-02 (tenant isolation enforced)
   Requirements covered: REQ-TEN-05, REQ-TEN-07, REQ-TEN-08, REQ-TEN-09,
                         REQ-INT-03

B. OBJECTIVE
   Implement identity and authorization: OIDC-based authentication, the
   per-role authentication strength the source specifies, and the ten-role
   matrix with its allow list, data scope and — critically — its explicit deny
   list, each deny proven by a negative test.

   Why this is necessary: sheet 04 specifies for all ten roles not only what
   they may do but what they are forbidden to do. Those denials carry the real
   safety value and are the ones implementations usually omit. Examples from
   the source: EXECUTION_ENGINEER is forbidden from independently reviewing
   their own work; FINANCE is forbidden from changing a delivery hash;
   SUPPORT_L2 is forbidden from manually setting a reviewer decision or a
   payment status; PLATFORM_OWNER is forbidden from a discipline signature
   without eligibility and from disabling audit.

   SCOPE BOUNDARY: authentication, authorization and the role matrix. The
   policy engine itself is P01-04. Reviewer eligibility logic is PHASE-07 —
   here you implement only the role-level gate.

C. CONTEXT
   Required inputs:
     - config/registries/rbac-roles.json (sheet 04, 10 roles with allow, data
       scope, deny, authentication strength and review cadence)
     - config/registries/admin-rbac-matrix.json (sheet 59, staff roles)
     - sheet 03 (ten access surfaces and their access boundaries)
   Constraint from the source: Nafath is not a public API and is conditional on
   enterprise onboarding; OTP and MFA are the documented interim identity path
   (sheet 23 row 2). Implement the interim path and leave a clean seam for
   Nafath. Do not claim Nafath integration.
   Authentication strengths the source specifies: strong MFA plus PAM for
   PLATFORM_OWNER; MFA for TENANT_ADMIN, PROJECT_MANAGER, EXECUTION_ENGINEER,
   PMO_CONTROLLER, AUDITOR; MFA plus step-up for QUALIFIED_REVIEWER; MFA plus
   dual approval for FINANCE; MFA plus JIT for SUPPORT_L2; secret or mTLS for
   API_CLIENT with 90-day rotation.

D. EXECUTION INSTRUCTIONS
   1. Implement OIDC authentication. Session or token claims must carry: subject,
      tenant_id (server-derived), roles, authentication strength achieved, and
      the time of the last step-up.
   2. Implement authentication strength as a first-class, checkable property:
        - MFA achieved or not;
        - step-up performed within a configured freshness window;
        - JIT elevation with an explicit expiry timestamp;
        - break-glass as a separate, time-boxed, dual-approved grant that
          expires automatically and cannot be renewed silently.
   3. Implement the role matrix from the register as data-driven authorization,
      not as scattered conditionals. One authorization decision point, fed by
      the registry file, so that sheet 04 and the code cannot drift.
   4. Implement the deny list explicitly. A role's absence of permission and a
      role's explicit prohibition are different states, and the prohibition
      must be auditable. Record a denial event naming the role, action and rule.
   5. Implement API_CLIENT credentials with scopes bound to exactly one tenant
      and a 90-day rotation policy, with rotation implemented (not just
      documented) and the old credential revocable.
   6. Map the ten access surfaces of sheet 03 to route groups with their stated
      access boundaries, including that the public surface has no operational
      data and no direct engine connection.
   7. Write a negative authorization test suite that, for every role in
      sheet 04, attempts every action in that role's deny column and asserts
      rejection plus an audit event. This suite is the deliverable that proves
      the phase, so it must be exhaustive against the register, not a sample.
   8. Add a test asserting that an expired JIT grant and an expired break-glass
      grant both stop working without any explicit revocation call.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - OIDC authentication with strength-aware claims
   - step-up, JIT and auto-expiring dual-approved break-glass
   - a single data-driven authorization decision point reading rbac-roles.json
   - API client credentials with scopes, tenant binding and working rotation
   - route grouping for the ten access surfaces
   - tests/security/rbac-negative.* covering every deny cell in sheet 04
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Run the negative authorization suite. Paste real output, and state the
     count of deny cells in the register versus the count of assertions you
     wrote. They must match.
   - Paste the test output for JIT and break-glass expiry.
   - Demonstrate credential rotation: issue, rotate, confirm the old credential
     is rejected.
   - Acceptance criterion: every deny cell in sheet 04 has a passing negative
     test; every elevated grant expires without intervention.

G. COMPLETION CONTRACT
   Definition of Done: authentication with strengths, data-driven authorization,
   exhaustive negative tests passing, expiry proven.
   Evidence to report: deny-cell coverage count, negative suite output, expiry
   test output, rotation demonstration.
   Remaining blockers: Nafath and any enterprise SSO that needs a provider
   agreement — report as blocked on the owner, with the interim path working.
   Next prompt: P01-04.
```

**المخرجات المتوقعة:** مصادقة بدرجات، نقطة قرار تفويض واحدة، مجموعة اختبارات سلبية كاملة.
**التحقق المطلوب:** تطابق عدد خلايا «يحظر» مع عدد التأكيدات؛ انتهاء صلاحية JIT وbreak-glass مُثبت.
**الاعتمادية التالية:** `P01-04`.

---

### P01-04 — محرك السياسة الذي يفشل مُغلقاً

<!-- meta
id: P01-04
phase: PHASE-01
title_en: Fail-closed policy engine with complete decision logging
prereq: [P01-03]
requirements: [REQ-GW-02, REQ-TEN-05, REQ-GOV-03]
-->

**ماذا سينفذ هذا الأمر؟** يبني محرك سياسة مركزياً يُصنّف ويقرر قبل كل عملية
حساسة، يفشل مُغلقاً عند أي شك، ويسجّل 100% من قراراته.

**لماذا نحتاجه؟** الورقة 70 الصف 3 تحدد «محرك سياسة ما قبل التنفيذ» يصنّف
البيانات والجغرافيا والموافقة والأدوات المسموحة ومخاطر المهمة، و«يفشل مُغلقاً»،
وضابط قبوله: «تسجيل 100% من قرارات السياسة». بناء هذا الآن — قبل البوابة
والوكلاء — يجعل كل المراحل اللاحقة تستهلك نقطة قرار واحدة لا عشرة شروط متناثرة.

**ما المتطلبات السابقة؟** `P01-03`.

**ما النتيجة المتوقعة؟** خدمة سياسة مُصدَرة بإصدار، قابلة للاختبار، مع سجل قرارات
كامل، ووضع افتراضي رافض.

**كيف نتحقق من نجاحه؟** اختبار يُزيل حزمة السياسة فيصبح كل قرار رفضاً لا سماحاً؛
واختبار يؤكد أن عدد القرارات المسجلة يساوي عدد الطلبات.

```text
TASK P01-04 — Fail-closed policy engine with complete decision logging

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-04
   Phase: PHASE-01
   Prerequisites: P01-03 (identity and roles available as policy input)
   Requirements covered: REQ-GW-02, REQ-TEN-05, REQ-GOV-03

B. OBJECTIVE
   Build one central, versioned policy decision service that every sensitive
   operation consults before acting. It classifies the request, decides, fails
   closed on any uncertainty, and logs 100 percent of its decisions.

   Why this is necessary: sheet 70 row 3 specifies a preflight policy engine
   that classifies data, geography, consent, allowed tools and task risk, that
   fails closed, and whose acceptance gate is that 100 percent of policy
   decisions are logged. Building it here — before the gateway and the agents —
   means later phases consume one decision point instead of scattering
   conditionals that drift.

   SCOPE BOUNDARY: the policy service, its input contract, its decision log and
   its tests. Do not implement the gateway, the router or agent execution. Do
   not encode pricing or payment rules here.

C. CONTEXT
   Required inputs:
     - config/registries/rbac-roles.json and admin-rbac-matrix.json
     - config/registries/routing-policies.json (task classes, for the risk
       classification vocabulary only)
     - sheet 70 row 3 (the engine's responsibilities)
     - sheet 68 row 4 (the control path: console -> platform API -> policy and
       approval -> runtime; never browser-to-agent, never browser-to-database)
   The two risk axes come from ADR-005 (sheet 02 row 6): Action Risk R0-R4 is
   authority to act; Professional Consequence P0-P3 is impact of error. They
   are independent inputs, not one score. P3 requires a specialist; R4 requires
   delegated authority.
   Policy-as-code is a source recommendation: sheet 22 row 30 lists Open Policy
   Agent as Recommended with the control "version and test bundles". Using it
   is justified by the source; if you choose otherwise, record an ADR.

D. EXECUTION INSTRUCTIONS
   1. Define the decision request contract. At minimum: actor identity, roles,
      authentication strength, tenant, project, action, resource class, data
      classification, declared task_type, action_risk (R0-R4), professional
      consequence (P0-P3), requested tools, destination geography, consent
      state, and a correlation id.
   2. Define the decision response contract: ALLOW | DENY | ALLOW_WITH_GATE,
      the matched rule id, the policy bundle version, the human gate required
      (if any), and a machine-readable reason code. Never return a bare boolean.
   3. Implement fail-closed semantics, exhaustively:
        - unknown action, unknown resource class or unknown classification ->
          DENY;
        - missing or unparseable policy bundle -> DENY (never ALLOW);
        - policy service unreachable or timed out -> the CALLER denies;
        - a required input field absent -> DENY with a reason code naming it.
      Each of these five cases needs its own test.
   4. Version the policy bundle. Every decision records the bundle version that
      produced it. Bundles are tested artifacts: add a bundle test suite that
      runs in CI, per the control in sheet 22 row 30.
   5. Implement the decision log:
        - one record per decision, written on the ALLOW path as well as the
          DENY path;
        - fields: correlation id, actor, tenant, action, decision, rule id,
          bundle version, timestamp UTC, latency;
        - no secrets, no payload content, no PII beyond identifiers;
        - written to the append-only store that P01-05 hardens.
   6. Encode the two risk axes as independent policy inputs with their source
      semantics: an R4 action requires a recorded delegation; a P3 consequence
      requires a specialist human gate. Do not collapse them into one number.
   7. Add an architectural guard test asserting the control path of sheet 68
      row 4: there is no route by which a browser-originated request reaches an
      agent runtime or the database without passing the platform API and the
      policy service. Implement this as a real test over the route table or
      dependency graph, not as documentation.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the policy decision service with versioned bundles
   - request and response contracts as typed schemas
   - the five fail-closed tests
   - the decision log writer
   - a policy bundle test suite in CI
   - the architectural control-path guard test
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of the five fail-closed tests.
   - Prove log completeness: run N mixed requests, assert exactly N decision
     records exist, and paste the count comparison.
   - Remove the policy bundle and show every decision becomes DENY. Paste it.
   - Confirm no decision record contains a secret or payload content: grep the
     log fixture and paste the result.
   - Acceptance criterion: decisions logged equals decisions made, with no
     exceptions; every uncertainty path denies.

G. COMPLETION CONTRACT
   Definition of Done: fail-closed policy service, 100 percent decision
   logging proven by count, control-path guard test passing.
   Evidence to report: fail-closed test output, the N-requests-to-N-records
   proof, the missing-bundle denial output.
   Remaining blockers: any classification vocabulary that depends on an
   unresolved open decision — name it and default it to DENY, never to ALLOW.
   Next prompt: P01-05.
```

**المخرجات المتوقعة:** خدمة سياسة بإصدارات، اختبارات الفشل المُغلق الخمسة، سجل قرارات كامل.
**التحقق المطلوب:** عدد القرارات المسجلة = عدد القرارات المتخذة؛ إزالة الحزمة تُنتج رفضاً شاملاً.
**الاعتمادية التالية:** `P01-05`.

---

### P01-05 — سجل التدقيق غير القابل للتعديل

<!-- meta
id: P01-05
phase: PHASE-01
title_en: Append-only, tamper-evident audit store
prereq: [P01-04]
requirements: [REQ-SEC-04, REQ-DAT-01, REQ-TEN-08]
-->

**ماذا سينفذ هذا الأمر؟** يبني مخزن تدقيق إضافي فقط (append-only/WORM) يسجّل
الفاعل والفعل وقيمة ما قبل وما بعد والزمن ومعرف الارتباط، ويُثبت أنه كاشف
للتلاعب.

**لماذا نحتاجه؟** الضابط `CTRL`/`SEC-06` في الورقة 27 الصف 7 بأولوية `CRITICAL`،
ودليله المطلوب: «اختبار تلاعب واسترجاع». والورقة 04 الصف 2 تحظر على مالك المنصة
نفسه «تعطيل audit» — أي أن السجل يجب أن يكون محمياً من أعلى صلاحية في النظام.

**ما المتطلبات السابقة؟** `P01-04`.

**ما النتيجة المتوقعة؟** مخزن تدقيق مُثبت، واستعلام استرجاع بنطاق مستأجر،
واختبار تلاعب يفشل الكشف إن عُطّل.

**كيف نتحقق من نجاحه؟** محاولة تعديل أو حذف سجل تدقيق تُرفض؛ تعديل مباشر في
المخزن يُكتشف بسلسلة تحقق.

```text
TASK P01-05 — Append-only, tamper-evident audit store

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-05
   Phase: PHASE-01
   Prerequisites: P01-04 (policy decisions are a primary audit producer)
   Requirements covered: REQ-SEC-04, REQ-DAT-01, REQ-TEN-08

B. OBJECTIVE
   Implement the audit and evidence store as append-only or WORM, recording
   actor, action, before and after values, timestamp and correlation id, and
   prove it is tamper-evident and retrievable.

   Why this is necessary: sheet 27 row 7 marks this control CRITICAL and names
   the required evidence as a tamper and retrieval test. Sheet 04 row 2
   forbids even PLATFORM_OWNER from disabling audit, so the store must be
   protected against the system's highest privilege. Sheet 28 row 20 defines
   AuditEvent as append-only by contract.

   SCOPE BOUNDARY: the audit store, its write path, its retrieval API and its
   integrity verification. Observability dashboards are PHASE-10. Retention and
   legal hold policy execution is PHASE-11; here you implement the retention
   field and the enforcement hook, not the PDPL workflow.

C. CONTEXT
   Required inputs:
     - the policy decision log writer from P01-04
     - the security events from P01-02
     - config/registries/data-entities.json, AuditEvent entry
   Producers that must write audit events, per the source: all services
   (sheet 28 row 20). At this point that means authentication, authorization
   denials, policy decisions, cross-tenant attempts, credential rotation and
   break-glass grants.

D. EXECUTION INSTRUCTIONS
   1. Implement the audit event schema: event_id, tenant_id, actor (subject and
      role), action, resource reference, before value, after value, decision,
      reason code, correlation id, causation id, occurred_at in UTC,
      recorded_at in UTC, and a retention class.
   2. Enforce append-only at the storage layer, not in application code:
        - revoke UPDATE and DELETE from the application role;
        - if the engine supports it, use an immutability or WORM feature;
        - if the store is object-based, enable object lock.
      Document precisely which mechanism you used and what privilege could
      still bypass it — then restrict that privilege and record who holds it.
   3. Implement tamper evidence: chain each record to the previous one with a
      cryptographic digest over the record's canonical form plus the previous
      digest, per tenant stream. Provide a verification routine that walks a
      stream and reports the first broken link.
   4. Redaction on write: secrets, tokens, PAN-like strings and raw payloads
      must never enter the store. Implement a redaction filter on the write
      path and test it with representative strings.
   5. Retrieval: a tenant-scoped, role-gated query API supporting filter by
      actor, action, resource, correlation id and time range, with cursor
      pagination. AUDITOR role is read-only with no bulk export beyond a
      configured limit (sheet 04 row 11 forbids excessive download).
   6. Protect against privileged disablement: adding a configuration flag that
      turns auditing off is prohibited. If a maintenance path must exist, it
      requires dual approval, is itself audited to a separate stream, and
      expires. Prove this with a test.
   7. Write the integrity tests:
        a. an UPDATE attempt on an audit record is rejected;
        b. a DELETE attempt is rejected;
        c. an out-of-band modification directly in the store is detected by the
           verification routine, which names the broken record;
        d. retrieval by correlation id returns the full causal chain for a
           multi-service request;
        e. the redaction filter strips every representative secret pattern;
        f. a cross-tenant audit read is denied (reuse the P01-02 helper).
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - audit event schema and migration
   - storage-level append-only enforcement with the mechanism documented
   - digest-chain tamper evidence plus a verification routine
   - a write-path redaction filter
   - a tenant-scoped, role-gated retrieval API with pagination
   - tests/security/audit-integrity.* covering cases a through f
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all six integrity tests.
   - For case c, show the verification routine naming the exact tampered
     record.
   - State which privilege could still bypass append-only, who holds it, and
     how that is controlled. If the answer is "none", prove it.
   - Acceptance criterion: a tamper is always detected and named; no audit
     write path can be disabled without dual approval and its own audit trail.

G. COMPLETION CONTRACT
   Definition of Done: append-only enforced at storage level, tamper detection
   working and demonstrated, retrieval scoped and paginated, redaction tested.
   Evidence to report: the six test outputs, the tamper-detection output, and
   the privilege analysis.
   Remaining blockers: any WORM or object-lock capability unavailable in the
   local environment — state what production must enable, and what the local
   fallback proves and does not prove.
   Next prompt: P02-01. PHASE-01 exit requires AT-SEC-001 green, the sheet-04
   deny suite green, and audit tamper detection demonstrated.
```

**المخرجات المتوقعة:** مخزن تدقيق إضافي فقط، سلسلة بصمات، API استرجاع، مرشّح حجب.
**التحقق المطلوب:** رفض التعديل والحذف، كشف التلاعب بتسمية السجل، حجب الأسرار.
**الاعتمادية التالية:** `P02-01`.

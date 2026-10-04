# PHASE-16 — التجارة المؤجلة (خارج نطاق الإطلاق)

<!-- phasemeta
id: PHASE-16
depends_on: [PHASE-14]
criticality: DEFERRED
-->

## حالة هذه المرحلة: مُغلقة

المصدر يؤجّل هذا النطاق صراحةً. الورقة 68 الصف 8:

> «White-label، والمستأجرون الخارجيون، وبيع الاشتراكات **مؤجلة صراحةً**»
> (Commercialization: White-label, external tenants and subscription sales are
> explicitly deferred).

والورقة 68 الصف 3 تحدد نطاق الإطلاق: «تشغيل أحادي المستأجر مملوك الآن؛ بدائيات
واعية بالمستأجر للمستقبل». والورقة 57 الصف 9 (`A08`) تصنّف الأثر إن تجاهلنا ذلك:
«Scope creep»، والتنفيذ المطلوب: «مستأجر واحد أولاً مع فرض سياق المستأجر».

لذلك هذه المرحلة **لا تُنفَّذ** إلا بتفويض مكتوب من المالك يرفع هذا التأجيل.

## لماذا تُدرَج المرحلة إذاً؟

لأن المصدر يحتوي ستة أوراق كاملة من المواصفات التجارية (43 إلى 48 و53 و55)،
وتجاهلها كان سيُنتج مكتبة أوامر ناقصة التغطية. وجودها هنا — مُعلَّمة ومُبوَّبة —
يحقق أمرين: تغطية كاملة للمصدر، ومنع التنفيذ غير المصرح به.

## الأوراق المُغطاة ولم تُنفَّذ

| الورقة | المحتوى | حالة المصدر |
|---|---|---|
| `43_COMMERCE_OVERVIEW` | ثماني قدرات تجارية `COM-01..COM-08` | `DESIGN ONLY` |
| `44_TENANT_BLUEPRINT` | ثمانية كيانات مستأجرين (جزء منها مُنفَّذ في `PHASE-01`) | `DESIGN ONLY` |
| `45_AGENT_MARKETPLACE` | تسعة حقول كتالوج الوكلاء | `SPEC` |
| `46_AGENT_STUDIO` | ثماني مراحل استوديو الوكلاء | `SPEC` |
| `47_WHITE_LABEL_PORTAL` | خمسة أنماط تسليم بعلامة بيضاء | `SPEC` |
| `48_BILLING_CONTRACTS` | ستة SKUs للفوترة | `SPEC` |
| `53_B2B_API_CONTRACT` | تسع عمليات API للأعمال | `SPEC` |
| `55_REQUIREMENTS_DELTA` | عشرة فروق `D01..D10` | `P0` داخل نطاق B2B المؤجل |

## ما نُفِّذ فعلاً من هذه الأوراق في مراحل أخرى

لتجنّب الالتباس: الأجزاء التي تخدم التشغيل أحادي المستأجر **نُفِّذت** في مراحل
سابقة، لأن المصدر يطلب «بدائيات واعية بالمستأجر»:

- `tenant_id` والعزل والـRLS: `PHASE-01` (`REQ-TEN-01`..`REQ-TEN-09`).
- كيانات `Organization`, `Tenant`, `Workspace`, `Membership`, `Project`,
  `EvidencePackage`, `AuditEvent` من الورقة 44: `PHASE-01`.
- عدادات الاستخدام ودفتره (`COM-07`): `PHASE-04` و`PHASE-08`.
- تصدير البيانات وحذفها (`COM-08`): `PHASE-11`.
- سطوح القراءة الإدارية للمناطق التجارية: `PHASE-13`.

**غير المُنفَّذ** هو السلوك التجاري متعدد المستأجرين: الكتالوج، والاستحقاقات،
والاشتراكات، والعلامة البيضاء، والدومينات المخصصة، والتضمين، وبيع الحزم.

## شروط الدخول

تفويض مكتوب من المالك يرفع التأجيل المسجَّل في الورقة 68 الصف 8، مُسجَّل في
`docs/OPEN-DECISIONS.md` ضد `OD-08`.

## شروط الخروج

لا تنطبق أثناء التأجيل. إن صدر التفويض: اجتياز اختبارات الاستحقاق والعلامة
والدومين والتضمين ومطابقة الفوترة، تحت دليل عزل متعدد المستأجرين.

## المتطلبات المغطاة في هذه المرحلة

`REQ-GOV-02`, `REQ-DEF-01`..`REQ-DEF-06`, `REQ-AGT-10`, `REQ-AGT-11`

---

## الأوامر التنفيذية

### P16-01 — بوابة التفويض (الأمر الوحيد القابل للتنفيذ الآن)

<!-- meta
id: P16-01
phase: PHASE-16
title_en: Commerce authorization gate and scope assessment
prereq: [P14-04]
requirements: [REQ-GOV-02, REQ-DEF-05, REQ-DEF-06]
-->

**ماذا سينفذ هذا الأمر؟** لا يبني أي ميزة تجارية. يُنتج تقييم نطاق وتفويضاً
صريحاً: ما الذي يلزم فعلاً لرفع التأجيل، وما تكلفته، وما مخاطره.

**لماذا نحتاجه؟** لأن القرار بين «مستأجر واحد الآن» و«تجارة متعددة المستأجرين»
قرار تجاري للمالك، لا قرار هندسي. والورقة 55 تحدد عشرة فروق `D01..D10` كلها
`P0` **داخل نطاق B2B** — وهذه الصياغة بالضبط هي ما يجعل تجاهلها خطأً وتنفيذها
بلا تفويض خطأً أيضاً.

**ما المتطلبات السابقة؟** `P14-04` — دفتر الأدلة يعمل، فنعرف الحالة الحقيقية
قبل إضافة نطاق.

**ما النتيجة المتوقعة؟** وثيقة تقييم نطاق وقرار مُسجَّل: إما تفويض مكتوب، أو
إبقاء التأجيل.

**كيف نتحقق من نجاحه؟** لا كود تجاري مُضاف؛ ووثيقة التقييم تربط كل فرق من
العشرة بتكلفته وأثره الأمني.

```text
TASK P16-01 — Commerce authorization gate and scope assessment

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P16-01
   Phase: PHASE-16 (Deferred commerce — explicitly out of launch scope)
   Prerequisites: P14-04 (the evidence ledger reflects the real platform state)
   Requirements covered: REQ-GOV-02, REQ-DEF-05, REQ-DEF-06

B. OBJECTIVE
   Produce a scope and risk assessment for lifting the commerce deferral, and
   record the owner's explicit decision. Build no commercial feature.

   Why this is necessary: sheet 68 row 8 explicitly defers white-label,
   external tenants and subscription sales. Sheet 68 row 3 scopes the launch to
   single-tenant owned operation with tenant-aware primitives. Sheet 57 row 9
   (A08) names the risk of ignoring that as scope creep. Sheet 55 marks its ten
   deltas P0 — but P0 within the B2B scope, which is precisely the phrasing
   that makes both ignoring them and implementing them without authorization
   wrong. The decision is commercial and belongs to the owner.

   SCOPE BOUNDARY: assessment and decision recording only. Do not create a
   catalog, an entitlement service, a branding service, a custom domain path,
   an embed token, a subscription or a B2B endpoint. Do not add a database
   table for any of them. If you find yourself writing commercial logic, stop.

C. CONTEXT
   Required inputs:
     - sheet 43 rows 2-9 (COM-01..COM-08, all DESIGN ONLY)
     - sheet 44 rows 2-9 (tenant blueprint entities; note which are already
       implemented in PHASE-01)
     - sheet 45 rows 2-10 (marketplace catalog fields, SPEC)
     - sheet 46 rows 2-9 (agent studio stages, SPEC)
     - sheet 47 rows 2-6 (five white-label delivery modes, SPEC)
     - sheet 48 rows 2-7 (six billing SKUs, SPEC, with the explicit caveat that
       prices are to be set commercially)
     - sheet 53 rows 2-10 (nine B2B API operations, SPEC)
     - sheet 55 rows 2-11 (ten deltas D01..D10 with owners, reference sheets
       and validation methods)
     - sheet 54 rows 2-11 for the go-live gates that are specifically B2B:
       G02 agent entitlement, G03 B2B billing and metering, G04 custom domain
       and SSO, G09 white-label security — all P0 release blockers, all
       UNVERIFIED
     - docs/evidence/GATE-ASSESSMENT.md from P14-04 for the platform's real
       current state

D. EXECUTION INSTRUCTIONS
   1. Write docs/commerce/SCOPE-ASSESSMENT.md. For each of the ten deltas
      D01..D10 from sheet 55, record:
        - the delta as the source states it;
        - what already exists from the earlier phases (several are partly
          satisfied: tenant isolation from PHASE-01, usage metering from
          PHASE-04 and PHASE-08, data export and deletion from PHASE-11, RAG
          tenant isolation from PHASE-06);
        - what remains genuinely unbuilt;
        - its security implications, especially for the four B2B go-live gates;
        - an engineering effort estimate with its basis;
        - its dependency on other unresolved open decisions.
   2. Assess the security surface that multi-tenant commerce adds, honestly and
      specifically:
        - custom domains and SSO introduce DNS verification, certificate
          management, CORS and token-scoping risk (sheet 47 row 3 requires DNS
          TXT proof, TLS and CORS; sheet 54 row 5 makes it a P0 gate);
        - the embedded widget introduces frame-ancestors, origin checking and
          signed short-lived token risk (sheet 47 row 4; sheet 43 row 6 states
          iframe permissions must not be bypassable);
        - white-label branding introduces an HTML and CSS injection surface
          (sheet 46 row 5 restricts it to safe HTML and CSS tokens only, and
          sheet 54 row 10 makes white-label security a P0 gate);
        - the agent studio introduces tenant-supplied prompt and tool
          configuration, which is an injection and privilege surface (sheet 45
          row 8 requires signed versioned config and that customization cannot
          break protection);
        - tenant-supplied knowledge corpora multiply the rights-gate and
          isolation surface (sheet 46 row 4);
        - entitlement becomes a security control, not a billing nicety: sheet
          45 row 10 requires that revocation immediately rejects new requests.
      State plainly that each of these is a new attack surface on a platform
      whose P0 security gates are not yet all green.
   3. Assess the operational surface: per-tenant quotas and fairness (sheet 45
      row 9, sheet 54 row 8), support for tenants you do not control, billing
      disputes and reconciliation across tenants (sheet 48, sheet 54 row 4),
      and the sales-to-provisioning process (sheet 43 row 7, which forbids
      automatically creating a paid subscription without a contract).
   4. State the prerequisite position clearly: which currently-open P0 gates
      must be PASS before multi-tenant commerce is responsible to ship. At
      minimum, tenant isolation (sheet 54 G01), engineer sign-off (G10) and
      disaster recovery (G12) should be evidenced before adding external
      tenants, because a multi-tenant failure is a multi-customer failure.
   5. Record the commercial inputs the owner must supply, which are entirely
      absent from the source: the pricing for every SKU in sheet 48 (the source
      says prices are to be set commercially), the contract templates, the
      trademark and IP terms for white-label (sheet 48 row 5 names them), and
      the tax treatment of subscriptions.
   6. Present the decision options neutrally, with their consequences:
        a. keep the deferral — the blueprint's execution scope ends at
           PHASE-15;
        b. lift it partially, for example a single named enterprise customer
           under a bespoke contract, which avoids the catalog and subscription
           machinery while still requiring the isolation and billing gates;
        c. lift it fully, which means building sheets 43 through 48 and 53 and
           satisfying the four B2B P0 gates.
      Give a recommendation with reasoning. Do not make the decision.
   7. Record the owner's answer against OD-08 in docs/OPEN-DECISIONS.md with
      the date, the decider and the scope authorized. If the answer is to keep
      the deferral, that is a complete and successful outcome for this prompt.
   8. Add a guard test asserting no commercial feature has been built: no
      catalog, entitlement, subscription, branding, custom-domain or embed
      table, endpoint or service exists. This test protects against gradual,
      unauthorized scope creep, which is exactly the risk sheet 57 row 9 names.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - docs/commerce/SCOPE-ASSESSMENT.md covering all ten deltas with existing,
     remaining, security, effort and dependencies
   - the security and operational surface assessment
   - the prerequisite gate position
   - the list of owner-supplied commercial inputs
   - three decision options with consequences and a recommendation
   - the recorded decision against OD-08
   - tests/governance/no-commerce-scope-creep.* as a standing guard
   - docs/EXECUTION-LOG.md entry
   NO commercial feature code.

F. VERIFICATION
   - Paste the scope assessment's delta table.
   - Paste the guard test output confirming no commercial feature exists.
   - Paste the recorded OD-08 decision, or state that the owner has not yet
     answered and that the deferral therefore stands.
   - Acceptance criterion: a complete, honest assessment exists; no commercial
     code was written; the decision is recorded or explicitly pending.

G. COMPLETION CONTRACT
   Definition of Done: the assessment written, the guard test in place, the
   decision recorded or pending.
   Evidence to report: the delta table, the guard test, the decision state.
   Remaining blockers: the decision itself is the owner's. If the deferral
   stands, say so plainly and stop — do not proceed to P16-02.
   Next prompt: P16-02, ONLY if the owner's recorded decision authorizes it.
```

**المخرجات المتوقعة:** وثيقة تقييم نطاق، تقييم سطح أمني، قرار مُسجَّل، اختبار حارس ضد التوسع غير المصرح به.
**التحقق المطلوب:** لا كود تجاري مُضاف؛ القرار مُسجَّل أو مُعلَّق صريحاً.
**الاعتمادية التالية:** `P16-02` — فقط عند تفويض مُسجَّل.

---

### P16-02 — تنفيذ التجارة متعددة المستأجرين (مشروط بالتفويض)

<!-- meta
id: P16-02
phase: PHASE-16
title_en: Multi-tenant commerce implementation (conditional on authorization)
prereq: [P16-01]
requirements: [REQ-DEF-01, REQ-DEF-02, REQ-DEF-03, REQ-DEF-04, REQ-AGT-10, REQ-AGT-11]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ الاستحقاقات والكتالوج والعلامة البيضاء والفوترة
وعقود B2B — **فقط** إذا كان قرار المالك المُسجَّل يُفوّض ذلك.

**لماذا نحتاجه؟** لإكمال تغطية المصدر. الأوراق 43 إلى 48 و53 مواصفات حقيقية
بحالة `SPEC` و`DESIGN ONLY`، ولها بوابات إصدار `P0` خاصة بها في الورقة 54.

**ما المتطلبات السابقة؟** `P16-01` **مع** قرار مُسجَّل يُفوّض التنفيذ. بلا ذلك،
هذا الأمر لا يُنفَّذ.

**ما النتيجة المتوقعة؟** استحقاق مفروض وقت التشغيل، وعلامة بيضاء آمنة، وفوترة
مُطابَقة — أو لا شيء، إن لم يصدر التفويض.

**كيف نتحقق من نجاحه؟** تشغيل وكيل بلا استحقاق فعّال يُرفض؛ وعزل بين مؤسستين
مُثبت؛ ومطابقة فاتورة مع الاستهلاك.

```text
TASK P16-02 — Multi-tenant commerce implementation (conditional on authorization)

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P16-02
   Phase: PHASE-16
   Prerequisites: P16-01 complete AND a recorded owner decision against OD-08
                  in docs/OPEN-DECISIONS.md that authorizes implementation,
                  naming the authorized scope
   Requirements covered: REQ-AGT-10, REQ-AGT-11, REQ-DEF-01, REQ-DEF-02,
                         REQ-DEF-03, REQ-DEF-04

B. STOP CONDITION — CHECK THIS FIRST
   Read docs/OPEN-DECISIONS.md and find OD-08.
   - If OD-08 is unresolved, or records that the deferral stands, or does not
     exist: STOP. Do not implement anything. Report that PHASE-16 remains
     closed per sheet 68 row 8, and that the blueprint's execution scope ends
     at PHASE-15.
   - If OD-08 records an authorization, implement only the scope it names. A
     partial authorization (for example a single enterprise customer under a
     bespoke contract) does NOT authorize the catalog, the studio or
     subscription sales.
   Do not treat this prompt's existence as authorization. Do not infer
   authorization from the owner's enthusiasm, from a conversation, or from the
   presence of specifications in the source. Only the recorded OD-08 decision
   authorizes work here.

C. OBJECTIVE
   Implement the authorized subset of multi-tenant commerce: agent
   entitlement, the catalog, tenant agent configuration, white-label delivery,
   billing and the B2B API — each behind its own P0 release gate.

   Why this is necessary: sheets 43 through 48 and 53 specify this scope, and
   sheet 54 defines four B2B-specific P0 release blockers for it. If the owner
   authorizes commercialization, these are the requirements.

   SCOPE BOUNDARY: only what OD-08 authorizes. Everything else stays closed.

D. CONTEXT
   Required inputs:
     - docs/commerce/SCOPE-ASSESSMENT.md from P16-01
     - sheet 45 rows 2-10, the catalog fields with their enforcement and
       acceptance, including that an unlicensed agent cannot run and that
       revocation immediately rejects new requests
     - sheet 46 rows 2-9, the eight studio stages with their platform
       validation, API, security policy and output
     - sheet 47 rows 2-6, the five delivery modes with their guardrails: org
       routing verification; DNS TXT proof, TLS and CORS; CSP frame-ancestors
       and origin checks; scopes, webhooks and quotas; isolation and residency
       review
     - sheet 48 rows 2-7, the six SKUs with their units, entitlements,
       overages, controls, lifecycles and commercial caveats
     - sheet 53 rows 2-10, the nine B2B operations with their error cases,
       access control and SLO evidence
     - sheet 43 rows 2-9, the eight commerce capabilities with their
       acceptance tests
     - sheet 54 rows 3, 4, 5, 10 — the four B2B P0 gates

E. EXECUTION INSTRUCTIONS
   1. Implement entitlement as a runtime security control, not a billing
      record: every agent run performs an entitlement preflight, and an agent
      without an active entitlement is refused. Sheet 45 row 10 requires that
      revocation take effect on new requests immediately, and sheet 52 row 4's
      acceptance is that an unlicensed run is denied. Implement revocation as
      immediate, not eventually-consistent.
   2. Implement the catalog per sheet 45 with versioned immutable SKUs,
      capability schemas, bundles, dependency resolution that rejects an
      incomplete bundle, an approved-model pool enforced by the P04-02 registry,
      human gates, signed versioned customization, and per-tenant limits on
      concurrency, requests per minute, spend and tokens.
   3. Implement tenant agent configuration per sheet 46 with its critical
      security property from row 3: a tenant configuration cannot override the
      system prompt or the platform's protections. Tenant-supplied prompts,
      rules, tools and knowledge are untrusted input and are subject to the
      P05-03 trust labels and the P05-02 tool allowlist. Run the P11-04
      adversarial suite against tenant-supplied configuration specifically.
   4. Implement tenant knowledge upload per sheet 46 row 4 with licence check,
      malware scan and provenance, into a tenant RAG namespace, reusing P06-01
      and P06-02 unchanged — the rights gate applies to tenant-supplied sources
      exactly as it does to platform sources.
   5. Implement branding per sheet 46 row 5 and sheet 47: contrast and image
      size validation, domain ownership verification by DNS TXT, and safe HTML
      and CSS tokens only. Treat the branding payload as untrusted and render
      it through a strict allowlist; a tenant-supplied style must not be able to
      execute script or exfiltrate via CSS. Add an injection test suite.
   6. Implement the delivery modes the authorization covers, each with its
      guardrails: hosted with verified org routing; custom domain with DNS
      proof, TLS and CORS; embedded widget with CSP frame-ancestors, origin
      checks and short-lived signed tokens; API-only with scopes, webhooks and
      quotas; enterprise private with an isolation and residency review.
   7. Implement billing per sheet 48 on top of the P08-04 ledger: per-SKU
      units, included entitlements, overage charges, hard and soft budgets, and
      the lifecycle each SKU names. Enforce sheet 43 row 7's rule that no paid
      subscription is created automatically without a contract. Leave every
      price as owner-supplied configuration — the source states prices are to
      be set commercially, so ship no default price.
   8. Implement the nine B2B operations of sheet 53 with their exact error
      cases: 409 on a duplicate organization, 422 on an invalid or incompatible
      configuration, 403 on an unsigned contract or an out-of-scope token, 409
      on unmet dependencies or a domain conflict, 402 on quota and 403 on
      license for a run, 404 on a missing catalog entry.
   9. Implement the sales-assisted path per sheet 43 row 7 and sheet 52 row 3:
      lead to quote to contract with dual approval, and provisioning only after
      a signed contract.
  10. Satisfy the four B2B P0 gates with real evidence, into the P14-04 ledger:
        - G02 entitlement: three-agent and four-agent bundles, revocation and
          an expired contract;
        - G03 billing and metering: invoice reconciliation, caps and refunds;
        - G04 custom domain and SSO: ownership proof, OIDC and token rotation;
        - G09 white-label security: CSP, CORS, domain routing and brand
          isolation.
  11. Run the full cross-organization isolation suite, extending P11-04's
      cross-tenant category to two real organizations with separate brands,
      domains, knowledge namespaces and entitlements. Sheet 43 row 4's
      acceptance is a leak-prevention test between two organizations, and
      sheet 43 row 5's is that one organization's identity is never exposed to
      another.
  12. Remove or update the P16-01 guard test, which asserted no commercial
      feature exists. Replace it with a scope-conformance test asserting that
      only the authorized subset was built.
  13. Tests:
        a. an agent run with no active entitlement -> refused;
        b. revocation -> the next request is refused immediately;
        c. an incomplete bundle -> rejected on dependency resolution;
        d. a model outside the approved pool -> blocked;
        e. a tenant configuration attempting to override the system prompt or a
           protection -> refused; the adversarial suite against tenant
           configuration passes;
        f. tenant knowledge from an unlicensed source -> refused by the rights
           gate;
        g. branding injection attempts -> neutralized; no script execution and
           no CSS-based exfiltration;
        h. a custom domain without DNS proof -> not activated;
        i. an embedded widget from an unapproved origin -> refused by CSP and
           origin checks;
        j. a subscription creation attempt without a signed contract ->
           refused;
        k. all nine B2B operations return their documented error codes under
           real conditions;
        l. the two-organization isolation suite passes across database, object
           storage, queues, vector namespaces, caches, traces, brands and
           domains;
        m. invoice reconciliation against metered usage balances;
        n. the scope-conformance test confirms only the authorized subset
           exists.
  14. Append to docs/EXECUTION-LOG.md.

F. DELIVERABLES
   Only within the authorized scope:
   - runtime entitlement preflight with immediate revocation
   - the versioned catalog with dependency resolution and per-tenant limits
   - tenant agent configuration that cannot override protections
   - tenant knowledge upload through the unchanged rights gate
   - branding with strict allowlisting and an injection test suite
   - the authorized delivery modes with their guardrails
   - billing with owner-supplied prices and contract-gated provisioning
   - the nine B2B operations with their exact error cases
   - the sales-assisted provisioning path
   - evidence for the four B2B P0 gates in the ledger
   - the two-organization isolation suite
   - the scope-conformance test replacing the P16-01 guard
   - docs/EXECUTION-LOG.md entry

G. VERIFICATION
   - Paste the OD-08 authorization you acted on, with its named scope.
   - Paste the output of all fourteen test groups.
   - Paste the two-organization isolation results across all eight surfaces.
   - Paste the four B2B gate records with their evidence.
   - Paste the scope-conformance test confirming nothing beyond the
     authorization was built.
   - Acceptance criterion: no unlicensed run is possible, revocation is
     immediate, no tenant configuration can weaken a protection, two
     organizations are provably isolated, and only the authorized scope exists.

H. COMPLETION CONTRACT
   Definition of Done: the authorized subset implemented with its four P0 gates
   evidenced and cross-organization isolation proven.
   Evidence to report: the authorization, the test outputs, the isolation
   results, the gate records, the scope-conformance proof.
   Remaining blockers: prices, contract templates, trademark and IP terms and
   tax treatment are owner-supplied. Report any P0 gate still open — and note
   that adding external tenants while a platform P0 security gate is open is a
   decision the owner must make explicitly, not a gap to work around.
   Next prompt: none. This is the final prompt in the library. Return to
   PHASE-14's governance cycle for ongoing operation.
```

**المخرجات المتوقعة:** لا شيء — إلا إذا كان `OD-08` يُفوّض؛ وحينها النطاق المُفوَّض فقط.
**التحقق المطلوب:** التفويض مُسجَّل ومُقتبَس؛ عزل مؤسستين مُثبت على ثمانية أسطح؛ اختبار مطابقة النطاق ناجح.
**الاعتمادية التالية:** لا شيء — هذا آخر أمر في المكتبة.

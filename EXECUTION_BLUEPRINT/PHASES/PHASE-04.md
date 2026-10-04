# PHASE-04 — بوابة الذكاء والتوجيه والميزانية

<!-- phasemeta
id: PHASE-04
depends_on: [PHASE-03]
criticality: P0
-->

## الغرض من المرحلة

هذه المرحلة تُنفّذ الطبقة الجديدة في الإصدار v11: الأوراق 70 إلى 77. وهي تحوّل
`ADR-002` («كل اتصال بالنماذج والأدوات Backend-to-Backend خلف API Gateway») إلى
مكوّن فعلي بثلاث عشرة مسؤولية محددة في الورقة 70.

القرار الحاكم في الورقة 77 الصف 2: «مزودون متعددون عبر بوابة مستقلة» مع رفض
صريح لـ«الارتباط الصلب بـOpenRouter». والورقة 77 الصف 4: «أهلية حتمية ← درجة
وتكلفة مقيسة ← canary» مع رفض «روليت النماذج المجانية المعتم». أي أن التوجيه يجب
أن يكون قابلاً للتدقيق، لا ذكياً وغامضاً.

## شروط الدخول

- اكتمال `PHASE-03`: محرك مسارات العمل يستطيع إرسال مهام مُنمَّطة.
- وجود خزانة أسرار (من `P01-04`/`P13-02` إن سبقت) أو خزانة بديلة موثقة.

## شروط الخروج

- محرك السياسة يسجّل 100% من القرارات ويفشل مُغلقاً.
- مزودان مستقلان على الأقل مُشغَّلان فعلاً.
- اختبارات فوضى (429/5xx/timeout/stalled stream) تُنتج بديلاً مُحدَّداً ومُختبراً.
- حد الميزانية يوقف حلقة جارية.
- دفتر الاستخدام يُسجّل مرة واحدة بالضبط ويُطابَق.

## المتطلبات المغطاة في هذه المرحلة

`ADR-002`, `REQ-GW-01`..`REQ-GW-14`, `REQ-GW-17`, `REQ-GW-20`, `REQ-API-06`,
`REQ-API-07`, `REQ-API-08`, `REQ-DAT-08`, `REQ-COM-10`

## تحذير مهم

الورقة 71 الصف 7 قاعدة غير قابلة للتفاوض: «لا LLM لحقيقة القياس المرجعية»
(No LLM for measurement ground truth). والورقة 71 الصف 9: في مسائل السلامة
والإنشاءات «LLM يساعد فقط» و«fail closed». أي توجيه يسمح لنموذج بإنتاج قياس أو
حكم سلامة نهائي يخالف المصدر.

---

## الأوامر التنفيذية

### P04-01 — مدخل البوابة ومغلف المهمة والبث

<!-- meta
id: P04-01
phase: PHASE-04
title_en: Gateway ingress, typed task envelope and streaming
prereq: [P03-05]
requirements: [ADR-002, REQ-GW-01, REQ-GW-02, REQ-API-06, REQ-API-07, REQ-API-08]
-->

**ماذا سينفذ هذا الأمر؟** يبني نقطة دخول واحدة `/v1/ai/execute` بمغلف مهمة
مُنمَّط وبث SSE، خلف مصادقة خدمة وRBAC وidempotency، مع اشتقاق المستأجر من الخادم.

**لماذا نحتاجه؟** الورقة 74 الصف 2 تحدد الشرط الحاسم: «المستأجر مشتق من الخادم؛
لا تثق أبداً بـ`tenant_id` من العميل». والورقة 74 الصف 4 تمنع ظهور أي أسرار أو
بيانات شخصية في البث. هذه البوابة هي المكان الوحيد الذي يُسمح فيه بالوصول إلى
النماذج، فأي مسار جانبي يُبطل `ADR-002`.

**ما المتطلبات السابقة؟** `P03-05`.

**ما النتيجة المتوقعة؟** نقطة تنفيذ واحدة، ونقطتا قراءة (حالة وبث)، واختبار
معماري يمنع أي مسار مباشر إلى مزود.

**كيف نتحقق من نجاحه؟** اختبار يؤكد عدم وجود أي استدعاء لمزود خارج البوابة؛
واختبار يرسل `tenant_id` كاذباً في الطلب ويتأكد من تجاهله.

```text
TASK P04-01 — Gateway ingress, typed task envelope and streaming

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-01
   Phase: PHASE-04 (AI gateway, model registry, routing and budget)
   Prerequisites: P03-05
   Requirements covered: ADR-002, REQ-GW-01, REQ-API-06, REQ-API-07

B. OBJECTIVE
   Build the private AI gateway: one entry point POST /v1/ai/execute taking a
   typed task envelope, plus execution read and SSE event endpoints, behind
   service OIDC authentication, tenant and project RBAC, WAF and idempotency —
   and make it the only path to any model provider.

   Why this is necessary: ADR-002 (sheet 02 row 3) requires every model and
   tool call to be backend-to-backend behind a gateway with no keys in the
   browser. Sheet 70 row 2 specifies this component. Sheet 74 row 2 adds the
   decisive rule: tenant is server-derived and a client-supplied tenant_id is
   never trusted. Sheet 74 row 4 forbids secrets or PII in the stream.

   SCOPE BOUNDARY: ingress, envelope, authorization, idempotency, streaming and
   the architectural guard. Model selection is P04-03. Provider calls are
   P04-04. Budget enforcement is P04-06. Output validation is P04-07. Here, a
   routed execution is dispatched to a test double.

C. CONTEXT
   Required inputs:
     - sheet 74 row 2: POST /v1/ai/execute request fields tenant_id,
       project_id, task_type, risk, modality, input_refs, budget,
       idempotency_key; response execution_id, state, trace_id
     - sheet 74 row 3: GET /v1/ai/executions/{id} returns state, spans, costs,
       model versions, evidence_refs; role-scoped
     - sheet 74 row 4: GET /v1/ai/executions/{id}/events takes last_event_id
       and returns SSE progress, agent events and partial artifacts, with no
       secrets or PII in streams
     - sheet 70 row 2: SLO note "p95 overhead under 150ms target; measure"
     - the policy service from P01-04 and the idempotency layer from P03-03
   Note on the SLO: the source states a target and explicitly instructs to
   measure it. Do not report a latency number you have not measured, and do not
   treat 150ms as achieved because it is written down.

D. EXECUTION INSTRUCTIONS
   1. Define the task envelope as a typed schema with: tenant_id (accepted in
      the payload for client convenience but IGNORED and overwritten from the
      authenticated principal), project_id, task_type, action_risk (R0-R4),
      professional_consequence (P0-P3), modality, input_refs (artifact and
      version and digest references only — never inline content), budget hints,
      and idempotency_key.
   2. Implement server-derived tenancy explicitly: resolve tenant from the
      authenticated principal, compare it against any client-supplied value,
      and on mismatch reject with 403 and emit a security event. Never silently
      accept the client value, and never silently ignore the mismatch.
   3. Enforce service OIDC authentication for internal callers and tenant plus
      project RBAC for user-originated calls, through the existing
      authorization point from P01-03. Consult the policy service from P01-04
      before dispatch; a DENY returns 403 with the reason code, an
      ALLOW_WITH_GATE returns a pending state that names the required human
      gate.
   4. Implement idempotency on execute per P03-03: a repeated key with the same
      request hash returns the original execution_id and creates no second
      execution.
   5. Validate input_refs: every reference must resolve to a CLEAN, existing
      artifact version whose digest matches, using the fail-closed resolver
      from P02-02. Inline payload content is rejected so that provenance is
      always preserved.
   6. Implement the execution record with state, trace_id, span references,
      cost references, resolved model versions and evidence refs, and expose it
      via GET /v1/ai/executions/{id} with role scoping.
   7. Implement the SSE endpoint with resumability by last_event_id and a
      monotonic sequence per execution. Apply a redaction filter on every
      emitted frame; the stream carries progress, state and artifact references,
      never raw prompts, provider responses, secrets or personal data.
   8. Emit ai.execution.completed and ai.execution.failed v1 through the outbox
      per sheet 74 rows 8-9, with consumer dedupe and DLQ.
   9. Implement the architectural guard, which is the most important deliverable
      of this prompt. Write a test that fails if any module outside the gateway
      package imports a provider SDK, constructs a provider HTTP client, or
      reads a provider credential. Enforce it with a dependency or import rule
      so a future contributor cannot bypass the gateway by accident. Also assert
      no client-side bundle can reach a provider: scan the browser build output
      for provider hostnames and credential names.
  10. Instrument gateway overhead: measure the time the gateway adds around the
      downstream call and record p50 and p95 as real measurements. Report the
      numbers you observe against the source's stated target. If you cannot
      produce a representative measurement, say so rather than quoting the
      target.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the typed task envelope schema
   - POST /v1/ai/execute, GET /v1/ai/executions/{id}, GET
     /v1/ai/executions/{id}/events
   - server-derived tenancy with mismatch rejection and security event
   - policy consultation before dispatch
   - input_ref resolution that fails closed
   - resumable, redacted SSE with per-execution sequencing
   - the two gateway events through the outbox
   - tests/architecture/no-provider-bypass.* plus the client bundle scan
   - gateway overhead instrumentation with measured p50 and p95
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the no-provider-bypass test output, then deliberately add a provider
     import outside the gateway, show the test failing, and remove it. Both
     outputs are required.
   - Paste the client bundle scan result.
   - Send a request whose body claims another tenant; paste the 403 and the
     security event.
   - Paste an SSE transcript showing resumption from last_event_id and showing
     a redacted field where a prompt would otherwise appear.
   - Paste the measured p50 and p95 gateway overhead with the sample size, and
     state plainly whether it meets the source's 150ms target or is not yet
     representative.
   - Acceptance criterion: no code path outside the gateway can reach a
     provider, and the test proving it can actually fail.

G. COMPLETION CONTRACT
   Definition of Done: single gateway entry with typed envelope, server-derived
   tenancy, redacted resumable streaming, and an enforced architectural guard
   proven able to fail.
   Evidence to report: both guard outputs, the bundle scan, the tenant-mismatch
   rejection, the SSE transcript, the measured overhead.
   Remaining blockers: none expected. If no real provider is configured yet,
   state that dispatch ran against a double and name P04-04.
   Next prompt: P04-02.
```

**المخرجات المتوقعة:** بوابة بنقطة دخول واحدة، بث مُحجَّب قابل للاستئناف، حارس معماري.
**التحقق المطلوب:** الحارس يفشل عند إضافة استيراد مزود خارج البوابة؛ رفض `tenant_id` الكاذب.
**الاعتمادية التالية:** `P04-02`.

---

### P04-02 — سجل النماذج وسجل القدرات

<!-- meta
id: P04-02
phase: PHASE-04
title_en: Model registry and capability registry
prereq: [P04-01]
requirements: [REQ-GW-03, REQ-GW-13, REQ-GW-19, REQ-GW-20]
-->

**ماذا سينفذ هذا الأمر؟** يبني سجل نماذج بالحقول الأحد عشر في الورقة 72، وسجل
قدرات يختار النماذج المؤهلة بحسب القدرة والنمط ودعم العربية ونافذة السياق
والتوافر، مع قائمة سماح بحسب تصنيف البيانات.

**لماذا نحتاجه؟** الورقة 72 الصف 6 تضع قاعدة دقيقة: `quality_score` يكون «لكل
مهمة بقياس offline/online؛ ولا يكون أبداً درجة عامة شاملة». وهذا يمنع الخطأ
الشائع: ترتيب النماذج بدرجة واحدة ثم اعتبارها صالحة لكل مهمة.

**ما المتطلبات السابقة؟** `P04-01`.

**ما النتيجة المتوقعة؟** سجل نماذج بإصدارات وحالة إصدار وحالة دائرة، وسجل قدرات
يُنتج مجموعة مؤهلين قابلة للتفسير.

**كيف نتحقق من نجاحه؟** لا نموذج يدخل مجموعة المؤهلين لتصنيف بيانات غير مسموح
له؛ ولا نموذج له درجة عامة.

```text
TASK P04-02 — Model registry and capability registry

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-02
   Phase: PHASE-04
   Prerequisites: P04-01
   Requirements covered: REQ-GW-03, REQ-GW-13, REQ-GW-19, REQ-GW-20

B. OBJECTIVE
   Implement the model registry with the eleven fields the source specifies,
   and the capability registry that produces an explainable eligible-model set
   filtered by verified capability, modality, Arabic support, context window,
   availability and data classification allowlist.

   Why this is necessary: sheet 72 sets a precise rule in row 6 — quality_score
   is per-task from offline and online benchmarks and is "never a global
   generic score". Sheet 70 row 4 requires selection by verified capability
   with an allowlist by classification and no unapproved provider. Sheet 77
   row 5 forbids assuming any gateway is Saudi-resident, so region and data
   policy are registry facts, not assumptions.

   SCOPE BOUNDARY: the two registries and eligibility computation. Scoring and
   final selection are P04-03. Benchmarks that populate quality_score are
   PHASE-14 — here you build the field, its provenance and the rule that an
   unpopulated score cannot be treated as good.

C. CONTEXT
   Required inputs:
     - config/registries/model-registry-schema.json from P00-02 (sheet 72
       rows 2-11): model_id (immutable provider/model/version id, owner AI
       platform); provider and region (legal entity and endpoint geography,
       owner Security); capabilities (reasoning, Arabic, vision, tool, JSON,
       context; owner Evaluation); data_policy (approved classes, retention,
       training, transfer; owner Legal); quality_score (per-task, owner QA);
       p50/p95 latency (per task, modality and load; owner SRE); cost_in/out
       (currency per million tokens, effective rate including cache, tools and
       taxes; owner FinOps); limits (RPM, TPM, concurrency, timeout, context;
       owner SRE); health/circuit (healthy, degraded, open, half-open; owner
       Runtime); release_status (candidate, canary, approved, blocked, retired;
       owner Governance)
     - docs/discovery/INTEGRATION-ACCESS-AUDIT.md from P00-03 for what each
       provider's agreement and region actually are
     - sheet 51 rows 2-9 for the nine SLA policy controls and their owners

D. EXECUTION INSTRUCTIONS
   1. Implement the model registry with all eleven fields. model_id is
      immutable and includes the provider, model and version so a route is
      always reproducible. A model entry is a versioned record; changing a
      field creates a new revision with an actor and timestamp.
   2. Make data_policy authoritative and sourced: approved data classes,
      retention period, whether provider training on inputs is permitted, and
      permitted transfer geographies. Each field records the document that
      establishes it (a DPA reference or contract id from P00-03). A field with
      no establishing document is NOT_PROVIDED, and a model with a
      NOT_PROVIDED data policy is ineligible for anything above the lowest
      classification. Do not infer a policy from a provider's marketing page.
   3. Implement quality_score strictly per task: a map from task class to a
      scored result with the evaluation run reference, the dataset reference and
      the measurement date. Reject any attempt to write a scalar global score —
      make it a type error, not a convention. An absent score for a task class
      means INELIGIBLE for quality-first routing in P04-03, never "assume
      acceptable".
   4. Implement release_status with its five values and enforce the lifecycle:
      candidate -> canary -> approved, and blocked or retired as terminal.
      Only approved models serve production traffic; canary serves only the
      configured canary share; blocked and retired serve nothing.
   5. Implement health and circuit state as runtime-owned fields updated by
      P04-04, with the four states the source names.
   6. Implement the capability registry: given a task_type, modality, required
      capabilities, required context window, data classification and tenant
      policy, return the eligible model set plus, for every excluded model, the
      specific exclusion reason. An eligibility result is explainable by
      construction — this is what makes sheet 77 row 4's "auditable decisions"
      achievable.
   7. Enforce the classification allowlist as a hard gate: a model whose
      data_policy does not include the request's data classification is
      excluded regardless of score, cost or availability. Likewise a model
      whose region is outside the permitted transfer geographies for that
      classification.
   8. Treat Arabic support as a verified capability, not an assumption. Sheet 64
      row 4 defines Arabic quality as an evaluation dimension with reviewer
      acceptance, currently NOT TESTED. Until an evaluation exists, the Arabic
      capability flag is UNVERIFIED and routing must surface that.
   9. Record every eligibility computation with its inputs, result and the
      registry revision used, so a past routing decision can be reconstructed.
  10. Tests:
        a. a model with NOT_PROVIDED data policy is excluded for a restricted
           classification, with the reason given;
        b. a model whose region is outside permitted transfer is excluded;
        c. a model with no quality_score for the requested task class is
           excluded from quality-first eligibility, with the reason;
        d. writing a scalar global quality score fails;
        e. a candidate or blocked or retired model never appears in a
           production eligible set;
        f. changing a registry field creates a new revision and leaves the old
           one intact;
        g. an eligibility result lists an exclusion reason for every excluded
           model, with none unexplained;
        h. a context window smaller than the request's requirement excludes the
           model.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the model registry with eleven fields, revisioned, with sourced
     data_policy
   - per-task quality_score typing that rejects a global score
   - release_status lifecycle enforcement
   - runtime health and circuit fields
   - the capability registry returning an explainable eligible set
   - the classification and region hard gates
   - eligibility computation audit records
   - tests/gateway/registry-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eight tests.
   - Paste one full eligibility result showing every model and its include or
     exclude reason.
   - List every registered model with its data_policy provenance document, or
     NOT_PROVIDED. State how many models are currently eligible for the highest
     data classification; if the answer is zero, say so plainly.
   - Acceptance criterion: no model is eligible without an establishing data
     policy document, and no eligibility result contains an unexplained
     exclusion.

G. COMPLETION CONTRACT
   Definition of Done: both registries implemented with the source's exact
   fields and rules; eligibility explainable; hard gates enforced.
   Evidence to report: the eight test outputs, a sample eligibility
   explanation, the model-to-data-policy provenance table.
   Remaining blockers: quality_score is empty until PHASE-14 benchmarks run,
   and the Arabic capability stays UNVERIFIED until then. Report both as
   expected, and confirm the registry refuses to pretend otherwise.
   Next prompt: P04-03.
```

**المخرجات المتوقعة:** سجل نماذج بأحد عشر حقلاً، سجل قدرات بأهلية مُفسَّرة.
**التحقق المطلوب:** رفض الدرجة العامة؛ استبعاد كل نموذج بلا مستند سياسة بيانات.
**الاعتمادية التالية:** `P04-03`.

---

### P04-03 — الراوتر التكيّفي وسياسات التوجيه

<!-- meta
id: P04-03
phase: PHASE-04
title_en: Adaptive router and the eight routing policies
prereq: [P04-02]
requirements: [REQ-GW-04, REQ-GW-14, REQ-GW-15, REQ-GW-16, REQ-GW-17]
-->

**ماذا سينفذ هذا الأمر؟** يبني الراوتر: قواعد حتمية أولاً، ثم درجة وتكلفة مقيسة،
ثم canary؛ وينفّذ سياسات التوجيه الثماني في الورقة 71 بأرضية جودة لكل صنف مهمة.

**لماذا نحتاجه؟** الورقة 77 الصف 4 ترفض «روليت النماذج المجانية المعتم» وتطلب
«قرارات قابلة للتدقيق». والورقة 70 الصف 5 تشترط: «قواعد حتمية أولاً؛ contextual
bandit فقط بعد التقييم». والورقة 71 تضع لكل صنف مهمة استراتيجية وفحص جودة وقاعدة
بديل وضابط تكلفة.

**ما المتطلبات السابقة؟** `P04-02`.

**ما النتيجة المتوقعة؟** راوتر حتمي قابل للتفسير والإعادة، وثماني سياسات مُنفَّذة،
وأرضية جودة تمنع التدهور الصامت.

**كيف نتحقق من نجاحه؟** إعادة نفس الطلب بنفس حالة السجل تُنتج نفس القرار؛ ومهام
القياس والسلامة لا تُوجَّه إلى نموذج أبداً.

```text
TASK P04-03 — Adaptive router and the eight routing policies

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-03
   Phase: PHASE-04
   Prerequisites: P04-02 (eligible model sets available)
   Requirements covered: REQ-GW-04, REQ-GW-14, REQ-GW-15, REQ-GW-16,
                         REQ-GW-17

B. OBJECTIVE
   Implement the adaptive router — quality-first for high-risk tasks, least-cost
   within a validated tier for routine tasks, deterministic rules before any
   learning — and the eight per-task-class routing policies with their quality
   checks, fallback rules and cost controls.

   Why this is necessary: sheet 70 row 5 requires deterministic rules first and
   permits a contextual bandit only after evaluation, with a quality floor per
   task. Sheet 77 row 4 adopts "deterministic eligibility, then measured score
   and cost, then canary" and explicitly rejects "opaque free-model roulette",
   because the rationale is auditable decisions.

   SCOPE BOUNDARY: selection logic and policy enforcement. Provider invocation
   and failover execution are P04-04. Do not implement a bandit or any online
   learning in this prompt — the source gates that behind evaluation evidence
   that does not exist yet.

C. CONTEXT
   Required inputs:
     - config/registries/routing-policies.json (sheet 71 rows 2-9), the eight
       task classes with candidate tier, route strategy, quality check,
       fallback rule and cost control:
       1. OCR/extraction — document vision verified; benchmark Arabic docs and
          plans, OCR deterministic first; check field accuracy and confidence;
          fallback a different approved vision model; cost control crop pages,
          only changed regions
       2. Routine support — fast low-cost; approved small model with RAG; check
          citation and answer grounding; fallback mid-tier approved; cost
          control max output tokens
       3. Architectural reasoning — high-quality reasoning; approved reasoning
          model; check constraint and evidence; fallback peer-quality approved;
          cost control bounded multi-step
       4. SBC compliance — high-quality plus rules; retrieve licensed
          authoritative codes and a rules engine; check clause citations plus
          human sign-off; fallback pause to human if evidence absent; cost
          control reuse indexed clauses
       5. BOQ/costing — deterministic engine plus LLM; LLM extracts only,
          calculators price; check unit, quantities, audit trail; fallback
          manual review if confidence low; cost control no repeated
          full-document context
       6. LiDAR geometry — native RoomPlan or CAD tools; NO LLM for measurement
          ground truth; check scan confidence plus known dimension; fallback
          manual tape or reference; cost control send geometry not video
       7. Live scan narration — small multimodal only as needed;
          event/keyframe triggered; check grounding and latency; fallback
          disable AI commentary safely; cost control frame sampling and local
          filtering
       8. Safety/structural — engineering deterministic plus expert; LLM
          assists only; check licensed reviewer approval; fallback fail closed;
          cost control premium route only when justified
     - sheet 63 rows 2-8, the parallel task-class table with escalation
       triggers, which refines the above
     - the eligible-set computation from P04-02

D. EXECUTION INSTRUCTIONS
   1. Implement routing as an ordered, auditable pipeline:
        stage 1 hard eligibility (from P04-02; classification, region,
                 capability, context, release_status) — non-negotiable;
        stage 2 policy strategy for the task class (from the register);
        stage 3 measured score and cost ranking within the validated tier;
        stage 4 canary share application.
      Each stage records what it removed and why. The final decision carries
      the full chain.
   2. Implement quality-first versus least-cost by risk: when action_risk or
      professional_consequence is high (R3-R4 or P2-P3), rank by measured
      quality for that task class and never substitute a cheaper model that
      lacks a score. For routine classes, rank by cost within the tier whose
      quality has been validated.
   3. Implement the per-class quality floor. A model with no measured score for
      the class cannot satisfy a floor. If no model clears the floor, the router
      returns NO_ELIGIBLE_ROUTE with the reason — it does not fall back to an
      unscored model. Sheet 70 row 5's gate is "quality floor per task"; an
      unscored route silently taken is exactly the failure this prevents.
   4. Implement the two deterministic-first classes as code paths that do not
      call a model at all:
        - LiDAR geometry (sheet 71 row 7): measurement ground truth comes from
          the native scan or CAD tool. The router must refuse to route a
          measurement-truth task to any model. Make this a hard assertion.
        - BOQ/costing (sheet 71 row 6): the model may extract, but pricing is
          computed by the calculator. The router marks the step EXTRACT_ONLY
          and the pricing path rejects a model-produced price.
   5. Implement fail-closed for safety and structural (sheet 71 row 9): the
      route is assist-only, the output cannot be final, and a licensed reviewer
      approval is a required downstream gate. If that gate is unavailable, the
      task does not run.
   6. Implement the pause-to-human fallback for SBC compliance when source
      evidence is absent (sheet 71 row 5), wired to the AWAITING_INFORMATION or
      AWAITING_REVIEW transition from P03-02 rather than to a guess.
   7. Implement multi-provider topology per sheet 77 row 2: the router must be
      able to select across at least two independent providers, and no code path
      may hard-depend on one aggregator. Add a test that removes one provider
      entirely and asserts the router still produces routes for the classes
      where another approved model is eligible.
   8. Implement canary: a configured share of eligible traffic for a canary
      model, with the share recorded on every decision, and an immediate
      rollback switch that takes effect without a deploy.
   9. Make decisions reproducible: given the same request and the same registry
      revision and policy version, the decision is identical. Record the
      registry revision, policy version and random seed (for canary assignment)
      on every decision.
  10. Tests:
        a. an R4/P3 task routes by measured quality and never to an unscored
           model;
        b. no model clears the floor -> NO_ELIGIBLE_ROUTE with the reason, and
           no call is made;
        c. a measurement-truth LiDAR task -> the router refuses any model
           route; assert with a model-client double that fails if called;
        d. a BOQ task -> marked EXTRACT_ONLY, and a model-produced price is
           rejected by the pricing path;
        e. a safety/structural task with no reviewer gate available -> does not
           run;
        f. an SBC compliance task with absent source evidence -> pauses to
           human, no fabricated citation;
        g. remove one provider -> routes still produced where another approved
           model is eligible;
        h. same request plus same registry revision plus same policy version ->
           byte-identical decision, twice;
        i. canary share honoured over a large sample within tolerance, and the
           rollback switch immediately stops canary assignment;
        j. the decision record for any route explains every stage's exclusions.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the four-stage auditable routing pipeline
   - risk-driven quality-first versus cost-first ranking
   - per-class quality floors with NO_ELIGIBLE_ROUTE semantics
   - the two deterministic-first paths with model routing hard-refused
   - fail-closed safety routing and pause-to-human compliance fallback
   - multi-provider selection with no single-aggregator dependency
   - canary with recorded share and instant rollback
   - reproducible decisions with registry revision, policy version and seed
   - tests/gateway/router-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - For case c, paste the double's assertion proving no model client was
     constructed or called.
   - For case h, paste both decision records and show they are identical.
   - Paste one full decision record showing stage-by-stage exclusions.
   - Acceptance criterion: no unscored model ever serves a high-risk task, no
     model ever produces measurement ground truth, and every decision is
     reproducible and explainable.

G. COMPLETION CONTRACT
   Definition of Done: deterministic, reproducible, explainable routing with
   enforced quality floors and the two no-model paths.
   Evidence to report: the ten test outputs, the no-call assertion, the
   reproducibility proof, a sample decision record.
   Remaining blockers: quality floors cannot be set numerically until PHASE-14
   produces benchmarks (open decision OD-04). Until then the floor
   configuration is empty and the router correctly returns NO_ELIGIBLE_ROUTE
   for quality-first classes. Report that as the expected, honest state — do
   not populate a placeholder floor to make routing appear to work.
   Next prompt: P04-04.
```

**المخرجات المتوقعة:** خط توجيه رباعي المراحل، أرضيات جودة، مسارا «بلا نموذج»، canary.
**التحقق المطلوب:** لا نموذج بلا درجة لمهمة عالية الخطر؛ لا نموذج لحقيقة القياس؛ قرار قابل للإعادة.
**الاعتمادية التالية:** `P04-04`.

---

### P04-04 — محوّلات المزودين والبديل وقاطع الدائرة

<!-- meta
id: P04-04
phase: PHASE-04
title_en: Provider adapters, fallback controller and circuit breaker
prereq: [P04-03]
requirements: [REQ-GW-05, REQ-GW-06, REQ-GW-17, REQ-SEC-01, REQ-OBS-03]
-->

**ماذا سينفذ هذا الأمر؟** يبني محوّلات مزودين تُطبّع العقد، مع مهل وإعادة محاولة
وقاطع دائرة، ووحدة تحكم بديل لا تُنزل الجودة صامتة.

**لماذا نحتاجه؟** الورقة 70 الصف 7 تضع القيد الحاسم: «لا تُنزل أبداً تحقق الهندسة
الحرج بصمت». والورقة 38 الصف 8 (`G-03`) حاجز إصدار يتطلب إثبات
«429/timeout/stalled stream» بـ«fault injection traces».

**ما المتطلبات السابقة؟** `P04-04` يعتمد على `P04-03`.

**ما النتيجة المتوقعة؟** محوّلان لمزودين مستقلين على الأقل، وبديل مُختبَر، وقاطع
دائرة بحالات أربع.

**كيف نتحقق من نجاحه؟** حقن أعطال 429 و5xx وtimeout وبث متوقف يُنتج سلوكاً
مُحدَّداً ومُسجَّلاً، لا تعليقاً ولا نجاحاً زائفاً.

```text
TASK P04-04 — Provider adapters, fallback controller and circuit breaker

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-04
   Phase: PHASE-04
   Prerequisites: P04-03 (routing decisions produced)
   Requirements covered: REQ-GW-05, REQ-GW-06, REQ-GW-17, REQ-SEC-01,
                         REQ-OBS-03

B. OBJECTIVE
   Implement provider adapters with a normalized contract, secrets from a
   vault, an egress allowlist, timeouts, bounded retries and a circuit breaker;
   plus a fallback controller that stays inside the approved region and data
   classification, preserves quality equivalence, and never silently downgrades
   critical engineering verification.

   Why this is necessary: sheet 70 row 6 specifies adapters with a normalized
   contract, vault secrets, egress allowlist and no browser keys. Sheet 70
   row 7 specifies the fallback controller and its hard rule against silent
   downgrade. Sheet 38 row 8 (G-03) is a release blocker requiring fault
   injection traces for 429, timeout and stalled stream. Sheet 76 row 5 (G04)
   requires chaos evidence.

   SCOPE BOUNDARY: provider invocation, resilience and failover. Do not change
   routing logic. Do not implement budget enforcement (P04-06) or output
   validation (P04-07).

C. CONTEXT
   Required inputs:
     - the routing decision from P04-03, which names model_id and a
       fallback chain
     - sheet 70 row 6 providers named as candidates: OpenAI, Anthropic, Google,
       with OpenRouter optional. Sheet 77 row 2 adopts multi-provider through an
       independent gateway and rejects hard lock-in to OpenRouter.
     - sheet 75 rows 2-3: the 429 runbook (bounded exponential jitter,
       backpressure, route to an approved alternate) and the provider outage
       runbook (stop retries, open circuit, fail over to allowed)
     - sheet 51 row 6: reliability control with timeouts, circuit breaker and
       retry jitter, metric p95 and error rate, fallback provider failover,
       proof chaos tests
   Credential reality: use only credentials already present in the environment,
   per the audit from P00-03. If none exist, implement against a contract-
   conformant local fake and report that no real provider was exercised. Do not
   create accounts and do not spend money.

D. EXECUTION INSTRUCTIONS
   1. Define one normalized adapter interface covering: text and multimodal
      completion, streaming, tool or function calling, structured JSON output,
      token accounting, and error classification. Every provider implements the
      same interface so the router is provider-agnostic.
   2. Implement a provider-independent error taxonomy mapping each provider's
      errors into the classes sheet 36 row 15 requires: errorCode, retryable,
      providerFailure, partialArtifacts. At minimum: RATE_LIMITED,
      TIMEOUT, STALLED_STREAM, SERVER_ERROR, INVALID_REQUEST,
      CONTENT_FILTERED, CONTEXT_EXCEEDED, AUTH_FAILED, QUOTA_EXCEEDED.
   3. Load credentials from the vault only, at call time, never into logs,
      traces, error messages or the SSE stream. Add a test asserting a forced
      adapter error does not include the credential anywhere in its message or
      stack.
   4. Enforce an egress allowlist at the network layer for the gateway process:
      only approved provider hostnames are reachable. Add a test asserting a
      call to a non-allowlisted host fails. This is the control that limits
      tool-based exfiltration (sheet 27 row 8).
   5. Implement timeouts at three levels: connection, first token, and total
      wall clock. A stalled stream is a distinct, detected failure — a stream
      that stops producing tokens must trip the first-token or inter-token
      timeout rather than hanging until the total budget expires.
   6. Implement bounded retries with exponential backoff and jitter per
      sheet 75 row 2, with a maximum attempt count and a maximum total added
      latency. Retry only errors classified retryable, and only steps whose
      side-effect class is SAFE_RETRYABLE per P03-02.
   7. Implement the circuit breaker with the four states sheet 72 row 10 names:
      healthy, degraded, open, half-open. Opening stops retries immediately
      (sheet 75 row 3). Half-open admits a probe. State changes update the model
      registry's health field and emit an event.
   8. Implement the fallback controller with the source's constraints:
        - a fallback candidate must be within the approved region and data
          classification for the request — never widen either to find capacity;
        - it must be quality-equivalent for the task class, using the per-class
          scores from P04-02;
        - for critical engineering verification (high P, and the
          safety/structural and SBC compliance classes), a downgrade is
          forbidden. If no equivalent route exists, the execution fails closed
          with FALLBACK_UNAVAILABLE. It does not quietly use a weaker model.
        - every fallback is recorded on the execution with the original model,
          the fallback model, the trigger and the equivalence justification.
   9. Implement backpressure: when providers are saturated, shed or queue by
      priority rather than amplifying load with retries. Sheet 73 row 2's
      action for a p95 breach is "shed low-priority load" — implement a
      priority signal so that is possible.
  10. Build the chaos test harness with a fault-injecting fake provider, and
      write the tests:
        a. 429 -> bounded jittered retry, then route to an approved alternate;
           assert attempt count and total added latency are within bounds;
        b. repeated 5xx -> circuit opens, retries stop immediately, registry
           health becomes open, event emitted;
        c. half-open probe succeeds -> state returns to healthy; probe fails ->
           back to open;
        d. stalled stream -> detected by the inter-token timeout, not by the
           total budget; execution ends with STALLED_STREAM and a partial
           artifact record if any;
        e. connection timeout -> classified TIMEOUT, retried per policy;
        f. fallback that would cross a region or classification boundary ->
           refused, execution fails closed;
        g. a high-P critical task with no quality-equivalent fallback ->
           FALLBACK_UNAVAILABLE, no downgrade;
        h. a forced adapter error -> no credential appears in the message,
           stack, log or stream;
        i. egress to a non-allowlisted host -> blocked;
        j. saturation -> low-priority load shed, high-priority served, no
           retry amplification.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the normalized adapter interface and at least two provider
     implementations (real where credentials exist, contract-conformant fakes
     otherwise, clearly labelled)
   - the provider-independent error taxonomy
   - vault-only credential loading with leak tests
   - the network egress allowlist
   - three-level timeouts including inter-token stall detection
   - bounded jittered retries limited to safe-retryable steps
   - the four-state circuit breaker wired to registry health
   - the fallback controller with region, classification and equivalence
     constraints and FALLBACK_UNAVAILABLE semantics
   - priority-based backpressure and load shedding
   - tests/chaos/*.* covering cases a through j, with traces retained as
     evidence for release gate G-03
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten chaos tests.
   - Retain and reference the fault-injection traces; sheet 38 row 8 names
     them as the required evidence for G-03, so they must be stored where the
     evidence ledger can cite them.
   - For case g, paste the FALLBACK_UNAVAILABLE outcome and show no provider
     call was made to a lower-quality model.
   - For case h, paste the grep over the error output proving no credential
     material.
   - State plainly which providers were exercised with real credentials and
     which with fakes.
   - Acceptance criterion: every one of the four fault classes in G-03 produces
     a bounded, recorded, non-hanging outcome, and no critical task is ever
     silently downgraded.

G. COMPLETION CONTRACT
   Definition of Done: two adapters behind one interface, chaos suite green,
   circuit breaker and fallback behaving per the source's constraints, traces
   retained.
   Evidence to report: the ten test outputs, the trace storage location, the
   real-versus-fake provider statement, the credential leak grep.
   Remaining blockers: providers without an agreement or credential (from
   P00-03) cannot be exercised for real. Name them; this is an owner-owned
   commercial blocker and a direct input to release gate G01 on sheet 76.
   Next prompt: P04-05.
```

**المخرجات المتوقعة:** محوّلان بواجهة واحدة، تصنيف أخطاء، قاطع دائرة، وحدة بديل.
**التحقق المطلوب:** أربع فئات أعطال بنتائج محدودة ومُسجَّلة؛ لا تدهور صامت لمهمة حرجة.
**الاعتمادية التالية:** `P04-05`.

---

### P04-05 — مُجمِّع السياق وذاكرة المطالبات

<!-- meta
id: P04-05
phase: PHASE-04
title_en: Context compiler and prompt cache
prereq: [P04-04]
requirements: [REQ-GW-07, REQ-GW-08, REQ-KNW-04]
-->

**ماذا سينفذ هذا الأمر؟** يبني مُجمِّع سياق محدود بالمهمة مع استشهادات وإزالة
تكرار دلالي واستدعاء مُفلتَر بنطاق المستأجر، وذاكرة مطالبات معزولة.

**لماذا نحتاجه؟** الورقة 77 الصف 6 تعتمد «RAG وميزانيات سياق وذاكرة وkeyframes
وأدوات أولاً»، وترفض «ضغط أدلة الهندسة بشكل أعمى»، والسبب المذكور: «الحفاظ على
المصدرية». والورقة 76 الصف 6 (`G05`) تجعل عزل المستأجر شاملاً للذاكرة والآثار
والسجلات، لا قاعدة البيانات وحدها.

**ما المتطلبات السابقة؟** `P04-04`.

**ما النتيجة المتوقعة؟** مُجمِّع سياق يقيس التوفير، وذاكرة معزولة بثلاثة أبعاد،
واستدعاء لا يمكن إصداره بلا فلتر مستأجر.

**كيف نتحقق من نجاحه؟** اختبار يؤكد أن ذاكرة مستأجر لا تخدم مستأجراً آخر أبداً؛
واختبار يؤكد أن الضغط لا يحذف استشهاداً أو مُحدِّد موضع.

```text
TASK P04-05 — Context compiler and prompt cache

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-05
   Phase: PHASE-04
   Prerequisites: P04-04
   Requirements covered: REQ-GW-07, REQ-GW-08, REQ-KNW-04

B. OBJECTIVE
   Implement the context compiler — task-scoped context with citations,
   semantic de-duplication and tenant-scoped ACL-filtered retrieval, reporting
   tokens saved against a baseline — and a prompt cache isolated by tenant,
   data classification and model version.

   Why this is necessary: sheet 70 rows 8-9 specify both components and their
   gates (tokens saved versus baseline; cache hit rate; isolation by tenant,
   classification and model version with no cross-tenant leakage). Sheet 77
   row 6 adopts context budgets and caching but explicitly rejects blindly
   compressing engineering evidence, because provenance must be preserved.
   Sheet 76 row 6 extends tenant isolation to cache, traces and logs.

   SCOPE BOUNDARY: context assembly and caching. The RAG corpora, their rights
   gate and their ingestion are PHASE-06 — here you build the retrieval
   interface with mandatory tenant filtering and consume whatever index exists.

C. CONTEXT
   Required inputs:
     - the mandatory-tenant-filter retrieval interface from P01-02 step 4
     - sheet 24 row 5 (RAG-PROJECT): metadata tenant, project, ACL, revision,
       hash, classification; strategy project-scoped index, no cross-tenant
     - sheet 71 cost controls per class: crop pages and only changed regions
       for extraction; max output tokens for routine; bounded multi-step for
       reasoning; reuse indexed clauses for compliance; no repeated
       full-document context for BOQ; send geometry not video for LiDAR; frame
       sampling for live narration

D. EXECUTION INSTRUCTIONS
   1. Implement a context budget per task class, read from configuration, with
      the per-class cost controls above encoded as assembly rules rather than as
      advice.
   2. Implement task-scoped assembly: the compiler receives the task envelope
      and returns a context package carrying, for every included element, its
      provenance — artifact, version, digest and locator, or source, version
      and anchor for a knowledge citation. An element with no provenance cannot
      enter the package. This is the mechanism that makes sheet 77 row 6's
      "preserve provenance" enforceable rather than aspirational.
   3. Implement semantic de-duplication that removes redundant passages but
      never removes a citation, a locator or a unit. Add a test asserting that
      de-duplication preserves the full citation set and every numeric value
      with its unit. Dropping a unit from engineering evidence is a correctness
      failure, not a size optimization.
   4. Implement budget overflow handling explicitly: when the assembled context
      exceeds the budget, the compiler reduces by the class's declared strategy
      (crop to changed regions, reuse indexed clauses, bound the step count) and
      records what it dropped. If it cannot fit within budget without dropping
      evidence that the task's quality check requires, it returns
      CONTEXT_BUDGET_EXCEEDED rather than silently truncating. Truncating
      engineering evidence silently is the failure sheet 77 row 6 rejects.
   5. Enforce mandatory tenant filtering structurally: the retrieval call cannot
      be constructed without a tenant scope. Make the unfiltered form
      unrepresentable in the type system or guarded by a single checked
      constructor, and test that bypassing it fails.
   6. Implement the prompt cache:
        - the cache key includes tenant, data classification, model id and
          version, prompt template version, and a digest of the stable prefix;
        - entries never cross any of those dimensions;
        - a classification change invalidates;
        - a model version change invalidates;
        - cache content is encrypted at rest and excluded from logs and traces.
   7. Measure and expose: tokens saved versus an uncompiled baseline, cache hit
      rate, and context assembly latency — as measured values feeding the
      PHASE-10 dashboards. Report real measurements only.
   8. Tests:
        a. tenant A's cached entry is never served to tenant B — attempt it
           directly against the cache and assert a miss;
        b. the same prompt under two classifications produces two entries;
        c. a model version bump invalidates;
        d. de-duplication preserves every citation and every value-with-unit;
        e. an element without provenance is refused entry to the package;
        f. a retrieval call cannot be built without a tenant scope;
        g. budget overflow that would drop required evidence returns
           CONTEXT_BUDGET_EXCEEDED rather than truncating;
        h. cache content does not appear in logs, traces or the SSE stream;
        i. measured tokens saved and hit rate are produced from real runs, with
           the sample size reported.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - per-class context budgets with the source's cost-control strategies
   - the provenance-carrying context package with refusal of unprovenanced
     elements
   - citation-and-unit-preserving semantic de-duplication
   - CONTEXT_BUDGET_EXCEEDED semantics instead of silent truncation
   - structurally mandatory tenant-scoped retrieval
   - the three-dimension isolated, encrypted prompt cache
   - measured tokens-saved, hit-rate and latency metrics
   - tests/gateway/context-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - For case a, paste the direct cache probe showing a miss across tenants.
   - For case d, paste the before and after context showing citations and units
     intact.
   - Paste the measured tokens-saved and hit-rate figures with sample sizes. If
     the sample is too small to be meaningful, say so rather than publishing it.
   - Acceptance criterion: no cache entry crosses tenant, classification or
     model version; no compression removes provenance; overflow fails loudly.

G. COMPLETION CONTRACT
   Definition of Done: context compiled within budget with provenance intact,
   cache isolated on all three dimensions, savings measured honestly.
   Evidence to report: the nine test outputs, the cross-tenant cache probe, the
   de-duplication comparison, the measured savings with sample size.
   Remaining blockers: real retrieval quality depends on PHASE-06 corpora,
   which are themselves blocked on source rights (OD-05). Report that the
   interface is complete and the corpora are not.
   Next prompt: P04-06.
```

**المخرجات المتوقعة:** مُجمِّع سياق بمصدرية محفوظة، ذاكرة معزولة بثلاثة أبعاد، قياسات حقيقية.
**التحقق المطلوب:** لا تجاوز ذاكرة بين المستأجرين؛ لا ضغط يحذف مصدرية؛ الفائض يفشل بصوت عالٍ.
**الاعتمادية التالية:** `P04-06`.

---

### P04-06 — وحدة الميزانية ودفتر الاستخدام

<!-- meta
id: P04-06
phase: PHASE-04
title_en: Budget controller and exactly-once usage ledger
prereq: [P04-05]
requirements: [REQ-GW-09, REQ-GW-11, REQ-DAT-08, REQ-COM-10, REQ-AGT-01]
-->

**ماذا سينفذ هذا الأمر؟** يبني وحدة ميزانية بتقدير مُسبق وحدود يومية وشهرية لكل
مهمة ومستأجر، ودفتر استخدام يُسجّل مرة واحدة بالضبط لكل تنفيذ.

**لماذا نحتاجه؟** الورقة 70 الصف 10 ضابطها: «لا نداء فوق الميزانية بلا تفويض».
والورقة 15 الصف 15 (`CTRL-014`) دليلها: «حد الميزانية يوقف الحلقة». والورقة 36
الصف 13 (`RT-08`) تشترط «الحفظ مرة واحدة بالضبط لكل تنفيذ». والورقة 39 الصف 12
تفرض `execution_id UNIQUE`.

**ما المتطلبات السابقة؟** `P04-05`.

**ما النتيجة المتوقعة؟** تقدير مُسبق يمنع التجاوز، وإيقاف صلب للحلقات الجارية،
ودفتر قابل للمطابقة.

**كيف نتحقق من نجاحه؟** حلقة تستهلك بلا حد تتوقف عند السقف؛ وإعادة محاولة لا
تُنتج سجل استخدام ثانياً.

```text
TASK P04-06 — Budget controller and exactly-once usage ledger

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-06
   Phase: PHASE-04
   Prerequisites: P04-05
   Requirements covered: REQ-GW-09, REQ-GW-11, REQ-DAT-08, REQ-COM-10,
                         REQ-AGT-01

B. OBJECTIVE
   Implement the budget controller — per-task, per-tenant daily and monthly
   token and SAR caps with a preflight estimate, a hard stop and approval
   thresholds — and the usage ledger that posts exactly once per execution and
   can be reconciled.

   Why this is necessary: sheet 70 row 10's gate is "no over-budget
   unauthorized calls". Sheet 15 row 15 (CTRL-014) requires the evidence
   "budget cap stops loop". Sheet 36 row 13 (RT-08) requires usage persisted
   exactly once per execution and reconciled with credits. Sheet 39 row 12
   enforces it with execution_id UNIQUE. Sheet 05 row 36 (FIN-03) requires
   attribution to tenant and workflow and prevention of runaway loops.

   SCOPE BOUNDARY: budget enforcement, usage recording and reconciliation
   inputs. Customer-facing pricing is PHASE-08. Cost dashboards are PHASE-10.

C. CONTEXT
   Required inputs:
     - config/registries/data-constraints.json, usage_ledger: required
       execution_id, tenant_id, input_tokens, output_tokens, cost;
       execution_id UNIQUE; index tenant_id, created_at; invariant
       "exactly-once posting"; retention "finance policy"
     - sheet 34 row 13: EV-08 UsageRecorded usage.recorded.v1, aggregate AI
       Core, required payload executionId, inputTokens, outputTokens, producer
       AI Core, consumer billing and observability, ordering key executionId,
       at-least-once, validation "reconcile ledger; no double-charge"
     - sheet 72 row 8: cost_in/out is the effective rate per million tokens
       including cache, tools and taxes
     - sheet 61 row 8: cost spike scenario — throttle and downgrade safe tasks,
       hard tenant and project cap, evidence usage ledger
   Important: all commercial rates in the source calculator are zero except
   VAT (sheet 19 row 54). Provider rates in the model registry must come from
   real contracts. If a rate is absent, the cost field is UNPRICED, and an
   UNPRICED execution still records tokens. Never invent a rate to make a cost
   number appear.

D. EXECUTION INSTRUCTIONS
   1. Implement budget scopes with independent caps: per execution, per task,
      per project, per tenant per day, and per tenant per month, in both tokens
      and currency.
   2. Implement the preflight estimate before dispatch: estimate input tokens
      from the assembled context and output tokens from the task class ceiling,
      price them from the model registry's effective rates, and compare against
      every applicable remaining cap. Over-cap requests are denied before any
      provider call, with a reason naming which cap was hit.
   3. Implement approval thresholds: a configurable band where the request is
      not denied but requires an explicit authorization, returning the
      ALLOW_WITH_GATE pending state from P04-01 rather than proceeding.
   4. Implement the hard stop during execution, which is the control CTRL-014
      requires evidence for. A multi-step or agentic execution re-checks the
      remaining budget before every step and before every provider call, and
      terminates with BUDGET_EXHAUSTED when the cap is reached. Termination
      records the partial artifacts produced so work is not lost silently.
   5. Implement the usage ledger:
        - one row per execution, keyed by execution_id with the UNIQUE
          constraint doing the enforcement;
        - fields: tenant_id, project_id, workflow_run_id, execution_id, model
          id and version, provider, input tokens, output tokens, cached tokens,
          tool units, cost with currency, rate revision used, and UNPRICED flag
          when a rate was absent;
        - writing is idempotent: a retry of the same execution updates nothing
          and inserts nothing new;
        - a provider retry inside one execution adds attempts to the same row's
          accounting rather than creating a second row, so attribution stays
          one-to-one with executions.
   6. Attribute usage to tenant and workflow per sheet 05 row 36, so cost per
      workflow (sheet 17 row 10) is computable without guesswork.
   7. Emit usage.recorded.v1 through the outbox with executionId as the
      ordering key, and implement the reconciliation input: a daily aggregate
      per provider that PHASE-10 compares against the provider's own billing.
   8. Implement graceful degradation per sheet 61 row 8: on approaching a cap,
      throttle and downgrade only tasks whose class permits it — never a
      critical engineering verification class, which must fail closed instead
      (consistent with P04-04).
   9. Tests:
        a. a preflight estimate over a cap -> denied before any provider call;
           assert with a provider double that fails if called;
        b. a request in the approval band -> pending with the gate named, no
           call made;
        c. a runaway multi-step loop -> BUDGET_EXHAUSTED at the cap, with the
           step count bounded and partial artifacts recorded. This is the
           CTRL-014 evidence;
        d. retry the same execution -> exactly one ledger row, unchanged;
        e. three provider attempts within one execution -> one row whose
           accounting includes all three attempts;
        f. concurrent executions for one tenant racing the same cap -> the cap
           is not exceeded; assert with a concurrency test, because a
           read-then-write check without locking will fail here;
        g. a model with no configured rate -> tokens recorded, cost UNPRICED,
           no invented number;
        h. daily and monthly caps roll over correctly across a boundary, in UTC;
        i. approaching a cap -> a routine class is downgraded, a critical class
           fails closed rather than being downgraded;
        j. the emitted usage event conforms to the sheet 34 envelope and carries
           executionId as the ordering key.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - budget scopes and caps in tokens and currency
   - the preflight estimator with pre-dispatch denial
   - approval-threshold banding wired to ALLOW_WITH_GATE
   - the in-execution hard stop with partial artifact recording
   - the usage ledger with execution_id UNIQUE and idempotent writes
   - tenant and workflow attribution
   - usage.recorded.v1 emission and the daily reconciliation aggregate
   - class-aware degradation that never downgrades critical verification
   - tests/finops/budget-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - For case c, paste the loop termination showing the cap, the step count and
     the recorded partial artifacts. Retain this as the CTRL-014 evidence.
   - For case f, paste the concurrency test result and state the mechanism
     preventing the race (lock, atomic decrement, or serialized reservation).
   - For case g, paste the ledger row showing UNPRICED.
   - Acceptance criterion: no provider call happens over a cap, no execution
     produces two ledger rows, and no cost number exists without a real rate.

G. COMPLETION CONTRACT
   Definition of Done: budgets enforced before and during execution, ledger
   exactly-once under retry and concurrency, attribution complete, no invented
   rates.
   Evidence to report: the ten test outputs, the CTRL-014 loop-stop evidence,
   the concurrency mechanism, the UNPRICED row.
   Remaining blockers: provider rates are owner-owned (open decision OD-03).
   Report how many registered models currently have a real rate and how many
   are UNPRICED.
   Next prompt: P04-07.
```

**المخرجات المتوقعة:** حدود ميزانية بتقدير مُسبق، إيقاف صلب أثناء التنفيذ، دفتر استخدام مرة واحدة.
**التحقق المطلوب:** الحلقة الجارية تتوقف عند السقف؛ لا سجل استخدام مكرر؛ لا تكلفة بلا معدل حقيقي.
**الاعتمادية التالية:** `P04-07`.

---

### P04-07 — مُدقِّق المخرجات

<!-- meta
id: P04-07
phase: PHASE-04
title_en: Output validator with provenance and deterministic checks
prereq: [P04-06]
requirements: [REQ-GW-10, REQ-GW-16, REQ-AGT-04, REQ-KNW-05]
-->

**ماذا سينفذ هذا الأمر؟** يبني مُدقِّق مخرجات يفرض مخطط JSON، ومصدرية المصادر،
وفحوصات حسابية وهندسية حتمية، ويطلب اعتماداً بشرياً للاستنتاجات الحرجة للسلامة.

**لماذا نحتاجه؟** الورقة 70 الصف 11 تحدد هذه المسؤولية بدقة، والورقة 36 الصف 11
(`RT-06`) تضيف: «يفشل مُغلقاً عند مخرج غير صالح». والورقة 37 الصف 11 تجعل
«رفض المخرج المُشوَّه» متطلباً مُتتبَّعاً بدليل «schema test + trace».

**ما المتطلبات السابقة؟** `P04-06`.

**ما النتيجة المتوقعة؟** مُدقِّق إلزامي على كل مخرج قبل أن يصبح مستهلَكاً، مع فشل
مُغلق ومسار تصعيد بشري.

**كيف نتحقق من نجاحه؟** مخرج غير مطابق للمخطط يُرفض؛ واستشهاد بلا إصدار يُرفض؛
وحساب غير متسق يُكتشف بحاسبة حتمية لا بنموذج.

```text
TASK P04-07 — Output validator with provenance and deterministic checks

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-07
   Phase: PHASE-04
   Prerequisites: P04-06
   Requirements covered: REQ-GW-10, REQ-GW-16, REQ-AGT-04, REQ-KNW-05

B. OBJECTIVE
   Implement the mandatory output validator: JSON schema enforcement, source
   provenance verification, deterministic math and CAD checks, and a required
   human approval path for safety-critical conclusions — with fail-closed
   behaviour on any invalid output.

   Why this is necessary: sheet 70 row 11 specifies exactly these four
   responsibilities with the gate "eval pass-rate by class". Sheet 36 row 11
   (RT-06) requires the result envelope to be JSON-schema validated and to fail
   closed on invalid output. Sheet 37 row 11 tracks "malformed result rejected"
   as a requirement whose proof is a schema test plus a trace. Sheet 10 row 13
   requires citations to carry source, version, anchor and rights.

   SCOPE BOUNDARY: validation of model and agent output inside the gateway. The
   findings schema and the review workflow are PHASE-07. The evaluation harness
   is PHASE-14. Here you enforce structure, provenance and arithmetic.

C. CONTEXT
   Required inputs:
     - sheet 36 row 11: result envelope fields status, structuredOutput,
       artifactRefs, citations, confidence; validation "JSON schema validated";
       failure action "fail closed on invalid output"
     - sheet 10 rows 13-14: citations carry source, version, anchor and rights
       and are required when a claim is made; confidence is a calibrated score
       for the machine and is explicitly "not an approval"
     - sheet 71 quality checks per class: field accuracy and confidence for
       extraction; citation and answer grounding for routine; constraint and
       evidence checks for architectural reasoning; clause citations plus human
       sign-off for SBC compliance; unit, quantities and audit trail for BOQ;
       scan confidence plus known dimension for LiDAR; grounding and latency for
       live narration; licensed reviewer approval for safety and structural
     - sheet 63 row 2: extraction uses grounding and schema as its quality gate

D. EXECUTION INSTRUCTIONS
   1. Implement the result envelope as a strict schema and validate every
      output against it before the output becomes visible to any consumer or to
      the SSE stream. Validation failure is terminal for that attempt: the
      execution records INVALID_OUTPUT with the validation detail and the
      trace, and does not emit a partial success.
   2. Implement structured-output enforcement per task class, each with its own
      output schema loaded from configuration, so a new task class cannot run
      without a declared output contract.
   3. Implement provenance verification on citations:
        - every citation must carry source, version, anchor and a rights
          snapshot;
        - the anchor must resolve against the cited source version — an
          unresolvable anchor is an invalid citation, not a warning;
        - the rights snapshot must say ALLOWED. A citation to a source whose
          rights are UNKNOWN is rejected, enforcing ADR-009 at the output
          boundary as well as at the retrieval boundary;
        - a claim requiring a citation that has none is rejected per sheet 10
          row 13.
      This is the mechanism behind sheet 37 row 13's requirement that a
      citation include the code edition and its applicability.
   4. Implement artifact reference verification: every artifactRef resolves to
      an existing version whose digest matches, using the fail-closed resolver
      from P02-02.
   5. Implement deterministic checks, run by code and never by a model:
        - unit consistency and dimensional analysis on every numeric claim with
          a unit; a value without a unit where the schema requires one is
          invalid;
        - arithmetic re-computation: any total, sum, area or quantity the output
          asserts is recomputed from its components, and a mismatch beyond a
          declared tolerance is a validation failure;
        - range and plausibility bounds per field from configuration;
        - geometry checks for CAD and scan outputs where the task class
          declares them.
      Sheet 71 row 6 is explicit that calculators price and the model only
      extracts, so a model-asserted price or total is rejected here.
   6. Implement confidence handling per sheet 10 row 14: confidence is recorded,
      is required to be within 0..1, and is never treated as an approval or as a
      substitute for a quality check. Add a test asserting that a high
      confidence value does not bypass any validation.
   7. Implement the human approval requirement for safety-critical conclusions:
      for the safety/structural and SBC compliance classes, and for any output
      with professional consequence P3, the validator marks the output
      PENDING_HUMAN_APPROVAL and the output cannot be consumed as final. It is
      routed to the review path that PHASE-07 implements. Until that path
      exists, the state is terminal-pending, never auto-approved.
   8. Record validation results per class so PHASE-14 can compute the
      "eval pass-rate by class" gate sheet 70 row 11 names.
   9. Tests:
        a. output violating the envelope schema -> INVALID_OUTPUT with detail
           and trace, nothing emitted to the stream;
        b. a claim with no citation -> rejected;
        c. a citation missing version or anchor -> rejected;
        d. a citation whose anchor does not resolve -> rejected, naming it;
        e. a citation to a source with UNKNOWN rights -> rejected (ADR-009 at
           the output boundary);
        f. an artifactRef whose digest no longer matches -> rejected;
        g. a numeric claim missing a required unit -> rejected;
        h. a total that does not equal the sum of its components beyond
           tolerance -> rejected, showing expected versus asserted;
        i. a model-asserted price in a BOQ-class output -> rejected;
        j. confidence 0.99 on a schema-invalid output -> still rejected;
        k. a P3 output -> PENDING_HUMAN_APPROVAL, not consumable as final;
        l. validation outcomes are recorded per class and queryable.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the strict result envelope schema and mandatory pre-emission validation
   - per-class output schemas loaded from configuration
   - citation provenance verification including rights and anchor resolution
   - artifact reference digest verification
   - deterministic unit, arithmetic, range and geometry checks
   - confidence recording with no approval semantics
   - PENDING_HUMAN_APPROVAL for safety-critical and P3 outputs
   - per-class validation result recording for the PHASE-14 gate
   - tests/gateway/validator-*.* covering cases a through l
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all twelve tests.
   - For case h, paste the expected-versus-asserted arithmetic comparison.
   - For case e, paste the rejection and the rights snapshot that caused it.
   - For case a, confirm from the SSE transcript that nothing was emitted
     before validation completed.
   - Acceptance criterion: no invalid, unprovenanced or arithmetically
     inconsistent output can reach a consumer, and no confidence value can
     bypass validation.

G. COMPLETION CONTRACT
   Definition of Done: mandatory validation with fail-closed semantics,
   provenance and rights enforced at the output boundary, deterministic checks
   catching arithmetic and unit errors, P3 held pending human approval.
   Evidence to report: the twelve test outputs, the arithmetic comparison, the
   rights rejection, the stream-ordering confirmation.
   Remaining blockers: the human approval path completes in PHASE-07; until
   then PENDING_HUMAN_APPROVAL is terminal. Confirm it is never auto-cleared.
   Next prompt: P05-01. PHASE-04 exit requires the chaos suite green, the
   budget loop-stop evidence retained, exactly-once ledger proven, and the
   no-provider-bypass guard green.
```

**المخرجات المتوقعة:** مُدقِّق إلزامي، تحقق مصدرية واستشهادات، فحوصات حتمية، حالة انتظار اعتماد بشري.
**التحقق المطلوب:** لا مخرج غير صالح أو بلا مصدرية يصل مستهلكاً؛ الثقة لا تتجاوز التحقق.
**الاعتمادية التالية:** `P05-01`.

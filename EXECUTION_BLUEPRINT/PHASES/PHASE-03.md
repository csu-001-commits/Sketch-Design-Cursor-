# PHASE-03 — محرك مسارات العمل والعقود

<!-- phasemeta
id: PHASE-03
depends_on: [PHASE-02]
criticality: P0
-->

## الغرض من المرحلة

`ADR-001` هو القرار الحاكم للمنتج كله: «المنتج هو Workflow Template محدد الإصدار
والمدخلات والمخرجات والمخاطر والتسعير والاختبارات. الوكلاء قدرات تنفذ خطوات داخل
القالب، وليسوا فريقاً حراً يؤلف مساراً جديداً لكل طلب» (الورقة 00 الصف 20،
والورقة 02 الصف 2).

هذا يعني أن محرك مسارات العمل يُبنى **قبل** الوكلاء وقبل بوابة الذكاء، لأنه هو من
يملك السلطة على ما يُنفَّذ ومتى. وهذه المرحلة تبني أيضاً الضمانات التي يستحيل
إضافتها لاحقاً: تثبيت الإصدار، والصمود أمام إعادة تشغيل العامل، وعدم تكرار الأثر
الجانبي.

## شروط الدخول

- اكتمال `PHASE-02`: مخرجات بإصدارات وبصمات، وبيان أدلة.

## شروط الخروج

- نجاح `AT-WF-001` (الفشل والإلغاء والانتهاء كحالات منفصلة بلا مهام معلقة).
- نجاح `AT-WF-002` (تثبيت الإصدار: التشغيل القديم يبقى على `v1.0`).
- إعادة تشغيل العامل لا تُفقد أي مهمة.
- تكرار `Idempotency-Key` لا يُنتج أثراً جانبياً مكرراً.
- صندوق الصادر يوصل مع إزالة تكرار؛ القوالب المسحوبة ومخططات غير الصالحة تُرفض.

## المتطلبات المغطاة في هذه المرحلة

`ADR-001`, `REQ-WF-01`..`REQ-WF-04`, `REQ-WF-07`, `REQ-WF-09`, `REQ-WF-10`,
`REQ-DAT-03`, `REQ-DAT-09`, `REQ-DAT-10`, `REQ-API-01`, `REQ-API-02`,
`REQ-API-04`, `REQ-API-05`

## تحذير مهم

الورقة 22 الصف 20 تقول عن LangGraph: «لا graph حر للإنتاج». واستخدام أي محرك
تنسيق (الورقة 22 الصف 19 توصي بـTemporal) مشروط بضوابطه المذكورة:
«Determinism/versioning/idempotency». أي تنفيذ يسمح للنموذج بتأليف خطوات جديدة
في وقت التشغيل يخالف `ADR-001` مباشرة.

---

## الأوامر التنفيذية

### P03-01 — سجل قوالب مسارات العمل وتثبيت الإصدار

<!-- meta
id: P03-01
phase: PHASE-03
title_en: Workflow template registry with immutable versions and routing
prereq: [P02-03]
requirements: [ADR-001, REQ-WF-02, REQ-WF-07, REQ-WF-10]
-->

**ماذا سينفذ هذا الأمر؟** يبني سجل قوالب غير قابل للتعديل بإصدارات دلالية، وراوتر
يختار قالباً معتمداً بالسياسة، ويرفض القوالب المسحوبة والمخططات غير الصالحة،
ويحوّل غياب التطابق إلى فرز بشري لا إلى مسار مُؤلَّف.

**لماذا نحتاجه؟** هذا هو `ADR-001` بالكود. والورقة 15 الصف 4 (`CTRL-003`) تطلب
دليلاً: «التشغيل يرجع إلى إصدار محدد بالضبط». والورقة 16 الصف 3 (`AT-WF-002`)
تحدد السيناريو: شغّل `v1.0` ثم انشر `v1.1`، فالقديم يبقى على `v1.0`.

**ما المتطلبات السابقة؟** `P02-03`.

**ما النتيجة المتوقعة؟** سجل قوالب مُحمَّل من `config/registries/workflow-templates.json`،
وراوتر بسياسة، ونجاح `AT-WF-002`.

**كيف نتحقق من نجاحه؟** نشر إصدار جديد أثناء تشغيل جارٍ لا يُغيّر إصدار ذلك
التشغيل؛ ومحاولة بدء قالب `retired` تُرفض.

```text
TASK P03-01 — Workflow template registry with immutable versions and routing

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-01
   Phase: PHASE-03 (Workflow runtime and contracts)
   Prerequisites: P02-03
   Requirements covered: ADR-001, REQ-WF-02, REQ-WF-07, REQ-WF-10

B. OBJECTIVE
   Implement the workflow template registry as immutable, semantically
   versioned, policy-gated definitions, plus a router that selects an approved
   template version and never composes a new path.

   Why this is necessary: this is ADR-001 expressed in code — the governing
   product decision of the whole platform (sheet 00 row 20, sheet 02 row 2).
   Sheet 15 row 4 (CTRL-003) requires the evidence "run references exact
   version". Sheet 16 row 3 (AT-WF-002) defines the test: start v1.0, publish
   v1.1, and the already-running instance stays on v1.0.

   SCOPE BOUNDARY: the registry, versioning, publication lifecycle and routing
   decision. Do not implement step execution, durability or the state machine —
   that is P03-02. Do not implement agents or model calls.

C. CONTEXT
   Required inputs:
     - config/registries/workflow-templates.json (sheet 07: 8 templates with
       workflow_id, version, segment, scope, capabilities, R, P, review
       requirement, pricing id, test suite id, evidence state)
     - the policy service from P01-04
   The eight templates and their source versions: WF-VILLA-REVIEW 1.0.0
   (PILOT TARGET), WF-BIM-COORD 0.9.0, WF-QTO 0.9.0, WF-SITE-REPORT 0.9.0,
   WF-MEP-REVIEW 0.8.0, WF-INFRA-REVIEW 0.8.0 (all DEFINED), WF-PAYMENT 1.0.0
   and WF-REVIEW-DELIVERY 1.0.0 (DESIGNED).
   Source constraint (sheet 05 row 3, CTL-02): the router selects by brief,
   policy and registry; no match yields manual triage; it halts on no template,
   a retired version, or an invalid schema.
   Source constraint (sheet 02 row 2) acceptance control: a template is valid
   only with owner, schema, tests, pricing and approval.

D. EXECUTION INSTRUCTIONS
   1. Model WorkflowTemplate and WorkflowTemplateVersion. Per
      config/registries/data-entities.json the keys are id, version and status,
      the purpose is an immutable versioned template, and the control is
      semantic versioning.
   2. Enforce the five-part validity gate from ADR-001's acceptance control. A
      version cannot reach status ACTIVE unless it has: a named owner, a valid
      input and output schema, a referenced test suite id, a referenced pricing
      id, and a recorded approval actor and timestamp. Reject publication
      otherwise, naming the missing part.
   3. Implement the version lifecycle: DRAFT -> ACTIVE -> DEPRECATED ->
      RETIRED. An ACTIVE or later version is immutable — editing it is
      impossible; a change produces a new semantic version. Enforce immutability
      with a database constraint or trigger, not application logic alone.
   4. Implement version pinning. Starting a run resolves the template version
      once, stores the exact resolved version on the run record, and every
      later step reads the pinned version. There is no code path that resolves
      "latest" after a run has started. Add a test that would fail if such a
      path existed.
   5. Implement the router:
        - input: a validated brief plus tenant policy;
        - output: either an exact template and version, or MANUAL_TRIAGE with a
          machine-readable reason;
        - it consults the policy service from P01-04 and records the policy
          bundle version in its decision;
        - it refuses to start a RETIRED version, refuses a brief failing the
          template's input schema, and refuses when no template matches;
        - it never synthesizes a capability list, a step order or a new
          template. Assert that the set of capabilities for a run is read from
          the pinned version and is not computed.
   6. Record a routing decision record for every routing attempt, including the
      rejected ones, with the reason. Sheet 05 row 3 tracks routing accuracy and
      misroutes as KPIs, which requires this record to exist.
   7. Load the eight templates from the registry file at startup, validating
      them against a schema. A registry file that fails validation prevents
      startup rather than degrading silently.
   8. Tests:
        a. AT-WF-002: start a run on v1.0.0; publish v1.1.0; assert the running
           instance still reports v1.0.0 and executes v1.0.0's capability list;
           assert a new run gets v1.1.0 according to the rollout policy;
        b. attempt to edit an ACTIVE version -> rejected at the database level;
        c. attempt to publish a version missing a test suite id -> rejected,
           naming the missing part; repeat for owner, schema, pricing and
           approval;
        d. attempt to start a RETIRED version -> rejected;
        e. submit a brief that matches no template -> MANUAL_TRIAGE with a
           reason, and no run created;
        f. submit a brief failing the input schema -> rejected with the
           validation detail;
        g. corrupt workflow-templates.json -> startup fails loudly.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - WorkflowTemplate and WorkflowTemplateVersion models and migrations
   - the five-part publication gate
   - the DRAFT/ACTIVE/DEPRECATED/RETIRED lifecycle with enforced immutability
   - version pinning on run creation
   - the policy-consulting router with MANUAL_TRIAGE output
   - routing decision records
   - startup-time registry validation
   - tests/workflow/at-wf-002.* plus cases b through g
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-WF-002 output showing the running instance pinned to v1.0.0 after
     v1.1.0 is published.
   - Paste the database-level rejection for case b.
   - Paste all five publication-gate rejections for case c.
   - Acceptance criterion: no code path resolves a template version after a run
     has started, and every routing attempt leaves a decision record.

G. COMPLETION CONTRACT
   Definition of Done: immutable versioned templates, enforced publication
   gate, proven version pinning, policy-gated routing with manual triage.
   Evidence to report: AT-WF-002 output, the seven test results, and the count
   of templates loaded versus the eight in the source.
   Remaining blockers: templates whose pricing id or test suite id does not yet
   exist — the source marks several DEFINED rather than built. Record them as
   publishable only in PHASE-15, and keep WF-VILLA-REVIEW as the PILOT TARGET.
   Next prompt: P03-02.
```

**المخرجات المتوقعة:** سجل قوالب غير قابل للتعديل، بوابة نشر خمسية، راوتر بسياسة.
**التحقق المطلوب:** `AT-WF-002` ناجح، ولا مسار كود يحلّ «الأحدث» بعد بدء التشغيل.
**الاعتمادية التالية:** `P03-02`.

---

### P03-02 — التنفيذ الصامد وآلة الحالات

<!-- meta
id: P03-02
phase: PHASE-03
title_en: Durable execution and the workflow state machine
prereq: [P03-01]
requirements: [REQ-WF-01, REQ-WF-03, REQ-WF-09, REQ-DAT-03]
-->

**ماذا سينفذ هذا الأمر؟** يبني محرك تنفيذ صامد وآلة الحالات الكاملة للورقة 09:
سبع عشرة حالة للمسار مع أحداثها وانتقالاتها وفاعليها وضوابطها.

**لماذا نحتاجه؟** الورقة 15 الصف 3 (`CTRL-002`) تجعل حالات الفشل والإلغاء
والانتهاء ضابطاً بأولوية `HIGH`، و`AT-WF-001` يطلب أن تكون «منفصلة ولا مهام
معلقة». الخلط بين `FAILED` و`CANCELLED` و`EXPIRED` يخفي الأعطال ويجعل مقياس
`Workflow failure rate` بلا معنى.

**ما المتطلبات السابقة؟** `P03-01`.

**ما النتيجة المتوقعة؟** محرك تنفيذ صامد، وآلة حالات مُنفَّذة كبيانات، ونجاح
`AT-WF-001`.

**كيف نتحقق من نجاحه؟** قتل العامل أثناء تشغيل لا يفقد مهمة؛ والانتقالات غير
المسموحة تُرفض؛ ولا تبقى مهمة معلقة بعد حالة نهائية.

```text
TASK P03-02 — Durable execution and the workflow state machine

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-02
   Phase: PHASE-03
   Prerequisites: P03-01 (pinned template versions)
   Requirements covered: REQ-WF-01, REQ-WF-03, REQ-WF-09, REQ-DAT-03

B. OBJECTIVE
   Implement durable workflow execution that survives worker restart with no
   lost work, and the full state machine the source specifies, with every
   terminal and exceptional state distinct.

   Why this is necessary: sheet 15 row 3 (CTRL-002) makes failure, cancel and
   expire states a HIGH control whose evidence is state tests plus event
   history. AT-WF-001 (sheet 16 row 2) requires that FAILED, CANCELLED and
   EXPIRED be separate with no dangling tasks. Collapsing them hides faults and
   makes the workflow failure rate KPI (sheet 30 row 7) meaningless. Sheet 37
   row 7 requires that restarting a worker mid-job loses nothing.

   SCOPE BOUNDARY: orchestration, state machine, tasks, timers and human
   waits. Idempotency and the outbox are P03-03. Agent and model execution are
   PHASE-04 and PHASE-05 — here a step is a typed, pluggable unit with a test
   double.

C. CONTEXT
   Required inputs:
     - sheet 09 rows 2-16 for the Workflow entity: states DRAFT, QUOTED,
       AWAITING_PAYMENT, PAYMENT_VERIFIED, QUEUED, RUNNING,
       AWAITING_INFORMATION, AWAITING_REVIEW, AWAITING_SECOND_REVIEW,
       AWAITING_CLIENT_DECISION, DELIVERED, ARCHIVED, plus the exceptional and
       terminal states FAILED, CANCELLED, EXPIRED, SUSPENDED and
       PARTIALLY_COMPLETED; each row names the event, the target state, the
       actor and the control
     - config/registries/data-constraints.json, workflow_runs: UNIQUE
       (tenant_id, idempotency_key), indexes project_id, status, created_at,
       invariant "state machine / retries"
     - sheet 05 row 4 (CTL-03): tasks, deadlines, dependencies, waits and
       retries under a state machine; halt when idempotency cannot be
       guaranteed or the retry budget is exceeded
   Tooling: sheet 22 row 19 recommends Temporal for durable execution, retries,
   timers, history and human waits, with the control
   "determinism/versioning/idempotency". Sheet 22 row 20 permits LangGraph for
   in-step human-in-the-loop barriers but states "no free graph for
   production". Choosing Temporal is source-supported; choosing otherwise
   requires an ADR and must still deliver durability, timers and replay.

D. EXECUTION INSTRUCTIONS
   1. Implement the state machine as data, derived from sheet 09, not as
      scattered conditionals. One transition table of
      (entity, from_state, event) -> (to_state, required_actor, guard). Load it
      from a registry file so the source and the code cannot drift.
   2. Enforce that an undeclared transition is impossible. Attempting one is an
      error with a reason code, never a silent no-op and never a fallthrough to
      a default state.
   3. Keep the exceptional states genuinely distinct, each with its own cause
      field:
        - FAILED carries an error class and the retry budget state;
        - CANCELLED carries the authorizing actor and a compensation record;
        - EXPIRED carries which timer fired and the reopen policy;
        - SUSPENDED carries the security, compliance, payment or COI reason and
          requires manual clearance to leave;
        - PARTIALLY_COMPLETED carries the explicit scope that succeeded and the
          scope that did not, per sheet 09 row 16.
   4. Implement durable orchestration:
        - run state and history are persisted, not held in memory;
        - a worker crash or restart resumes from persisted state;
        - every step is at-least-once with a declared side-effect class
          (SAFE_RETRYABLE, UNSAFE_RETRYABLE, IRREVERSIBLE) per sheet 36 row 10;
        - an IRREVERSIBLE step requires a manual gate and is never auto-retried.
   5. Implement tasks per config/registries/data-entities.json: task_id,
      run_id, assignee; a task is a human or machine step with a retry policy
      and a lease. A lease expiring returns the task to the queue rather than
      stranding it.
   6. Implement timers and human waits: quote expiry, payment expiry,
      assignment offer expiry and RFI waits, each producing the correct EXPIRED
      transition from sheet 09 row 14.
   7. Implement structured RFI: entering AWAITING_INFORMATION records what is
      missing, from whom, and the deadline — per sheet 09 row 7, the control is
      "structured RFI", not a free-text note.
   8. Guarantee no dangling tasks: reaching any terminal state cancels or closes
      every outstanding task and timer for that run. Add an invariant check that
      asserts zero open tasks and zero armed timers for a terminal run, and run
      it as part of the test suite.
   9. Implement retry budgets. Exceeding the budget transitions to FAILED with
      the budget state recorded; it never loops. Sheet 05 row 4 names exceeding
      retry as a stop condition.
  10. Tests — AT-WF-001 plus the state machine suite:
        a. force a parser step to fail -> FAILED, distinct, with error class,
           no open tasks, no armed timers;
        b. cancel a running run -> CANCELLED with authorizing actor and a
           compensation record, no open tasks;
        c. let an assignment offer expire -> EXPIRED naming the timer, no open
           tasks;
        d. assert the three outcomes above are distinguishable in both the run
           record and the event history;
        e. kill the worker process mid-run, restart it, assert the run resumes
           and completes with no duplicated step and no lost step;
        f. attempt an undeclared transition -> rejected with a reason code;
        g. suspend a run -> SUSPENDED, and assert it cannot leave that state
           without a recorded manual clearance;
        h. exceed the retry budget -> FAILED with budget state, no infinite
           loop;
        i. assert the terminal-state invariant (zero open tasks, zero armed
           timers) for every terminal state.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the data-driven transition table plus its registry file
   - durable run and task persistence with resume-after-restart
   - distinct exceptional states with their cause fields
   - tasks with leases, timers, human waits and structured RFI
   - side-effect classes with IRREVERSIBLE gating
   - retry budgets
   - the terminal-state invariant check
   - tests/workflow/at-wf-001.* plus cases e through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-WF-001 output showing FAILED, CANCELLED and EXPIRED as distinct
     outcomes with no dangling tasks.
   - Paste the worker-kill test output showing the run resuming and completing,
     with step execution counts proving no duplication and no loss.
   - Paste the undeclared-transition rejection.
   - State the count of transitions in sheet 09 versus the count in your
     transition table. They must match.
   - Acceptance criterion: AT-WF-001 green; restart loses nothing; no terminal
     run holds an open task or an armed timer.

G. COMPLETION CONTRACT
   Definition of Done: durable execution proven by worker kill, full state
   machine enforced from data, exceptional states distinct, no dangling work.
   Evidence to report: AT-WF-001 output, the restart test output, the
   transition count comparison, the invariant check output.
   Remaining blockers: any state in sheet 09 whose triggering event belongs to
   a later phase (payment, review, delivery) — implement the transition and
   drive it with a test double now, and name the phase that wires the real
   producer.
   Next prompt: P03-03.
```

**المخرجات المتوقعة:** جدول انتقالات مُحمَّل من بيانات، تنفيذ صامد، حالات استثنائية مميّزة.
**التحقق المطلوب:** `AT-WF-001` ناجح؛ قتل العامل لا يفقد ولا يكرر؛ ثابت الحالة النهائية مُتحقَّق.
**الاعتمادية التالية:** `P03-03`.

---

### P03-03 — عدم التكرار وصندوق الصادر وعقود الأحداث

<!-- meta
id: P03-03
phase: PHASE-03
title_en: Idempotency, transactional outbox and event contracts
prereq: [P03-02]
requirements: [REQ-WF-04, REQ-DAT-09, REQ-DAT-10, REQ-API-04, REQ-API-05]
-->

**ماذا سينفذ هذا الأمر؟** يبني مفاتيح عدم التكرار، وصندوق صادر معاملاتي، وطابور
رسائل ميتة، ومغلف الأحداث الموحد للورقة 34 بأحداثه الثمانية.

**لماذا نحتاجه؟** الورقة 38 الصف 9 (`G-04 Side-effect safety`) ضابط حاجز للإصدار:
«لا شحن مكرر ولا إرسال مكرر»، ودليله «DB constraint + replay test». والورقة 37
الصف 8 تجعلها متطلباً مُتتبَّعاً. وبدون صندوق صادر معاملاتي لا يمكن تحقيق
«at-least-once» المذكورة في كل صفوف الورقة 34.

**ما المتطلبات السابقة؟** `P03-02`.

**ما النتيجة المتوقعة؟** عدم تكرار مفروض بقيد قاعدة بيانات، وصندوق صادر مع إعادة
محاولة وDLQ، وأحداث مطابقة للمغلف.

**كيف نتحقق من نجاحه؟** إعادة إرسال نفس المفتاح لا تُنتج أثراً ثانياً؛ وإعادة
تشغيل الأحداث خارج الترتيب ومكررة لا تُنتج حالة خاطئة.

```text
TASK P03-03 — Idempotency, transactional outbox and event contracts

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-03
   Phase: PHASE-03
   Prerequisites: P03-02 (durable runs and tasks)
   Requirements covered: REQ-WF-04, REQ-DAT-09, REQ-DAT-10, REQ-API-04,
                         REQ-API-05

B. OBJECTIVE
   Make side effects exactly-once observable: database-enforced idempotency
   keys, a transactional outbox with retry and dead-letter handling, and the
   source's common event envelope with its eight versioned domain events.

   Why this is necessary: sheet 38 row 9 (G-04) is a release blocker whose pass
   criterion is "no duplicate charges or dispatch" and whose required evidence
   is "DB constraint plus replay test". Sheet 37 row 8 tracks it as a
   requirement. Every event row in sheet 34 specifies at-least-once delivery,
   which is only honest if an outbox and consumer-side dedupe exist.

   SCOPE BOUNDARY: idempotency, the outbox, delivery semantics and event
   schemas. Payment-specific webhook verification is PHASE-08 and builds on
   this. Do not implement business handlers beyond what the tests need.

C. CONTEXT
   Required inputs:
     - config/registries/data-constraints.json: idempotency_keys with
       tenant_id, key, request_hash, response_ref; UNIQUE (tenant_id, key);
       index expires_at; invariant "conflict on hash mismatch"; retention
       "TTL by operation". outbox_events with event_id, tenant_id,
       aggregate_id, payload, status; UNIQUE event_id; index status,
       next_attempt_at; invariant "transactional outbox"
     - sheet 34 row 3: the common envelope — eventId UUID, eventType,
       schemaVersion, tenantId, correlationId, causationId, occurredAt UTC,
       payload
     - sheet 34 rows 6-13: EV-01 ProjectCreated project.created.v1; EV-02
       EvidenceSubmitted evidence.submitted.v1; EV-03 WorkflowRequested
       workflow.requested.v1; EV-04 AgentStepCompleted
       agent.step.completed.v1; EV-05 ReviewDecisionRecorded review.decision.v1;
       EV-06 EstimateIssued estimate.issued.v1; EV-07 DeliverableReleased
       deliverable.released.v1; EV-08 UsageRecorded usage.recorded.v1 — each
       with aggregate, required payload fields, producer, consumer, ordering
       key, delivery and a validation rule
     - the minimal outbox stub from P02-03, which this prompt generalizes

D. EXECUTION INSTRUCTIONS
   1. Implement idempotency as a request-level mechanism:
        - operations that sheet 26 and sheet 33 mark as requiring an
          Idempotency-Key reject the request with 400 when it is absent;
        - the first request records (tenant_id, key, request_hash,
          response_ref) in the same transaction as its effect;
        - a replay with the same key and the same request hash returns the
          stored response, and performs no new effect;
        - a replay with the same key but a different request hash returns 409
          and performs no effect — this is the "conflict on hash mismatch"
          invariant;
        - keys expire by a per-operation TTL, and expiry is a documented
          behaviour change, not a silent window.
   2. Implement the transactional outbox:
        - the domain change and the outbox row are written in one transaction,
          so an event cannot exist without its effect and vice versa;
        - a separate dispatcher reads PENDING rows ordered by
          next_attempt_at, publishes, and marks them SENT;
        - failures use bounded exponential backoff with jitter and a maximum
          attempt count, then move to the dead-letter queue with the full
          failure history;
        - the dispatcher is safe to run in multiple instances: use row-level
          locking or equivalent so one event is dispatched once.
   3. Implement the envelope exactly as sheet 34 row 3 specifies, as a schema
      file that every producer validates against before the outbox write. A
      non-conforming event fails at write time, not at consume time.
   4. Implement the eight events of sheet 34 as versioned schemas with their
      required payload fields and their declared ordering keys. Ordering is
      guaranteed per ordering key, not globally — implement and document it that
      way rather than implying total ordering you cannot provide.
   5. Implement consumer-side dedupe by eventId, because delivery is
      at-least-once. Provide one shared, tested dedupe helper so every consumer
      is protected identically.
   6. Implement the dead-letter queue with: a reason, the attempt history, the
      original envelope, a tenant scope, and an operator replay path that is
      itself idempotent and audited.
   7. Tests — the replay suite:
        a. repeat a create request with the same key and body -> one entity,
           identical response, no second event;
        b. repeat with the same key and a changed body -> 409, no effect;
        c. omit a required Idempotency-Key -> 400;
        d. crash the process between the domain write and the dispatch ->
           restart and assert the event is still delivered exactly once;
        e. deliver the same event twice to a consumer -> the effect applies
           once;
        f. deliver two events for one ordering key out of order -> assert the
           consumer reaches the correct final state, and that an older event
           cannot overwrite a newer state;
        g. exhaust retries -> the event lands in the DLQ with its history, and
           no partial effect remains;
        h. replay from the DLQ -> idempotent, audited, no duplicate effect;
        i. emit an event missing a required envelope field -> rejected at write
           time;
        j. run two dispatcher instances concurrently -> assert each event is
           published exactly once.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - idempotency_keys table, middleware and 409-on-hash-mismatch semantics
   - the transactional outbox with a concurrency-safe dispatcher
   - the envelope schema file plus the eight event schemas
   - the shared consumer dedupe helper
   - the DLQ with an idempotent, audited replay path
   - tests/events/replay-suite.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the replay suite output for all ten cases.
   - For case a, show the database constraint doing the work: paste the unique
     violation that your handler converts into the stored response.
   - For case d, show the crash point and the post-restart delivery count.
   - For case j, paste the per-event publish counts from the concurrent run.
   - Acceptance criterion: no duplicate effect in any of the ten cases, and the
     guarantee rests on a database constraint rather than on application timing.

G. COMPLETION CONTRACT
   Definition of Done: idempotency enforced by constraint, outbox delivering
   exactly-once-observably, all eight event schemas conforming to the envelope,
   DLQ working with audited replay.
   Evidence to report: the ten test outputs, the constraint violation proof,
   the concurrent dispatcher counts.
   Remaining blockers: events whose producer belongs to a later phase (EV-04
   from the gateway, EV-05 from review, EV-06 from costing, EV-07 from
   delivery, EV-08 from usage) — define the schema and test it with a producer
   double now, and name the phase that wires the real producer.
   Next prompt: P03-04.
```

**المخرجات المتوقعة:** مفاتيح عدم تكرار، صندوق صادر، مغلف وثمانية أحداث، DLQ.
**التحقق المطلوب:** عشر حالات إعادة تشغيل بلا أثر مكرر، والضمان من قيد قاعدة بيانات.
**الاعتمادية التالية:** `P03-04`.

---

### P03-04 — سطح الـAPI للمنتج وعقوده

<!-- meta
id: P03-04
phase: PHASE-03
title_en: Product API surface and contract tests
prereq: [P03-03]
requirements: [REQ-API-01, REQ-API-02, REQ-API-03, REQ-WF-01]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ سطح الـAPI للمنتج: تسع عشرة عملية في الورقة 26،
وعشرة عقود مُسمّاة في الورقة 33، مع اختبارات عقود حقيقية.

**لماذا نحتاجه؟** الورقة 38 الصف 6 (`G-01 API security`) حاجز إصدار بمعيار نجاح
«صفر تسريب بين المستأجرين»، والورقة 40 الصف 8 تقول صراحة إن عقود الـAPI
«موثقة» لكن حالتها `UNVERIFIED` وتحتاج «runtime contract tests». هذا الأمر يحوّل
الوثيقة إلى عقد مُختبَر.

**ما المتطلبات السابقة؟** `P03-03`.

**ما النتيجة المتوقعة؟** مواصفة OpenAPI مُولَّدة أو مُؤلَّفة، ونقاط نهاية مُنفَّذة،
واختبارات عقود تتحقق من رموز الحالة والنطاقات والأحداث.

**كيف نتحقق من نجاحه؟** لكل عملية اختبار يتحقق من: النطاق المطلوب، رموز الحالة
المذكورة، الحدث المُصدَر، وسلوك عدم التكرار.

```text
TASK P03-04 — Product API surface and contract tests

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-04
   Phase: PHASE-03
   Prerequisites: P03-03 (idempotency and events)
   Requirements covered: REQ-API-01, REQ-API-02, REQ-API-03, REQ-WF-01

B. OBJECTIVE
   Implement the product API surface the source specifies and prove it with
   runtime contract tests covering scope, status codes, emitted events and
   idempotency behaviour.

   Why this is necessary: sheet 38 row 6 (G-01) is a release blocker whose pass
   criterion is zero cross-tenant leaks, with required evidence of a CI report
   and a penetration test. Sheet 40 row 8 states plainly that API contracts are
   "Documented" but their verdict is UNVERIFIED and runtime contract tests are
   required. This prompt converts documentation into a tested contract.

   SCOPE BOUNDARY: the operations listed below, their authorization, their
   status codes, their events and their idempotency. Business logic that belongs
   to a later phase is implemented as a validated, authorized endpoint whose
   handler delegates to a clearly marked not-yet-implemented boundary that
   returns 501 — never a fake success.

C. CONTEXT
   Required inputs:
     - sheet 26 rows 2-20, nineteen operations with purpose, scope,
       idempotency or concurrency control, event and response codes:
       POST /v1/projects (projects:write, Idempotency-Key, project.created,
       201/400/403/409); POST /v1/requests (requests:write, request.created,
       201/422); POST /v1/uploads/init (files:write,
       file.uploaded|quarantined, 201/413/415); POST /v1/quotes (quotes:write,
       quote.created, 201/422); POST /v1/quotes/{id}/accept (quotes:accept,
       version/etag, quote.accepted, 200/409/410); POST
       /v1/payments/sessions (payments:write, Idempotency-Key,
       payment.initiated, 201/422); POST /v1/webhooks/payments/{provider}
       (provider signature, payment.*, 200/400/401); POST /v1/workflow-runs
       (runs:write, Idempotency-Key, workflow.queued, 202/409/422); GET
       /v1/workflow-runs/{id} (runs:read, ETag, 200/403/404); POST
       /v1/workflow-runs/{id}/cancel (runs:cancel, workflow.cancelled,
       202/409); POST /v1/workflow-runs/{id}/retry (runs:retry,
       task.retry_scheduled, 202/409); POST /v1/workflow-runs/{id}/resume
       (runs:resume, workflow.resumed, 202/409); GET /v1/findings
       (findings:read, cursor, 200); POST /v1/reviews/{id}/decisions
       (reviews:decide, review hash/etag, review.decision_recorded,
       200/409/422); POST /v1/reviews/{id}/return (reviews:decide,
       review.returned, 202); POST /v1/deliveries/{id}/lock (deliveries:lock,
       delivery.locked, 200/409); POST /v1/deliveries/{id}/sign
       (deliveries:sign, delivery.signed, 202/409); POST
       /v1/deliveries/{id}/release (deliveries:release, delivery.released,
       202/409); GET /v1/verify/{token} (public token, rate limit,
       verification.viewed, 200/404/410)
     - sheet 33 rows 6-15, the ten named contracts API-01..API-10 with request
       and response schema names, scopes, retry semantics, status codes, events
       and security invariants
   Cross-cutting invariant from sheet 33 row 7: never reveal cross-tenant
   existence. Reuse the uniform authorization helper from P01-02.

D. EXECUTION INSTRUCTIONS
   1. Author an OpenAPI document covering every operation above, with named
      request and response schemas matching sheet 33's names
      (CreateProjectRequest, ProjectResponse, EvidenceManifestRequest,
      EvidenceReceipt, StartWorkflowRequest, WorkflowRun, ReviewDecisionRequest,
      ReviewDecision, EstimateRequest, EstimateResponse, DeliverableManifest,
      UsageQuery, UsagePage, WebhookSubscriptionRequest, Subscription).
   2. Implement request validation from the schema, returning 422 with a
      machine-readable field-level detail. Validation happens before
      authorization side effects and before any state change.
   3. Enforce scopes exactly as listed. A token lacking the scope gets 403; a
      token for another tenant gets the uniform not-found/forbidden response
      from P01-02.
   4. Implement concurrency control where the source specifies it: ETag on GET
      /v1/workflow-runs/{id}; version or etag on quote accept; review hash or
      etag on review decisions; artifact version on delivery lock. A stale
      precondition returns 409; a gone resource returns 410 where the source
      lists it.
   5. Implement cursor pagination on GET /v1/findings and GET /v1/usage, with
      an opaque, tamper-resistant cursor that encodes the tenant scope so a
      cursor cannot be replayed across tenants.
   6. Rate-limit GET /v1/verify/{token} per the source's control, and keep the
      verification response minimal: digest and status only. It is a public
      surface, so it must not leak project, client or reviewer identity.
   7. Emit the specified event for each operation through the outbox from
      P03-03, never directly.
   8. For operations whose domain logic belongs to a later phase, return 501
      from a single clearly named boundary function with the owning phase in
      the response detail. Record the list. A stubbed endpoint must never return
      200 with invented data — that is the fabrication this project's
      governance model exists to prevent.
   9. Write the contract test suite. For every operation assert: the success
      path and code; every documented error code is reachable by a real
      condition; missing scope gives 403; cross-tenant gives the uniform
      response with no leakage; the documented event is emitted exactly once;
      idempotency behaves per P03-03 where a key is required; the response
      validates against the OpenAPI schema.
  10. Add a contract-drift test asserting every route in the application
      appears in the OpenAPI document and vice versa, so the document cannot
      rot.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the OpenAPI document with sheet 33's schema names
   - the nineteen implemented operations with scopes, codes and events
   - ETag and precondition handling, cursor pagination, verify rate limiting
   - the single 501 boundary with its documented inventory
   - tests/contract/*.* covering every operation
   - the contract-drift test
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the contract suite output with the per-operation pass list.
   - State the operation count: nineteen from sheet 26 plus the ten named
     contracts from sheet 33, and how your implementation maps to both (several
     overlap — show the mapping explicitly rather than double-counting).
   - Paste a cross-tenant attempt for three different operations showing
     identical response shapes.
   - List every endpoint currently returning 501 with its owning phase.
   - Acceptance criterion: every documented status code is reachable by a real
     test, no endpoint returns fabricated success data, and the drift test
     passes.

G. COMPLETION CONTRACT
   Definition of Done: the API surface implemented and contract-tested, drift
   test green, stubs honestly returning 501.
   Evidence to report: contract suite output, the sheet 26 to sheet 33 mapping
   table, the cross-tenant uniformity proof, the 501 inventory.
   Remaining blockers: the 501 list is the expected blocker set. Each entry
   must name the phase that completes it.
   Next prompt: P03-05.
```

**المخرجات المتوقعة:** مواصفة OpenAPI، تسع عشرة عملية، اختبارات عقود، اختبار انحراف.
**التحقق المطلوب:** كل رمز حالة موثق قابل للوصول باختبار حقيقي؛ لا نقطة نهاية ترجع نجاحاً مُلفَّقاً.
**الاعتمادية التالية:** `P03-05`.

---

### P03-05 — خدمة SLA والمؤقتات والتصعيد

<!-- meta
id: P03-05
phase: PHASE-03
title_en: SLA service, timers and escalation
prereq: [P03-04]
requirements: [REQ-WF-09, REQ-WF-01, REQ-OBS-05]
-->

**ماذا سينفذ هذا الأمر؟** يبني خدمة SLA: مواعيد لكل خطوة، تذكيرات، تصعيد، وتسجيل
زمن دقيق لقياس «Time to signed delivery».

**لماذا نحتاجه؟** الورقة 05 الصف 4 تحدد مخرجات `CTL-03` بأنها
«tasks/timers/escalations»، ومؤشراتها «SLA؛ stuck runs؛ recovery». والورقة 17
الصف 9 تعرّف مقياساً زمنياً محدداً: من `payment verified` إلى `release`. بدون
مؤقتات وأحداث زمنية موثوقة لا يمكن قياس هذا ولا اكتشاف التشغيل المتوقف.

**ما المتطلبات السابقة؟** `P03-04`.

**ما النتيجة المتوقعة؟** مؤقتات صامدة، تصعيد مُسجَّل، وكشف للتشغيل المتوقف.

**كيف نتحقق من نجاحه؟** تشغيل بلا نبض يُكتشف ويُصعَّد؛ والمقياس الزمني يُحسب من
أحداث حقيقية لا من حقول مُحدَّثة يدوياً.

```text
TASK P03-05 — SLA service, timers and escalation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-05
   Phase: PHASE-03
   Prerequisites: P03-04
   Requirements covered: REQ-WF-09, REQ-WF-01, REQ-OBS-05

B. OBJECTIVE
   Implement durable SLA timers, reminders, escalation and stuck-run detection,
   and derive the source's time metrics from real event history rather than from
   hand-maintained fields.

   Why this is necessary: sheet 05 row 4 defines CTL-03's outputs as tasks,
   timers and escalations with KPIs for SLA, stuck runs and recovery. Sheet 17
   row 9 defines "time to signed delivery" precisely as payment verified to
   release. Sheet 61 row 3 defines the stuck-workflow support scenario with
   detection by missing heartbeat. None of these are measurable without durable
   timers and a trustworthy event history.

   SCOPE BOUNDARY: timers, deadlines, reminders, escalation routing and
   stuck-run detection, plus the metric derivation query. Dashboards and alert
   delivery are PHASE-10. Do not build notification channels beyond an
   abstracted dispatch interface with a test double.

C. CONTEXT
   Required inputs:
     - the durable runtime from P03-02 and the outbox from P03-03
     - sheet 09 row 14: TIME_BOUND entities expire on timer.expired with a
       reopen policy — quote, payment and assignment expiry
     - sheet 13 row 10: SLA handling is reminder, then expiry, then
       reassignment, and must never bypass a hard filter
     - sheet 17 rows 8-9: workflow failure segmented by step, tool and tenant
       (daily, SRE, SLO); time to signed delivery segmented by service and
       complexity
     - sheet 61 row 3: workflow stuck, trigger "no heartbeat", first response
       "inspect task and lease", safe action "pause or requeue idempotently"

D. EXECUTION INSTRUCTIONS
   1. Implement deadlines as first-class durable records: subject reference,
      deadline in UTC, purpose, reminder schedule, escalation target and
      current state. They survive restart because they live in the datastore,
      not in an in-process scheduler.
   2. Implement the reminder-then-expiry ladder of sheet 13 row 10: configurable
      reminders before the deadline, then the EXPIRED transition, then the
      reassignment or reopen action the source specifies for that subject.
      Expiry must never relax a hard filter — assert that in a test.
   3. Implement escalation routing: on breach, route to the role the source
      names for that subject (for example Review Ops for an assignment offer,
      Finance for a payment exception, PM for a scope change), record the
      escalation, and emit an event. Escalation is recorded even when nobody
      acts, so the record cannot be lost.
   4. Implement heartbeat and lease monitoring: a running task renews a lease;
      a missing heartbeat beyond a threshold marks the run STUCK_SUSPECTED,
      records the task and lease state for the operator per sheet 61 row 3, and
      offers the idempotent pause-or-requeue action. Detection does not itself
      mutate the run beyond the suspicion marker.
   5. Derive metrics from event history, not from mutable columns:
        - time to signed delivery as the interval between the
          payment-verified event and the delivery-released event for a run;
        - workflow failure rate segmented by step, tool and tenant;
        - stuck-run count and recovery time.
      Implement them as queries over the event store so a value can always be
      recomputed and audited. Do not maintain a denormalized metric column that
      can silently diverge.
   6. Make the metric outputs explicitly unthresholded. Sheet 30 row 14 forbids
      populating current values from anything but documented operational
      sources, and sheet 30 rows 3-9 mark these targets TBD. Your API returns
      the measured value and the literal state PENDING for the target, never a
      placeholder target that would make a dashboard look green.
   7. Tests:
        a. a deadline fires after restart of the process -> timer durability
           proven;
        b. the reminder ladder fires in order, then expiry, then the configured
           reopen or reassignment action;
        c. an expiry cannot bypass a hard filter -> reassignment still applies
           every filter;
        d. a breach produces an escalation record and event even with no
           handler subscribed;
        e. a task stops heartbeating -> STUCK_SUSPECTED with task and lease
           state captured; the requeue action is idempotent when applied twice;
        f. time to signed delivery computed from a synthetic event history
           matches a hand-calculated expected value;
        g. a metric with a TBD target returns PENDING, never a number.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - durable deadline and reminder records with escalation routing
   - heartbeat and lease monitoring with stuck-run detection
   - event-derived metric queries for the source's time and failure metrics
   - the PENDING-target semantics for unthresholded KPIs
   - an abstracted notification dispatch interface with a test double
   - tests/sla/*.* covering cases a through g
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all seven tests.
   - For case a, show the process restart and the timer still firing.
   - For case f, show the synthetic history, your computed value and the
     hand-calculated expectation side by side.
   - For case g, paste the API response showing PENDING rather than a number.
   - Acceptance criterion: timers survive restart, escalations are never lost,
     and no metric reports a target the source has not set.

G. COMPLETION CONTRACT
   Definition of Done: durable timers, working escalation, stuck-run detection,
   event-derived metrics with honest PENDING targets.
   Evidence to report: the seven test outputs, the restart proof, the metric
   calculation comparison.
   Remaining blockers: KPI targets remain owner-owned (open decision OD-04).
   Report that the measurement path is ready and the thresholds are not set.
   Next prompt: P04-01. PHASE-03 exit requires AT-WF-001 and AT-WF-002 green,
   the replay suite green, and the contract-drift test green.
```

**المخرجات المتوقعة:** مؤقتات صامدة، تصعيد مُسجَّل، مقاييس مشتقة من الأحداث.
**التحقق المطلوب:** المؤقتات تصمد لإعادة التشغيل؛ لا مقياس يُظهر هدفاً لم يحدده المصدر.
**الاعتمادية التالية:** `P04-01`.

# PHASE-05 — تشغيل الوكلاء والسجل والإصدارات

<!-- phasemeta
id: PHASE-05
depends_on: [PHASE-04]
criticality: P0
-->

## الغرض من المرحلة

المصدر يحسم طبيعة الوكلاء في الورقة 00 الصف 20: «الوكلاء قدرات تنفذ خطوات داخل
القالب، وليسوا فريقاً حراً يؤلف مساراً جديداً لكل طلب». وفي الورقة 57 الصف 4
ملاحظة حرجة: «قدرات السجل ليست مكافئة لإصدارات وكلاء قابلة للنشر» — أي أن وجود
44 قدرة في جدول لا يعني وجود 44 وكيلاً جاهزاً.

لذلك هذه المرحلة تبني عقد التشغيل العشاري في الورقة 36، ودورة حياة الإصدارات في
الورقة 62، وحدود الأدوات ودفاعات الحقن.

## شروط الدخول

- اكتمال `PHASE-04`: البوابة تفرض السياسة والتوجيه والميزانية والتحقق.

## شروط الخروج

- أداة غير مُسجَّلة تُحجَب عند الإرسال.
- مغلف نتيجة مُشوَّه يفشل مُغلقاً.
- إصدارات وكلاء غير قابلة للتعديل مع canary ورجوع مُثبت.
- اختبار عزل حزمة السياق ناجح.

## المتطلبات المغطاة في هذه المرحلة

`ADR-005`, `REQ-AGT-01`..`REQ-AGT-08`, `REQ-SEC-05`, `REQ-DAT-04`, `REQ-API-05`

## تحذير مهم

الورقة 62 الصف 2 تقول صراحة: «لا أدوات عشوائية ديناميكية» (No dynamic arbitrary
tools). وأي قدرة في الورقة 05 لها عمود «شروط الإيقاف» — وهذه الشروط ليست
توصيات، بل هي نقاط توقف إلزامية.

---

## الأوامر التنفيذية

### P05-01 — عقد تشغيل الوكيل بمجالاته العشرة

<!-- meta
id: P05-01
phase: PHASE-05
title_en: Agent runtime contract RT-01..RT-10
prereq: [P04-07]
requirements: [REQ-AGT-01, REQ-AGT-02, REQ-AGT-04, REQ-AGT-05, REQ-DAT-04]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ عقد تشغيل الوكلاء في الورقة 36: هوية التنفيذ،
تعريف الوكيل، حزمة السياق، توجيه النموذج، ضوابط التنفيذ، مغلف النتيجة، الأدلة
والتدقيق، دفتر الاستخدام، تصعيد HITL، وتصنيف الفشل — كل مجال بثابته وبإجراء فشله.

**لماذا نحتاجه؟** الورقة 36 الصف 3 تصف نفسها بأنها «مواصفة تصميم لا مُتحقَّقاً
منها في التشغيل»، وتشترط أن «كل تنفيذ يجب أن يكون قابلاً للإسناد والإعادة
ومحدوداً بالسياسة». هذه الثلاثة تحتاج بنية لا نوايا.

**ما المتطلبات السابقة؟** `P04-07`.

**ما النتيجة المتوقعة؟** عقد تنفيذ مُنفَّذ بعشرة مجالات، كل منها بثابت مفروض
واختبار لإجراء الفشل.

**كيف نتحقق من نجاحه؟** لكل صف من `RT-01` إلى `RT-10` اختبار يُفعّل إجراء الفشل
المذكور في المصدر.

```text
TASK P05-01 — Agent runtime contract RT-01..RT-10

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-01
   Phase: PHASE-05 (Agent runtime, registry and versioning)
   Prerequisites: P04-07
   Requirements covered: REQ-AGT-01, REQ-AGT-02, REQ-AGT-04, REQ-AGT-05,
                         REQ-DAT-04

B. OBJECTIVE
   Implement the ten agent runtime contract areas with their fields,
   invariants and failure actions exactly as the source specifies, so every
   execution is attributable, reproducible and policy-constrained.

   Why this is necessary: sheet 36 row 3 states the contract's purpose in those
   three words and declares itself a design specification that is not
   runtime-verified. This prompt is what makes it verified. Each row names a
   failure action, and a failure action that is not implemented is not a
   contract.

   SCOPE BOUNDARY: the execution contract and its enforcement. The agent
   catalogue and versioning lifecycle are P05-02. Tool safety hardening is
   P05-03. The individual 44 capabilities are not implemented here — PHASE-09
   and PHASE-15 implement them behind this contract.

C. CONTEXT
   Required inputs, sheet 36 rows 6-15, each as area / fields / invariant /
   failure action:
     RT-01 Execution identity — executionId, tenantId, projectId,
       workflowRunId, stepId / required UUIDs, tenant-scoped / reject before
       dispatch
     RT-02 Agent definition — agentId, registryVersion, capabilities,
       toolAllowlist / pinned immutable version / block unregistered tools
     RT-03 Context package — projectSnapshot, evidenceRefs, knowledgeRefs,
       policyVersion / least privilege, signed refs / never mix projects or
       tenants
     RT-04 Model routing — capability, classification, budget, maxLatency,
       fallbackChain / no model bypass of policy / escalate on uncertainty
     RT-05 Execution controls — timeout, retryPolicy, idempotencyKey,
       sideEffectClass / retry only safe operations / manual gate for
       irreversible effects
     RT-06 Result envelope — status, structuredOutput, artifactRefs, citations,
       confidence / JSON schema validated / fail closed on invalid output
     RT-07 Evidence and audit — traceId, promptVersion, toolCalls,
       reviewDecision / redact secrets, immutable trace / audit every action
     RT-08 Usage ledger — inputTokens, outputTokens, cost, provider,
       executionId / persist exactly once per execution / reconcile with
       credits
     RT-09 HITL escalation — reason, reviewerRole, deadline, decision /
       qualified reviewer, explicit decision / no self-approval
     RT-10 Failure taxonomy — errorCode, retryable, providerFailure,
       partialArtifacts / circuit breaker plus dead-letter queue / no silent
       success
   Also required: config/registries/data-constraints.json, agent_executions:
   UNIQUE (run_id, step_id, attempt); invariant "trace/model lineage";
   retention "redact prompts".
   Already built and to be reused, not reimplemented: the validator (P04-07)
   satisfies RT-06; the ledger (P04-06) satisfies RT-08; the circuit breaker
   (P04-04) is half of RT-10; the policy service (P01-04) backs RT-04.

D. EXECUTION INSTRUCTIONS
   1. Implement the execution identity record with all five RT-01 fields as
      required, tenant-scoped UUIDs. A dispatch missing any of them is rejected
      before anything runs — not logged and continued.
   2. Implement agent_executions per the data constraint, with UNIQUE
      (run_id, step_id, attempt) so attempts are distinguishable and
      countable, and with prompt redaction at rest per the retention rule.
   3. Implement the context package builder (RT-03) on top of P04-05, adding:
        - least privilege: the package contains only what the step's declared
          inputs require, and the builder refuses a request for a broader
          scope;
        - signed references: evidenceRefs and knowledgeRefs are
          integrity-checked at use time;
        - the hard invariant "never mix projects or tenants": the package is
          constructed for exactly one (tenant, project) pair and a second pair
          cannot be added. Enforce structurally and test it.
   4. Implement RT-04's invariant: a step cannot select a model outside the
      policy decision. There is no parameter by which a caller can name a model
      directly and bypass P04-03. Add a test asserting a caller-supplied model
      id is ignored or rejected. "Escalate on uncertainty" means that when the
      router returns NO_ELIGIBLE_ROUTE the step escalates to HITL rather than
      proceeding.
   5. Implement RT-05's side-effect classes and gating, reusing P03-02's
      classes. An IRREVERSIBLE step requires a recorded manual gate before
      execution and is never retried automatically.
   6. Implement RT-07: a trace id links the whole execution; promptVersion and
      every tool call are recorded; the trace is immutable and secret-redacted;
      every action produces an audit record in the P01-05 store.
   7. Implement RT-09 HITL escalation with its four fields and its two
      invariants: the escalation names a qualified reviewer role and requires
      an explicit decision, and self-approval is impossible — the actor who
      produced the output cannot be the actor who approves it. Enforce the
      self-approval prohibition here as well as in PHASE-07, because the
      runtime must not be able to request it.
   8. Implement RT-10's taxonomy completely, with the explicit rule "no silent
      success": an execution that produced partial artifacts and then failed
      reports FAILED with the partial artifacts referenced, never a success
      status with missing output. Add the dead-letter path for executions that
      cannot be completed.
   9. Implement reproducibility: given the same execution identity, agent
      version, context package digest, policy version and model version, the
      execution is replayable and its inputs are reconstructable from the
      trace. Provide a replay command that reconstructs and re-runs an
      execution for debugging, clearly marked as producing a new execution id.
  10. Tests — one per contract area, driving the source's failure action:
        a. RT-01: dispatch missing projectId -> rejected before dispatch, no
           provider call;
        b. RT-02: a step requesting a tool outside the allowlist -> blocked;
        c. RT-03: attempt to add a second project's evidence to a package ->
           impossible or rejected; attempt a broader scope than declared ->
           refused;
        d. RT-04: caller supplies a model id -> ignored or rejected;
           NO_ELIGIBLE_ROUTE -> escalates to HITL, does not proceed;
        e. RT-05: an IRREVERSIBLE step without a manual gate -> does not run;
           it is never auto-retried;
        f. RT-06: invalid envelope -> fails closed (reuse the P04-07 suite);
        g. RT-07: a forced failure -> the trace exists, contains no secret, and
           cannot be mutated;
        h. RT-08: exactly-once ledger (reuse the P04-06 suite);
        i. RT-09: the producing actor attempts to approve -> refused;
        j. RT-10: partial-then-failed execution -> FAILED with partial
           artifacts, never success; an uncompletable execution reaches the
           DLQ.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the execution identity record with required-field rejection
   - agent_executions with its uniqueness constraint and prompt redaction
   - the least-privilege, single-tenant-single-project context package builder
   - policy-bound model selection with no caller override
   - side-effect class gating for irreversible steps
   - immutable, redacted traces with full tool-call recording
   - HITL escalation with enforced no-self-approval
   - the complete failure taxonomy with no-silent-success and a DLQ path
   - the replay command
   - tests/agent/rt-*.* with one test per contract area
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten contract-area tests.
   - State the mapping of RT-01..RT-10 to the test that proves each failure
     action. All ten must be covered.
   - For case c, show that mixing tenants is structurally impossible rather
     than merely checked.
   - For case j, paste the FAILED-with-partials record.
   - Acceptance criterion: every one of the ten failure actions in sheet 36 is
     exercised by a passing test.

G. COMPLETION CONTRACT
   Definition of Done: all ten contract areas enforced, each failure action
   tested, executions attributable, reproducible and policy-constrained.
   Evidence to report: the ten test outputs, the RT-to-test mapping table, the
   structural isolation demonstration.
   Remaining blockers: none expected. If a contract area depends on a later
   phase (RT-09's reviewer registry is PHASE-07), enforce the runtime half now
   and name the completing prompt.
   Next prompt: P05-02.
```

**المخرجات المتوقعة:** عقد تنفيذ بعشرة مجالات مفروضة، تتبّع غير قابل للتعديل، مسار DLQ.
**التحقق المطلوب:** كل إجراء فشل في الورقة 36 مُفعَّل باختبار ناجح.
**الاعتمادية التالية:** `P05-02`.

---

### P05-02 — سجل الوكلاء ودورة حياة الإصدارات

<!-- meta
id: P05-02
phase: PHASE-05
title_en: Agent registry, versioning lifecycle, canary and rollback
prereq: [P05-01]
requirements: [REQ-AGT-03, REQ-AGT-06, REQ-AGT-07, REQ-AGT-08]
-->

**ماذا سينفذ هذا الأمر؟** يبني الكيانات الخمسة في الورقة 62
(`AgentDefinition`, `AgentVersion`, `AgentDeployment`, `AgentRun`,
`AgentOutput`) مع بوابة إصدار وقاعدة رجوع لكل منها.

**لماذا نحتاجه؟** الورقة 57 الصف 4 تحدد الفجوة بدقة: السجل ليس إصدارات قابلة
للنشر، والأثر «إصدارات غير مُتحكَّم بها»، والدليل المطلوب «إثبات رجوع». والورقة 58
الصف 4 تجعل تفعيل أو تعطيل إصدار وكيل في الإنتاج يحتاج «موافقة مزدوجة» و«canary +
rollback».

**ما المتطلبات السابقة؟** `P05-01`.

**ما النتيجة المتوقعة؟** سجل وكلاء بإصدارات غير قابلة للتعديل، ونشر تدريجي،
ورجوع مُثبت.

**كيف نتحقق من نجاحه؟** نشر إصدار ثم الرجوع عنه يُنتج دليلاً مُسجَّلاً؛ وتعديل
إصدار منشور مستحيل.

```text
TASK P05-02 — Agent registry, versioning lifecycle, canary and rollback

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-02
   Phase: PHASE-05
   Prerequisites: P05-01
   Requirements covered: REQ-AGT-03, REQ-AGT-06, REQ-AGT-07, REQ-AGT-08

B. OBJECTIVE
   Implement the five agent lifecycle objects with their mandatory fields,
   release gates and rollback rules, so a capability in a table becomes a
   deployable, versioned, reversible artifact.

   Why this is necessary: sheet 57 row 4 names the gap precisely — registry
   capabilities are not equivalent to deployable agent versions, the impact is
   uncontrolled releases, and the required acceptance evidence is rollback
   proof. Sheet 58 row 4 requires dual approval plus canary and rollback to
   enable or disable an agent version in production. Sheet 62 row 2 forbids
   dynamic arbitrary tools.

   SCOPE BOUNDARY: the registry, versioning, deployment and rollback. The
   tool-safety controls are P05-03. The evaluation suites that gate releases
   are PHASE-14 — here you build the gate and the hook, and an unpopulated
   eval suite must block, not pass.

C. CONTEXT
   Required inputs, sheet 62 rows 2-6, each as object / mandatory fields /
   release gate / rollback / notes:
     AgentDefinition — agent_id, capability, domain, input_schema,
       output_schema / owner approved / keep prior version / no dynamic
       arbitrary tools
     AgentVersion — version, prompt_hash, tools, model_policy, eval_suite /
       golden-set pass / pin previous version / immutable
     AgentDeployment — environment, traffic percentage, concurrency, budget /
       canary and shadow / traffic switch / per-project visibility
     AgentRun — execution_id, tenant_id, project_id, task_id, evidence_refs /
       idempotent task / compensate only / audit immutable
     AgentOutput — schema_version, provenance, confidence, citations,
       reviewer_state / validation plus policy / re-run as new version / no
       unsupported engineering signoff
   Also: config/registries/agent-capabilities.json and pmo-capabilities.json
   from P00-02 (the 44 plus 8 capability definitions, each with R, P, human
   gate, stop conditions, workflows, KPIs and owner).

D. EXECUTION INSTRUCTIONS
   1. Implement AgentDefinition with its five mandatory fields. input_schema
      and output_schema are required and validated — a definition without them
      cannot be created. The owner-approved gate means a definition is DRAFT
      until a recorded owner approval exists.
   2. Implement AgentVersion as immutable after publication, with prompt_hash
      computed over the canonical prompt template, the explicit tool list, the
      model policy reference and the eval_suite reference. Enforce immutability
      at the database level as in P03-01.
   3. Implement the golden-set release gate: publishing an AgentVersion
      requires a passing evaluation run reference for its eval_suite. If no
      evaluation exists, publication is BLOCKED. Do not provide an override
      that silently bypasses the gate; if a break-glass path is required, it
      needs dual approval, an expiry and its own audit stream, consistent with
      P01-03.
   4. Implement AgentDeployment with environment, traffic percentage,
      concurrency limit and budget, including shadow mode (the version runs and
      is scored but its output is not consumed) and canary mode (a traffic
      share consumes it). Per-project visibility means a deployment can be
      scoped to named projects.
   5. Implement dual approval for production deployment changes per sheet 58
      row 4: two distinct approver identities, neither of whom is the author.
      Enforce distinctness; a single person holding two roles cannot satisfy it.
   6. Implement rollback as a first-class operation: a traffic switch back to
      the pinned previous version that takes effect without a deploy, records
      who, when and why, and emits an event. The previous version is always
      retained per the AgentDefinition rollback rule.
   7. Implement AgentRun per the source: idempotent task, compensate-only (no
      destructive undo), immutable audit. Reuse P03-03's idempotency and
      P01-05's audit store.
   8. Implement AgentOutput with schema_version, provenance, confidence,
      citations and reviewer_state, and enforce the note "no unsupported
      engineering signoff": an output cannot carry an approved reviewer_state
      unless a real review decision from PHASE-07 exists. Until PHASE-07,
      reviewer_state can only be NONE or PENDING.
   9. Map the capability registers to definitions: generate or validate an
      AgentDefinition per capability in agent-capabilities.json, carrying that
      capability's R rating, P rating, human gate and stop conditions as
      definition metadata. Record clearly which definitions have a published,
      eval-passing version (expected: none at this stage) and which are
      definition-only. This is the explicit correction of the sheet 57 row 4
      gap, and the honest answer at the end of this prompt is that 52
      capabilities are defined and few or none are deployable.
  10. Implement stop conditions as enforced preconditions: each capability's
      stop conditions from the register become machine-checkable guards that
      halt the step with a named reason. Where a stop condition cannot be
      expressed mechanically, record it as a required human gate instead of
      discarding it.
  11. Tests:
        a. create a definition without an output schema -> rejected;
        b. publish a version with no passing evaluation -> BLOCKED, naming the
           missing eval;
        c. edit a published version -> rejected at the database level;
        d. production deployment with one approver -> rejected; with two
           distinct non-author approvers -> accepted;
        e. canary at a configured share -> traffic distribution within
           tolerance; shadow mode -> output scored but not consumed, proven by
           asserting no consumer received it;
        f. rollback -> previous version serving within the switch window,
           recorded with actor and reason, event emitted. Retain this as the
           sheet 57 row 4 rollback proof;
        g. an output claiming an approved reviewer_state with no review
           decision -> rejected;
        h. a capability whose stop condition is triggered -> step halts with
           the named reason;
        i. a step requesting a tool not in its version's tool list -> blocked
           (reinforcing RT-02).
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the five lifecycle objects with mandatory fields and migrations
   - immutable published versions with prompt_hash
   - the golden-set publication gate that blocks without evaluation evidence
   - deployments with canary, shadow, concurrency and budget
   - dual approval with enforced approver distinctness
   - rollback as a recorded, deploy-free traffic switch
   - capability-to-definition mapping with an honest deployability report
   - stop conditions as enforced guards or recorded human gates
   - tests/agent/registry-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - Paste the rollback evidence from case f — this is a named acceptance
     requirement in sheet 57 row 4.
   - Report the deployability table: total capabilities defined, versions
     created, versions with a passing evaluation, versions deployed. State the
     real numbers even when they are zero.
   - Acceptance criterion: no version publishes without evaluation evidence, no
     published version is mutable, and rollback is demonstrated end to end.

G. COMPLETION CONTRACT
   Definition of Done: five objects implemented, publication gated on
   evaluation, dual approval and rollback proven, capabilities mapped with an
   honest deployability count.
   Evidence to report: the nine test outputs, the rollback proof, the
   deployability table.
   Remaining blockers: evaluation suites and golden sets arrive in PHASE-14, so
   the number of publishable versions is expected to be zero or near zero now.
   Report that as correct behaviour rather than working around the gate.
   Next prompt: P05-03.
```

**المخرجات المتوقعة:** خمسة كيانات دورة حياة، بوابة تقييم، canary وshadow، رجوع مُثبت.
**التحقق المطلوب:** لا نشر بلا دليل تقييم؛ لا تعديل لإصدار منشور؛ رجوع مُثبت من طرف إلى طرف.
**الاعتمادية التالية:** `P05-03`.

---

### P05-03 — حدود الأدوات ومنع الحقن والتسريب

<!-- meta
id: P05-03
phase: PHASE-05
title_en: Tool boundary, injection defence and egress control
prereq: [P05-02]
requirements: [REQ-SEC-05, REQ-SEC-06, REQ-AGT-03, REQ-AGT-02]
-->

**ماذا سينفذ هذا الأمر؟** يبني حدود الأدوات: قائمة سماح، أقل صلاحية، تسميات ثقة
للمدخلات، منع خروج غير مصرح به، ودفاعات ضد حقن المطالبات.

**لماذا نحتاجه؟** الورقة 27 الصف 8 (`SEC-07`) بأولوية `CRITICAL` ودليلها
«اختبارات خصومية». والورقة 57 الصف 10 (`A09`) تحدد الأثر: «تسريب بيانات»،
والتنفيذ المطلوب: «tool allowlist, egress policy, input trust labels»، والدليل:
«red-team suite». ملف العميل مُدخَل غير موثوق بطبيعته، وسيصل إلى نموذج له أدوات.

**ما المتطلبات السابقة؟** `P05-02`.

**ما النتيجة المتوقعة؟** طبقة أدوات مُقيَّدة بقائمة سماح لكل إصدار وكيل، وتسميات
ثقة مُنفَّذة، ومنع خروج مفروض.

**كيف نتحقق من نجاحه؟** محاولة استخراج سر عبر تعليمات مزروعة في ملف عميل تفشل
وتُسجَّل؛ ونداء خروج غير مُدرج يُحجَب.

```text
TASK P05-03 — Tool boundary, injection defence and egress control

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-03
   Phase: PHASE-05
   Prerequisites: P05-02
   Requirements covered: REQ-SEC-05, REQ-SEC-06, REQ-AGT-02, REQ-AGT-03

B. OBJECTIVE
   Implement the tool execution boundary: a per-agent-version tool allowlist,
   least-privilege tool credentials, input trust labels, enforced egress
   control, and defences against prompt injection and tool-based exfiltration.

   Why this is necessary: sheet 27 row 8 (SEC-07) is CRITICAL with required
   evidence of adversarial tests. Sheet 57 row 10 (A09) names the impact as
   data leakage, the required implementation as tool allowlist plus egress
   policy plus input trust labels, and the acceptance evidence as a red-team
   suite. A customer drawing is untrusted input by construction, and it will
   reach a model that holds tools.

   SCOPE BOUNDARY: the tool boundary and its adversarial tests. The full
   red-team programme and its reporting are PHASE-11; this prompt builds the
   controls and a first adversarial suite that PHASE-11 extends.

C. CONTEXT
   Required inputs:
     - the AgentVersion tool list from P05-02 and RT-02 from P05-01
     - the network egress allowlist from P04-04 step 4
     - sheet 36 row 7: block unregistered tools
     - sheet 62 row 2: no dynamic arbitrary tools
     - sheet 45 row 7 and sheet 05 agent rows: each capability names a human
       gate
   Threat model note: the attacker's input arrives as document content,
   filenames, metadata, OCR text, EXIF fields, IFC property values and
   retrieved knowledge passages. All of these are untrusted. Instructions found
   inside them are data, never commands.

D. EXECUTION INSTRUCTIONS
   1. Implement the tool registry: every tool has an id, a version, a typed
      input and output schema, a declared side-effect class, a declared egress
      requirement and an owner. A tool not in the registry cannot be invoked by
      any path. Tool construction from a model-produced name is prohibited —
      resolution happens only against the registry.
   2. Enforce the per-version allowlist: the set of callable tools for a step
      is the intersection of the agent version's declared tool list and the
      policy decision's permitted tools. An invocation outside that set is
      blocked and recorded as a security event, not merely refused.
   3. Implement least-privilege tool credentials: each tool receives a
      credential scoped to the current tenant, project and operation, minted at
      invocation time with a short lifetime. A tool never receives a broad or
      long-lived credential, and never receives the provider credentials.
   4. Implement input trust labels: every element entering a context package
      carries a trust label (SYSTEM, OPERATOR, TENANT_CONFIG,
      UNTRUSTED_DOCUMENT, UNTRUSTED_RETRIEVAL, UNTRUSTED_EXTERNAL). The label
      travels with the element. Rules:
        - no instruction from an UNTRUSTED_* element may change the step's tool
          set, its policy decision, its budget, its destination or its output
          schema;
        - a tool invocation whose arguments derive from an UNTRUSTED_* element
          is checked against the tool's schema and its argument allowlist, and
          free-form passthrough of untrusted text into a tool argument that
          controls a destination (a URL, a path, a recipient, a query target)
          is prohibited;
        - the system prompt and the untrusted content are structurally
          separated in the request to the provider, and the model is instructed
          that document content is data.
   5. Enforce egress control at the tool layer in addition to the network
      layer: a tool that performs a network call declares its permitted
      destinations, and a destination derived from untrusted content is
      rejected. This blocks the classic exfiltration path where injected text
      supplies a callback URL.
   6. Implement output-side leak prevention: scan tool results and model output
      for credential-shaped strings and for content belonging to another
      tenant's namespace before they enter the context or the stream. A hit is
      an incident, not a redaction-and-continue.
   7. Implement the human gate for tool calls where the capability register
      demands it, and for any tool whose side-effect class is IRREVERSIBLE,
      reusing P03-02's gating.
   8. Build the first adversarial suite. These tests use planted hostile
      content inside otherwise normal fixtures:
        a. a PDF whose text instructs the agent to reveal its system prompt ->
           no system prompt in output, event recorded;
        b. a PDF instructing the agent to call a tool not in its allowlist ->
           blocked, event recorded;
        c. a PDF supplying an external URL and instructing an upload -> egress
           refused at both the tool and network layers;
        d. an IFC property value containing an injection payload -> treated as
           data, no behaviour change;
        e. a retrieved knowledge passage containing an injection payload ->
           treated as data;
        f. a filename and EXIF field containing injection payloads -> treated
           as data;
        g. an attempt to widen the tool set at runtime through a model-produced
           tool name -> resolution fails against the registry;
        h. a tool argument built from untrusted text that names a path outside
           the tenant prefix -> rejected;
        i. a tool result containing a credential-shaped string -> flagged as an
           incident and not propagated;
        j. a tool result containing another tenant's identifier -> flagged as
           an incident.
      Every one of these assertions must be able to fail: demonstrate at least
      three by temporarily weakening the control.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the tool registry with typed schemas and declared egress
   - per-version allowlist intersection enforcement with security events
   - short-lived, narrowly scoped tool credentials
   - the input trust label system with its four prohibition rules
   - tool-layer egress destination control
   - output-side credential and cross-tenant leak detection
   - human gating for declared and irreversible tool calls
   - tests/security/red-team-agents.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten adversarial tests.
   - For at least three cases, paste the weakened-control run showing the test
     failing, then the restored run showing it passing.
   - Paste the security events generated by cases a, b and c.
   - Acceptance criterion: no planted instruction in untrusted content changes
     tool set, destination, budget or schema; every attempt is recorded.

G. COMPLETION CONTRACT
   Definition of Done: tool boundary enforced, trust labels implemented with
   their prohibitions, egress controlled at two layers, adversarial suite
   passing and proven able to fail.
   Evidence to report: the ten test outputs, the three weakened-control
   demonstrations, the security event records.
   Remaining blockers: this is a first suite, not a complete programme.
   PHASE-11 extends it; say so rather than implying completeness.
   Next prompt: P05-04.
```

**المخرجات المتوقعة:** سجل أدوات، قائمة سماح لكل إصدار، تسميات ثقة، تحكم خروج بطبقتين.
**التحقق المطلوب:** عشر حالات خصومية ناجحة، وثلاث منها مُثبت قدرتها على الفشل.
**الاعتمادية التالية:** `P05-04`.

---

### P05-04 — محرك R/P والبوابات البشرية

<!-- meta
id: P05-04
phase: PHASE-05
title_en: Two-axis risk engine and human gates
prereq: [P05-03]
requirements: [ADR-005, REQ-AGT-08, REQ-AGT-09, REQ-SVC-02]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ `ADR-005`: محور `Action Risk R0-R4` منفصلاً عن
محور `Professional Consequence P0-P3`، ويربط كل مستوى ببوابته البشرية.

**لماذا نحتاجه؟** `ADR-005` ضابط قبوله: «P3 لمتخصص؛ R4 بتفويض». والورقة 35 الصف 6
تضع الحارس الأشد: «لا اعتماد مُرخَّص من الذكاء الاصطناعي». وبدون محرك يفرض هذين
المحورين بشكل منفصل، ستختلط صلاحية الفعل بأثر الخطأ، وهو بالضبط ما يحذّر منه
المصدر.

**ما المتطلبات السابقة؟** `P05-03`.

**ما النتيجة المتوقعة؟** محرك مخاطر بمحورين مستقلين، وبوابات بشرية إلزامية لكل
قدرة بحسب تصنيفها في الورقة 05.

**كيف نتحقق من نجاحه؟** قدرة `P3` لا تُنتج مخرجاً نهائياً بلا متخصص؛ وفعل `R4`
لا يُنفَّذ بلا تفويض مُسجَّل.

```text
TASK P05-04 — Two-axis risk engine and human gates

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-04
   Phase: PHASE-05
   Prerequisites: P05-03
   Requirements covered: ADR-005, REQ-AGT-08, REQ-AGT-09, REQ-SVC-02

B. OBJECTIVE
   Implement the two independent risk axes and the human gates they imply:
   Action Risk R0-R4 governing authority to act, and Professional Consequence
   P0-P3 governing the impact of an error, with the source's acceptance control
   enforced — P3 requires a specialist and R4 requires delegated authority.

   Why this is necessary: ADR-005 (sheet 02 row 6) exists precisely to stop the
   two being conflated, and its stated reason is to separate authority to act
   from the consequence of error. Sheet 35 row 6 sets the absolute guardrail:
   no licensed approval by AI. Every one of the 52 capability rows in sheets 05
   and 06 carries an R value, a P value and a named human gate, so the engine
   is what makes those columns operative.

   SCOPE BOUNDARY: the risk engine, gate resolution and enforcement at the
   runtime boundary. Reviewer eligibility matching, assignment and signature
   are PHASE-07. Here, a required specialist gate is resolved to a role and
   held pending; PHASE-07 fills it with a real qualified person.

C. CONTEXT
   Required inputs:
     - config/registries/agent-capabilities.json and pmo-capabilities.json:
       every capability's action_risk, professional_consequence,
       human_gate_ar and stop_conditions_ar
     - ADR-005 acceptance control: "P3 requires a specialist; R4 requires
       delegation"
     - sheet 05 examples showing the axes are genuinely independent: DOC-01 is
       R4/P3; FIN-02 is R4/P2; GOV-01 is R3/P3; DAT-01 is R1/P2; CTL-01 is
       R1/P1
     - sheet 35 row 6 guardrail: no licensed approval by AI

D. EXECUTION INSTRUCTIONS
   1. Implement the two axes as separate, non-collapsible values on every step
      and every output. Reject any code that derives one from the other or
      combines them into a single score. The independence is the whole point of
      the ADR.
   2. Define, in configuration, the gate policy per axis level:
        - Action Risk: R0 and R1 proceed; R2 requires a named approver role;
          R3 requires an approver plus a recorded rationale; R4 requires a
          recorded delegation of authority naming the delegator, the delegate,
          the scope and the expiry.
        - Professional Consequence: P0 and P1 need no specialist; P2 requires a
          qualified reviewer in scope; P3 requires a qualified specialist in
          the matching discipline, and, where the capability register says so,
          a second review.
      Implement both ladders independently, and resolve a step's requirement as
      the union of both — the stricter requirement on each axis applies, and
      satisfying one axis never satisfies the other.
   3. Implement R4 delegation as a real, auditable object: delegator identity,
      delegate identity, scope, validity window, and a revocation path. An R4
      action without an active, in-scope delegation does not execute.
   4. Implement the P3 specialist requirement as a blocking gate that resolves
      to a discipline-specific role and holds the output in the
      PENDING_HUMAN_APPROVAL state from P04-07. No automatic clearance, no
      timeout-based approval, no default approve.
   5. Implement the absolute guardrail of sheet 35 row 6 as an enforced
      invariant: no system actor other than a qualified human reviewer can set
      an output to an approved or certified state. Add a test that attempts it
      as the highest-privileged service identity and asserts refusal. This is
      the same prohibition sheet 04 row 2 places on PLATFORM_OWNER.
   6. Implement the human gates named in the capability register as resolved
      role requirements, so each capability's gate column becomes a machine
      requirement rather than prose. Where the register's gate names a
      function (for example Quality Lead, QS or Cost Manager, HSE Officer, BIM
      Coordinator), map it to a role in the RBAC register and fail loudly on an
      unmapped gate rather than defaulting to no gate.
   7. Implement the second-review trigger: where a capability or the
      eligibility matrix requires a second review (sheet 12 names triggers per
      code, such as every P3 for fire review), the engine requires two distinct
      qualified reviewers and records both.
   8. Make the risk classification visible on outputs and in the trace, so a
      downstream consumer cannot treat a P3 output as routine.
   9. Tests:
        a. an R4 step with no delegation -> does not execute, reason recorded;
        b. an R4 step with an expired or out-of-scope delegation -> does not
           execute;
        c. an R4/P1 step with a valid delegation -> executes, and no specialist
           gate is demanded (proving axis independence in one direction);
        d. an R1/P3 step -> executes but its output is held
           PENDING_HUMAN_APPROVAL for a specialist (proving independence in the
           other direction);
        e. a service identity, including the highest-privileged one, attempts
           to approve a P3 output -> refused;
        f. a capability whose human gate is unmapped -> the step fails loudly
           at configuration load, not silently at runtime;
        g. a P3 capability with a second-review trigger -> two distinct
           reviewers required, one is insufficient;
        h. an attempt to store a single combined risk score -> rejected;
        i. the risk classification appears on the output and in the trace.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the two independent axes with a type-level prohibition on collapsing them
   - the two gate ladders in configuration, resolved as a union
   - R4 delegation objects with scope, expiry and revocation
   - P3 specialist gating with no automatic clearance
   - the no-AI-approval invariant enforced against all service identities
   - capability human gates mapped to RBAC roles with loud failure on gaps
   - the second-review trigger
   - risk classification surfaced on outputs and traces
   - tests/agent/risk-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - For cases c and d, state explicitly how they prove the axes are
     independent.
   - For case e, paste the refusal with the identity that attempted it.
   - Report how many of the 52 capabilities have a gate that maps cleanly to an
     RBAC role and how many do not. An unmapped gate is a real finding to
     report, not a gap to paper over.
   - Acceptance criterion: no R4 action without delegation, no P3 output
     approved by any non-human, and the axes provably independent.

G. COMPLETION CONTRACT
   Definition of Done: both axes enforced independently, delegation and
   specialist gating working, the no-AI-approval invariant proven, gates mapped.
   Evidence to report: the nine test outputs, the independence argument, the
   gate mapping coverage count.
   Remaining blockers: real qualified reviewers do not exist until PHASE-07, so
   every P3 output is expected to sit PENDING_HUMAN_APPROVAL. Confirm nothing
   auto-clears it.
   Next prompt: P06-01. PHASE-05 exit requires the RT suite green, rollback
   proven, the adversarial suite green, and the no-AI-approval invariant proven.
```

**المخرجات المتوقعة:** محرك مخاطر بمحورين مستقلين، تفويضات R4، بوابات P3، حارس «لا اعتماد من الذكاء».
**التحقق المطلوب:** استقلال المحورين مُثبت؛ لا هوية خدمة تستطيع اعتماد مخرج P3.
**الاعتمادية التالية:** `P06-01`.

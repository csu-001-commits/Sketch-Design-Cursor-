# PHASE-10 — الرصد والموثوقية وFinOps

<!-- phasemeta
id: PHASE-10
depends_on: [PHASE-04, PHASE-09]
criticality: P0
-->

## الغرض من المرحلة

الورقة 77 الصف 7 تحسم فلسفة هذه المرحلة: تعتمد «آثار OTel ودفتر استخدام وتقييم
جودة وكتب تشغيل الحوادث»، وترفض صراحة «لوحة جميلة بأرقام حقيقية مُختلقة»
(pretty dashboard with invented live numbers). والورقة 30 الصف 14 تكرر: «القيم
الحالية لا تُملأ إلا من مصادر تشغيل موثقة. لا تستخدم أرقاماً افتراضية لإظهار
النجاح».

لذلك هذه المرحلة تبني القياس الحقيقي، وتترك المؤشر فارغاً إن لم يُقَس.

## شروط الدخول

- اكتمال `PHASE-04`: البوابة ومحرك مسارات العمل يُصدران قياسات.

## شروط الخروج

- تسع لوحات حيّة بتنبيهات مُختبَرة.
- أثر واحد يربط المهمة بالوكيل والنموذج والأداة والدليل والمراجعة.
- تدريب استرجاع كارثي يحقق `RTO` و`RPO` مُعلَنين.
- مطابقة الاستخدام مع فواتير المزود.

## المتطلبات المغطاة في هذه المرحلة

`REQ-OBS-01`, `REQ-OBS-02`, `REQ-OBS-03`, `REQ-OBS-05`, `REQ-SEC-14`,
`REQ-COM-11`, `REQ-GW-11`

---

## الأوامر التنفيذية

### P10-01 — التتبع الموحد وربط السلسلة

<!-- meta
id: P10-01
phase: PHASE-10
title_en: Unified tracing and the six-level linkage
prereq: [P09-03]
requirements: [REQ-OBS-02, REQ-GW-11, REQ-SEC-04]
-->

**ماذا سينفذ هذا الأمر؟** يبني تتبعاً موحداً بـOpenTelemetry يربط
`trace_id` ← المهمة ← الوكيل ← النموذج ← الأداة ← الدليل ← المراجعة، مع حجب
البيانات الحساسة.

**لماذا نحتاجه؟** الورقة 73 الصف 10 تُسمّي هذا «Trace drilldown» وتحدد إجراءه
عند النقص: «instrument pipeline» — أي أن غياب الربط عيب تقني لا نقص في لوحة.
والورقة 22 الصف 22 توصي بـOpenTelemetry بضابط: «Redaction وcorrelation».

**ما المتطلبات السابقة؟** `P09-03`.

**ما النتيجة المتوقعة؟** تتبع كامل قابل للتنقل في ستة مستويات، بلا أسرار ولا
بيانات شخصية.

**كيف نتحقق من نجاحه؟** اختبار يبدأ من `trace_id` واحد ويصل إلى قرار المراجعة؛
واختبار يؤكد غياب الأسرار من كل الآثار.

```text
TASK P10-01 — Unified tracing and the six-level linkage

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P10-01
   Phase: PHASE-10 (Observability, reliability and FinOps)
   Prerequisites: P09-03
   Requirements covered: REQ-OBS-02, REQ-GW-11, REQ-SEC-04

B. OBJECTIVE
   Implement unified distributed tracing with the source's required linkage —
   trace_id to task to agent to model to tool to evidence to review — with
   secret and PII scrubbing and scoped retention.

   Why this is necessary: sheet 73 row 10 names this drilldown and defines the
   action for a missing linkage as "instrument pipeline", making an incomplete
   chain an engineering defect rather than a reporting gap. Sheet 70 row 12
   requires tracing of all spans with PII scrubbing and scoped audit and
   retention. Sheet 22 row 22 adopts OpenTelemetry with the control "redaction
   and correlation".

   SCOPE BOUNDARY: tracing, correlation and redaction. Dashboards are P10-02.
   Do not add a metrics backend decision here beyond what tracing needs; record
   it as an ADR if you must choose one.

C. CONTEXT
   Required inputs:
     - the correlation and causation ids from the event envelope (P03-03)
     - the execution identity from RT-01 (P05-01) and the trace_id from RT-07
     - the evidence manifests (P02-03) and review decisions (P07-04)
     - sheet 73 row 10: dimension "correlation IDs"; alert "missing linkage";
       action "instrument pipeline"
   Constraint: traces are a disclosure surface. Sheet 76 row 6 (G05) extends
   tenant isolation explicitly to traces and logs, so a trace is tenant-scoped
   data, not operational exhaust.

D. EXECUTION INSTRUCTIONS
   1. Adopt OpenTelemetry and instrument every service boundary: API ingress,
      policy decisions, workflow transitions, task dispatch, agent executions,
      gateway routing, provider calls, tool calls, retrieval queries, evidence
      writes, review decisions and delivery operations.
   2. Propagate one correlation id from the originating request through every
      downstream span, event and job, including across the outbox and the queue
      so an asynchronous continuation stays on the same trace. Carry causation
      ids so a chain of events is reconstructable.
   3. Implement the six-level linkage as queryable relationships, not merely as
      span attributes: from a trace_id, resolve the workflow task, the agent
      version, the model version, the tool invocations, the evidence manifests
      and the review decisions. Provide one API or command that performs this
      walk and returns the full chain.
   4. Implement a linkage completeness check that runs over recent traces and
      reports any trace missing a level it should have, per sheet 73 row 10's
      alert condition. Wire it as a test and as a monitored signal.
   5. Implement redaction at the instrumentation layer, not at the viewing
      layer, so sensitive data never reaches the backend: deny-by-default
      attribute allowlists for span attributes; prompt and completion bodies
      excluded or hashed; credential and token patterns scrubbed; customer
      personal data reduced to identifiers. Add a test that injects
      representative secrets and PII through a traced path and asserts the
      exported spans are clean.
   6. Enforce tenant scoping on trace access: an operator query is scoped and
      audited, and cross-tenant trace access is denied through the P01-02
      helper. Support access is JIT and masked per sheet 03 row 9 and sheet 58
      row 13 ("no cross-tenant access", "sanitized logs").
   7. Implement retention per class with the retention and legal-hold hooks
      from P02-02, so traces expire on schedule and a held trace is preserved.
   8. Record sampling honestly: if you sample, record the sampling decision and
      rate on the trace and surface it wherever trace-derived counts are shown,
      so a sampled count is never presented as a complete count.
   9. Tests:
        a. from one trace_id, the walk returns all six levels for a completed
           villa run;
        b. an asynchronous continuation through the outbox and queue stays on
           the same correlation id;
        c. injected secrets and PII do not appear in exported spans;
        d. a cross-tenant trace query -> denied;
        e. the linkage completeness check flags a deliberately
           un-instrumented step;
        f. retention expiry removes an out-of-policy trace; a legal hold
           prevents it;
        g. a sampled trace carries its sampling rate, and a trace-derived count
           reports that it is sampled.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - OpenTelemetry instrumentation across every listed boundary
   - correlation and causation propagation including across async boundaries
   - the queryable six-level linkage walk
   - the linkage completeness check as a test and a signal
   - instrumentation-layer redaction with an attribute allowlist
   - tenant-scoped, audited, JIT-masked trace access
   - retention and legal-hold handling
   - honest sampling disclosure
   - tests/observability/trace-*.* covering cases a through g
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the six-level walk output for a real villa run.
   - Paste the redaction test showing injected secrets absent from exported
     spans.
   - Paste the completeness check flagging the un-instrumented step.
   - Acceptance criterion: no trace is missing a level it should have, and no
     trace contains a secret or unnecessary personal data.

G. COMPLETION CONTRACT
   Definition of Done: tracing complete across all boundaries, the six-level
   walk working, redaction proven, access scoped.
   Evidence to report: the walk output, the redaction proof, the completeness
   check result, the sampling configuration.
   Remaining blockers: none expected. Name any boundary you could not
   instrument and why.
   Next prompt: P10-02.
```

**المخرجات المتوقعة:** تتبع موحد، تنقّل بستة مستويات، حجب على مستوى القياس.
**التحقق المطلوب:** لا أثر ناقص مستوى؛ لا أسرار في الآثار المُصدَّرة.
**الاعتمادية التالية:** `P10-02`.

---

### P10-02 — اللوحات التسع والتنبيهات

<!-- meta
id: P10-02
phase: PHASE-10
title_en: The nine dashboards and tested alerts
prereq: [P10-01]
requirements: [REQ-OBS-01, REQ-OBS-05, REQ-GW-11]
-->

**ماذا سينفذ هذا الأمر؟** يبني اللوحات التسع في الورقة 73، كل منها بإشاراتها
وأبعادها ومُحفِّز تنبيهها وإجرائها، مع تنبيهات مُختبَرة بتدريب حقيقي.

**لماذا نحتاجه؟** الورقة 38 الصف 15 (`G-10`) حاجز إصدار بمعيار «لوحات وتنبيهات
قابلة للتفعيل» ودليل مطلوب «screenshots + alert drill». والورقة 76 الصف 11
(`G10`) تكرر: «لوحات وتنبيهات وكتب تشغيل مُختبَرة». لوحة بلا تدريب تنبيه ليست
دليلاً.

**ما المتطلبات السابقة؟** `P10-01`.

**ما النتيجة المتوقعة؟** تسع لوحات مبنية من قياسات حقيقية، وتنبيهات مُفعَّلة
ومُختبَرة، ومؤشرات فارغة حيث لا قياس.

**كيف نتحقق من نجاحه؟** تدريب تنبيه لكل لوحة يُنتج تنبيهاً فعلياً يصل إلى
المناوب؛ ومؤشر بلا مصدر يظهر `PENDING` لا رقماً.

```text
TASK P10-02 — The nine dashboards and tested alerts

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P10-02
   Phase: PHASE-10
   Prerequisites: P10-01
   Requirements covered: REQ-OBS-01, REQ-OBS-05, REQ-GW-11

B. OBJECTIVE
   Build the nine dashboards the source specifies, each from real measured
   signals, with its alert trigger wired and drilled — and with any metric that
   has no real source left explicitly empty rather than filled.

   Why this is necessary: sheet 38 row 15 (G-10) is a release blocker whose
   pass criterion is actionable dashboards and alerts, with required evidence
   of screenshots plus an alert drill. Sheet 76 row 11 (G10) repeats it. Sheet
   77 row 7 explicitly rejects "pretty dashboard with invented live numbers".
   Sheet 30 row 14 forbids populating current values from anything but
   documented operational sources.

   SCOPE BOUNDARY: dashboards, alert rules and drills. Runbooks are P10-03. DR
   is P10-04.

C. CONTEXT
   Required inputs, sheet 73 rows 2-10, each as dashboard / signals /
   dimensions / example alert trigger / action:
     Golden signals / RPS, error percentage, p50, p95, p99, saturation /
       route, provider, model, tenant / p95 above SLO for 10 minutes / shed
       low-priority load
     Capacity / queue age, depth, worker busy, in-flight, TPM and RPM headroom
       / workflow, provider / oldest job above 120 seconds / scale worker or
       switch approved provider
     Model quality / eval score, invalid JSON percentage, unsupported claim
       percentage, human override / task, model, version / quality floor
       breached / roll back routing
     Cost / SAR per project and task, in, out and cache tokens, budget burn /
       tenant, agent, project / forecast above budget / throttle, require
       approval
     Reliability / 429, 5xx, timeout, retry, fallback success, circuit state /
       provider, region / fallback above 15 percent for 15 minutes / incident
       and capacity escalation
     Retrieval / RAG hit, citations, vector latency, ACL denied / index,
       tenant / citation coverage drops / pause sensitive workflows
     Scan ingestion / frame drops, upload latency, geometry confidence, scan
       completion / device, OS, project / low quality above threshold / prompt
       recapture
     Privacy / blocked routes, redaction failure, denied egress /
       classification / any unapproved transfer / immediate block and audit
     Trace drilldown / the six-level chain / correlation IDs / missing linkage
       / instrument pipeline
   And sheet 30 rows 2-12, the twelve KPIs with their targets, several of which
   are TBD.

D. EXECUTION INSTRUCTIONS
   1. Build each of the nine dashboards with exactly the signals and dimensions
      the source names. Where a signal's source does not exist yet (scan
      ingestion before PHASE-12), build the panel and show NO DATA with the
      owning phase named — not a zero, and not a placeholder series.
   2. Implement each alert rule with the source's trigger semantics, including
      its duration window where given (p95 above SLO for 10 minutes; fallback
      above 15 percent for 15 minutes; oldest job above 120 seconds). A
      threshold without a window produces alert noise, and the source specified
      windows deliberately.
   3. Wire each alert to its stated action. Where the action is automatic (shed
      low-priority load, throttle, pause sensitive workflows, immediate block),
      implement the automation and test it. Where it is human (incident
      escalation, require approval, prompt recapture), route it to the on-call
      path and record the routing.
   4. Implement the KPI surface from sheet 30 with honest states. A KPI whose
      target is TBD shows the measured value and the target state PENDING. A
      KPI whose current value has no documented operational source shows NO
      SOURCE. Three KPIs have a hard target of zero — cross-tenant confirmed
      incidents, reviewer mismatch incidents and duplicate activation — and
      those are alerting conditions on any non-zero value, with cross-tenant
      incidents carrying the source's Stop-the-line action.
   5. Implement the model quality dashboard's inputs carefully: eval score
      comes from PHASE-14 and will be empty until then; invalid JSON
      percentage and unsupported claim percentage come from the P04-07
      validator and are available now; human override comes from P07-04
      decisions and is available now. Show each panel's real availability.
   6. Implement the cost dashboard from the usage ledger (P04-06), with budget
      burn and forecast. Where a model is UNPRICED, the cost panel shows token
      volumes and an explicit UNPRICED portion rather than understating cost as
      zero.
   7. Run an alert drill for every one of the nine dashboards: inject or
      simulate the trigger condition, confirm the alert fires, confirm it
      reaches the configured recipient, confirm the stated action occurs, and
      record the drill. This is the evidence G-10 names.
   8. Capture dashboard evidence for the release gate: for each dashboard,
      record what it shows, from which real signal, and its current data
      availability.
   9. Add a guard test asserting no dashboard panel is backed by a constant, a
      hardcoded series or a random generator. Sheet 77 row 7 rejects invented
      live numbers, and this test is how that rejection becomes enforceable.
  10. Tests and drills:
        a. nine alert drills, one per dashboard, each with the fired alert, the
           delivery and the resulting action;
        b. a KPI with a TBD target shows PENDING, never a number;
        c. a KPI with no documented source shows NO SOURCE;
        d. a non-zero cross-tenant incident count triggers the Stop-the-line
           action path;
        e. an UNPRICED model's cost panel shows the unpriced portion explicitly;
        f. a panel whose upstream signal does not exist shows NO DATA with the
           owning phase;
        g. the no-fabricated-data guard test passes, and fails when a constant
           series is deliberately introduced.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - nine dashboards with the source's exact signals and dimensions
   - alert rules with their duration windows
   - automated actions implemented and tested; human actions routed to on-call
   - the KPI surface with PENDING, NO SOURCE and hard-zero alerting
   - the cost dashboard with explicit UNPRICED handling
   - nine recorded alert drills
   - dashboard evidence captured for G-10
   - the no-fabricated-data guard test
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the nine alert drill records showing trigger, delivery and action.
   - Paste the KPI surface output showing PENDING and NO SOURCE states.
   - Paste the guard test both passing and failing on an injected constant.
   - State, per dashboard, which panels have real data today and which show NO
     DATA.
   - Acceptance criterion: every alert has been drilled end to end, and no
     panel or KPI displays a number that is not measured.

G. COMPLETION CONTRACT
   Definition of Done: nine dashboards live from real signals, nine alerts
   drilled, honest empty states, fabrication guard enforced.
   Evidence to report: the drill records, the KPI state output, the guard test
   both ways, the per-dashboard data availability table.
   Remaining blockers: KPI targets are owner-owned (OD-04); eval scores arrive
   in PHASE-14; scan signals arrive in PHASE-12. Name all three.
   Next prompt: P10-03.
```

**المخرجات المتوقعة:** تسع لوحات بإشارات حقيقية، تسعة تدريبات تنبيه، حارس ضد الأرقام المُختلقة.
**التحقق المطلوب:** كل تنبيه مُدرَّب من طرف إلى طرف؛ لا لوحة تعرض رقماً غير مقيس.
**الاعتمادية التالية:** `P10-03`.

---

### P10-03 — كتب التشغيل ومسارات الدعم

<!-- meta
id: P10-03
phase: PHASE-10
title_en: SRE runbooks and support operations
prereq: [P10-02]
requirements: [REQ-OBS-03, REQ-OBS-04, REQ-COM-11]
-->

**ماذا سينفذ هذا الأمر؟** يبني كتب التشغيل السبعة في الورقة 75 ومسارات الدعم
السبعة في الورقة 61، كأدوات قابلة للتنفيذ لا وثائق.

**لماذا نحتاجه؟** الورقة 76 الصف 11 تطلب «كتب تشغيل مُختبَرة». والورقة 61 تحدد
لكل سيناريو «إجراءً آمناً» محدداً — مثل «pause/requeue idempotently» للتشغيل
المتوقف، و«throttle and downgrade safe tasks» لارتفاع التكلفة. هذه الإجراءات يجب
أن تكون أزراراً مُؤمَّنة لا خطوات يدوية في وقت الحادث.

**ما المتطلبات السابقة؟** `P10-02`.

**ما النتيجة المتوقعة؟** كتب تشغيل مع إجراءات آمنة مُنفَّذة ومُدرَّبة، ومطابقة
يومية فعّالة.

**كيف نتحقق من نجاحه؟** لكل سيناريو تدريب يُنفَّذ إجراؤه الآمن ويُسجَّل أثره؛
وإعادة تنفيذ الإجراء لا تُنتج أثراً مزدوجاً.

```text
TASK P10-03 — SRE runbooks and support operations

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P10-03
   Phase: PHASE-10
   Prerequisites: P10-02
   Requirements covered: REQ-OBS-03, REQ-OBS-04, REQ-COM-11

B. OBJECTIVE
   Implement the seven SRE runbooks and the seven support operations scenarios
   as executable, audited, idempotent safe actions — not as prose documents —
   and drill each one.

   Why this is necessary: sheet 76 row 11 (G10) requires tested runbooks as
   evidence. Sheet 75 and sheet 61 each specify a concrete safe action per
   scenario, and an action that only exists as a sentence in a wiki is
   performed badly at three in the morning. Sheet 61 row 3's action
   "pause/requeue idempotently" is a software requirement, not a human
   instruction.

   SCOPE BOUNDARY: the runbooks, their safe actions and their drills. The admin
   control plane that exposes them to staff is PHASE-13 — here you implement the
   actions and their guarantees, and wire them behind the existing
   authorization.

C. CONTEXT
   Required inputs, sheet 75 rows 2-8, each as scenario / detection / immediate
   response / recovery and evidence:
     429 throttling / rate-limit counters and backlog / bounded exponential
       jitter, backpressure, route to an approved alternate / load test and
       budget checks
     Provider outage / 5xx or circuit open / stop retries, open circuit, fail
       over where allowed / synthetic probes and incident review
     High spend / burn-rate alert / hard budget cutoff for noncritical tasks /
       ledger reconcile and approval
     Latency spike / p95 and p99 plus queue age / trace the bottleneck, limit
       concurrency, scale workers / capacity model and postmortem
     Bad answer regression / eval or human override / roll back the prompt or
       model policy, quarantine outputs / golden dataset replay
     Cross-tenant exposure / DLP or ACL anomaly / disable the route, isolate,
       rotate credentials, notify security / incident policy and audit
     Scan upload failure / upload retries and checksum / resumable encrypted
       upload, offline queue / evidence integrity verification
   And sheet 61 rows 2-8, each as scenario / trigger / first response / safe
   action / escalation / evidence / target:
     Model 429 / provider quota / route to an alternate approved model /
       circuit breaker plus bounded retry / AI on-call / trace and quota / no
       fabricated SLA
     Workflow stuck / no heartbeat / inspect task and lease / pause or requeue
       idempotently / SRE / execution id / SLO pending
     API failure / 5xx spike / check connector health / disable connector or
       fall back / integration on-call / synthetic tests / SLO pending
     Bad engineering result / quality flag / quarantine the deliverable / human
       review plus incident / engineering lead / evidence package / block
       delivery
     Data exposure / cross-tenant access suspicion / revoke token, isolate /
       security incident response / security lead / immutable logs / immediate
     LiDAR low confidence / coverage or accuracy low / request rescan / mark
       provisional / qualified engineer / confidence map / before approval
     Cost spike / token budget breached / throttle and downgrade safe tasks /
       hard tenant and project cap / Finance and AI on-call / usage ledger /
       within budget

D. EXECUTION INSTRUCTIONS
   1. Implement each safe action as an idempotent, authorized, audited
      operation with a typed input and a recorded outcome. At minimum:
      pause-queue, resume-queue, requeue-task, cancel-task, open-circuit,
      close-circuit, disable-connector, enable-connector, rollback-model-policy,
      rollback-agent-version, quarantine-deliverable, set-hard-budget-cap,
      limit-concurrency, revoke-token, isolate-tenant-route, request-rescan,
      mark-evidence-provisional.
   2. Make every action idempotent in the strict sense: applying it twice has
      the same effect as once, and the second application is recorded as a
      no-op rather than failing confusingly. Sheet 61 row 3 names idempotency
      explicitly for pause and requeue.
   3. Implement authorization per the source's role assignments and sheet 59's
      matrix: SRE may retry and pause; Support L2 retries under policy; AI
      operator changes model routing under dual approval; Security admin
      revokes and isolates; Finance sets budget caps with AI on-call. An action
      outside a role's authority is refused and audited.
   4. Implement the quarantine action for a bad engineering result per sheet 61
      row 5 with the target "block delivery": quarantining a deliverable
      prevents release immediately, even if it was already signed, and records
      the reason. It does not delete anything.
   5. Implement the detection side of each runbook as a monitored signal from
      P10-02, so a runbook is entered from an alert rather than from a human
      noticing.
   6. Write each runbook as a short executable document: the trigger, the
      diagnostic queries or commands to run, the decision points, the safe
      action to invoke, the escalation path, the evidence to capture, and the
      stated target. Keep the diagnostics as real commands against real
      signals.
   7. Implement the no-fabricated-SLA rule from sheet 61 row 2's target column:
      a runbook never tells an operator to communicate an SLA or recovery time
      the system cannot support. Where the source says "SLO pending", the
      runbook says the SLO is not yet established.
   8. Implement the daily reconciliation operational loop from P08-04 as a
      scheduled job with its report delivered to Finance, satisfying the A10
      requirement for daily reconciliation.
   9. Drill all seven SRE runbooks and all seven support scenarios, with
      overlaps handled once: inject the condition, enter the runbook from the
      alert, run the diagnostics, invoke the safe action, verify the effect,
      and capture the evidence the source names.
  10. Tests and drills:
        a. fourteen scenario drills (deduplicated where sheets 75 and 61
           overlap), each with the alert, the diagnostics output, the action
           invocation and the verified effect;
        b. each safe action applied twice -> idempotent, second recorded as a
           no-op;
        c. each safe action attempted by an unauthorized role -> refused and
           audited;
        d. quarantine on a signed, unreleased deliverable -> release blocked
           immediately;
        e. the stuck-workflow drill -> pause then requeue, with no duplicated
           side effect, proven by the P03-03 replay guarantees;
        f. the cost spike drill -> safe tasks downgraded, a critical
           verification task fails closed rather than being downgraded;
        g. the cross-tenant exposure drill -> route disabled, tenant isolated,
           credentials rotated, immutable log entries present;
        h. the daily reconciliation job runs on schedule and delivers its
           report.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - seventeen idempotent, authorized, audited safe actions
   - role-based authorization per sheet 59
   - quarantine that blocks release immediately
   - alert-driven runbook entry
   - fourteen executable runbook documents with real diagnostics
   - the no-fabricated-SLA rule applied
   - the scheduled daily reconciliation loop
   - recorded drills for every scenario
   - tests/ops/runbook-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the drill records for all fourteen scenarios.
   - Paste the double-application result for at least five safe actions.
   - Paste the unauthorized-role refusals.
   - Paste the cost spike drill showing the critical task failing closed rather
     than downgrading.
   - Acceptance criterion: every scenario has been drilled, every safe action
     is idempotent and authorized, and no runbook promises an SLA the system
     has not established.

G. COMPLETION CONTRACT
   Definition of Done: safe actions implemented and drilled, runbooks
   executable, reconciliation scheduled, authorization enforced.
   Evidence to report: the fourteen drill records, the idempotency results, the
   authorization refusals.
   Remaining blockers: SLO targets remain unestablished per the source's "SLO
   pending". Report that the runbooks reflect it honestly.
   Next prompt: P10-04.
```

**المخرجات المتوقعة:** سبعة عشر إجراءً آمناً، أربعة عشر كتاب تشغيل مُدرَّب، حلقة مطابقة يومية.
**التحقق المطلوب:** كل إجراء idempotent ومُفوَّض؛ لا كتاب تشغيل يَعِد بـSLA غير مُثبت.
**الاعتمادية التالية:** `P10-04`.

---

### P10-04 — النسخ الاحتياطي والاسترجاع وRTO/RPO

<!-- meta
id: P10-04
phase: PHASE-10
title_en: Backup, disaster recovery and the RTO/RPO drill
prereq: [P10-03]
requirements: [REQ-SEC-14, REQ-SEC-03, REQ-EVL-08]
-->

**ماذا سينفذ هذا الأمر؟** يبني النسخ الاحتياطي والاسترجاع وتدريباً حقيقياً يقيس
`RTO` و`RPO` فعلياً.

**لماذا نحتاجه؟** الورقة 57 الصف 8 (`A07`) تقول بوضوح: «لا دليل مُختبَر على
الاسترجاع من الكوارث»، والأثر «انقطاع الخدمة»، والدليل المطلوب «RTO/RPO test
evidence». والورقة 38 الصف 13 (`G-08`) حاجز إصدار: «بيئة اختبار مُسترجعة».
نسخة احتياطية لم تُسترجَع ليست نسخة احتياطية.

**ما المتطلبات السابقة؟** `P10-03`.

**ما النتيجة المتوقعة؟** نسخ احتياطي مُشفَّر ومُختبَر، وتدريب استرجاع كامل بأرقام
`RTO`/`RPO` مقيسة.

**كيف نتحقق من نجاحه؟** استرجاع كامل إلى بيئة نظيفة ينجح، وسلامة البيانات
المُسترجَعة مُتحقَّقة بالبصمات، والزمن مقيس لا مُقدَّر.

```text
TASK P10-04 — Backup, disaster recovery and the RTO/RPO drill

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P10-04
   Phase: PHASE-10
   Prerequisites: P10-03
   Requirements covered: REQ-SEC-14, REQ-SEC-03, REQ-EVL-08

B. OBJECTIVE
   Implement backups, recovery procedures and a real restore drill that
   measures actual RTO and RPO, producing the evidence the source demands.

   Why this is necessary: sheet 57 row 8 (A07) records that there is no tested
   disaster recovery evidence, names the impact as service outage, requires
   backup restore and failover drills, and names the acceptance evidence as
   RTO/RPO test evidence. Sheet 38 row 13 (G-08) is a release blocker whose
   pass criterion is a restored test environment. Sheet 54 row 13 (G12) makes
   disaster recovery a P0 release blocker. An unrestored backup is not a
   backup.

   SCOPE BOUNDARY: backup, restore, integrity verification and the drill. Do
   not perform a destructive action on any live environment. The drill restores
   into a separate, clearly named recovery environment.

C. CONTEXT
   Required inputs:
     - sheet 27 row 16 (SEC-15): backups, DR, RTO and RPO, queue durability,
       circuit breakers; evidence a DR drill
     - sheet 27 row 6 (SEC-05): encryption in transit and at rest, keys and
       backups; evidence config plus a restore test
     - sheet 42 row 14 (G10 in the evidence ledger): backup restore and
       RPO/RTO, currently NOT RUN
     - the append-only audit store (P01-05), immutable artifacts (P02-02) and
       the financial ledger (P08-04), each of which has integrity properties a
       restore must preserve
   Scope of what must be recoverable: the relational data, the object store
   including locked artifacts, the audit store, the event outbox and queues,
   the vector indexes, the secrets (by reference, through the vault's own
   recovery path), and the configuration and policy bundles.

D. EXECUTION INSTRUCTIONS
   1. Define and document the recovery objectives explicitly before measuring:
      a target RTO and RPO per data class. The source does not set numbers, so
      these are PROPOSED values requiring owner ratification — state them as
      proposed, then measure what the system actually achieves.
   2. Implement backups per data class:
        - relational: periodic full plus continuous write-ahead archiving so a
          point-in-time restore is possible;
        - object store: versioned with the object lock from P02-02 preserved
          in the backup, because a restore that loses immutability loses the
          control;
        - audit store: backed up in a way that preserves the digest chain, so
          post-restore verification still works;
        - queues and outbox: the outbox is in the relational backup by
          construction (P03-03), which is one of the reasons the source
          requires a transactional outbox;
        - vector indexes: either backed up or reproducibly rebuildable from
          source corpora, with the rebuild time counted in the RTO;
        - configuration and policy bundles: versioned in the repository and
          deployable.
   3. Encrypt backups at rest and in transit with keys managed separately from
      the primary environment, and verify that a backup cannot be decrypted
      with only primary-environment access.
   4. Implement automated backup verification: every backup is test-restored
      or at minimum structurally validated on a schedule, and a failed
      verification raises an alert. A backup whose restorability is unknown is
      reported as unverified.
   5. Execute the full drill into a clean, isolated recovery environment:
        - record the start time;
        - restore every data class;
        - bring up the services;
        - run the smoke suite and the integrity checks;
        - record the end time and compute actual RTO;
        - determine the last recoverable transaction and compute actual RPO.
   6. Verify integrity after restore, which is the part most drills skip:
        - the audit digest chain verifies end to end (P01-05);
        - locked artifacts are still immutable and their digests match
          (P02-02);
        - the financial ledger balances and its invariants hold (P08-04);
        - idempotency keys and outbox state are consistent, so a post-restore
          replay does not double-apply a side effect — test this explicitly by
          replaying a window of events after restore and asserting no duplicate
          effect;
        - evidence manifests verify (P02-03).
   7. Drill the provider failover path from P04-04 as part of this exercise,
      since sheet 57 row 8 names failover drills alongside restore.
   8. Record the drill as release-gate evidence at docs/evidence/G-08-dr-drill/
      with the environment, the deployment SHA, the owner, the timestamps, the
      measured RTO and RPO, the smoke and integrity results, and every
      deviation from the procedure.
   9. Update the evidence ledger entry honestly: a drill that restored but
      failed an integrity check is a FAIL, not a PASS with a caveat.
  10. Tests and drill:
        a. the full restore drill with measured RTO and RPO;
        b. post-restore audit chain verification;
        c. post-restore artifact immutability and digest verification;
        d. post-restore ledger balance and invariant verification;
        e. post-restore event replay -> no duplicate side effect;
        f. a backup cannot be decrypted with primary-environment access alone;
        g. scheduled backup verification raises an alert on an injected
           corrupt backup;
        h. the provider failover drill.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - documented proposed RTO and RPO per data class, marked as needing
     ratification
   - per-class backups including lock-preserving object backup and
     chain-preserving audit backup
   - separately keyed backup encryption
   - scheduled automated backup verification with alerting
   - the executed restore drill with measured RTO and RPO
   - the five post-restore integrity verifications
   - the provider failover drill
   - docs/evidence/G-08-dr-drill/ as release-gate evidence
   - an honestly recorded evidence ledger entry
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the drill timeline with the measured RTO and RPO as numbers, and
     state them against the proposed targets.
   - Paste all five post-restore integrity verification outputs.
   - Paste the event replay result proving no duplicate side effect.
   - Paste the backup decryption failure from case f.
   - Acceptance criterion: a full restore succeeds, every integrity property
     survives it, a post-restore replay causes no duplicate effect, and RTO and
     RPO are measured rather than estimated.

G. COMPLETION CONTRACT
   Definition of Done: backups implemented and verified, a full drill executed
   with measured objectives, every integrity property verified after restore,
   evidence recorded.
   Evidence to report: the drill timeline with measured numbers, the five
   integrity outputs, the replay result, the evidence directory path.
   Remaining blockers: RTO and RPO targets need owner ratification. If any data
   class could not be restored in the available environment, say which and why
   — and then the gate is not PASS.
   Next prompt: P11-01. PHASE-10 exit requires nine drilled alerts, the
   six-level trace walk, a measured DR drill, and a clean reconciliation run.
```

**المخرجات المتوقعة:** نسخ احتياطي بحسب فئة البيانات، تدريب استرجاع بأرقام مقيسة، تحقق سلامة بعد الاسترجاع.
**التحقق المطلوب:** `RTO`/`RPO` مقيسان لا مُقدَّران؛ سلسلة التدقيق وثبات المخرجات تصمد للاسترجاع؛ لا أثر مزدوج عند الإعادة.
**الاعتمادية التالية:** `P11-01`.

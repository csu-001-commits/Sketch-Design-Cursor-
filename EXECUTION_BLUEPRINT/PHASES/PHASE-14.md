# PHASE-14 — التقييم والتعلم وبوابات الإصدار

<!-- phasemeta
id: PHASE-14
depends_on: [PHASE-09, PHASE-10, PHASE-11, PHASE-13]
criticality: P0
-->

## الغرض من المرحلة

هذه المرحلة تُنفّذ `ADR-008`، أهم قرار حوكمي في المصدر: «وجود سجل لا يثبت
التنفيذ؛ يلزم build + passed test + evidence + approver»، وسببه: «منع الجاهزية
الزائفة».

المصدر يحتوي أربع مجموعات بوابات منفصلة — الورقة 38 (`G-01..G-10`)، والورقة 42
(`G01..G12`)، والورقة 54 (`G01..G12`)، والورقة 76 (`G01..G10`) — وكلها بحالة
`Open` أو `UNVERIFIED` أو `NOT RUN` أو `NOT VERIFIED`. وهذه المرحلة تحوّلها إلى
بوابات مفروضة بالكود لا جداول.

## شروط الدخول

- وصول `PHASE-09`, `PHASE-10`, `PHASE-11`, `PHASE-13` إلى شروط خروجها.

## شروط الخروج

- تنفيذ الاختبارات الثلاثة عشر `AT-*` كلها بدليل مُرفق.
- بوابة الانحدار تحجب مرشّحاً تحت العتبة.
- دفتر الأدلة مُعبَّأ من تشغيلات قابلة للإعادة.
- لا أثر يدّعي `READY` بلا مرجع بناء واختبار ناجح ودليل ومعتمد.

## المتطلبات المغطاة في هذه المرحلة

`ADR-008`, `REQ-GOV-04`, `REQ-GOV-07`, `REQ-GOV-08`, `REQ-EVL-01`..`REQ-EVL-10`,
`REQ-OBS-06`, `REQ-OBS-07`, `REQ-KNW-07`, `REQ-GW-18`, `REQ-OPN-02`, `REQ-OPN-07`

---

## الأوامر التنفيذية

### P14-01 — المجموعات الذهبية ومحرك التقييم

<!-- meta
id: P14-01
phase: PHASE-14
title_en: Golden datasets and the evaluation harness
prereq: [P13-04]
requirements: [REQ-KNW-07, REQ-EVL-04, REQ-OBS-06]
-->

**ماذا سينفذ هذا الأمر؟** يبني المجموعات الذهبية بحقوقها وتقسيمها وضبط تسريبها،
ومحرك تقييم يُنتج نتائج قابلة للإعادة ومُصدَرة.

**لماذا نحتاجه؟** الورقة 24 الصف 11 تحدد `RAG-GOLDEN` بـ«consent/right/de-id/
label/split» و«Evaluation only؛ leakage control». والورقة 05 الصف 38 (`EVAL-01`)
شروط إيقافها: «حق غائب؛ contamination؛ regression». مجموعة ذهبية ملوَّثة تُنتج
أرقاماً مطمئنة وكاذبة.

**ما المتطلبات السابقة؟** `P13-04`.

**ما النتيجة المتوقعة؟** مجموعات ذهبية موثقة الحقوق ومعزولة، ومحرك تقييم
بإصدارات.

**كيف نتحقق من نجاحه؟** اختبار تلوث يكشف تسرّب عنصر من مجموعة التدريب أو الإنتاج
إلى مجموعة التقييم؛ وعنصر بلا حق استخدام يُرفض.

```text
TASK P14-01 — Golden datasets and the evaluation harness

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P14-01
   Phase: PHASE-14 (Evaluation, learning and release governance)
   Prerequisites: P13-04
   Requirements covered: REQ-KNW-07, REQ-EVL-04, REQ-OBS-06

B. OBJECTIVE
   Build the golden evaluation datasets with recorded rights, consent,
   de-identification, labels and splits under leakage control, and an
   evaluation harness that produces versioned, reproducible results.

   Why this is necessary: sheet 24 row 11 defines RAG-GOLDEN as evaluation-only
   with leakage control and requires consent, usage right, de-identification,
   labels and splits. Sheet 05 row 38 (EVAL-01) names its stop conditions as an
   absent right, contamination and regression, and states "no training without
   a right". A contaminated golden set produces reassuring numbers that are
   false, which is worse than having no numbers.

   SCOPE BOUNDARY: datasets and the harness. The specific model benchmarks are
   P14-02. The regression gate is P14-03.

C. CONTEXT
   Required inputs:
     - the RAG-GOLDEN isolation from P06-02 step 5 (unreachable from
       production credentials)
     - the source rights register from P06-01, which governs whether a document
       may be used at all
     - sheet 17 rows 2-12, the eleven evaluation metrics with their definitions,
       segmentations, cadences and owners
     - sheet 17 rows 17-26, the ten-stage learning cycle: capture, review,
       label, sample, measure, segment, investigate, improve, validate, release
       and monitor
     - sheet 64 rows 2-8, the seven evaluation dimensions, all NOT TESTED

D. EXECUTION INSTRUCTIONS
   1. Implement the dataset entity with the five metadata requirements from
      sheet 24 row 11 as mandatory fields: consent reference, usage right
      reference, de-identification status and method, labels, and split
      assignment (train, development, test, holdout). An item missing any of
      them cannot be added.
   2. Enforce the rights precondition: an item derived from a customer document
      requires both the customer's consent for evaluation use and a source
      right permitting it. SRC-PROJECT records "no training by default" (sheet
      25 row 4), so evaluation use is a distinct, separately consented purpose
      — not an implied extension of service delivery. Implement it as a named
      purpose in the P11-01 RoPA.
   3. Implement de-identification with a recorded method and a verification
      step: identifiers removed or pseudonymized, and a check that the
      de-identified item does not still contain obvious identifiers. Record the
      residual risk.
   4. Implement split assignment as immutable per item, and implement
      contamination detection as an active, automated check:
        - an item in the evaluation split must not appear in any training or
          fine-tuning set;
        - an item must not appear in a production retrieval corpus in a form
          that would let a model retrieve its own answer;
        - detect near-duplicates, not only exact matches, using a content
          digest plus a similarity check, because a reformatted copy is still
          contamination;
        - a detected contamination invalidates the affected results and raises
          an alert rather than being quietly excluded.
   5. Implement the labelled ground truth for the engineering domain, which is
      the part that cannot be automated: for each golden case, the expected
      findings with their severity and discipline, recorded by a qualified
      reviewer, with the labeller identity and date. Sheet 64 row 2 requires a
      "golden project corpus, blind reviewer". Implement blind labelling —
      the labeller does not see the model's output.
   6. Implement the evaluation harness:
        - an evaluation run references the dataset version, the dataset split,
          the agent version, the model version, the prompt version, the policy
          version and the harness version;
        - results are stored per case and per aggregate, with the full
          per-case record retained so an aggregate can always be re-derived;
        - a run is reproducible: the same references produce the same result,
          except where provider non-determinism applies, in which case the run
          records the sampling parameters and repeats enough times to report a
          variance rather than a single number;
        - runs are stored as EvaluationRun per sheet 28 row 21 with the control
          "no client leakage".
   7. Implement the metric computations from sheet 17 with their exact
      definitions:
        - finding precision: accepted or substantively retained divided by
          reviewed;
        - finding recall: important issues detected divided by what the
          reviewer found, which requires the double-review sample sheet 17
          row 3 names;
        - citation validity: the citation accurately supports the claim, which
          per P06-03 requires human labelling and must not be computed from
          resolution alone;
        - reviewer override rate, segmented by reason, agent and version, with
          sheet 17 row 5's explicit note that it is for diagnosis, not
          punishment;
        - inter-reviewer agreement from the double-review sample;
        - escalation accuracy for P3 cases.
      Implement each with its segmentation dimensions, because an aggregate
      without segmentation hides the failure.
   8. Implement the ten-stage learning cycle as a traceable process with
      artifacts at each stage, wired to the real data: capture from the traces
      (P10-01), review from the decisions (P07-04), label here, stratified
      sampling including the silent cases sheet 17 row 20 names, measure,
      segment, investigate, improve in a controlled branch, validate, and
      release with canary and rollback.
   9. Implement the stratified sampling requirement from sheet 17 row 20
      explicitly: the sample covers accepted, rejected and — critically —
      silent cases, meaning cases where the system produced nothing. A sample
      drawn only from produced findings cannot measure recall.
  10. Tests:
        a. an item without a consent reference -> rejected;
        b. an item from a source whose right forbids evaluation use -> rejected;
        c. a de-identified item still containing an obvious identifier ->
           flagged;
        d. an exact duplicate across splits -> contamination detected;
        e. a reformatted near-duplicate across splits -> contamination
           detected;
        f. a golden case present in a production retrieval corpus ->
           contamination detected, affected results invalidated, alert raised;
        g. an evaluation run with the same references -> reproducible, or
           reports variance with its sampling parameters;
        h. an aggregate metric can be re-derived from the retained per-case
           records;
        i. metric segmentation is present on every metric;
        j. a sample without silent cases -> rejected by the stratified sampler;
        k. a production credential cannot read the evaluation dataset.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the dataset entity with five mandatory metadata requirements
   - rights and consent preconditions with evaluation as a named RoPA purpose
   - de-identification with method recording and verification
   - immutable splits and active exact plus near-duplicate contamination
     detection
   - blind qualified-reviewer ground-truth labelling
   - the versioned, reproducible evaluation harness with per-case retention
   - the six metric computations with their exact definitions and segmentations
   - the ten-stage learning cycle wired to real data
   - stratified sampling including silent cases
   - tests/eval/dataset-*.* covering cases a through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eleven tests.
   - Paste the near-duplicate contamination detection from case e.
   - Paste one metric computation with its segmentation and its per-case
     derivation.
   - Report the dataset's real size, how many cases have qualified-reviewer
     labels, and how many have full rights clearance. Report zeros honestly.
   - Acceptance criterion: no item enters without rights and consent, no
     contamination goes undetected, and no metric exists without its
     segmentation and its re-derivable basis.

G. COMPLETION CONTRACT
   Definition of Done: datasets rights-cleared and contamination-checked, the
   harness reproducible, metrics computed per the source's definitions, the
   learning cycle wired.
   Evidence to report: the eleven test outputs, the contamination detection,
   the metric derivation, the honest dataset size report.
   Remaining blockers: qualified-reviewer labelling is human capacity the owner
   must supply, and the golden corpus needs real projects with evaluation
   consent. Report both; a harness with an empty dataset measures nothing.
   Next prompt: P14-02.
```

**المخرجات المتوقعة:** مجموعات ذهبية موثقة الحقوق، كشف تلوث دقيق، محرك تقييم بإصدارات، مقاييس مُقسَّمة.
**التحقق المطلوب:** لا عنصر بلا حق وموافقة؛ لا تلوث غير مكتشَف؛ المعاينة تتضمن الحالات الصامتة.
**الاعتمادية التالية:** `P14-02`.

---

### P14-02 — قياس النماذج بأبعاده السبعة

<!-- meta
id: P14-02
phase: PHASE-14
title_en: Model benchmarking across the seven evaluation dimensions
prereq: [P14-01]
requirements: [REQ-EVL-04, REQ-GW-18, REQ-GW-13, REQ-OPN-07]
-->

**ماذا سينفذ هذا الأمر؟** يُشغّل القياس الفعلي للنماذج على الأبعاد السبعة في
الورقة 64، ويُعبّئ `quality_score` لكل مهمة في سجل النماذج.

**لماذا نحتاجه؟** الورقة 77 الصف 3 تعتمد: «قياس 2 نماذج استدلال متقدمة + 2
سريعة + 2 للرؤية»، وترفض «افتراض أن نموذجاً محدداً هو الأفضل بلا تقييم». والورقة
57 الصف 7 (`A06`) تحدد الفجوة: «أساس النموذج المجاني/المحلي يفتقر إلى إثبات
موثوقية للمؤسسات». وبدون هذا القياس، راوتر `P04-03` يبقى عائداً بـ
`NO_ELIGIBLE_ROUTE`.

**ما المتطلبات السابقة؟** `P14-01`.

**ما النتيجة المتوقعة؟** تقارير قياس لكل بُعد ولكل صنف مهمة، و`quality_score`
مُعبَّأ بمصدره.

**كيف نتحقق من نجاحه؟** كل درجة في السجل لها مرجع تشغيل تقييم وتاريخ ومجموعة
بيانات؛ ولا درجة بلا مصدر.

```text
TASK P14-02 — Model benchmarking across the seven evaluation dimensions

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P14-02
   Phase: PHASE-14
   Prerequisites: P14-01
   Requirements covered: REQ-EVL-04, REQ-GW-13, REQ-GW-18, REQ-OPN-07

B. OBJECTIVE
   Run the actual benchmarks across the seven evaluation dimensions, for the
   candidate model set the source prescribes, and populate the per-task
   quality_score in the model registry with its full provenance.

   Why this is necessary: sheet 77 row 3 adopts benchmarking two premium
   reasoning, two fast and two vision candidates, and rejects assuming a
   specific model is best without evaluation. Sheet 57 row 7 (A06) records that
   a free or local model baseline lacks enterprise reliability proof, requiring
   paid and direct providers be benchmarked with a golden-set report as
   evidence. Sheet 64's seven dimensions are all NOT TESTED. Until this runs,
   the P04-03 router correctly refuses quality-first routing.

   SCOPE BOUNDARY: benchmarking and score population. Do not change routing
   logic. Respect the budget controller — benchmarking spends real money, so
   get an explicit budget authorization before running paid providers.

C. CONTEXT
   Required inputs, sheet 64 rows 2-8, each as metric / test method / release
   threshold / evidence / status:
     Engineering correctness / golden project corpus, blind reviewer / set by
       the engineering lead / versioned evaluation / NOT TESTED
     Grounding / citation checks and hallucination tests / no unsupported
       safety claims / evidence linked / NOT TESTED
     Arabic quality / Saudi Arabic engineering terminology / reviewer
       acceptance / bilingual eval / NOT TESTED
     Latency / P50 and P95 end to end under load / measured SLO / load test /
       NOT TESTED
     Reliability / 429, timeout and outage chaos / successful safe fallback /
       fault injection / NOT TESTED
     Cost / tokens and SAR per deliverable / budget per task / ledger
       reconciliation / NOT TESTED
     Privacy / PII leakage, prompt injection, exfiltration / zero critical
       leaks / security eval / NOT TESTED
   And sheet 71's eight task classes, since scores are per task class and a
   single global score is prohibited by sheet 72 row 6.

D. EXECUTION INSTRUCTIONS
   1. Obtain and record an explicit budget authorization for the benchmark run,
      with a hard cap enforced through the P04-06 budget controller. Report the
      actual spend afterwards. Do not start a paid benchmark without it.
   2. Define the candidate set per sheet 77 row 3: two premium reasoning, two
      fast and two vision candidates, chosen from providers that passed the
      P11-04 residency assessment and have a DPA. Record which candidates you
      could not include and why — a model with no DPA is not a candidate, and
      sheet 57 row 7 specifically requires benchmarking paid and direct
      providers rather than relying on a free baseline.
   3. Benchmark engineering correctness per task class against the golden
      corpus with blind reviewer scoring: the reviewer sees the output without
      knowing which model produced it, and scores against the labelled ground
      truth. Report precision and recall per class with confidence intervals
      given the sample size — and if the sample is too small for a meaningful
      interval, say so rather than reporting a point estimate as fact.
   4. Benchmark grounding with citation checks and hallucination probes: cases
      where the correct answer is "the evidence does not support a conclusion".
      The source's threshold is "no unsupported safety claims", which is an
      absolute — a single unsupported safety claim is a failure for that
      candidate, not a percentage.
   5. Benchmark Arabic quality against Saudi Arabic engineering terminology
      with reviewer acceptance, bilingually. Until this runs, the Arabic
      capability flag from P04-02 stays UNVERIFIED. Report per-candidate
      acceptance and the specific terminology failures, since those are
      actionable.
   6. Benchmark latency with P50 and P95 end to end under load, which means
      through the real gateway with real context assembly, not a bare provider
      call. Record the load profile. Sheet 51 row 7 requires p95 at peak
      concurrent load, so run a concurrency profile, not a serial loop.
   7. Benchmark reliability by reusing the P04-04 chaos harness per candidate:
      429, timeout and outage, measuring whether the safe fallback succeeded.
   8. Benchmark cost as tokens and SAR per completed deliverable, not per call,
      reconciled against the P04-06 ledger and the provider's own billing.
      Where a rate is absent, report tokens and mark cost UNPRICED.
   9. Benchmark privacy by running the P11-04 red-team categories per
      candidate: PII leakage, prompt injection susceptibility and exfiltration.
      The threshold is zero critical leaks, again an absolute.
  10. Populate quality_score in the model registry per task class, each entry
      carrying the evaluation run reference, the dataset version, the
      measurement date and the sample size. A dimension you could not measure
      stays empty — never estimated, never interpolated from a similar model,
      never taken from a vendor's published benchmark.
  11. Produce the benchmark report: per candidate, per dimension, per task
      class, with the method, the sample size, the result, the uncertainty and
      the conclusion. Include an explicit recommendation per task class and the
      reasoning, since sheet 77 row 4 requires auditable decisions.
  12. Update the release thresholds where the source says they are owner-set
      ("set by the engineering lead", "reviewer acceptance", "measured SLO",
      "budget per task") by proposing values derived from the measurements and
      flagging them for ratification. Do not set them unilaterally and do not
      leave them at a placeholder.
  13. Tests and runs:
        a. the benchmark run completes within its authorized budget; report the
           actual spend;
        b. engineering correctness per class per candidate with sample sizes;
        c. a candidate producing one unsupported safety claim -> recorded as a
           grounding failure, not an averaged-away percentage;
        d. Arabic quality results with the specific terminology failures;
        e. latency under a concurrency profile, p50 and p95;
        f. reliability per candidate from the chaos harness;
        g. cost per deliverable, reconciled, with UNPRICED where applicable;
        h. privacy results per candidate against the red-team categories;
        i. every populated quality_score carries its run reference, dataset
           version, date and sample size; a test asserts no score exists
           without them;
        j. an attempt to write a score from a vendor-published figure ->
           rejected.
  14. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the recorded budget authorization and the actual spend
   - the candidate set with exclusions and their reasons
   - seven benchmark suites with their methods and results
   - per-task-class quality_score population with full provenance
   - docs/evidence/G02-model-benchmarks/ with the full report
   - proposed release thresholds flagged for ratification
   - tests/eval/benchmark-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the per-dimension, per-candidate result tables with sample sizes.
   - Paste the actual spend against the authorized cap.
   - Paste the provenance assertion from case i.
   - State which dimensions you could not measure and why, and confirm those
     scores remain empty.
   - Acceptance criterion: no score exists without a real measurement and its
     provenance, and absolute thresholds are treated as absolute.

G. COMPLETION CONTRACT
   Definition of Done: benchmarks run within budget, scores populated with
   provenance, the report produced, thresholds proposed for ratification.
   Evidence to report: the result tables, the spend, the provenance assertion,
   the unmeasured list.
   Remaining blockers: candidates excluded for want of a DPA are owner-owned
   procurement; release thresholds need the engineering lead's ratification
   (OD-04). This prompt is what unblocks the P04-03 router's quality-first
   path — state which task classes now have a usable floor and which do not.
   Next prompt: P14-03.
```

**المخرجات المتوقعة:** سبع مجموعات قياس، `quality_score` لكل صنف مهمة بمصدريته، تقرير مُفصَّل.
**التحقق المطلوب:** لا درجة بلا قياس حقيقي ومصدرية؛ العتبات المطلقة تُعامَل كمطلقة.
**الاعتمادية التالية:** `P14-03`.

---

### P14-03 — بوابة الانحدار الحاجزة

<!-- meta
id: P14-03
phase: PHASE-14
title_en: The blocking regression gate
prereq: [P14-02]
requirements: [REQ-EVL-03, REQ-AGT-06, REQ-OBS-06, REQ-OPN-02]
-->

**ماذا سينفذ هذا الأمر؟** يبني بوابة انحدار تحجب الإصدار عندما يهبط مرشّح تحت
العتبة، وتربط النشر بالرجوع.

**لماذا نحتاجه؟** `AT-EVAL-001` (الورقة 16 الصف 12) يحدد السيناريو: «مرشّح تحت
العتبة» والمتوقع: «الإصدار محجوب والرجوع جاهز». والورقة 15 الصف 12 (`CTRL-011`)
دليله: «العتبة تحجب الإصدار». والورقة 05 الصف 38 تمنع «الترقية عند الهبوط».

**ما المتطلبات السابقة؟** `P14-02`.

**ما النتيجة المتوقعة؟** بوابة مفروضة في مسار النشر، وحجب فعلي، ورجوع جاهز
ومُثبت.

**كيف نتحقق من نجاحه؟** `AT-EVAL-001` ناجح؛ ومحاولة نشر مرشّح هابط تُرفض فعلياً
لا تُسجَّل تحذيراً.

```text
TASK P14-03 — The blocking regression gate

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P14-03
   Phase: PHASE-14
   Prerequisites: P14-02
   Requirements covered: REQ-EVL-03, REQ-AGT-06, REQ-OBS-06, REQ-OPN-02

B. OBJECTIVE
   Implement a regression gate that actually blocks a release when a candidate
   falls below threshold, wired into the deployment path, with rollback
   prepared and proven.

   Why this is necessary: AT-EVAL-001 (sheet 16 row 12) expects "release
   blocked and rollback ready". Sheet 15 row 12 (CTRL-011) requires the
   evidence "threshold blocks release". Sheet 05 row 38 forbids promotion on a
   decline. Sheet 73 row 4's action for a breached quality floor is to roll
   back routing. A gate that logs a warning and proceeds is not a gate.

   SCOPE BOUNDARY: the gate and its deployment integration. Do not change the
   benchmark methodology. Do not add an override that bypasses the gate without
   the controls described below.

C. CONTEXT
   Required inputs:
     - the harness and metrics from P14-01, the scores from P14-02
     - the AgentVersion publication gate from P05-02 step 3, which this prompt
       completes
     - the model policy rollout from P04-03 and the deployment path from P05-02
     - sheet 17 rows 2-7, which mark finding precision, citation validity and
       escalation accuracy as release gates and finding recall as the P3 gate
     - sheet 30 rows 3-5, whose targets are TBD pending a baseline

D. EXECUTION INSTRUCTIONS
   1. Implement the gate as a required check on every release path: an agent
      version publication, a prompt change, a model policy change and a routing
      change. The gate is evaluated by the deployment command, and a BLOCK
      result prevents the deployment rather than annotating it.
   2. Implement the comparison properly, because this is where regression gates
      usually fail:
        - compare candidate against the current production baseline on the same
          dataset version and the same split, not against a historical number
          measured on a different dataset;
        - compare per segment, not only on the aggregate, because an aggregate
          can hold while a discipline or a severity band collapses. Sheet 17
          requires segmentation by workflow, discipline, version and P for
          precision and by workflow, discipline and severity for recall;
        - account for sample-size uncertainty: a difference within the noise
          band is not an improvement and must not be reported as one. Where the
          sample is too small to distinguish, the gate returns INSUFFICIENT
          EVIDENCE, which blocks — it does not pass.
   3. Implement absolute floors separately from relative regression: the source
      sets some thresholds as absolutes, notably no unsupported safety claims
      and zero critical privacy leaks (sheet 64 rows 3 and 8), and zero
      cross-tenant incidents (sheet 30 row 2). An absolute violation blocks
      regardless of any improvement elsewhere.
   4. Implement threshold configuration with honest states, since sheet 30
      marks most targets TBD: a metric with no ratified threshold cannot pass
      the gate on that metric. The gate reports THRESHOLD_NOT_SET and blocks
      the release paths that depend on it. Do not substitute a default
      threshold to make the gate green — that reintroduces exactly the false
      readiness ADR-008 exists to prevent.
   5. Implement rollback readiness as a precondition the gate checks, not an
      afterthought: before a deployment proceeds, the gate verifies that the
      previous version is retained, that the rollback path has been exercised
      for this artifact type, and that a rollback token or switch exists.
      Sheet 16 row 12's expectation is "release blocked and rollback ready",
      so readiness is part of the gate.
   6. Implement the canary-and-monitor stage per sheet 17 row 26: after a
      passing gate, deployment proceeds via canary with the quality metrics
      monitored, and an automatic rollback triggers on a floor breach during
      canary. Wire it to the P10-02 model quality dashboard and its alert.
   7. Implement the override with strict controls, because an unoverridable
      gate will eventually be worked around in a worse way: an override
      requires dual approval by named roles, a recorded justification, a
      mandatory expiry, a canary-only scope, its own audit stream, and an entry
      in the open risks register. An override can never clear an absolute floor
      violation. Report every override in the monthly governance review.
   8. Implement drift monitoring per sheet 17 row 26: production quality
      metrics are compared against the evaluation baseline continuously, and a
      divergence beyond tolerance raises an alert, because a model that passed
      at release can degrade.
   9. Tests — AT-EVAL-001 plus the gate suite:
        a. AT-EVAL-001: a candidate below threshold -> release BLOCKED, and
           rollback readiness confirmed. Paste the block and the readiness
           check;
        b. an aggregate that holds while one discipline segment regresses ->
           BLOCKED on the segment;
        c. a difference inside the noise band -> not treated as an improvement;
           INSUFFICIENT EVIDENCE blocks;
        d. an unsupported safety claim in the candidate -> BLOCKED regardless
           of aggregate improvement;
        e. a metric with no ratified threshold -> THRESHOLD_NOT_SET, release
           blocked, no default applied;
        f. a deployment attempted without a retained previous version ->
           BLOCKED on rollback readiness;
        g. a canary breaching a floor -> automatic rollback, alert raised;
        h. an override without dual approval -> refused; with it -> permitted,
           expiring, canary-scoped, audited, and recorded in the risks
           register;
        i. an override attempting to clear an absolute floor violation ->
           refused;
        j. production drift beyond tolerance -> alert raised.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the gate as a required, blocking check on four release paths
   - same-dataset, per-segment, uncertainty-aware comparison with INSUFFICIENT
     EVIDENCE semantics
   - absolute floors enforced independently of relative regression
   - THRESHOLD_NOT_SET blocking rather than defaulting
   - rollback readiness as a gate precondition
   - canary with automatic rollback on a floor breach
   - the tightly controlled, expiring, auditable override that cannot clear an
     absolute
   - production drift monitoring with alerting
   - tests/eval/at-eval-001.* plus cases b through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-EVAL-001 output showing the block and the rollback readiness
     confirmation.
   - Paste case b showing the segment-level block despite a holding aggregate.
   - Paste case e showing THRESHOLD_NOT_SET blocking.
   - Paste case i showing an override refused against an absolute floor.
   - Acceptance criterion: a declining candidate cannot be released, an
     unratified threshold blocks rather than defaults, and no override clears
     an absolute.

G. COMPLETION CONTRACT
   Definition of Done: the gate blocking on all four release paths, segment and
   uncertainty aware, absolutes inviolable, rollback verified, drift monitored.
   Evidence to report: AT-EVAL-001 output, the ten test results, the override
   control demonstration.
   Remaining blockers: most thresholds remain unratified (OD-04), so most
   release paths are legitimately blocked. Report exactly which paths are open
   and which are blocked, and why. A fully blocked gate at this stage is the
   correct and honest state.
   Next prompt: P14-04.
```

**المخرجات المتوقعة:** بوابة حاجزة على أربعة مسارات، مقارنة بالقطاعات وبعدم اليقين، عتبات مطلقة، canary برجوع آلي.
**التحقق المطلوب:** `AT-EVAL-001` ناجح؛ عتبة غير مُصادَق عليها تحجب لا تفترض؛ لا تجاوز لعتبة مطلقة.
**الاعتمادية التالية:** `P14-04`.

---

### P14-04 — دفتر الأدلة وفرض بوابات الإصدار

<!-- meta
id: P14-04
phase: PHASE-14
title_en: Evidence ledger and enforced release gates
prereq: [P14-03]
requirements: [ADR-008, REQ-GOV-04, REQ-GOV-07, REQ-GOV-08, REQ-EVL-01, REQ-EVL-02, REQ-EVL-05, REQ-EVL-06, REQ-EVL-07, REQ-EVL-08, REQ-EVL-09, REQ-EVL-10]
-->

**ماذا سينفذ هذا الأمر؟** يبني دفتر الأدلة ويفرض مجموعات البوابات الأربع كبوابات
برمجية، ويُنفّذ `ADR-008` بالكود: لا `READY` بلا مرجع بناء واختبار ناجح ودليل
ومعتمد.

**لماذا نحتاجه؟** الورقة 42 تحتوي اثني عشر بنداً كلها `NOT RUN`، والورقة 40
الصف 18 تحسب `Controls blocked/unverified` = 8 من 8. والورقة 15 الصف 19 تحدد
الشرط: «READY تتطلب build reference وآخر Test Run ناجح وEvidence Link
وapproved_by/at». هذه هي اللحظة التي يتحول فيها دفتر الأدلة من جدول إلى ضابط.

**ما المتطلبات السابقة؟** `P14-03`.

**ما النتيجة المتوقعة؟** دفتر أدلة مُعبَّأ آلياً من تشغيلات حقيقية، وبوابات تحجب
الإصدار فعلاً.

**كيف نتحقق من نجاحه؟** لا بند يصبح `PASS` بلا الأربعة المطلوبة؛ ومحاولة إصدار
مع بوابة `P0` مفتوحة تُرفض.

```text
TASK P14-04 — Evidence ledger and enforced release gates

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P14-04
   Phase: PHASE-14
   Prerequisites: P14-03
   Requirements covered: ADR-008, REQ-GOV-04, REQ-GOV-07, REQ-GOV-08,
                         REQ-EVL-02, REQ-EVL-05, REQ-EVL-06, REQ-EVL-07,
                         REQ-EVL-08, REQ-EVL-09, REQ-EVL-10

B. OBJECTIVE
   Implement the evidence ledger, populate it automatically from real test and
   drill runs, and enforce the source's four distinct gate sets as software
   gates on the release path — making ADR-008 executable.

   Why this is necessary: ADR-008 (sheet 02 row 9) states that a row never
   proves execution, and sheet 15 row 19 defines READY as requiring a build
   reference, the last successful test run, an evidence link and an approver
   with a timestamp. Sheet 42 holds twelve gate rows, all NOT RUN. Sheet 40
   row 18 computes eight of eight controls as blocked or unverified. Sheet 38,
   sheet 54 and sheet 76 hold three further gate sets, all open. Today these
   are spreadsheets; this prompt makes them a mechanism.

   SCOPE BOUNDARY: the ledger, the gate enforcement and the readiness
   vocabulary. Do not mark a gate PASS on the owner's behalf; approval is an
   owner action the system records.

C. CONTEXT
   Required inputs — the four gate sets, kept distinct because the source keeps
   them distinct:
     sheet 38 (G-01..G-10, production readiness): API security, queue
       durability, fallback execution, side-effect safety, credits
       persistence, HITL compliance, knowledge provenance, operational
       recovery, PDPL and retention, observability — each with a verification,
       a pass criterion, an owner, required evidence, and the decision "Block
       release"; all Open
     sheet 42 (G01..G12, evidence ledger): villa E2E, tenant isolation, RBAC
       escalation, API schema contract, event replay and idempotency, agent
       fallback and timeout, data migration rollback, audit log integrity,
       secrets and PII leak scan, backup restore and RPO/RTO, load and latency
       SLO, human approval and sign-off — each needing test or proof,
       environment, owner, evidence URL, executed-at and result; all NOT RUN
     sheet 54 (G01..G12, go-live): tenant isolation and RLS, agent
       entitlement, B2B billing and metering, custom domain and SSO, camera
       permissions and PDPL, LiDAR precision disclaimers, concurrent load,
       provider failover, white-label security, engineer sign-off, customer
       portal UX, disaster recovery — eleven are P0 release blockers, one is
       P1; all UNVERIFIED
     sheet 76 (G01..G10, gateway): provider DPA and residency, model benchmark,
       burst and soak load, chaos, tenant isolation including RAG cache traces
       and logs, cost ledger reconciliation, human approval and deterministic
       checks, rollback canary audit and secret rotation, scan consent and
       privacy, dashboards alerts and runbooks; all NOT VERIFIED
   And config/registries/release-gates.json from P00-02, which already holds
   the three sets it imported, plus the sheet 42 ledger.

D. EXECUTION INSTRUCTIONS
   1. Implement the GateRecord entity with the fields sheet 42 and sheet 15
      row 19 jointly require: gate set, gate id, requirement, test or proof
      reference, environment, owner, evidence URI, build reference, deployment
      SHA, last successful test run reference, executed_at, result, approver
      identity, approved_at, blocker notes, and the release-blocker flag.
   2. Enforce the ADR-008 condition in the type system and in storage: a gate
      cannot hold result PASS unless all four of build reference, a passing
      test run reference, an evidence URI and an approver with a timestamp are
      present. Make the invalid combination unrepresentable or rejected by a
      constraint, so it cannot be set by a script, a migration or an
      administrator.
   3. Implement automatic population from real runs: the test and drill
      harnesses from earlier phases write their results into the ledger with
      their evidence paths, build references and timestamps. A gate's technical
      evidence is produced by execution, never typed in. Typed-in evidence is
      permitted only for an inherently manual artifact (a legal assessment, a
      tabletop report), and those entries are marked as manual with their
      author.
   4. Implement the readiness vocabulary and enforce it, per sheet 15 row 19
      and sheet 68: the allowed states are the source's own — DEFINED,
      DESIGNED, SPEC, PLANNED, UNVERIFIED, NOT RUN, NOT VERIFIED, PARTIAL,
      PASS, FAIL. Add a repository-wide scan that fails the build if any
      artifact claims READY, DONE, COMPLETE, VERIFIED or PRODUCTION-READY for a
      control whose gate is not PASS. Sheet 32 row 3 records that removing
      unevidenced READY claims was an approved decision, so this scan
      operationalizes it.
   5. Implement the release gate as a real blocking check: a deployment to a
      production-equivalent environment evaluates every gate flagged as a
      release blocker and refuses when any is not PASS. The refusal lists each
      failing gate, its owner and its missing element. Wire it into the
      deployment path, not into a reporting job.
   6. Keep the four gate sets separate and report them separately, because they
      have different owners and different scopes. Add a cross-set mapping so a
      single piece of evidence can satisfy related gates in different sets
      without being double-counted — for example the tenant isolation test
      serves sheet 38 G-01, sheet 42 G02, sheet 54 G01 and sheet 76 G05, and
      the mapping must make that explicit rather than implying four independent
      proofs.
   7. Implement the executive cockpit recomputation from sheet 40: the counts
      of evidenced versus blocked or unverified controls are computed from the
      ledger, never typed. Sheet 40 row 17 counts VERIFIED and row 18 counts
      UNVERIFIED plus BLOCKED, so implement both as queries. The cockpit must
      show the real number, which at this stage will be low.
   8. Implement the traceability matrix from sheet 37 as a generated artifact:
      requirement to API reference to event reference to acceptance test to
      owner to evidence state to required proof, generated from the registries
      and the ledger so it cannot drift. Sheet 37 row 3 sets the default
      evidence state to "Not verified" unless direct runtime evidence exists —
      implement that default.
   9. Implement the sixteen CTRL controls from sheet 15 as ledger-backed
      records with their priority, required evidence and test id, so each
      control's state is derived from its test's real result.
  10. Implement the approval workflow: an owner approves a gate with step-up
      authentication, and the approval records what evidence they reviewed. An
      approval on a gate whose evidence later changes is invalidated and the
      gate returns to its prior state, because the approval was of specific
      evidence. Add a test.
  11. Run the full gate assessment and produce the honest current state: for
      each of the four sets, every gate with its real result. Expect a large
      majority to be not-PASS, and report that plainly.
  12. Tests:
        a. an attempt to set PASS without a build reference -> rejected; repeat
           for each of the four required elements;
        b. a test harness run populates its gate automatically with its
           evidence path and build reference;
        c. the READY-claim scan fails the build on an injected unevidenced
           READY claim, and passes when removed;
        d. a deployment with an open P0 release-blocker gate -> refused, listing
           the failing gates;
        e. the cross-set mapping shows one tenant isolation proof satisfying
           four gates without claiming four proofs;
        f. the cockpit counts are computed from the ledger and change when a
           gate changes;
        g. the traceability matrix is generated and defaults to Not verified
           without runtime evidence;
        h. an approval is invalidated when its underlying evidence changes;
        i. a manual evidence entry is marked manual with its author.
  13. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the GateRecord entity with the ADR-008 invariant enforced in storage
   - automatic ledger population from the test and drill harnesses
   - the enforced readiness vocabulary and the repository-wide READY-claim scan
   - the blocking release gate wired into the deployment path
   - four separately reported gate sets with an explicit cross-set mapping
   - the ledger-computed executive cockpit
   - the generated sheet 37 traceability matrix with its Not-verified default
   - the sixteen CTRL controls as ledger-backed records
   - the step-up approval workflow with evidence-change invalidation
   - docs/evidence/GATE-ASSESSMENT.md with the honest current state of all
     forty-four gates
   - tests/governance/gates-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the four rejections from case a.
   - Paste the READY-claim scan failing and passing.
   - Paste the deployment refusal from case d with its failing gate list.
   - Paste the gate assessment summary: per set, how many PASS, PARTIAL, FAIL
     and not-run. Report the real numbers.
   - Acceptance criterion: no gate can reach PASS without all four elements, no
     deployment proceeds with an open P0 blocker, and no artifact claims READY
     without an evidenced gate.

G. COMPLETION CONTRACT
   Definition of Done: the ledger enforcing ADR-008 structurally, gates
   blocking deployment, the vocabulary scan in the build, the cockpit and
   matrix generated, the honest assessment published.
   Evidence to report: the rejection outputs, the scan both ways, the
   deployment refusal, the full gate assessment.
   Remaining blockers: every gate awaiting an owner's approval or an
   owner-supplied input (DPAs, a pen test, rate cards, thresholds, devices, a
   real reviewer) is listed with its owner. The expected honest outcome of this
   prompt is a mostly-blocked gate board, which is the point of ADR-008.
   Next prompt: P14-05.
```

**المخرجات المتوقعة:** دفتر أدلة يفرض `ADR-008`، بوابة إصدار حاجزة، مسح يرفض ادعاء `READY`، تقييم صريح لأربع وأربعين بوابة.
**التحقق المطلوب:** لا `PASS` بلا العناصر الأربعة؛ لا نشر مع بوابة `P0` مفتوحة.
**الاعتمادية التالية:** `P14-05`.

---

### P14-05 — دورة التعلم وحكومة الإصدار المستمرة

<!-- meta
id: P14-05
phase: PHASE-14
title_en: Continuous learning loop and ongoing release governance
prereq: [P14-04]
requirements: [REQ-OBS-06, REQ-OBS-07, REQ-REV-07, REQ-EVL-05, REQ-OPN-02]
-->

**ماذا سينفذ هذا الأمر؟** يُشغّل دورة التعلم العشرية في الورقة 17 كعملية دورية
حقيقية، ويثبّت حكومة الإصدار المستمرة بمراجعات دورية ومالكين.

**لماذا نحتاجه؟** الورقة 17 تحدد لكل مقياس تكراراً ومالكاً: أسبوعي، شهري، يومي،
فوري. ودورة التعلم بلا جدول ولا مالك تتوقف بعد أول تشغيل. والورقة 13 الصف 11
تضع قيداً مهماً: «لا عقوبة آلية بلا مراجعة».

**ما المتطلبات السابقة؟** `P14-04`.

**ما النتيجة المتوقعة؟** دورة تعلم مجدولة بمخرجات، ومراجعة حكومة دورية، وسجل
مخاطر مفتوحة حيّ.

**كيف نتحقق من نجاحه؟** تشغيل دورة كاملة يُنتج تحسيناً مُقترحاً مُدلَّلاً ومُقاساً؛
ولا عقوبة آلية على مراجع.

```text
TASK P14-05 — Continuous learning loop and ongoing release governance

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P14-05
   Phase: PHASE-14
   Prerequisites: P14-04
   Requirements covered: REQ-OBS-06, REQ-OBS-07, REQ-REV-07, REQ-EVL-05,
                         REQ-OPN-02

B. OBJECTIVE
   Operationalize the ten-stage learning cycle as a scheduled process with real
   owners and artifacts, and establish ongoing release governance: periodic
   metric reviews at the source's cadences, a live open-risks register, and the
   baseline-setting process that converts TBD targets into ratified thresholds.

   Why this is necessary: sheet 17 assigns every metric a cadence and an owner
   — immediate for cross-tenant incidents, daily for workflow failure, time to
   delivery and cost, weekly for precision, citation validity, override and
   escalation accuracy, monthly for recall, agreement and margin. A cycle
   without a schedule and an owner runs once and stops. Sheet 30 row 14 and
   sheet 17 rows 2-3 require thresholds to come from a real baseline, which is
   a process, not a one-off.

   SCOPE BOUNDARY: the recurring process, its artifacts and the governance
   records. Do not change the metric definitions or the gate mechanics.

C. CONTEXT
   Required inputs:
     - sheet 17 rows 2-12 with each metric's cadence, owner and use (release
       gate, P3 gate, investigate, calibration, SLO, SLA, margin,
       Stop-the-line, commercial gate)
     - sheet 17 rows 17-26, the ten stages
     - sheet 13 row 11: no automated penalty for a reviewer without human
       review
     - sheet 11 row 14: reviewer performance metrics reviewed monthly
     - sheet 04's per-role access review cadences: quarterly for
       PLATFORM_OWNER, TENANT_ADMIN and FINANCE, semi-annual for
       PROJECT_MANAGER and PMO_CONTROLLER, at project end for
       EXECUTION_ENGINEER, before every assignment for QUALIFIED_REVIEWER,
       monthly for SUPPORT_L2, 90-day rotation for API_CLIENT
     - the ledger and gates from P14-04

D. EXECUTION INSTRUCTIONS
   1. Implement the metric review schedule as real scheduled jobs at the
      source's cadences, each producing a dated review artifact naming the
      metric, its value, its segments, its trend, its owner, the findings and
      the actions with due dates. An unowned action is not accepted by the
      artifact.
   2. Implement the immediate-cadence path for cross-tenant incidents with the
      Stop-the-line action sheet 30 row 2 specifies: a confirmed incident halts
      the affected release path and raises an incident, rather than waiting for
      a weekly review.
   3. Implement the baseline-setting process that resolves OD-04: once enough
      real volume exists, compute the distribution of each TBD metric, propose
      a threshold with its statistical basis, present it for ratification, and
      record the ratified value with its approver and date. Until ratified, the
      P14-03 gate continues to block on THRESHOLD_NOT_SET. Implement the
      proposal generation, not the ratification.
   4. Implement the double-review sampling programme that recall and
      inter-reviewer agreement require (sheet 17 rows 3 and 6): a scheduled
      sample of completed reviews is independently re-reviewed, and the results
      feed both metrics. Without this programme, recall is unmeasurable, so
      make it a first-class scheduled process with a sampling rate and a
      capacity cost the owner can see.
   5. Implement reviewer performance review per sheet 11 row 14 monthly, with
      the sheet 13 row 11 constraint enforced in code: the system surfaces
      metrics and recommendations and cannot itself suspend, downrank or
      penalize a reviewer. Only a human decision recorded by the review
      committee changes a reviewer's status. Add a test asserting no automated
      path changes approval_status.
   6. Implement the access review cycles per sheet 04's per-role cadences, each
      producing a review artifact listing the role, its holders, their
      entitlements, their recent use and the reviewer's decision, with
      revocations executed as commands through P13-01.
   7. Implement the open-risks register as a live artifact: every unresolved
      open decision, every override granted under P14-03, every gate blocked on
      an owner input, every security finding without a fix, and every PROPOSED
      value awaiting ratification — each with an owner, an impact, a due date
      and a status. Generate it from the system's own state rather than
      maintaining it by hand, so it cannot understate the position.
   8. Implement the investigate stage of the cycle (sheet 17 row 23) as a
      structured attribution: a quality regression is attributed to retrieval,
      extraction, prompt, tool, policy, data or reviewer, with the evidence for
      the attribution. This is what makes an improvement targeted rather than
      speculative.
   9. Implement the improve stage as a controlled branch (sheet 17 row 24): a
      proposed change to a template, a RAG collection or a tool is developed
      against the evaluation harness, measured, and submitted to the P14-03
      gate. No improvement reaches production without passing the gate.
  10. Run one complete cycle end to end on real data and produce its artifacts,
      so the process is demonstrated rather than merely configured.
  11. Implement the governance review package: a periodic report combining the
      gate board, the metric reviews, the open-risks register, the override log
      and the access reviews, for the owner's governance meeting.
  12. Tests and runs:
        a. each scheduled review job runs at its cadence and produces its dated
           artifact; an action without an owner is rejected by the artifact;
        b. a confirmed cross-tenant incident triggers Stop-the-line immediately;
        c. the baseline process produces a threshold proposal with its
           statistical basis and does not self-ratify;
        d. the double-review sampling programme runs and produces recall and
           agreement inputs;
        e. no automated path changes a reviewer's approval_status;
        f. an access review produces its artifact and an executed revocation;
        g. the open-risks register is generated from system state and includes
           every open decision, override, blocked gate and PROPOSED value;
        h. a regression is attributed to a named cause with evidence;
        i. an improvement branch must pass the P14-03 gate to reach production;
        j. one complete cycle produces all ten stage artifacts.
  13. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - scheduled metric reviews at the source's cadences with owned-action
     artifacts
   - the immediate Stop-the-line path for cross-tenant incidents
   - the baseline-setting process generating ratifiable threshold proposals
   - the double-review sampling programme
   - monthly reviewer performance review with no automated penalty
   - per-role access review cycles with executed revocations
   - the generated live open-risks register
   - structured regression attribution
   - the controlled improvement branch gated by P14-03
   - one demonstrated complete cycle with all ten stage artifacts
   - the periodic governance review package
   - tests/governance/learning-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the artifacts from one complete cycle, stage by stage.
   - Paste the generated open-risks register.
   - Paste case e proving no automated reviewer penalty.
   - Paste one threshold proposal with its statistical basis.
   - Acceptance criterion: the cycle runs on a schedule with owned actions, the
     risks register reflects real system state, and no reviewer is penalized
     automatically.

G. COMPLETION CONTRACT
   Definition of Done: the cycle scheduled and demonstrated end to end,
   governance reviews producing real artifacts, the risks register generated,
   threshold proposals ready for ratification.
   Evidence to report: the cycle artifacts, the risks register, the
   no-auto-penalty proof, a threshold proposal.
   Remaining blockers: ratification of thresholds, double-review capacity and
   governance meeting cadence are owner decisions. Report them.
   Next prompt: P15-01. PHASE-14 exit requires all thirteen AT tests executed
   with evidence, the regression gate blocking, the ledger populated from real
   runs, and no artifact claiming READY without an evidenced gate.
```

**المخرجات المتوقعة:** دورة تعلم مجدولة بعشر مراحل، سجل مخاطر مُولَّد، مراجعات وصول، مقترحات عتبات.
**التحقق المطلوب:** لا عقوبة آلية على مراجع؛ سجل المخاطر مُشتق من حالة النظام الحقيقية.
**الاعتمادية التالية:** `P15-01`.

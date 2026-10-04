# PHASE-09 — المسار الذهبي لمراجعة الفيلا

<!-- phasemeta
id: PHASE-09
depends_on: [PHASE-04, PHASE-05, PHASE-07, PHASE-08]
criticality: P0
-->

## الغرض من المرحلة

`WF-VILLA-REVIEW@1.0.0` هو القالب الوحيد في الورقة 07 المُعلَّم `PILOT TARGET`.
والورقة 08 تفصّله إلى عشر مراحل بشروط انتقال وحالات فشل وبوابات بشرية. والورقة 42
تضع `G01 Villa workflow E2E` أول بند في دفتر الأدلة، وحالته `NOT RUN`.

هذه المرحلة لا تبني مكوناً جديداً كبيراً. وظيفتها أن تُوصِّل كل ما بُني في
المراحل 01 إلى 08 في شريحة رأسية واحدة تعمل من طرف إلى طرف على مجموعة مخططات
حقيقية، وتُنتج أول دليل حقيقي على أن المنصة تعمل.

## شروط الدخول

- وصول كل المراحل `PHASE-04`, `PHASE-05`, `PHASE-07`, `PHASE-08` إلى شروط خروجها.

## شروط الخروج

- تشغيل المراحل العشر من طرف إلى طرف على مجموعة مخططات حقيقية بأثر تدقيقي كامل.
- استيفاء بند `G01` في دفتر الأدلة بدليل قابل للإعادة.

## المتطلبات المغطاة في هذه المرحلة

`REQ-WF-08`, `REQ-AGT-08`, `REQ-SVC-01`, `REQ-SVC-02`, `REQ-EVL-07`

## قيد موروث يجب حمله

`OD-05` (حقوق `SBC 2024`) ما زال محجوباً. لذلك مرحلة الامتثال (المرحلة 5 في
الورقة 08) **لا تستطيع** إنتاج ملاحظات مستشهدة بالكود السعودي. المسار يُشغَّل
بملاحظات غير كودية (برنامج، مساحات، حركة، اتساق مستندات) ويُسجَّل القيد صريحاً.
لا يجوز إخفاء هذا القيد ولا تعويضه بمصدر بديل غير مرخَّص.

---

## الأوامر التنفيذية

### P09-01 — الاستقبال والتوجيه وفهم الملفات

<!-- meta
id: P09-01
phase: PHASE-09
title_en: Villa path stages 1-4 — intake, routing, quote and file intelligence
prereq: [P08-04]
requirements: [REQ-WF-08, REQ-AGT-08]
-->

**ماذا سينفذ هذا الأمر؟** يُنفّذ المراحل الأربع الأولى من الورقة 08: الاستقبال
(`CTL-01`)، والتوجيه (`CTL-02`)، والعرض والدفع (`FIN-01/02`)، وفهم الملفات
(`DAT-01`).

**لماذا نحتاجه؟** هذه المراحل تحوّل طلب عميل غير منظم إلى `brief.json` صالح
وتشغيلاً مُثبَّت الإصدار. والورقة 05 الصف 2 تضع قيداً دقيقاً على `CTL-01`: «فصل
تصريح العميل عن الاستنتاج» — أي أن ما قاله العميل وما استنتجه النظام يجب أن
يكونا حقلين مختلفين.

**ما المتطلبات السابقة؟** `P08-04`.

**ما النتيجة المتوقعة؟** مسار يصل إلى حالة `RUNNING` بملفات مفهومة وثقة مُسجَّلة.

**كيف نتحقق من نجاحه؟** `brief` ناقص يُنتج `AWAITING_INFORMATION` بـRFI منظم؛
وملف منخفض الثقة يُوجَّه للتحقق البشري لا يُستهلك بثقة.

```text
TASK P09-01 — Villa path stages 1-4: intake, routing, quote and file intelligence

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P09-01
   Phase: PHASE-09 (Villa golden path end to end)
   Prerequisites: P08-04; PHASE-04, PHASE-05, PHASE-07 and PHASE-08 at their
                  exit conditions
   Requirements covered: REQ-WF-08, REQ-AGT-08

B. OBJECTIVE
   Implement stages 1 through 4 of the WF-VILLA-REVIEW golden path: intake and
   brief construction, template routing, quote and payment, and file
   intelligence — each with the transition condition, failure state and human
   gate the source specifies.

   Why this is necessary: sheet 07 row 2 marks WF-VILLA-REVIEW@1.0.0 as the
   PILOT TARGET, the only template so marked. Sheet 08 rows 2-5 define these
   four stages precisely. Sheet 42 row 5 lists Villa workflow E2E as evidence
   gate G01, currently NOT RUN.

   SCOPE BOUNDARY: these four stages only, wired to existing components. Do not
   rebuild the gateway, the workflow engine, the payment system or the file
   gateway — compose them. Stages 5 through 7 are P09-02; stages 8 through 10
   are already built in PHASE-07 and are exercised in P09-03.

C. CONTEXT
   Required inputs, sheet 08 rows 2-5, each as stage / executor / description /
   transition condition / failure or wait / human gate:
     1 Intake / CTL-01 / request, consent, location, area, deliverables /
       brief schema valid / AWAITING_INFORMATION / none
     2 Routing / CTL-02 / select WF-VILLA-REVIEW@1.0.0 and tenant policy /
       template active / REJECTED or MANUAL_TRIAGE / PMO
     3 Quote and payment / FIN-01 and FIN-02 / price from actual inputs,
       acceptance, checkout, webhook / amount, currency and status match /
       PAYMENT_FAILED or EXPIRED / Finance exception
     4 File intelligence / DAT-01 / scan and extract pages, scale, rooms,
       confidence / malware clean and coverage / FAILED or RFI / sample
       verification
   Capability constraints from sheet 05:
     row 2 (CTL-01): inputs are the request, files, identity and catalogue;
       outputs are brief.json, gaps and an RFI; it must separate the client's
       statements from inference; it stops on missing identity or consent, a
       malicious file, or an unsupported service; R1/P1; human gate is the
       project manager on ambiguity
     row 20 (DAT-01): decompose PDF, images, tables and IFC with locations and
       confidence, preserving the original; low confidence is reviewed; stops
       on malware, encrypted files, or untrustworthy scale; R1/P2; human gate
       is sample verification; KPIs field accuracy and corrections

D. EXECUTION INSTRUCTIONS
   1. Implement the brief schema with an explicit separation between
      client_stated and system_inferred for every substantive field (location,
      area, occupancy, scope, deliverables, deadline). Each inferred value
      carries its basis and a confidence. This separation is a named
      requirement in sheet 05 row 2 and is what prevents an inference being
      later treated as a client instruction.
   2. Implement gap detection and structured RFI generation: a brief failing
      schema validation produces an itemized list of what is missing, from
      whom, and why it is needed, driving AWAITING_INFORMATION per P03-02
      step 7. Never fill a gap with a default.
   3. Implement CTL-01's stop conditions as hard halts: missing identity
      verification, missing PDPL consent, a quarantined file, or a service not
      in the catalogue. Each halt names its reason to the user.
   4. Wire routing to P03-01's router, pinning WF-VILLA-REVIEW@1.0.0, and
      implement the MANUAL_TRIAGE path to the PMO human gate. A brief that does
      not match the template is never forced into it.
   5. Wire the quote and payment stage to P08-01 through P08-03. Implement the
      source's transition condition literally: amount, currency and status must
      all match before PAYMENT_VERIFIED. Implement the Finance exception gate
      for PAYMENT_FAILED and EXPIRED.
   6. Implement file intelligence as a deterministic-first pipeline, per
      sheet 71 row 2's routing policy (OCR deterministic first, then a verified
      vision model only where needed):
        - text and structure extraction from the native PDF layer first;
        - OCR only for raster content;
        - a vision model only where deterministic extraction fails, routed
          through the gateway (never directly);
        - page inventory, drawing scale detection, title block parsing, and
          room or space identification, each with a locator and a confidence;
        - the original bytes are preserved untouched (sheet 05 row 20).
   7. Implement scale handling as a named risk: an undetermined or
      untrustworthy drawing scale is a stop condition in sheet 05 row 20. The
      pipeline must not infer dimensions from an unverified scale. It records
      scale_confidence and halts or escalates when below threshold.
   8. Implement coverage as the transition condition: the stage advances only
      when the extraction covered the required proportion of pages and the
      required artefacts (title block, floor plans, elevations as the template
      declares). Partial coverage produces an RFI, not a silent partial result.
   9. Implement the sample verification human gate: a configurable sample of
      extracted fields is presented for human confirmation, and the result
      feeds the field-accuracy KPI from sheet 05 row 20.
  10. Record a document map artifact per sheet 05 row 20's declared output
      (document map, entities, anchors), stored as a versioned artifact with
      an evidence manifest from P02-03 so later findings can anchor to it.
  11. Tests:
        a. a brief missing consent -> halt with the reason, no run created;
        b. a brief missing area -> AWAITING_INFORMATION with an itemized RFI,
           no default applied;
        c. client_stated and system_inferred are separate and an inferred value
           carries its basis;
        d. a brief that matches no template -> MANUAL_TRIAGE to PMO;
        e. a payment whose amount differs from the quote -> not verified
           (reuses the P08-03 control);
        f. a quarantined file at intake -> halt, no extraction attempted;
        g. an encrypted PDF -> stop condition, named;
        h. a drawing with undetectable scale -> halt or escalation, with no
           inferred dimension;
        i. coverage below threshold -> RFI, not a partial pass;
        j. deterministic extraction succeeds -> no vision model call; assert
           with a gateway double;
        k. the document map is stored as a versioned artifact with a verifiable
           evidence manifest.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the brief schema with client_stated and system_inferred separation
   - gap detection and structured RFI generation
   - CTL-01 stop conditions as hard halts
   - routing wired with a MANUAL_TRIAGE human gate
   - the quote and payment stage with the three-way match condition
   - the deterministic-first file intelligence pipeline with confidences
   - scale confidence handling with a halt below threshold
   - coverage-gated advancement
   - the sample verification human gate feeding field accuracy
   - the document map artifact with an evidence manifest
   - tests/villa/stages-1-4.* covering cases a through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eleven tests.
   - For case j, paste the gateway double's assertion that no vision model was
     called when deterministic extraction sufficed.
   - Paste a sample brief showing the two separated field sets.
   - Acceptance criterion: no gap is ever filled by default, no dimension is
     inferred from an untrusted scale, and partial coverage never passes as
     complete.

G. COMPLETION CONTRACT
   Definition of Done: stages 1-4 run on a real drawing set, every stop
   condition enforced, the document map stored and verifiable.
   Evidence to report: the eleven test outputs, the brief sample, the document
   map manifest verification.
   Remaining blockers: none expected within these four stages. Note that
   payment can only be exercised against a sandbox or fake per P08-03.
   Next prompt: P09-02.
```

**المخرجات المتوقعة:** مخطط `brief` بفصل التصريح عن الاستنتاج، خط فهم ملفات حتمي أولاً، خريطة مستند.
**التحقق المطلوب:** لا فراغ يُملأ افتراضياً؛ لا بُعد يُستنتج من مقياس غير موثوق؛ التغطية الجزئية لا تمر.
**الاعتمادية التالية:** `P09-02`.

---

### P09-02 — الامتثال والمسودة المعمارية وبوابة الجودة

<!-- meta
id: P09-02
phase: PHASE-09
title_en: Villa path stages 5-7 — compliance, architectural draft, quality gate
prereq: [P09-01]
requirements: [REQ-WF-08, REQ-AGT-08, REQ-KNW-06, REQ-SVC-02]
-->

**ماذا سينفذ هذا الأمر؟** يُنفّذ المراحل 5 إلى 7: الامتثال (`COM-01`)، والمسودة
المعمارية (`DSN-01`)، وبوابة الجودة (`GOV-01`).

**لماذا نحتاجه؟** هذه هي المراحل التي تُنتج القيمة المهنية. والورقة 05 الصف 5
تضع على `GOV-01` قيداً جوهرياً: «لا تستبدل المتخصص» — أي أن بوابة الجودة فحص
آلي للاكتمال والاتساق، وليست بديلاً عن المراجع المؤهل.

**ما المتطلبات السابقة؟** `P09-01`.

**ما النتيجة المتوقعة؟** ملاحظات مُنمَّطة مرتبطة بالمخطط، وبوابة جودة تمنع
الانتقال عند أي عيب حاجز.

**كيف نتحقق من نجاحه؟** finding بلا دليل أو باستشهاد غير صالح لا يمر البوابة؛
والقيد المتعلق بحقوق `SBC` مُسجَّل صريحاً في مخرجات المرحلة.

```text
TASK P09-02 — Villa path stages 5-7: compliance, architectural draft, quality gate

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P09-02
   Phase: PHASE-09
   Prerequisites: P09-01
   Requirements covered: REQ-WF-08, REQ-AGT-08, REQ-KNW-06, REQ-SVC-02

B. OBJECTIVE
   Implement stages 5 through 7 of the villa golden path: the compliance stage
   with its rights and citation gates, the architectural draft producing typed
   findings anchored to the drawing, and the quality gate that blocks
   advancement on any blocking defect.

   Why this is necessary: these stages produce the professional value. Sheet 05
   row 5 constrains GOV-01 with the clause "does not replace the specialist" —
   the quality gate is an automated completeness, citation, consistency and
   R/P check, not a substitute for the qualified reviewer. Sheet 08 rows 6-8
   define each stage's transition condition and failure state.

   SCOPE BOUNDARY: these three stages. The reviewer assignment, decisions,
   lock, signature and delivery are already built in PHASE-07 and are exercised
   in P09-03.

C. CONTEXT
   Required inputs, sheet 08 rows 6-8:
     5 Compliance / COM-01 / occupancy, location, edition, rights, cited
       observations / rights ALLOWED and an exact citation / SUSPENDED /
       compliance specialist
     6 Architecture draft / DSN-01 / individual findings anchored to the
       drawing / schema and evidence valid / RETURN_FOR_CORRECTION / after
       quality
     7 Quality gate / GOV-01 / completeness, citations, R/P, second review /
       all blocking checks pass / FAILED or SUSPENDED / Quality Lead
   Capability constraints from sheet 05:
     row 11 (COM-01): determine editions and jurisdiction, convert permitted
       text into rules and cited findings; stops on UNKNOWN rights, unknown
       edition or conflict; R2/P3; human gate is the discipline specialist
     row 12 (DSN-01): review programme, areas, circulation, egress and access,
       issuing findings linked to the drawing; inputs brief, PDF, DWG, IFC;
       outputs findings, markups, variance; stops on unclear use or scale;
       R2/P3; human gate is a qualified architect; KPIs finding acceptance and
       misses
     row 5 (GOV-01): check evidence, citations, consistency and R/P before the
       output advances; does not replace the specialist; outputs pass, fail,
       defects or escalation; stops on an unlicensed source, a missing citation
       or an invalid schema; R3/P3
   INHERITED CONSTRAINT: SRC-SBC-2024 rights are UNKNOWN and the source
   decision is BLOCK until ALLOWED (sheet 25 row 2, open decision OD-05).
   Therefore the compliance stage cannot produce Saudi-code-cited findings.

D. EXECUTION INSTRUCTIONS
   1. Implement the compliance stage on top of P06-03. Its first action is the
      applicability determination (occupancy, location, effective date). Its
      second is the rights check. Given the inherited constraint, the expected
      and correct behaviour today is that Saudi code citation is blocked.
   2. Implement that blocked path honestly and visibly: the stage records
      COMPLIANCE_SOURCE_BLOCKED naming SRC-SBC-2024 and the UNKNOWN rights,
      produces no code-cited finding, and surfaces the limitation in the run's
      output and in the delivery package's scope statement. It must not
      substitute an unlicensed secondary source, a model's recollection of the
      code, or a generic best-practice statement dressed as a code requirement.
      Add a test with a model double that attempts exactly that substitution
      and assert rejection.
   3. Implement the stage's three stop conditions from sheet 05 row 11:
      UNKNOWN rights, unknown edition, and conflict between applicable
      requirements, each halting with a named reason and escalating to the
      compliance specialist rather than choosing.
   4. Implement the architectural draft stage (DSN-01) producing typed findings
      per P07-01 across the review areas the source names: programme
      conformance, area schedule, circulation, egress and accessibility. Every
      finding:
        - is a single testable observation;
        - anchors to the document map from P09-01 with a page and grid locator;
        - carries its discipline (ARCH), finding_type, severity, R and P;
        - carries complete created_by provenance;
        - carries a citation only where a verified one exists.
      Non-code findings — programme mismatches, area discrepancies against the
      stated brief, internal document inconsistencies, missing information —
      are fully producible today and are what the pilot exercises.
   5. Implement markups and variance output per sheet 05 row 12, as artifact
      versions anchored to source pages.
   6. Implement DSN-01's stop conditions: unclear use or occupancy, and
      untrustworthy scale (inherited from P09-01). The stage halts rather than
      guessing.
   7. Implement the quality gate (GOV-01) as a set of named, individually
      reported blocking and non-blocking checks:
        blocking — every finding validates against the schema; every finding
          has resolvable evidence; every normative claim has a verified,
          rights-cleared citation; no finding cites an unlicensed source; every
          finding carries R and P; every P3 finding has its second-review
          trigger evaluated; no finding is a duplicate of another in the same
          set;
        non-blocking — style, length, terminology consistency, recommended
          action clarity.
      A blocking failure produces FAILED or SUSPENDED per the source and
      returns the set for correction. Report every check by name with its
      result, so the gate is auditable rather than a single boolean.
   8. Enforce the "does not replace the specialist" constraint structurally: a
      quality-gate PASS advances the set to AWAITING_REVIEW and can never set a
      finding to ACCEPTED or mark an output approved. Add a test asserting the
      gate cannot produce an approval.
   9. Implement the Quality Lead human gate for the FAILED and SUSPENDED
      outcomes.
  10. Tests:
        a. the compliance stage with SBC blocked -> COMPLIANCE_SOURCE_BLOCKED
           recorded, no code-cited finding, the limitation surfaced in the run
           output;
        b. a model double attempting to state a code requirement without a
           verified citation -> rejected, no finding created;
        c. an unknown edition -> halt, escalated, no default to newest;
        d. conflicting applicable requirements -> halt with both recorded;
        e. a draft finding with no resolvable evidence -> blocked by the
           quality gate, named;
        f. a draft finding citing an unlicensed source -> blocked, named;
        g. a compound finding -> blocked by the single-observation rule;
        h. a duplicate finding -> blocked;
        i. a P3 finding -> its second-review trigger evaluated and recorded;
        j. the quality gate attempting to set a finding to ACCEPTED ->
           impossible;
        k. a PASS advances to AWAITING_REVIEW with every check reported by
           name.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the compliance stage with applicability, rights gating and the explicit
     COMPLIANCE_SOURCE_BLOCKED outcome
   - rejection of uncited normative claims and unlicensed substitution
   - the three compliance stop conditions
   - the architectural draft stage producing anchored typed findings
   - markup and variance artifacts
   - the DSN-01 stop conditions
   - the named-check quality gate with blocking and non-blocking results
   - the structural guarantee that the gate cannot approve
   - the Quality Lead human gate
   - tests/villa/stages-5-7.* covering cases a through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eleven tests.
   - Paste the case b rejection — this is the control that prevents the single
     most damaging failure mode in this product, an invented code requirement.
   - Paste one quality gate report showing every check by name with its result.
   - State clearly in your report that Saudi code compliance findings are
     blocked by OD-05 and what the pilot can therefore demonstrate.
   - Acceptance criterion: no normative claim exists without a verified
     citation, no unlicensed substitution occurs, and the quality gate never
     approves anything.

G. COMPLETION CONTRACT
   Definition of Done: the three stages implemented, blocked compliance handled
   honestly and visibly, findings anchored and schema-valid, the gate auditable
   and incapable of approval.
   Evidence to report: the eleven test outputs, the substitution rejection, a
   named-check gate report, the explicit OD-05 limitation statement.
   Remaining blockers: OD-05 constrains the pilot's scope. Carry it into
   P09-03's evidence record rather than omitting it.
   Next prompt: P09-03.
```

**المخرجات المتوقعة:** مرحلة امتثال محجوبة بشفافية، ملاحظات مُنمَّطة مرتبطة بالمخطط، بوابة جودة مُفصَّلة.
**التحقق المطلوب:** رفض أي ادعاء كودي بلا استشهاد مُتحقَّق؛ البوابة لا تستطيع الاعتماد.
**الاعتمادية التالية:** `P09-03`.

---

### P09-03 — التشغيل الكامل من طرف إلى طرف ودليل G01

<!-- meta
id: P09-03
phase: PHASE-09
title_en: Full end-to-end villa run and the G01 evidence record
prereq: [P09-02]
requirements: [REQ-WF-08, REQ-EVL-07, REQ-SVC-01, REQ-GOV-04]
-->

**ماذا سينفذ هذا الأمر؟** يُشغّل المسار كاملاً — المراحل العشر — على مجموعة
مخططات حقيقية، ويجمع دليلاً قابلاً للإعادة لاستيفاء البند `G01`.

**لماذا نحتاجه؟** الورقة 42 تضع `G01 Villa workflow E2E` أول بند في دفتر الأدلة
بحالة `NOT RUN`، وتطلب لكل بند: اختبار/إثبات، بيئة، مالك، رابط دليل، وقت تنفيذ،
ونتيجة. والورقة 68 الصف 7 تحدد ما يجب إرفاقه: «logs وtest artifacts ومالك وبيئة
وطابع زمني وdeployment SHA».

**ما المتطلبات السابقة؟** `P09-02`.

**ما النتيجة المتوقعة؟** تشغيل واحد موثق بالكامل من الطلب إلى الحزمة الموقَّعة
المُفرَج عنها، مع أثر تدقيقي متصل.

**كيف نتحقق من نجاحه؟** الأثر يربط `trace_id` بالمهمة والوكيل والنموذج والأداة
والدليل والمراجعة؛ ويمكن إعادة التشغيل والحصول على نفس النتيجة البنيوية.

```text
TASK P09-03 — Full end-to-end villa run and the G01 evidence record

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P09-03
   Phase: PHASE-09
   Prerequisites: P09-02
   Requirements covered: REQ-WF-08, REQ-EVL-07, REQ-SVC-01, REQ-GOV-04

B. OBJECTIVE
   Execute the complete ten-stage WF-VILLA-REVIEW path on a real drawing set,
   end to end, and assemble a reproducible evidence record that satisfies
   evidence-ledger gate G01.

   Why this is necessary: sheet 42 row 5 lists Villa workflow E2E as gate G01
   with status NOT RUN, and requires per row a test or proof, an environment,
   an owner, an evidence URL, an execution timestamp and a result. Sheet 68
   row 7 specifies what must be attached to a release gate: logs, test
   artifacts, owner, environment, timestamp and deployment SHA. Sheet 40 row 13
   lists "Golden villa workflow E2E required" as the evidence needed to move
   human review from UNVERIFIED.

   SCOPE BOUNDARY: executing and evidencing the path. Fix defects you find that
   are inside the path's wiring; a defect in a component owned by an earlier
   phase is reported and fixed there, with the prompt id named. Do not
   extend scope to other workflows.

C. CONTEXT
   Required inputs:
     - the ten stages of sheet 08, now implemented across P09-01, P09-02 and
       PHASE-07
     - sheet 07 row 2: WF-VILLA-REVIEW, version 1.0.0, segment individual or
       office, scope "preliminary architectural review and not an approval
       design", capabilities CTL-01, CTL-02, DAT-01, COM-01, DSN-01, GOV-01,
       REV-01, DOC-01, EVAL-01, R2/P3, review by an architectural reviewer with
       a second review per trigger, pricing PRICE-VILLA-v1, test suite
       AT-VILLA-v1, evidence state PILOT TARGET
     - sheet 35 row 6 (SVC-01) guardrail: no licensed approval by AI
     - sheet 73 row 10: the trace must link trace_id to task, agent, model,
       tool, evidence and review
   Test data requirement: a real villa drawing set. If you do not have one, use
   a synthetic but realistic set and say so explicitly — a synthetic run is
   partial evidence for G01, not full evidence, and the evidence record must
   state which it was.

D. EXECUTION INSTRUCTIONS
   1. Define AT-VILLA-v1 as the named test suite sheet 07 row 2 requires: a
      scripted end-to-end scenario covering all ten stages with assertions at
      every transition condition from sheet 08.
   2. Execute the happy path end to end and capture, at every stage: the stage
      entered and exited, the transition condition evaluated, the actor, the
      artifacts produced with digests, the model and agent versions used, the
      policy and routing decisions, the cost recorded, and the elapsed time.
   3. Execute the human stages for real rather than simulating them:
        - a real reviewer account passing the hard filters with a recorded
          eligibility snapshot;
        - real item-level decisions with reason codes;
        - a real step-up authenticated signature over the locked digest;
        - the commercial gate satisfied by a sandbox payment or a recorded
          contractual authorization.
      A simulated reviewer invalidates the evidence for G01 and for sheet 38
      row 11's G-06. If a real reviewer is unavailable, say so and mark the
      gate PARTIAL.
   4. Verify the trace linkage requirement of sheet 73 row 10 on this run: from
      one trace_id, walk to the task, the agent version, the model version, the
      tool calls, the evidence manifests and the review decisions. A missing
      link is an instrumentation defect to fix now, because it is also a
      PHASE-10 exit criterion.
   5. Execute the failure paths too, because the source defines a failure state
      for every stage and G01 is not satisfied by a happy path alone. At
      minimum: an incomplete brief producing an RFI and recovering; a payment
      failure and recovery; a quality gate FAILED and a correction cycle; an
      offer expiry and reassignment; and a post-signature mutation producing
      INVALIDATED and a new cycle.
   6. Verify the product-level guardrails on the produced package:
        - the scope statement says this is a preliminary architectural review
          and not an approval design, per sheet 07 row 2;
        - no licensed approval is implied, per sheet 35 row 6;
        - the OD-05 compliance limitation from P09-02 is stated in the package;
        - the signature's scope matches the reviewer's eligibility.
   7. Assemble the evidence record at docs/evidence/G01-villa-e2e/ containing:
      the run identifiers; the environment; the deployment SHA; the owner; the
      UTC timestamps; the full AT-VILLA-v1 output; the captured logs and
      traces; the produced artifacts with their digests; the reviewer identity
      reference and eligibility snapshot id; the payment or authorization
      evidence reference; the cost record; and a result of PASS, PARTIAL or
      FAIL with the reasons.
   8. Update config/registries/release-gates.json and the evidence ledger with
      G01's real result. Per ADR-008 and sheet 15 row 19, the entry requires a
      build reference, the last successful test run, the evidence link and the
      approver — if no approver has signed off, the gate is not PASS, however
      good the run was. Record it as PARTIAL pending approval.
   9. Re-run AT-VILLA-v1 a second time and confirm structural reproducibility:
      the same stages, the same decisions given the same inputs, the same
      artifact structure. Digests of generated documents may differ if they
      embed timestamps — if so, state which fields are non-deterministic and
      why, rather than ignoring the difference.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the AT-VILLA-v1 suite covering all ten stages and their failure paths
   - a completed end-to-end run with real human stages where possible
   - verified trace linkage across the full chain
   - executed failure and recovery paths
   - guardrail verification on the produced package
   - docs/evidence/G01-villa-e2e/ with the complete evidence record
   - an updated evidence ledger entry for G01 with its honest result
   - a reproducibility re-run with non-determinism documented
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the AT-VILLA-v1 output for the happy path and for each failure path.
   - Paste the trace walk from one trace_id through all six linked levels.
   - Paste the package's scope statement showing the three required
     limitations.
   - State plainly whether the drawing set was real or synthetic, whether the
     reviewer was real, and therefore whether G01 is PASS, PARTIAL or FAIL.
   - Acceptance criterion: the path completes end to end with a connected audit
     trail, every failure path behaves as the source specifies, and the
     evidence record is complete enough for an auditor to reproduce the run.

G. COMPLETION CONTRACT
   Definition of Done: the run executed, every stage and failure path
   evidenced, the trace connected, the evidence record assembled, and the gate
   result recorded honestly — including PARTIAL where a real reviewer, a real
   drawing set or an approver was unavailable.
   Evidence to report: the suite outputs, the trace walk, the evidence
   directory path, the gate result with its justification.
   Remaining blockers: OD-05 limits compliance scope; approver sign-off is an
   owner action; a real drawing set and a real reviewer may be owner-supplied.
   Name each. Do not record PASS to close the phase.
   Next prompt: P10-01. PHASE-09 exit requires a completed end-to-end run with
   a connected audit trail and a recorded G01 result.
```

**المخرجات المتوقعة:** مجموعة `AT-VILLA-v1`، تشغيل موثق كامل، سجل دليل `G01`.
**التحقق المطلوب:** أثر متصل بستة مستويات؛ كل مسار فشل مُنفَّذ؛ النتيجة مُسجَّلة بصدق (`PASS`/`PARTIAL`/`FAIL`).
**الاعتمادية التالية:** `P10-01`.

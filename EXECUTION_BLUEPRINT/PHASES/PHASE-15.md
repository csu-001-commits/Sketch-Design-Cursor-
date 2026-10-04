# PHASE-15 — التوسع في المسارات التخصصية

<!-- phasemeta
id: PHASE-15
depends_on: [PHASE-09, PHASE-14]
criticality: P1
-->

## الغرض من المرحلة

الورقة 07 تحتوي ستة قوالب غير `WF-VILLA-REVIEW`، خمسة منها بحالة `DEFINED`
وإصدارات `0.8.0` أو `0.9.0` — أي أنها مُعرَّفة لا جاهزة. والورقة 29 ترتّب التوسع
على مراحل: `BIM/QTO/MEP` ثم `PMO & Enterprise` ثم `Site/Infra/Handover`، وكل
مرحلة لها «بوابة قرار» و«دليل» مطلوبان.

القاعدة الحاكمة لهذه المرحلة: لا قالب يُعرَض على عميل قبل أن تكتمل أربعة أمور —
مجموعة اختبار مُنفَّذة، وأدوات مُتحقَّق منها، ومجموعة مراجعين مؤهلين، ونموذج تسعير
خاص به.

## شروط الدخول

- المسار الذهبي أخضر (`PHASE-09`) ومحرك التقييم موثوق (`PHASE-14`).

## شروط الخروج

- لكل قالب مُضاف: مجموعة اختبار مُعرَّفة ومُنفَّذة، أدوات مُتحقَّق منها، مراجعون
  مؤهلون، ونموذج تسعير — قبل أي تعريض.

## المتطلبات المغطاة في هذه المرحلة

`REQ-EXP-01`..`REQ-EXP-07`, `REQ-AGT-09`, `REQ-INT-05`, `REQ-DAT-07`,
`REQ-SVC-01`

---

## الأوامر التنفيذية

### P15-01 — بوابة إدخال القوالب الجديدة

<!-- meta
id: P15-01
phase: PHASE-15
title_en: The workflow onboarding gate
prereq: [P14-05]
requirements: [REQ-EXP-07, REQ-EXP-06, REQ-SVC-01]
-->

**ماذا سينفذ هذا الأمر؟** يبني عملية موحدة ومُبوَّبة لإضافة أي قالب جديد، بدلاً
من تكرار جهد مخصص لكل قالب.

**لماذا نحتاجه؟** `ADR-001` يشترط لكل قالب «owner + schema + tests + pricing +
approval». وستة قوالب تنتظر. بناء بوابة إدخال واحدة يضمن أن القالب السادس يخضع
لنفس الصرامة التي خضع لها الأول، ويمنع الانحراف الذي يحدث عندما يُضاف كل قالب
بطريقته.

**ما المتطلبات السابقة؟** `P14-05`.

**ما النتيجة المتوقعة؟** عملية إدخال مُنفَّذة بقائمة تحقق إلزامية وبوابة قرار.

**كيف نتحقق من نجاحه؟** قالب ناقص أي عنصر من الأربعة لا يمكن تفعيله؛ والبوابة
تُنتج سجل قرار.

```text
TASK P15-01 — The workflow onboarding gate

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P15-01
   Phase: PHASE-15 (Expansion workflows)
   Prerequisites: P14-05
   Requirements covered: REQ-EXP-06, REQ-EXP-07, REQ-SVC-01

B. OBJECTIVE
   Build one standardized, gated onboarding process for adding any new workflow
   template, so each of the six remaining templates meets the same bar as the
   villa pilot rather than being bolted on ad hoc.

   Why this is necessary: ADR-001's acceptance control requires owner, schema,
   tests, pricing and approval for every template. Sheet 07 holds six templates
   at DEFINED with versions 0.8.0 and 0.9.0, meaning specified but not ready.
   Sheet 29 sequences expansion in stages, each with a decision gate and
   required evidence. A per-template improvised path is how a platform
   accumulates workflows that nobody can price, test or staff.

   SCOPE BOUNDARY: the onboarding process and its gate. Do not implement a
   specific workflow here — P15-02 and P15-03 use this process.

C. CONTEXT
   Required inputs:
     - config/registries/workflow-templates.json, the eight templates with
       their capability lists, R and P ratings, review requirements, pricing
       ids, test suite ids and evidence states
     - the template registry and publication gate from P03-01
     - the eligibility matrix from P07-02 and the engineering tool register
       from P00-02 (sheet 22, twenty-nine tools with adoption decisions
       Production, Recommended, Evaluate, Option, Enterprise and Specialist)
     - sheet 20 rows 2-6, the five pricing scenarios, including the explicit
       warning in row 3 that capability count is not a pricing unit
     - sheet 29 rows 2-8, the staged roadmap with per-stage owners, evidence
       and decision gates

D. EXECUTION INSTRUCTIONS
   1. Implement the onboarding checklist as an enforced record with these
      mandatory sections, each of which must be complete before the template
      can leave DRAFT:
        a. Scope statement: what the workflow does and, explicitly, what it
           does not do. Sheet 07 row 2 models this with "preliminary
           architectural review and not an approval design". Every template
           needs an equivalent negative boundary.
        b. Input and output schemas, validated.
        c. Capability list, referencing existing registered agent definitions
           only. A workflow may not name a capability that has no definition.
        d. Risk rating: the R and P values per step, and the resulting human
           gates resolved to roles via P05-04.
        e. Tool validation: for every engineering tool the workflow depends on,
           its adoption decision from sheet 22, its licence status, its version,
           and a recorded validation test. A tool marked Evaluate or Specialist
           in the source cannot be used in production without a recorded
           validation and, where the source says Specialist, a named
           specialist.
        f. Reviewer pool: the eligibility codes required, and evidence that at
           least the minimum viable number of qualified, non-conflicted
           reviewers exists for each. A workflow with no eligible reviewer
           cannot run, per the NO_ELIGIBLE_REVIEWER outcome in P07-03.
        g. Pricing model: the components from sheet 18 that apply, the rate
           requirements, and an explicit statement that capability count is not
           a pricing unit per sheet 20 row 3.
        h. Test suite: the named suite from the registry (AT-BIM-v1, AT-QTO-v1,
           AT-MEP-v1, AT-INFRA-v1, AT-SITE-v1, AT-PAY-v1, AT-DEL-v1), defined
           and executed with evidence.
        i. Knowledge dependencies: which RAG collections the workflow needs and
           whether their rights permit use. A workflow depending on a BLOCKED
           source cannot be activated for that function.
        j. Owner and approval: a named accountable owner and a recorded
           approval.
   2. Wire the checklist to the P03-01 publication gate so an incomplete
      checklist structurally prevents activation, rather than being a document
      someone is supposed to read.
   3. Implement the decision gate per sheet 29: each template's activation
      produces a decision record naming the evidence reviewed, the decision,
      the decider, the date, and any conditions or scope limits imposed.
   4. Implement a staged exposure policy: a newly activated template starts
      internal-only, then limited pilot with named projects, then general
      availability, each stage requiring its own evidence. Sheet 29's stages
      each have their own decision gate, so exposure is incremental by design.
   5. Implement the dependency check that reports, for a proposed template,
      everything that blocks it: missing capability definitions, unvalidated
      tools, insufficient reviewer pools, absent rates, undefined test suites
      and blocked knowledge sources. Run it for all six pending templates and
      publish the result — this tells the owner what each expansion actually
      costs.
   6. Implement the scenario-based pricing review per sheet 20: for each
      template, record which of the five scenarios it corresponds to and the
      pricing method the source names (the sheet 19 calculator for villa,
      bottom-up per step for multi-storey, milestones plus change orders for
      design and delivery, a project-specific model for towers, per model or
      GB or run or cycle for BIM coordination).
   7. Tests:
        a. a template missing its test suite -> cannot leave DRAFT, naming the
           gap; repeat for each of the ten checklist sections;
        b. a template naming a capability with no definition -> rejected;
        c. a template depending on a tool marked Specialist with no named
           specialist -> rejected;
        d. a template whose eligibility codes have no qualified reviewers ->
           cannot be activated;
        e. a template depending on a BLOCKED knowledge source -> that function
           cannot be activated;
        f. activation produces a decision record with evidence and conditions;
        g. a newly activated template is internal-only until its pilot evidence
           exists;
        h. the dependency check runs for all six pending templates and reports
           their blockers.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the ten-section onboarding checklist as an enforced record
   - wiring into the P03-01 publication gate
   - decision records per activation with conditions
   - the three-stage exposure policy
   - the dependency check, run and published for all six pending templates
   - scenario-based pricing review records
   - tests/expansion/onboarding-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the ten rejections from case a.
   - Paste the dependency check output for all six pending templates, with
     their blockers.
   - Paste one activation decision record.
   - Acceptance criterion: no template can be activated with any checklist
     section incomplete, and the dependency report tells the owner the true
     cost of each expansion.

G. COMPLETION CONTRACT
   Definition of Done: the gate enforced, decision records produced, the
   dependency report published for all six templates.
   Evidence to report: the rejection outputs, the dependency report, a decision
   record.
   Remaining blockers: the dependency report is itself the blocker list.
   Reviewer pools, tool licences and rate cards are owner-owned. Present the
   report as the input to the owner's expansion decision.
   Next prompt: P15-02.
```

**المخرجات المتوقعة:** قائمة تحقق بعشرة أقسام مفروضة، سجلات قرار، تقرير اعتماديات للقوالب الستة.
**التحقق المطلوب:** لا تفعيل مع قسم ناقص؛ تقرير الاعتماديات يكشف التكلفة الحقيقية للتوسع.
**الاعتمادية التالية:** `P15-02`.

---

### P15-02 — مسارات BIM والكميات

<!-- meta
id: P15-02
phase: PHASE-15
title_en: BIM coordination and quantity take-off workflows
prereq: [P15-01]
requirements: [REQ-EXP-01, REQ-EXP-02, REQ-DAT-07, REQ-INT-05]
-->

**ماذا سينفذ هذا الأمر؟** يُدخل `WF-BIM-COORD` و`WF-QTO` عبر بوابة `P15-01`،
بقدراتهما وأدواتهما ومراجعيهما واختباراتهما.

**لماذا نحتاجه؟** الورقة 29 الصف 6 تضع المرحلة 4 (`BIM/QTO/MEP`) بدليل مطلوب:
«Benchmarks وtool validation»، وبوابة قرار: «خدمات B2B محدودة». والورقة 05 الصف
23 (`CST-01`) تضع قيداً حاسماً على الكميات: «إظهار غير القابل للقياس» — أي أن
المخرج يجب أن يُعلن ما لم يستطع قياسه، لا أن يصمت عنه.

**ما المتطلبات السابقة؟** `P15-01`.

**ما النتيجة المتوقعة؟** مسارا BIM والكميات مُدخَلان بأدلتهما، أو مُسجَّلان
كمحجوبين بأسباب محددة.

**كيف نتحقق من نجاحه؟** `AT-BIM-v1` و`AT-QTO-v1` مُعرَّفان ومُنفَّذان؛ وكمية بلا
قاعدة قياس أو بمصدر سعر غائب لا تُنتَج.

```text
TASK P15-02 — BIM coordination and quantity take-off workflows

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P15-02
   Phase: PHASE-15
   Prerequisites: P15-01
   Requirements covered: REQ-EXP-01, REQ-EXP-02, REQ-DAT-07, REQ-INT-05

B. OBJECTIVE
   Onboard WF-BIM-COORD and WF-QTO through the P15-01 gate, implementing their
   capabilities, validating their tools, establishing their reviewer pools and
   defining and executing their test suites.

   Why this is necessary: sheet 29 row 6 places BIM, QTO and MEP in stage 4
   with required evidence of benchmarks and tool validation and a decision gate
   of limited B2B services. Sheet 05 row 23 (CST-01) sets a decisive constraint
   on quantities: surface what cannot be measured. A take-off that silently
   omits unmeasurable scope is worse than no take-off, because it looks
   complete.

   SCOPE BOUNDARY: these two workflows. MEP, infrastructure and site are
   P15-03. Do not acquire a commercial tool licence without owner
   authorization.

C. CONTEXT
   Required inputs:
     - sheet 07 row 3: WF-BIM-COORD, version 0.9.0, segment office or
       developer, scope federation, IDS, clashes and BCF; capabilities CTL-01,
       BIM-01, BIM-02, GOV-01, DOC-01, PMO-02; R2/P3; review by a BIM
       coordinator plus discipline owners; pricing PRICE-BIM-v1; test suite
       AT-BIM-v1; state DEFINED
     - sheet 07 row 4: WF-QTO, version 0.9.0, segment office or contractor,
       scope traceable quantities under LOD constraints; capabilities DAT-01,
       BIM-01, CST-01, GOV-01, REV-01, DOC-01; R2/P3; review by QS or cost
       manager; pricing PRICE-QTO-v1; test suite AT-QTO-v1; state DEFINED
     - sheet 05 row 21 (BIM-01): index schema, GUID, units, coordinates, IDS
       and versions without modifying production; stops on a schema, units or
       georeferencing conflict; human gate BIM Coordinator
     - sheet 05 row 22 (BIM-02): run clash rules, de-duplicate, link BCF and
       re-verify after fix; stops on georeferencing failure or missing rules;
       human gate BIM plus the discipline owner
     - sheet 05 row 23 (CST-01): extract quantities by measurement rules, link
       GUID and page, surface the unmeasurable; QS approves; stops on LOD,
       units, rule or price issues
     - sheet 22 tool rows: IfcOpenShell (Recommended), buildingSMART IDS
       (Production), BCF (Production), Autodesk Platform Services (Evaluate),
       Navisworks via BIM-02, Cost DB
     - sheet 12 rows 7-8: eligibility codes BIM-COORD (second review on clash
       P3) and QS-QTO (second review on high value)
     - config/registries/data-constraints.json, boq_items: UNIQUE (estimate_id,
       line_no), invariant "unit plus source refs", retention "versioned
       snapshots"

D. EXECUTION INSTRUCTIONS
   1. Complete the P15-01 checklist for both templates, including their
      negative scope statements. For BIM coordination, the boundary includes
      that a clash report is not a design change instruction and that BIM-COORD
      holders cannot give a discipline signature (sheet 12 row 7). For QTO, the
      boundary includes that quantities are not a priced estimate and that a
      price without a source is prohibited (sheet 12 row 8).
   2. Implement BIM-01: parse and index IFC with schema version, GUIDs, units
      and coordinate reference, validate against IDS, and diff versions —
      explicitly without modifying the production model. Implement the three
      stop conditions as halts: a schema conflict, a units conflict and a
      georeferencing conflict. Units and georeferencing errors silently carried
      forward produce confidently wrong quantities later, which is why the
      source halts on them.
   3. Implement BIM-02: run clash rules with configured tolerances,
      de-duplicate results, produce typed clashes linked to BCF with GUID
      references, and re-verify after a reported fix. Implement the stop
      conditions: georeferencing failure and missing rules. Track the source's
      KPIs, clash precision and reopened clashes.
   4. Implement CST-01 with its three disciplines of rigour:
        - measurement rules are explicit, versioned and cited on every quantity,
          because a quantity without its measurement basis is not auditable;
        - every quantity links to its source GUID or page, satisfying the
          traceability the template's scope demands;
        - the unmeasurable is surfaced as a first-class output: scope the
          model does not support, elements below the LOD threshold, and
          ambiguous assemblies are listed explicitly with the reason, and the
          BOQ states its own coverage. Add a test asserting a model with
          deliberately missing information produces an explicit unmeasurable
          list rather than a shorter BOQ.
        - LOD is a gate: a take-off requested at a precision the model's LOD
          cannot support is refused with the LOD gap named.
   5. Implement boq_items per the data constraint with its uniqueness, its
      mandatory unit and source references, and versioned snapshots. A line
      without a unit or a source reference cannot be written.
   6. Enforce the pricing separation from sheet 71 row 6: the model extracts,
      the calculator prices, and a model-asserted price is rejected (already
      enforced in P04-07; verify it here for this workflow). A price with no
      dated source is prohibited per sheet 12 row 8.
   7. Validate the tools per sheet 22 and record the validation: for
      IfcOpenShell record the version, the licence and a geometry and
      quantity validation against a known reference model; for IDS and BCF
      record conformance against the official specifications; for anything
      marked Evaluate record that it is unvalidated and therefore not usable in
      production without owner authorization and a validation run.
   8. Define and execute AT-BIM-v1 and AT-QTO-v1 as named suites:
        - AT-BIM-v1: federation of multiple models, IDS validation pass and
          fail, clash detection against a known expected set with precision and
          recall, BCF round trip, re-verification after a fix, and each stop
          condition;
        - AT-QTO-v1: quantity extraction against a reference model with known
          quantities, measurement rule citation on every line, GUID
          traceability, the unmeasurable list, LOD refusal, unit enforcement,
          and the model-asserted-price rejection.
   9. Establish the reviewer pools for BIM-COORD and QS-QTO per sheet 12,
      including their second-review triggers (clash P3, high value). Report
      honestly whether qualified reviewers exist. Without them, the templates
      are onboarded but not activatable.
  10. Produce the benchmark evidence sheet 29 row 6 requires: measured
      performance and accuracy on reference models, with the model
      characteristics stated, so the benchmark is interpretable.
  11. Tests:
        a. both checklists complete, or the gaps named;
        b. an IFC with a units conflict -> halt, named;
        c. an IFC with a georeferencing conflict -> halt, named;
        d. an IFC with an unsupported schema version -> halt, named;
        e. clash detection against a known expected set -> precision and recall
           reported; de-duplication verified; BCF round trip verified;
           re-verification after a fix closes the clash;
        f. a take-off on a model with missing information -> an explicit
           unmeasurable list, not a shorter BOQ;
        g. a take-off requested beyond the model's LOD -> refused with the gap
           named;
        h. a BOQ line without a unit or a source reference -> rejected;
        i. a model-asserted price -> rejected;
        j. a price without a dated source -> rejected;
        k. tool validation records exist for every production-path tool;
        l. AT-BIM-v1 and AT-QTO-v1 both execute with their evidence.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - completed onboarding checklists for both templates with negative scope
     statements
   - BIM-01 indexing and IDS validation with three enforced stop conditions
   - BIM-02 clash detection with de-duplication, BCF linkage and
     re-verification
   - CST-01 with versioned measurement rules, GUID traceability, the explicit
     unmeasurable list and LOD gating
   - boq_items with enforced units and source references
   - verified pricing separation
   - tool validation records per sheet 22
   - AT-BIM-v1 and AT-QTO-v1 defined and executed
   - reviewer pool status for BIM-COORD and QS-QTO
   - docs/evidence/expansion/bim-qto-benchmarks/ with the benchmark evidence
   - tests/expansion/bim-*.*, qto-*.* covering cases a through l
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all twelve tests.
   - Paste case f showing the unmeasurable list beside the BOQ coverage
     statement.
   - Paste the clash precision and recall figures with the reference set
     description.
   - State whether qualified reviewers exist for each code and therefore
     whether each template is activatable.
   - Acceptance criterion: no quantity exists without a measurement rule and a
     source reference, the unmeasurable is always surfaced, and a units or
     georeferencing conflict always halts.

G. COMPLETION CONTRACT
   Definition of Done: both templates onboarded through the gate with executed
   suites, validated tools and honest reviewer-pool and activation status.
   Evidence to report: the twelve test outputs, the unmeasurable list, the
   benchmark figures, the activation status.
   Remaining blockers: tool licences, reviewer recruitment and rate cards are
   owner-owned. A template onboarded but not activatable is a correct outcome —
   report it as such.
   Next prompt: P15-03.
```

**المخرجات المتوقعة:** قالبا BIM والكميات مُدخَلان، قائمة «غير قابل للقياس» صريحة، تحقق أدوات، مجموعتا اختبار مُنفَّذتان.
**التحقق المطلوب:** لا كمية بلا قاعدة قياس ومرجع مصدر؛ تعارض الوحدات أو الإحداثيات يوقف دائماً.
**الاعتمادية التالية:** `P15-03`.

---

### P15-03 — MEP والبنية التحتية والموقع وPMO

<!-- meta
id: P15-03
phase: PHASE-15
title_en: MEP, infrastructure, site report and the PMO capabilities
prereq: [P15-02]
requirements: [REQ-EXP-03, REQ-EXP-04, REQ-EXP-05, REQ-AGT-09, REQ-EXP-07]
-->

**ماذا سينفذ هذا الأمر؟** يُدخل `WF-MEP-REVIEW` و`WF-INFRA-REVIEW` و
`WF-SITE-REPORT` عبر البوابة، ويُنفّذ قدرات PMO الثماني.

**لماذا نحتاجه؟** الورقة 29 الصف 7 تضع المرحلة 5 (`PMO & Enterprise`) بدليل
مطلوب: «DR/load/access review». والورقة 06 تحدد قدرات PMO الثماني بحدودها، ولكل
منها قيد صريح — مثل `PMO-03`: «لا EOT أو اعتماد بلا Planner»، و`PMO-04`: «دون
اعتماد نقل ميزانية».

**ما المتطلبات السابقة؟** `P15-02`.

**ما النتيجة المتوقعة؟** ثلاثة قوالب مُدخَلة، وثماني قدرات PMO بحدود سلطتها
مفروضة.

**كيف نتحقق من نجاحه؟** كل قدرة PMO ترفض الفعل المحظور عليها؛ ومسار MEP يفرض
مراجعاً لكل تخصص.

```text
TASK P15-03 — MEP, infrastructure, site report and the PMO capabilities

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P15-03
   Phase: PHASE-15
   Prerequisites: P15-02
   Requirements covered: REQ-AGT-09, REQ-EXP-03, REQ-EXP-04, REQ-EXP-05,
                         REQ-EXP-07

B. OBJECTIVE
   Onboard WF-MEP-REVIEW, WF-INFRA-REVIEW and WF-SITE-REPORT through the
   P15-01 gate, and implement the eight PMO capabilities with their authority
   limits enforced.

   Why this is necessary: sheet 29 row 7 places PMO and enterprise in stage 5
   with required evidence of DR, load and access review. Sheet 06 defines each
   PMO capability with an explicit authority limit, and those limits are the
   substance — PMO-03 may not grant an extension of time or approve without a
   planner, PMO-04 may not approve a budget transfer, PMO-06 may not execute a
   change before a decision except in a documented emergency, PMO-01 may not
   cancel or reallocate budget automatically.

   SCOPE BOUNDARY: these three templates and the eight PMO capabilities. The
   remaining workflow families the source names for later stages — site and
   infrastructure field operations, handover and asset management (sheet 29
   row 8) — are not onboarded here; record them as the next expansion.

C. CONTEXT
   Required inputs:
     - sheet 07 row 6: WF-MEP-REVIEW, version 0.8.0, scope separated and
       coordinated MEP review; capabilities DAT-01, DSN-04, DSN-05, DSN-06,
       BIM-02, GOV-01, REV-01; R2/P3; a reviewer per discipline; pricing
       PRICE-MEP-v1; suite AT-MEP-v1; DEFINED
     - sheet 07 row 7: WF-INFRA-REVIEW, version 0.8.0, scope roads, networks,
       levels and connection points; capabilities STD-02, INF-01, GEO-01,
       BIM-01, GOV-01, REV-01; R2/P3; civil, survey and geotechnical review;
       pricing PRICE-INFRA-v1; suite AT-INFRA-v1; DEFINED
     - sheet 07 row 5: WF-SITE-REPORT, version 0.9.0, scope converting site
       evidence into a report and candidate progress; capabilities EXE-04,
       EXE-01, GOV-01, DOC-01; R2/P2; site engineer review; pricing
       PRICE-SITE-v1; suite AT-SITE-v1; DEFINED
     - sheet 05 rows 15-17 (DSN-04 electrical, DSN-05 mechanical, DSN-06
       plumbing and fire) with their stop conditions: a missing supply source
       or short-circuit data; missing weather or occupancy data; an unknown
       fire strategy or pressure
     - sheet 05 rows 8, 18, 19 (STD-02 site and survey, INF-01 infrastructure,
       GEO-01 geotechnical) with their stop conditions: unknown CRS or
       unestablished boundaries; missing connection points or flood data; a
       borehole location mismatch or an unsigned report
     - sheet 05 rows 24, 27 (EXE-01 progress, EXE-04 site reports) with their
       stop conditions: an unapproved baseline or missing evidence; untrusted
       time, place or privacy
     - sheet 06 rows 2-9, the eight PMO capabilities with their authority
       limits, human approvers, stop conditions and KPIs
     - sheet 12 rows 4-6, 9: eligibility codes ELEC-BUILDING, MECH-HVAC,
       FIRE-REVIEW and CIVIL-INFRA with their prohibitions and second-review
       triggers

D. EXECUTION INSTRUCTIONS
   1. Complete the P15-01 checklist for all three templates with negative scope
      statements drawn from the source: MEP review does not approve a utility
      connection or issue a fire authority approval (sheet 12 rows 4 and 6);
      infrastructure review does not produce a legal survey or a geotechnical
      study (sheet 12 row 9, sheet 05 rows 8 and 19); a site report's
      observation is not proof on its own (sheet 05 row 27).
   2. Implement the MEP review with a reviewer per discipline, which the
      template requires explicitly. Electrical, mechanical, and plumbing and
      fire findings each need their own eligible reviewer, and a single
      reviewer cannot sign across disciplines they are prohibited from.
      Enforce the sheet 12 prohibitions: ELEC-BUILDING excludes utility and
      fire; MECH-HVAC excludes fire without scope; FIRE-REVIEW excludes
      official authority approval and requires second review on every P3.
   3. Implement the three MEP stop conditions as halts, not warnings. A load
      calculation without a known supply source, a thermal calculation without
      weather and occupancy data, and a fire review without a fire strategy are
      each refusals.
   4. Implement the infrastructure review with CRS handling as a first-class
      requirement: an unknown coordinate reference system halts, and
      coordinates are never accepted without one (consistent with the GEO
      locator rule in P02-03). Implement the connection-point and flood-data
      stop conditions.
   5. Implement GEO-01 with its explicit limit from sheet 05 row 19: it
      summarizes and links a geotechnical report to foundations and does not
      replace the study. An unsigned geotechnical report is a stop condition.
   6. Implement WF-SITE-REPORT with the evidence discipline sheet 05 row 27
      demands: time, place and privacy must be trustworthy, and an observation
      alone is not proof. Implement candidate progress as explicitly candidate
      — EXE-01 may not grant an extension of time (sheet 05 row 24), and
      progress without evidence is rejected. Wire it to the PHASE-12 capture
      evidence where available.
   7. Implement the eight PMO capabilities, each with its authority limit
      enforced in code rather than documented:
        - PMO-01 portfolio: produces priority scenarios; cannot cancel a
          project or reallocate budget automatically;
        - PMO-02 stage gates: a checklist alone is insufficient; a waiver is
          temporary with a named owner and an expiry; an unresolved P3 blocks;
        - PMO-03 planning: reviews schedule quality; cannot grant an extension
          of time or approve without a planner;
        - PMO-04 cost control: produces EAC and ETC; cannot approve a budget
          transfer;
        - PMO-05 risk: formulates cause, event and impact with an owner,
          response and trigger; a critical risk without an owner is a stop
          condition; project risk stays separate from the AI R and P axes;
        - PMO-06 change: records the basis and routes authority; no execution
          before a decision except a documented emergency; exceeding limits is
          a stop condition;
        - PMO-07 contracts and claims: produces obligations and a chronology;
          no final legal opinion; handles privilege carefully;
        - PMO-08 reporting: blocks unreconciled data; every variance needs a
          cause, an owner and a date.
      For each, add a test that attempts the prohibited action and asserts
      refusal. These eight tests are the deliverable that makes sheet 06
      operative.
   8. Implement the waiver mechanism for PMO-02 properly: time-boxed, owned,
      audited, and automatically expiring, with waiver aging tracked as the
      source's KPI. An expired waiver re-blocks the gate.
   9. Define and execute AT-MEP-v1, AT-INFRA-v1 and AT-SITE-v1 with their stop
      conditions and their per-discipline review requirements.
  10. Produce the stage 5 evidence sheet 29 row 7 requires — DR, load and
      access review — by referencing the P10-04 DR drill, running a load test
      against the expanded workflow set, and running the access review from
      P14-05. A load test against only the villa path does not evidence stage 5.
  11. Record the remaining expansion scope from sheet 29 row 8 (field
      operations, LiDAR-based as-built, QA and HSE, infrastructure delivery,
      asset handover) as a named future stage with its dependency list, rather
      than silently dropping it.
  12. Tests:
        a. all three checklists complete or their gaps named;
        b. an MEP finding assigned to a reviewer prohibited from that
           discipline -> refused;
        c. a fire finding at P3 without a second review -> cannot complete;
        d. each of the three MEP stop conditions -> halt, named;
        e. coordinates without a CRS -> rejected; an unknown CRS -> halt;
        f. missing connection points or flood data -> halt;
        g. an unsigned geotechnical report -> halt;
        h. site progress without evidence -> rejected; progress is marked
           candidate;
        i. eight PMO prohibition tests, one per capability, each asserting the
           forbidden action is refused;
        j. an expired PMO-02 waiver -> the gate re-blocks;
        k. AT-MEP-v1, AT-INFRA-v1 and AT-SITE-v1 execute with their evidence;
        l. the load test covers the expanded workflow set, not only villa.
  13. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - three completed onboarding checklists with negative scope statements
   - MEP review with per-discipline reviewers and enforced prohibitions
   - all stop conditions for MEP, infrastructure, geotechnical and site
     capabilities
   - CRS-mandatory coordinate handling
   - candidate-only site progress with evidence requirements
   - the eight PMO capabilities with authority limits enforced in code
   - the expiring, aged waiver mechanism
   - AT-MEP-v1, AT-INFRA-v1 and AT-SITE-v1 defined and executed
   - stage 5 evidence: DR reference, an expanded load test, an access review
   - the recorded future expansion stage with its dependencies
   - tests/expansion/mep-*.*, infra-*.*, site-*.*, pmo-*.* covering cases a
     through l
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all twelve test groups.
   - Paste the eight PMO prohibition refusals individually — these are the
     evidence that sheet 06's authority limits are real.
   - Paste the load test results across the expanded workflow set.
   - State, per template, whether it is activatable and what blocks it.
   - Acceptance criterion: every PMO capability refuses its prohibited action,
     every stop condition halts, and no coordinate is accepted without a CRS.

G. COMPLETION CONTRACT
   Definition of Done: three templates onboarded with executed suites, eight
   PMO capabilities with enforced limits, stage 5 evidence assembled, future
   scope recorded.
   Evidence to report: the test outputs, the eight prohibition refusals, the
   load test, the per-template activation status.
   Remaining blockers: reviewer pools for ELEC-BUILDING, MECH-HVAC,
   FIRE-REVIEW and CIVIL-INFRA, tool licences, and rate cards are owner-owned.
   FIRE-REVIEW requires an internal committee per sheet 12 row 6 — report
   whether one exists.
   Next prompt: P16-01, only if the owner has reversed the commerce deferral.
   Otherwise the blueprint's execution scope ends here, with PHASE-16 closed.
```

**المخرجات المتوقعة:** ثلاثة قوالب مُدخَلة، ثماني قدرات PMO بحدود مفروضة، أدلة المرحلة 5.
**التحقق المطلوب:** كل قدرة PMO ترفض فعلها المحظور؛ لا إحداثيات بلا نظام مرجعي.
**الاعتمادية التالية:** `P16-01` — فقط إذا رفع المالك تأجيل التجارة.

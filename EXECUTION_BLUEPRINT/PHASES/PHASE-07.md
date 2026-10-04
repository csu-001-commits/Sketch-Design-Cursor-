# PHASE-07 — الملاحظات والمراجعة والأهلية والتسليم

<!-- phasemeta
id: PHASE-07
depends_on: [PHASE-03, PHASE-06]
criticality: P0
-->

## الغرض من المرحلة

هذه هي المرحلة التي تجعل المنصة **مهنية** لا مجرد مُولِّد نصوص. ثلاثة قرارات
معتمدة تتقاطع فيها:

- `ADR-004`: المخرج المهني هو `Finding` منظم مرتبط بالدليل وبقرار مراجع.
- `ADR-006`: قرار المراجع يرتبط بنسخة وبصمة، والتغيير يعيد الدورة.
- `ADR-010`: «الذكاء يقترح؛ الاعتماد المهني باسم مؤهل محدد النطاق».

والورقة 35 الصف 6 تضع الحد الذي لا يُجاوَز: «لا اعتماد مُرخَّص من الذكاء
الاصطناعي». والورقة 54 الصف 11 (`G10`) تجعل «توقيع المهندس» حاجز إصدار `P0`.

## شروط الدخول

- اكتمال `PHASE-03` (محرك مسارات العمل) و`PHASE-06` (الاستشهادات المُتحقَّقة).

## شروط الخروج

- نجاح `AT-REV-001` (قرارات على مستوى كل finding مع السبب والبصمة والزمن).
- نجاح `AT-REV-002` (الأهلية وتعارض المصالح: المنتهي والمتعارض يُستبعدان).
- نجاح `AT-DEL-001` (تغيير بايت بعد التوقيع يُبطل الربط).
- رفض المراجعة الذاتية.
- المرشّحات الصلبة غير قابلة للتجاوز.
- لا إفراج قبل توقيع مرتبط بالبصمة المُراجَعة.

## المتطلبات المغطاة في هذه المرحلة

`ADR-004`, `ADR-006`, `ADR-010`, `REQ-FND-01`..`REQ-FND-03`,
`REQ-REV-01`..`REQ-REV-07`, `REQ-DEL-01`..`REQ-DEL-05`, `REQ-WF-05`,
`REQ-WF-06`, `REQ-SEC-13`, `REQ-DAT-06`, `REQ-SVC-02`, `REQ-GW-16`

## تحذير مهم

الورقة 13 الصف 3 تحدد «المرشّحات الصلبة» وتقول إن فشلها يعني «استبعاد موثق».
والورقة 13 الصف 10 تضيف القيد الحاسم: «لا تجاوز hard filter» حتى عند انتهاء
المهلة وإعادة الإسناد. أي بناء يسمح بتجاوز إداري لمرشّح صلب يُسقط المساءلة
المهنية كلها.

---

## الأوامر التنفيذية

### P07-01 — مخطط الملاحظات المُنمَّط

<!-- meta
id: P07-01
phase: PHASE-07
title_en: Typed findings schema
prereq: [P06-03]
requirements: [ADR-004, REQ-FND-01, REQ-FND-02, REQ-FND-03]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ مخطط `Finding` بحقوله الواحد والعشرين في الورقة
10، بإلزاماتها الدقيقة ودلالاتها.

**لماذا نحتاجه؟** `ADR-004` ضابط قبوله: «لا تقرير حرج بلا findings». والورقة 10
تحدد لكل حقل نوعه ودرجة إلزامه: بعضها «إلزامي»، وبعضها «عند الادعاء»، وبعضها «بعد
المراجعة»، وبعضها «للآلة». هذه الفروق هي ما يجعل الـfinding قابلاً للقياس.

**ما المتطلبات السابقة؟** `P06-03`.

**ما النتيجة المتوقعة؟** مخطط مُنفَّذ ومُتحقَّق، وواجهة استعلام `GET /v1/findings`.

**كيف نتحقق من نجاحه؟** finding بلا دليل يُرفض؛ وادعاء بلا استشهاد يُرفض؛ ولا
يمكن ضبط `reviewer_decision` إلا من مسار المراجعة.

```text
TASK P07-01 — Typed findings schema

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P07-01
   Phase: PHASE-07 (Findings, review, eligibility and delivery)
   Prerequisites: P06-03
   Requirements covered: ADR-004, REQ-FND-01, REQ-FND-02, REQ-FND-03

B. OBJECTIVE
   Implement the Finding as a typed, validated entity with the twenty-one
   fields the source specifies and their exact obligation levels, so
   professional quality becomes measurable at the item level.

   Why this is necessary: ADR-004 (sheet 02 row 5) makes the typed finding the
   professional output and its acceptance control is "no critical report
   without findings". The source's obligation levels differ per field —
   mandatory, required-when-a-claim-is-made, required-after-review,
   machine-only — and those distinctions are what make precision, recall and
   override rates computable in PHASE-14.

   SCOPE BOUNDARY: the finding entity, its validation and its query API. The
   reviewer decision flow is P07-04. Do not implement the review UI.

C. CONTEXT
   Required inputs, config/registries/finding-schema.json (sheet 10 rows 2-22),
   each as field / type / obligation:
     finding_id UUID or ULID / mandatory
     tenant_id ID / mandatory, derived from identity
     workflow_id and version String and SemVer / mandatory
     project and artifact_version IDs / mandatory
     discipline Enum ARCH, STRUCT, MEP, CIVIL, BIM, HSE / mandatory
     finding_type Enum / mandatory
     severity Enum INFO, LOW, MEDIUM, HIGH, CRITICAL / mandatory
     action_risk R0-R4 / mandatory
     professional_consequence P0-P3 / mandatory
     statement Text / mandatory — one single testable observation
     evidence[] Object[] / mandatory — artifact, page, grid, GUID, hash
     citations[] Object[] / required when a claim is made
     confidence 0..1 / machine only — a calibrated score, not an approval
     recommended_action Code or Text / mandatory — an assignable action
     status Enum OPEN, IN_REVIEW, ACCEPTED, MODIFIED, REJECTED, DEFERRED,
       CLOSED / mandatory
     created_by Object / mandatory — agent, model, prompt and tool versions
     reviewer_decision Enum ACCEPT, MODIFY, REJECT, DEFER, NEEDS_INFO / after
       review
     reason_code Enum / for modification or rejection
     reviewer_comment Text / per decision
     reviewed_hash SHA-256 / for signature
     decision_signature_ref ID / per policy
   Also: config/registries/data-constraints.json has no findings table, but
   review_decisions is UNIQUE (artifact_id, review_version) and append-only.

D. EXECUTION INSTRUCTIONS
   1. Implement the entity with all twenty-one fields and enforce each
      obligation level distinctly in validation. A field that is mandatory at
      creation and a field that is mandatory only after review are different
      rules; implement both rather than one lax schema.
   2. Enforce "one single testable observation" for statement (sheet 10 row 11)
      as a real constraint, not a comment: validate a maximum length, reject
      enumerations and multi-issue text where detectable (for example a
      statement containing multiple numbered items or multiple distinct
      severity claims), and document the heuristic. A compound finding cannot be
      reviewed item-by-item, which breaks the whole measurement model.
   3. Enforce the mandatory evidence array using the locators from P02-03.
      Every evidence object resolves against the referenced artifact version
      and digest; an unresolvable locator invalidates the finding.
   4. Enforce citations conditionally: when the finding's type or statement
      asserts a normative requirement, at least one verified citation from
      P06-03 is required. Implement the condition explicitly by finding_type
      rather than leaving it to the producer's discretion.
   5. Implement confidence as machine-only with the source's semantics: range
      0..1, recorded, and structurally incapable of acting as an approval. Add a
      test asserting confidence has no effect on status transitions.
   6. Implement created_by as a provenance object carrying agent id and version,
      model id and version, prompt version and tool versions, populated from the
      execution trace in P05-01. A finding whose provenance is incomplete is
      invalid — without it, precision cannot be attributed to a version.
   7. Implement status with the source's seven values and a transition guard:
      only the review path (P07-04) may move a finding to ACCEPTED, MODIFIED,
      REJECTED or DEFERRED. An agent, a service identity or an administrator
      cannot set those states. Test it against the highest-privileged identity,
      reinforcing ADR-010 and sheet 35 row 6.
   8. Implement reviewer_decision, reason_code, reviewer_comment, reviewed_hash
      and decision_signature_ref as settable only by P07-04, with
      reviewed_hash bound to the artifact version digest.
   9. Implement a controlled reason_code enumeration (the source gives
      INSUFFICIENT_EVIDENCE as an example in row 19) covering at minimum:
      INSUFFICIENT_EVIDENCE, INCORRECT_CITATION, OUT_OF_SCOPE,
      DUPLICATE, SEVERITY_DISAGREEMENT, FACTUAL_ERROR,
      REQUIRES_SPECIALIST, AWAITING_CLIENT_DATA. Record that this list is a
      DERIVED extension of the source's single example and needs owner
      ratification.
  10. Implement GET /v1/findings per sheet 26 row 14 with cursor pagination and
      findings:read scope, filterable by project, artifact version, discipline,
      severity, status and decision.
  11. Tests:
        a. a finding with no evidence -> rejected;
        b. a finding whose evidence locator does not resolve -> rejected;
        c. a normative finding with no citation -> rejected;
        d. a compound statement -> rejected by the single-observation rule;
        e. confidence 0.99 does not change status and does not substitute for a
           decision;
        f. an agent or admin identity attempting to set ACCEPTED -> refused;
        g. a finding with incomplete created_by provenance -> rejected;
        h. reviewed_hash that does not match the referenced artifact version
           digest -> rejected;
        i. GET /v1/findings is tenant-scoped and its cursor cannot be replayed
           across tenants.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the Finding entity and migration with twenty-one fields
   - per-obligation-level validation
   - the single-observation constraint with a documented heuristic
   - mandatory resolvable evidence and conditional verified citations
   - machine-only confidence with no approval power
   - complete created_by provenance from the execution trace
   - status transition guards restricting review states to the review path
   - the reason_code enumeration, marked DERIVED
   - GET /v1/findings with scoped cursor pagination
   - tests/findings/schema-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - Paste the field-by-field obligation table showing your implementation
     against the twenty-one rows of sheet 10, confirming all twenty-one exist.
   - For case f, name the identity used and paste the refusal.
   - Acceptance criterion: no finding exists without resolvable evidence and
     complete provenance, and no non-reviewer can set a review status.

G. COMPLETION CONTRACT
   Definition of Done: all twenty-one fields implemented with correct
   obligations, guards enforced, query API scoped.
   Evidence to report: the nine test outputs, the twenty-one-field mapping
   table, the privileged-refusal proof.
   Remaining blockers: the reason_code list is DERIVED and needs owner
   ratification; record it as a new open decision.
   Next prompt: P07-02.
```

**المخرجات المتوقعة:** كيان `Finding` بواحد وعشرين حقلاً، حُرّاس انتقال الحالة، `GET /v1/findings`.
**التحقق المطلوب:** لا finding بلا دليل قابل للحل ولا بلا مصدرية كاملة؛ لا هوية غير مراجع تضبط حالة مراجعة.
**الاعتمادية التالية:** `P07-02`.

---

### P07-02 — سجل المراجعين ومصفوفة الأهلية

<!-- meta
id: P07-02
phase: PHASE-07
title_en: Reviewer registry and eligibility matrix
prereq: [P07-01]
requirements: [REQ-REV-01, REQ-REV-02, REQ-INT-02, ADR-010]
-->

**ماذا سينفذ هذا الأمر؟** يبني سجل المراجعين بمجموعاته الخمس عشرة في الورقة 11،
ومصفوفة الأهلية بأكوادها الثمانية في الورقة 12، مع لقطة أهلية قابلة للتدقيق.

**لماذا نحتاجه؟** `ADR-010` ضابط قبوله: «eligibility snapshot + COI + MFA».
والورقة 11 تصنّف كل حقل (`Confidential`, `Restricted`, `Highly restricted`)
وتحدد طريقة التحقق ودورة التجديد — ومعظمها «قبل كل إسناد». والورقة 12 تحدد لكل
كود نطاقاً ومحظورات ومُحفِّز مراجعة ثانية ومدة صلاحية.

**ما المتطلبات السابقة؟** `P07-01`.

**ما النتيجة المتوقعة؟** سجل مراجعين مُصنَّف البيانات، ومصفوفة أهلية مُنفَّذة،
ولقطة أهلية ثابتة لكل إسناد.

**كيف نتحقق من نجاحه؟** عضوية منتهية تُستبعد؛ وطلب خارج النطاق يُرفض؛ ولقطة
الأهلية لا تتغير بعد تسجيلها.

```text
TASK P07-02 — Reviewer registry and eligibility matrix

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P07-02
   Phase: PHASE-07
   Prerequisites: P07-01
   Requirements covered: ADR-010, REQ-REV-01, REQ-REV-02, REQ-INT-02

B. OBJECTIVE
   Implement the reviewer registry with its fifteen field groups, their data
   classifications, verification methods and renewal cadences, plus the
   eligibility matrix with its eight codes, scopes, prohibitions,
   second-review triggers and validity periods — and the immutable eligibility
   snapshot that binds an assignment to the qualifications that applied at that
   moment.

   Why this is necessary: ADR-010's acceptance control is an eligibility
   snapshot plus conflict-of-interest declaration plus MFA. Sheet 11 classifies
   each field group and states that most must be verified before every
   assignment, not annually. Sheet 12 defines, per code, what the reviewer may
   and may not review. Sheet 15 row 6 (CTRL-005) is CRITICAL with the evidence
   "hard-filter tests".

   SCOPE BOUNDARY: the registry, the matrix and the snapshot. Assignment
   matching, COI evaluation and offer handling are P07-03. Reviewer-facing UI
   is out of scope.

C. CONTEXT
   Required inputs, config/registries/reviewer-registry.json derived from sheet
   11 rows 2-16, each as group / field / classification / verification /
   renewal:
     Identity / legal_name / Confidential / strong identity document /
       annual or on change
     Identity / identity_status NOT_STARTED, PENDING, VERIFIED, FAILED,
       EXPIRED / Restricted / identity provider / per provider
     Professional / SCE_reference, never displayed in full / Restricted /
       official SCE channel or documented review / before assignment
     Professional / membership_status and expiry / Internal / official channel
       with dated evidence / before every assignment
     Professional / discipline and subdiscipline / Internal / documents plus
       committee / annual
     Professional / professional_scope — permitted finding types and projects /
       Internal / eligibility matrix / before assignment
     Experience / experience_evidence / Restricted / CV, references, samples /
       every two years
     Assessment / platform_assessment — case-based test and calibration /
       Internal / evaluation / annual
     Legal / agreement_status — liability, confidentiality, signature use /
       Restricted / e-sign and DMS / on amendment
     Conflict / COI_declarations / Highly restricted / declaration plus entity
       graph / every assignment
     Capacity / availability / Internal / calendar or portal / live
     Commercial / rate_card / Highly restricted / contract and finance / per
       contract
     Quality / performance_metrics / Restricted / evaluation / monthly
     Status / approval_status PENDING, APPROVED, CONDITIONAL, SUSPENDED,
       EXPIRED / Internal / committee / continuous
     Security / MFA, device, session / Highly restricted / IAM / live
   And config/registries/eligibility-matrix.json (sheet 12 rows 2-9), each as
   code / task / discipline / conditions / scope / prohibited / second review /
   validity:
     ARCH-RES-VILLA / villa review / architect / membership, assessment,
       experience, agreement, MFA / villas within the workflow / structural,
       fire, approval drawings / P3 or complex egress / 12 months
     STRUCT-LOWRISE / low-rise structural / structural engineer / membership,
       case assessment, approved tools / defined height and scope /
       geotechnical or silent modification / instability or foundations /
       12 months
     ELEC-BUILDING / building electrical / electrical engineer / membership,
       LV and ELV experience, assessment / loads, panels, lighting / utility
       and fire outside scope / life safety / 12 months
     MECH-HVAC / HVAC / mechanical engineer / membership, loads and
       ventilation, assessment / HVAC for the category / fire without scope /
       smoke or IAQ P3 / 12 months
     FIRE-REVIEW / fire / qualified specialist / experience, certificates,
       internal committee / findings within the contract / official authority
       approval / every P3 / 6-12 months
     BIM-COORD / BIM coordination / BIM coordinator / IFC, BCF, IDS assessment
       / quality and clashes / discipline signature / clash P3 / 12 months
     QS-QTO / quantities / QS or cost / measurement rules, traceability
       assessment / QTO and BOQ / price without a source / high value /
       12 months
     CIVIL-INFRA / infrastructure / civil engineer / networks, roads, GIS and
       survey literacy / roads and networks / legal survey, geotechnical /
       flood or utility / 12 months

D. EXECUTION INSTRUCTIONS
   1. Implement the registry with per-field data classification enforced by
      access control, not by convention. A Highly restricted field (COI
      declarations, rate card, MFA and session data) is readable only by the
      roles the RBAC register permits, and never returned in a list endpoint.
      SCE_reference is never displayed in full — implement masking at the
      serialization layer so no endpoint can leak it.
   2. Implement verification records rather than bare status fields. Each
      verified field carries: the verification method used, the evidence
      reference, the checker identity, the check timestamp and the expiry. A
      status with no verification record is NOT_VERIFIED. Use the two-mode
      verification abstraction from P06-03 step 9 for SCE membership, with
      scraping excluded.
   3. Implement renewal cadence enforcement with the source's granularity. The
      critical case is "before every assignment" for membership status and
      professional scope: the system re-checks at assignment time and a stale
      check does not satisfy it. Implement expiry as computed from the check
      timestamp, so a lapsed verification automatically stops qualifying.
   4. Implement the eligibility matrix with all eight codes and their five
      operative parts: conditions (all must hold), scope (what may be
      reviewed), prohibitions (what may never be reviewed even if otherwise
      qualified), second-review trigger, and validity period.
   5. Implement prohibitions as absolute. A reviewer holding ARCH-RES-VILLA is
      prohibited from structural, fire and approval drawings regardless of any
      other code they hold — unless they separately hold the code that permits
      it. Prohibitions are evaluated per code and per requested task, and a
      prohibition hit is a hard exclusion.
   6. Implement the eligibility snapshot as an immutable record created at
      assignment time, capturing: the reviewer identity, every code held with
      its validity window, every verification record state, the COI
      declaration reference, the MFA and step-up state, and the matrix version
      used. Enforce immutability in storage as in P02-02. This is the object
      ADR-010 requires and the object an auditor will ask for years later.
   7. Implement approval_status with the five source values, where SUSPENDED
      and EXPIRED are immediate hard exclusions and CONDITIONAL carries the
      conditions and is only usable within them.
   8. Implement the performance metrics container for sheet 11 row 14 and
      sheet 17 rows 5-6 (override rate, inter-reviewer agreement), with the
      explicit rule from sheet 13 row 11: no automated penalty without human
      review. Metrics are recorded and surfaced; they never automatically
      suspend a reviewer. Add a test asserting no code path auto-suspends.
   9. Implement rate_card as Highly restricted and versioned, consumed only by
      the pricing engine in PHASE-08, never exposed to a project user.
  10. Tests:
        a. a reviewer with expired membership -> not eligible, with the reason;
        b. a reviewer whose membership check is stale at assignment time -> not
           eligible even though the stored status says valid;
        c. a reviewer holding ARCH-RES-VILLA requested for a structural task ->
           excluded by prohibition;
        d. a SUSPENDED reviewer -> excluded;
        e. a CONDITIONAL reviewer outside their conditions -> excluded; inside
           them -> eligible;
        f. SCE_reference is never returned in full by any endpoint — assert
           across the serialization layer;
        g. a Highly restricted field is not readable by a project-scoped role;
        h. an eligibility snapshot cannot be modified after creation;
        i. a poor performance metric does not auto-suspend;
        j. a FIRE-REVIEW task at P3 -> second-review trigger fires.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the reviewer registry with classification-enforced access and SCE masking
   - verification records with method, evidence, checker, timestamp and expiry
   - renewal cadence enforcement including before-every-assignment semantics
   - the eight-code eligibility matrix with absolute prohibitions
   - the immutable eligibility snapshot with the matrix version
   - approval_status semantics including CONDITIONAL
   - performance metrics with no automated penalty
   - versioned, restricted rate cards
   - tests/review/registry-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - Paste the field-group table showing all fifteen groups implemented with
     their classification and renewal rule.
   - Paste the eight eligibility codes with their prohibitions as implemented.
   - Acceptance criterion: no reviewer qualifies on a stale check, no
     prohibition is bypassable, and the snapshot is immutable.

G. COMPLETION CONTRACT
   Definition of Done: fifteen field groups and eight codes implemented,
   verification records enforced, snapshot immutable, no auto-penalty.
   Evidence to report: the ten test outputs, the field-group table, the code
   and prohibition table.
   Remaining blockers: SCE has no proven verification API (sheet 23 row 3), so
   membership verification runs in documented-manual-review mode. Report that
   explicitly as an operational dependency with a named owner.
   Next prompt: P07-03.
```

**المخرجات المتوقعة:** سجل مراجعين مُصنَّف، مصفوفة أهلية بثمانية أكواد، لقطة أهلية ثابتة.
**التحقق المطلوب:** لا تأهيل على فحص قديم؛ لا تجاوز لمحظور؛ اللقطة غير قابلة للتعديل.
**الاعتمادية التالية:** `P07-03`.

---

### P07-03 — الإسناد: المرشّحات الصلبة وتعارض المصالح والاستقلالية

<!-- meta
id: P07-03
phase: PHASE-07
title_en: Assignment with hard filters, COI and independence
prereq: [P07-02]
requirements: [REQ-REV-03, REQ-REV-04, REQ-REV-05, REQ-REV-06, REQ-WF-05]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ مراحل الإسناد العشر في الورقة 13: ملف المهمة،
المرشّحات الصلبة، تعارض المصالح، الاستقلالية، الترتيب بأوزانه، العرض، القبول،
قفل المخرج، إدارة SLA، ومتابعة الجودة.

**لماذا نحتاجه؟** `AT-REV-002` يحدد السيناريو بدقة: ثلاثة مراجعين — منتهي
الصلاحية، وذو تعارض، ومؤهل — والمتوقع «استبعاد الأولين وعرض للثالث». والورقة 13
الصف 5 تفرض: «منشئ المخرج لا يراجع نفسه؛ فصل four-eyes».

**ما المتطلبات السابقة؟** `P07-02`.

**ما النتيجة المتوقعة؟** خط إسناد بعشر مراحل، ترتيب قابل للإعادة، وعرض بمهلة.

**كيف نتحقق من نجاحه؟** `AT-REV-002` ناجح؛ ومحاولة إسناد منشئ المخرج لنفسه
تُرفض؛ وإعادة الإسناد بعد المهلة تُطبّق كل المرشّحات مرة أخرى.

```text
TASK P07-03 — Assignment with hard filters, COI and independence

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P07-03
   Phase: PHASE-07
   Prerequisites: P07-02
   Requirements covered: REQ-REV-03, REQ-REV-04, REQ-REV-05, REQ-REV-06,
                         REQ-WF-05

B. OBJECTIVE
   Implement the ten-stage reviewer assignment pipeline with non-overridable
   hard filters, conflict-of-interest evaluation, enforced independence,
   reproducible weighted ranking, and a time-bounded offer and acceptance flow.

   Why this is necessary: AT-REV-002 (sheet 16 row 6) specifies the test — an
   expired reviewer, a conflicted reviewer and a qualified reviewer, expecting
   the first two excluded and the third offered. Sheet 13 row 3 makes hard
   filter failure a documented exclusion. Sheet 13 row 5 forbids self-review
   and requires four-eyes separation. Sheet 13 row 10 forbids bypassing a hard
   filter even during SLA-driven reassignment.

   SCOPE BOUNDARY: assignment, offer and acceptance. The decision flow is
   P07-04. Notification delivery uses the abstracted interface from P03-05.

C. CONTEXT
   Required inputs, sheet 13 rows 2-11, the ten stages as number / stage /
   data or rule / actor / acceptance control:
     1 create task profile / discipline, project type, R and P, location,
       deadline, independence / CTL-03 and REV-01 / schema valid
     2 hard filters / identity VERIFIED, membership, eligibility, agreement,
       MFA, capacity / REV-01 / failure equals a documented exclusion
     3 COI check / client, owner, designer, contractor, supplier, prior
       relationships / REV-01 plus reviewer / declaration per assignment
     4 independence / the producer of the output does not review it; four-eyes
       separation / policy engine / pass or an approved exception
     5 ranking / discipline 30 percent, eligibility 20 percent, quality
       15 percent, availability 15 percent, sector 10 percent, language or
       location 10 percent / REV-01 / weights approved per workflow
     6 offer / scope, duration, fee, confidentiality / Review Ops / OFFERED
       with an expiry
     7 accept and declare / acceptance, COI, availability, scope
       responsibility / reviewer / ACCEPTED, else the next candidate
     8 lock artifact / SHA-256 lock and eligibility snapshot recorded /
       DOC-01 / IN_REVIEW only after lock
     9 SLA handling / reminder then expiry then reassignment / CTL-03 / never
       bypass a hard filter
    10 quality follow-up / decisions, reason codes, time, complaints /
       EVAL-01 / no automated penalty without review
   Also sheet 09 rows 17-21: the Review sub-state machine OFFERED, ACCEPTED,
   IN_REVIEW, DECIDED, NEEDS_INFORMATION, EXPIRED with the controls COI, hash
   pinned, all decided, RFI and reassign.

D. EXECUTION INSTRUCTIONS
   1. Implement the task profile with every field stage 1 names, validated
      against a schema. An invalid profile stops the pipeline.
   2. Implement hard filters as a non-overridable gate. There is no
      administrative parameter, role or flag that skips them. Each failure
      produces a documented exclusion record naming the filter, the reviewer
      and the evidence. Add a test attempting an override as the
      highest-privileged identity and asserting refusal.
   3. Implement COI evaluation over the relationship types the source names —
      client, owner, designer, contractor, supplier and prior relationships —
      using an entity graph as sheet 11 row 11 specifies. A declared or
      detected conflict is a hard exclusion. A fresh declaration is required
      per assignment; a previous declaration does not carry over.
   4. Implement independence in the policy engine, not in the matching code, so
      it is auditable: the actor or agent version that produced the artifact
      cannot be the reviewer, and four-eyes separation is enforced for the
      second review. Sheet 13 row 4 permits an approved exception — implement
      it as a recorded, dual-approved, scoped and expiring exception, never a
      silent bypass, and never applicable to the hard filters of stage 2.
   5. Implement ranking with the six weights summing to 100, loaded from
      per-workflow configuration since the source says weights are approved per
      workflow. Ranking is reproducible: the same candidate pool, the same
      weights version and the same input data produce the same order. Record
      the weights version and the per-criterion scores on the assignment so a
      selection can be explained later.
   6. Implement the offer with scope, duration, fee and confidentiality terms
      and a hard expiry, emitting OFFERED. On expiry, emit EXPIRED and advance
      to the next ranked candidate — re-running every hard filter and the COI
      check for that candidate, per sheet 13 row 10.
   7. Implement acceptance requiring four declarations from the reviewer:
      acceptance of the task, the COI declaration, availability confirmation
      and scope responsibility acknowledgement. Missing any one leaves the
      offer unaccepted.
   8. Implement the lock-before-review ordering, which is ADR-006's acceptance
      control: the artifact is locked (P02-02) and the eligibility snapshot
      (P07-02) is recorded before the review state becomes IN_REVIEW. Add a
      test asserting IN_REVIEW is unreachable without both.
   9. Implement SLA handling per stage 9 using P03-05's timers: reminder, then
      expiry, then reassignment, with the hard-filter re-application.
  10. Implement the quality follow-up record per stage 10: decisions, reason
      codes, elapsed time and complaints, feeding PHASE-14, with the explicit
      no-automated-penalty rule already enforced in P07-02.
  11. Implement the no-eligible-reviewer outcome honestly: when the pool is
      empty after filters, the task does not proceed. It records
      NO_ELIGIBLE_REVIEWER with the exclusion reasons for every candidate and
      escalates to Review Ops. Sheet 05 row 37 names "no qualified reviewer" as
      a stop condition for REV-01.
  12. Tests — AT-REV-002 plus the pipeline suite:
        a. AT-REV-002: an expired reviewer, a conflicted reviewer and a
           qualified reviewer in one pool -> the first two excluded with
           documented reasons, the third offered;
        b. an attempt to override a hard filter as the highest-privileged
           identity -> refused;
        c. the producing actor is the only candidate -> NO_ELIGIBLE_REVIEWER,
           never a self-review;
        d. a second review assigned to the first reviewer -> refused by
           four-eyes;
        e. an approved independence exception -> recorded, dual-approved,
           scoped and expiring; it does not relax any stage-2 filter;
        f. identical pool plus identical weights version -> identical ranking,
           twice, with per-criterion scores recorded;
        g. offer expiry -> EXPIRED, next candidate offered, and every hard
           filter and the COI check re-run for that candidate;
        h. acceptance missing the COI declaration -> not accepted;
        i. attempt to reach IN_REVIEW without an artifact lock -> refused;
           without an eligibility snapshot -> refused;
        j. empty pool -> NO_ELIGIBLE_REVIEWER with per-candidate exclusion
           reasons and an escalation record.
  13. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the validated task profile
   - non-overridable hard filters with documented exclusion records
   - COI evaluation over an entity graph with per-assignment declarations
   - policy-engine independence with recorded, expiring exceptions
   - reproducible six-weight ranking with recorded per-criterion scores
   - time-bounded offers with filter re-application on reassignment
   - four-part acceptance
   - enforced lock-and-snapshot-before-IN_REVIEW ordering
   - SLA ladder and quality follow-up records
   - NO_ELIGIBLE_REVIEWER as an honest terminal outcome
   - tests/review/at-rev-002.* plus cases b through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-REV-002 output with the exclusion reasons for the first two
     candidates.
   - Paste the override-refusal from case b naming the identity used.
   - Paste both ranking runs from case f showing identical order and scores.
   - Paste the case g output showing filters re-run for the next candidate.
   - Acceptance criterion: no hard filter is ever bypassed, no self-review is
     possible, and ranking is reproducible and explainable.

G. COMPLETION CONTRACT
   Definition of Done: ten stages implemented, AT-REV-002 green, independence
   and hard filters proven non-overridable, ranking reproducible.
   Evidence to report: AT-REV-002 output, the ten test results, the ranking
   reproducibility proof.
   Remaining blockers: per-workflow ranking weights need owner approval
   (sheet 13 row 5 says weights are approved per workflow). Report the default
   you used as the source's stated split and flag it for ratification.
   Next prompt: P07-04.
```

**المخرجات المتوقعة:** خط إسناد بعشر مراحل، مرشّحات صلبة غير قابلة للتجاوز، ترتيب قابل للإعادة.
**التحقق المطلوب:** `AT-REV-002` ناجح؛ رفض المراجعة الذاتية؛ إعادة تطبيق المرشّحات عند إعادة الإسناد.
**الاعتمادية التالية:** `P07-04`.

---

### P07-04 — قرارات المراجعة على مستوى كل ملاحظة

<!-- meta
id: P07-04
phase: PHASE-07
title_en: Item-level review decisions and reason codes
prereq: [P07-03]
requirements: [ADR-004, REQ-FND-01, REQ-DAT-06, REQ-WF-05, REQ-API-05]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ قرار المراجع لكل finding على حدة: `ACCEPT`,
`MODIFY`, `REJECT`, `DEFER`, `NEEDS_INFO`، مع رمز سبب وتعليق وبصمة وزمن، في سجل
إضافي فقط.

**لماذا نحتاجه؟** `AT-REV-001` (الورقة 16 الصف 5) يحدد المتوقع: «كل قرار وreason
وhash وtime محفوظ». والورقة 15 الصف 5 (`CTRL-004`) بأولوية `CRITICAL`. والورقة 39
الصف 10 تفرض `UNIQUE (artifact_id, review_version)` و«append-only».

**ما المتطلبات السابقة؟** `P07-03`.

**ما النتيجة المتوقعة؟** قرارات مُسجَّلة لا تُعدَّل، وانتقال `DECIDED` فقط عند
حسم كل بند مادي.

**كيف نتحقق من نجاحه؟** `AT-REV-001` ناجح؛ ومحاولة تعديل قرار مُسجَّل تُرفض؛
والانتقال إلى `DECIDED` يُرفض إن بقي بند مادي غير محسوم.

```text
TASK P07-04 — Item-level review decisions and reason codes

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P07-04
   Phase: PHASE-07
   Prerequisites: P07-03
   Requirements covered: ADR-004, REQ-FND-01, REQ-DAT-06, REQ-WF-05,
                         REQ-API-05

B. OBJECTIVE
   Implement per-finding reviewer decisions with the five decision values,
   mandatory reason codes for modification and rejection, the reviewed digest,
   the timestamp and the reviewer identity, stored append-only, with the
   DECIDED transition gated on every material item being resolved.

   Why this is necessary: AT-REV-001 (sheet 16 row 5) expects every decision,
   reason, hash and time to be stored. Sheet 15 row 5 (CTRL-004) is CRITICAL
   with the evidence "schema tests plus sample". Sheet 09 row 19 gates the
   DECIDED transition on "all decided". Sheet 39 row 10 requires UNIQUE
   (artifact_id, review_version) and append-only storage.

   SCOPE BOUNDARY: the decision record, its API and the state gate. Signature
   and delivery are P07-05.

C. CONTEXT
   Required inputs:
     - sheet 26 row 15: POST /v1/reviews/{id}/decisions, scope reviews:decide,
       concurrency by review hash or etag, emits review.decision_recorded,
       responses 200/409/422
     - sheet 26 row 16: POST /v1/reviews/{id}/return for return and RFI, emits
       review.returned, 202
     - sheet 34 row 10: EV-05 ReviewDecisionRecorded review.decision.v1,
       required payload reviewId, decision, reviewerId, ordering key reviewId,
       validation "append-only review evidence"
     - sheet 10 rows 18-22: reviewer_decision, reason_code, reviewer_comment,
       reviewed_hash, decision_signature_ref
     - sheet 09 row 20: IN_REVIEW plus request_info -> NEEDS_INFORMATION with
       the control RFI

D. EXECUTION INSTRUCTIONS
   1. Implement the ReviewDecision entity with UNIQUE (artifact_id,
      review_version) and storage-level append-only enforcement as in P01-05.
      A decision is never updated; a changed opinion is a new review version.
   2. Implement the five decision values with their obligations:
        - ACCEPT: no reason code required, comment optional;
        - MODIFY: reason code required, comment required, and the modified
          statement recorded as a new finding revision linked to the original —
          the original is never edited in place;
        - REJECT: reason code required, comment required;
        - DEFER: reason code required plus a defer-until condition or date;
        - NEEDS_INFO: a structured RFI required, naming what is missing and
          from whom, driving the NEEDS_INFORMATION transition.
   3. Bind every decision to the reviewed digest. The decision records
      reviewed_hash taken from the locked artifact version, and a decision
      submitted against a stale digest returns 409 — the reviewer must see the
      current locked bytes. This is ADR-006 at the decision boundary.
   4. Implement concurrency control per sheet 26 row 15 using the review hash
      or etag, so two concurrent submissions cannot both apply.
   5. Implement the material-item gate for DECIDED: define "material" by
      severity and professional consequence (configurable, defaulting to
      everything above INFO, and always including every P2 and P3 item), and
      refuse the DECIDED transition while any material item is undecided. The
      refusal names the outstanding items.
   6. Implement reviewer authority checks at decision time, not only at
      assignment time: the deciding identity must be the accepted reviewer, must
      still pass the hard filters, must still hold the eligibility code covering
      that finding's discipline and type, and must have a fresh step-up
      authentication per sheet 04 row 6. A decision from a reviewer whose
      membership lapsed between acceptance and decision is refused.
   7. Enforce scope per finding: a reviewer decides only findings inside their
      eligibility scope. A finding outside it is not decidable by them and is
      routed for an additional assignment rather than silently accepted.
   8. Implement the second review where triggered (P07-02 and P07-03): the
      second reviewer's decisions are recorded independently, disagreements are
      preserved rather than overwritten, and the resolution path is recorded.
      Sheet 17 row 6 measures inter-reviewer agreement, which requires both
      opinions to survive.
   9. Implement the return and RFI endpoint with the structured RFI from
      P03-02 step 7.
  10. Emit review.decision.v1 per the envelope, with reviewId as the ordering
      key, through the outbox.
  11. Implement the decision audit view: for any artifact version, the complete
      decision history with reviewer, decision, reason, digest and time —
      queryable, since this is what AT-REV-001 verifies and what an auditor
      needs.
  12. Tests — AT-REV-001 plus the decision suite:
        a. AT-REV-001: modify a finding, reject one, request information on one
           -> every decision stored with its reason code, reviewed digest,
           timestamp and reviewer identity; verify by reading them back;
        b. MODIFY creates a linked finding revision and leaves the original
           intact;
        c. an attempt to update a stored decision -> refused at the storage
           level;
        d. a decision against a stale digest -> 409;
        e. two concurrent decisions on the same review -> one applies, the
           other 409;
        f. DECIDED while a P3 item is undecided -> refused, naming it;
        g. a reviewer whose membership lapsed after acceptance -> decision
           refused;
        h. a decision without fresh step-up authentication -> refused;
        i. a reviewer deciding a finding outside their eligibility scope ->
           refused;
        j. second review disagreement -> both opinions retained and queryable;
        k. MODIFY without a reason code -> 422;
        l. the emitted event conforms to the envelope with reviewId as ordering
           key.
  13. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the ReviewDecision entity with its uniqueness constraint and append-only
     storage
   - the five decision values with per-value obligations
   - digest binding with 409 on staleness
   - etag concurrency control
   - the material-item gate for DECIDED
   - decision-time authority, freshness, scope and step-up checks
   - independent second-review recording with disagreement preservation
   - the structured return and RFI endpoint
   - review.decision.v1 emission
   - the decision audit view
   - tests/review/at-rev-001.* plus cases b through l
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-REV-001 output including the read-back of each stored decision
     showing reason, digest and time.
   - Paste the storage-level refusal from case c.
   - Paste the case f refusal naming the outstanding P3 item.
   - Paste the case g and h refusals.
   - Acceptance criterion: every decision is immutable, digest-bound,
     authority-checked and step-up-authenticated, and DECIDED is unreachable
     with an open material item.

G. COMPLETION CONTRACT
   Definition of Done: AT-REV-001 green, decisions append-only and
   digest-bound, authority re-checked at decision time, second-review
   disagreements preserved.
   Evidence to report: AT-REV-001 output, the twelve test results, the audit
   view sample.
   Remaining blockers: the materiality definition is DERIVED beyond the
   source's phrase "all material items decided" (sheet 08 row 10). Record the
   default you implemented and flag it for owner ratification.
   Next prompt: P07-05.
```

**المخرجات المتوقعة:** قرارات إضافية فقط مرتبطة بالبصمة، بوابة البنود المادية، سجل قرارات قابل للتدقيق.
**التحقق المطلوب:** `AT-REV-001` ناجح؛ لا تعديل لقرار مُسجَّل؛ لا `DECIDED` مع بند مادي مفتوح.
**الاعتمادية التالية:** `P07-05`.

---

### P07-05 — القفل والتوقيع على البصمة وحزمة التسليم

<!-- meta
id: P07-05
phase: PHASE-07
title_en: Lock, hash-bound signature and the delivery package
prereq: [P07-04]
requirements: [ADR-006, ADR-010, REQ-DEL-01, REQ-DEL-05, REQ-SEC-13, REQ-SVC-02, REQ-WF-06]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ خطوات التسليم من القفل إلى التوقيع: `step-up MFA`،
توقيع مرتبط بالبصمة والقرار والنطاق، وحزمة تسليم بـmanifest وشهادة وQR.

**لماذا نحتاجه؟** `ADR-006` ضابط قبوله «قفل قبل القرار»، و`AT-DEL-001` يحدد
الاختبار: «وقّع ثم غيّر byte» والمتوقع «`INVALIDATED` ويلزم توقيع جديد». والورقة
27 الصف 15 (`SEC-14`) تضع ضوابط التوقيع الإلكتروني الخمسة: «الهوية والقصد
والبصمة والطابع الزمني والشهادة والإبطال».

**ما المتطلبات السابقة؟** `P07-04`.

**ما النتيجة المتوقعة؟** توقيع مرتبط بالبصمة، وحزمة تسليم ثابتة، وإبطال آلي عند
التغيير.

**كيف نتحقق من نجاحه؟** `AT-DEL-001` ناجح؛ والتوقيع يتطلب step-up؛ ولا توقيع من
هوية خدمة.

```text
TASK P07-05 — Lock, hash-bound signature and the delivery package

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P07-05
   Phase: PHASE-07
   Prerequisites: P07-04
   Requirements covered: ADR-006, ADR-010, REQ-DEL-01, REQ-DEL-05,
                         REQ-SEC-13, REQ-WF-06

B. OBJECTIVE
   Implement the delivery chain from lock through signature: step-up
   authenticated signing bound to the reviewed digest, the decision and the
   scope; and a fixed delivery package with a manifest, certificate and
   verification token.

   Why this is necessary: ADR-006's acceptance control is "lock before
   decision" and AT-DEL-001 (sheet 16 row 7) tests signing then mutating one
   byte, expecting INVALIDATED and a required new signature. Sheet 27 row 15
   (SEC-14) names the five e-signature controls: identity, intent, hash,
   timestamp, certificate and revocation. Sheet 05 row 6 (DOC-01) states the
   package is generated from approved findings with a manifest and digest and
   "never signs on behalf of an engineer".

   SCOPE BOUNDARY: lock, sign and package generation. Release and the public
   verification page are P07-06. Payment gating is PHASE-08.

C. CONTEXT
   Required inputs, sheet 14 rows 2-11 (the ten delivery steps), of which this
   prompt implements steps 1 through 6:
     1 prepare candidate / findings, files, sources, versions / CANDIDATE /
       DOC-01 / manifest draft
     2 quality gate / schema, citations, rights, states / PASS / GOV-01 / no
       blocking defect
     3 lock / artifact_version, SHA-256, immutable reference / LOCKED /
       evidence service / hash plus timestamp
     4 assign / eligibility snapshot, COI, acceptance / IN_REVIEW / REV-01 /
       snapshot id
     5 decide findings / a decision per material finding / DECIDED / reviewer /
       reason codes
     6 sign decision / step-up MFA, signature over the hash, the decision and
       the scope / SIGNED / reviewer and provider / signature reference
   Also sheet 26 row 18: POST /v1/deliveries/{id}/sign, scope
   deliveries:sign, concurrency by hash or request, emits delivery.signed,
   responses 202/409.
   Also sheet 09 rows 24-26: LOCKED plus sign -> SIGNED binding the hash;
   SIGNED plus hash_mismatch -> INVALIDATED requiring a new review.

D. EXECUTION INSTRUCTIONS
   1. Implement the candidate preparation (step 1): assemble the findings,
      their evidence manifests, the cited sources with versions, and the
      component versions, into a draft manifest.
   2. Implement the quality gate (step 2) as a blocking check before lock:
      every finding validates against its schema; every claim has a verified
      citation; every cited source's rights permit quotation; every finding's
      status is terminal for this delivery. A blocking defect prevents lock and
      names the defect. This is GOV-01's role in sheet 05 row 5, which is
      explicit that it "does not replace the specialist".
   3. Reuse the lock from P02-02 for step 3 and enforce the ordering: lock
      before assignment, assignment before IN_REVIEW, decisions before
      signature. Add an ordering test for the full chain.
   4. Implement the signature with all five SEC-14 controls:
        - identity: the signer is the accepted qualified reviewer, verified
          against the eligibility snapshot, with their identity_status
          VERIFIED;
        - intent: an explicit, recorded act of signing that states what is
          being attested and its scope limits; not a side effect of saving;
        - hash: the signature covers a canonical payload containing the
          reviewed artifact digest, the decision set digest, the reviewer
          identity, the eligibility snapshot id and the scope statement;
        - timestamp: a trusted timestamp recorded with the signature;
        - certificate and revocation: the signing credential reference and a
          revocation check at verification time.
   5. Require fresh step-up authentication at signing per sheet 04 row 6 and
      sheet 14 row 7. A signature attempt without a step-up inside the
      freshness window is refused.
   6. Enforce that no service identity can sign. Only a human qualified
      reviewer within their recorded scope may produce a signature. Add a test
      attempting to sign as the platform owner service identity and as the
      highest-privileged staff role, asserting refusal in both cases. This is
      ADR-010 and sheet 35 row 6 at the signature boundary, and sheet 04 row 2
      forbids PLATFORM_OWNER from a discipline signature without eligibility.
   7. Implement scope limitation on the signature: the signature states what
      the reviewer is and is not attesting, derived from their eligibility
      scope and the matrix prohibitions. A signature cannot be presented as
      covering a discipline the signer is prohibited from.
   8. Implement automatic invalidation: the integrity verification from P02-02
      runs against signed artifacts, and a digest mismatch transitions the
      delivery to INVALIDATED, voids the signature linkage, emits an event and
      requires a new review cycle. Nothing downstream may consume an
      INVALIDATED delivery.
   9. Implement the package generation per sheet 05 row 6: the report, a
      manifest listing every component with its digest, a certificate carrying
      the signature and scope, and a verification token for the P07-06 page.
      The package itself is an artifact version with its own digest and is
      locked on creation.
  10. Tests — AT-DEL-001 plus the signing suite:
        a. AT-DEL-001: sign a delivery, then alter one byte of the artifact ->
           integrity verification detects it, the delivery becomes INVALIDATED,
           the signature linkage is void, and a new signature is required.
           Paste the full sequence;
        b. an attempt to sign without fresh step-up -> refused;
        c. an attempt to sign as a service identity -> refused;
        d. an attempt to sign as the highest-privileged staff role without
           eligibility -> refused;
        e. a signature whose scope would cover a prohibited discipline ->
           refused;
        f. an attempt to lock with a blocking quality defect -> refused, naming
           the defect;
        g. ordering violations: assign before lock -> refused; sign before all
           material decisions -> refused;
        h. a revoked signing credential -> verification reports the signature
           as invalid;
        i. consuming an INVALIDATED delivery -> refused;
        j. the generated package is itself locked and its manifest digests all
           match their components.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - candidate preparation and the blocking quality gate
   - the enforced lock, assign, decide, sign ordering
   - the signature with all five SEC-14 controls over a canonical payload
   - mandatory fresh step-up at signing
   - the no-service-identity-signing invariant
   - scope-limited signatures respecting matrix prohibitions
   - automatic INVALIDATED transition on digest mismatch
   - the locked delivery package with manifest, certificate and token
   - tests/delivery/at-del-001.* plus cases b through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the full AT-DEL-001 sequence showing sign, mutate, detect,
     INVALIDATED, new signature required.
   - Paste the refusals for cases c and d naming the identities used.
   - Paste the ordering violation refusals from case g.
   - Acceptance criterion: a signature always binds to exact reviewed bytes, no
     non-human can sign, and a single byte change always invalidates.

G. COMPLETION CONTRACT
   Definition of Done: AT-DEL-001 green, five e-signature controls
   implemented, step-up required, signing restricted to eligible humans,
   package locked and manifest-verified.
   Evidence to report: the AT-DEL-001 sequence, the ten test results, the
   package manifest verification.
   Remaining blockers: the signing credential and timestamp authority are
   procurement dependencies. If a real e-signature provider is not configured,
   state that the implementation ran against a local signing key and that
   SEC-14's certificate and revocation controls are therefore only partially
   evidenced.
   Next prompt: P07-06.
```

**المخرجات المتوقعة:** توقيع بخمسة ضوابط، ترتيب مفروض، إبطال آلي، حزمة مقفلة.
**التحقق المطلوب:** `AT-DEL-001` ناجح؛ لا توقيع من هوية خدمة؛ تغيير بايت يُبطل.
**الاعتمادية التالية:** `P07-06`.

---

### P07-06 — الإفراج وصفحة التحقق والإبطال

<!-- meta
id: P07-06
phase: PHASE-07
title_en: Release, public verification and revocation
prereq: [P07-05]
requirements: [REQ-DEL-02, REQ-DEL-03, REQ-DEL-04, REQ-API-01, REQ-API-05]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ خطوات التسليم 7 إلى 10: البوابة التجارية،
والإفراج، وصفحة تحقق عامة محدودة، وقاعدة التغيير بعد التوقيع.

**لماذا نحتاجه؟** الورقة 14 الصف 8 تشترط «مرحلة مدفوعة أو تفويض عقدي» قبل
الإفراج. والورقة 14 الصف 10 تحدد صفحة تحقق «محدودة تعرض hash والحالة» مع
«Revocation». والورقة 38 الصف 11 (`G-06`) حاجز إصدار: «لا مخرجات غير معتمدة».

**ما المتطلبات السابقة؟** `P07-05`.

**ما النتيجة المتوقعة؟** إفراج مُبوَّب، وصفحة تحقق لا تُسرّب، وسياسة إبطال.

**كيف نتحقق من نجاحه؟** لا إفراج بلا دليل دفع أو تفويض؛ وصفحة التحقق لا تكشف
هوية المشروع أو العميل أو المراجع.

```text
TASK P07-06 — Release, public verification and revocation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P07-06
   Phase: PHASE-07
   Prerequisites: P07-05
   Requirements covered: REQ-DEL-02, REQ-DEL-03, REQ-DEL-04, REQ-API-01,
                         REQ-API-05

B. OBJECTIVE
   Implement delivery steps 7 through 10: the commercial gate before release,
   the release itself, a minimal public verification surface, and the
   change-after-signature rule that forces a new version and a new review.

   Why this is necessary: sheet 14 row 8 requires a paid milestone or a
   contractual authorization as payment evidence before release is allowed.
   Sheet 14 row 10 specifies a limited verification page showing the digest and
   the status, with revocation. Sheet 14 row 11 forbids silent replacement.
   Sheet 38 row 11 (G-06) is a release blocker whose pass criterion is "no
   unapproved deliverables".

   SCOPE BOUNDARY: release gating, the public verification endpoint and
   revocation. The payment system itself is PHASE-08 — here, the gate consumes
   a payment-evidence interface and a contractual-authorization record, and
   must deny when neither is satisfied.

C. CONTEXT
   Required inputs, sheet 14 rows 8-11:
     7 commercial gate / a paid milestone or contractual authorization /
       release allowed / FIN-02 and PM / payment evidence
     8 release / PDF, manifest, certificate, QR / RELEASED / DOC-01 / delivery
       id
     9 verify / a limited verification page showing hash and status / ACTIVE /
       verification service / revocation
    10 change after sign / any change means a new version, a new digest and a
       new review / INVALIDATED / system / no silent replacement
   Also sheet 26 row 19: POST /v1/deliveries/{id}/release, scope
   deliveries:release, emits delivery.released, responses 202/409.
   Also sheet 26 row 20: GET /v1/verify/{token}, public token, rate limited,
   emits verification.viewed, responses 200/404/410.
   Also sheet 34 row 12: EV-07 DeliverableReleased deliverable.released.v1,
   required payload deliverableId, approvedAt, validation "HITL approval
   mandatory".

D. EXECUTION INSTRUCTIONS
   1. Implement the commercial gate as a hard precondition with exactly two
      satisfying conditions: verified payment evidence for the relevant
      milestone, or a recorded contractual authorization naming the authorizing
      party, the contract reference and the scope. Neither present means
      release is denied. A screenshot, a claim or an operator assertion is not
      evidence — sheet 21 row 5 is explicit that a transfer image never opens a
      milestone.
   2. Implement release requiring all of: delivery state SIGNED, a valid
      signature whose credential is not revoked, a current digest matching the
      signed digest, and the commercial gate satisfied. Any failure returns 409
      naming the unmet condition.
   3. Enforce the HITL validation rule from sheet 34 row 12: the release event
      cannot be emitted without a recorded human approval. Add a test asserting
      a release attempt with no reviewer signature is impossible, satisfying
      G-06's "no unapproved deliverables".
   4. Implement the public verification endpoint with deliberate minimalism. It
      returns only: the digest, the delivery status (ACTIVE, REVOKED or
      INVALIDATED), the issue date, and the scope statement from the
      certificate. It must not return the project name, the client identity,
      the reviewer name, the findings, the file, or any identifier that enables
      enumeration. Treat it as a hostile surface.
   5. Harden the verification token: high-entropy, non-sequential, not derived
      from the delivery id, revocable, and rate limited per the source's
      control. Return 404 for an unknown token and 410 for a token whose
      delivery is revoked or invalidated, per the source's response codes. Add
      an enumeration test that confirms a sequential scan yields nothing.
   6. Implement revocation: an authorized role can revoke a released delivery
      with a recorded reason, after which verification reports REVOKED and the
      package download is refused. Revocation is audited and emits an event.
   7. Implement the change-after-signature rule end to end: any change to a
      released delivery's content creates a new artifact version, invalidates
      the prior signature linkage, sets the previous delivery to INVALIDATED,
      and requires a full new review and signature cycle. There is no code path
      that replaces content under an existing delivery id. Prove it with an
      architectural test.
   8. Implement delivery lineage so a client can see that delivery v2
      supersedes v1 and why, satisfying "no silent replacement".
   9. Emit deliverable.released.v1 through the outbox with the required
      payload.
  10. Tests:
        a. release with neither payment evidence nor contractual authorization
           -> denied, naming the unmet condition;
        b. release with a contractual authorization -> allowed, with the
           authorization recorded;
        c. release of a delivery with no signature -> impossible (G-06);
        d. release with a revoked signing credential -> denied;
        e. release when the current digest no longer matches the signed digest
           -> denied;
        f. the verification response contains no project, client, reviewer or
           finding data — assert field-by-field against an allowlist;
        g. sequential token enumeration -> no information disclosed; rate limit
           engages;
        h. an unknown token -> 404; a revoked delivery's token -> 410;
        i. revocation -> verification reports REVOKED and the download is
           refused;
        j. an attempt to replace content under an existing delivery id ->
           architecturally impossible; the change produces a new version with
           the old one INVALIDATED and lineage recorded.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the two-condition commercial gate with evidence requirements
   - release preconditions with 409 reporting
   - the HITL-mandatory release event
   - the minimal, hardened public verification endpoint
   - revocable, enumeration-resistant, rate-limited tokens
   - revocation with audit and event
   - the architecturally enforced change-after-signature rule with lineage
   - deliverable.released.v1 emission
   - tests/delivery/release-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - Paste the verification response beside its field allowlist for case f.
   - Paste the enumeration test result for case g.
   - Paste the architectural test for case j, then weaken it, show failure,
     restore it.
   - Acceptance criterion: nothing releases without human approval and
     commercial authorization, the public surface leaks nothing, and content
     can never be silently replaced.

G. COMPLETION CONTRACT
   Definition of Done: release gated on signature and commercial evidence, the
   public surface minimal and hardened, revocation working, silent replacement
   impossible.
   Evidence to report: the ten test outputs, the allowlist comparison, the
   enumeration result, the architectural test both ways.
   Remaining blockers: real payment evidence arrives in PHASE-08; until then
   release runs on contractual authorization only. State that clearly.
   Next prompt: P08-01. PHASE-07 exit requires AT-REV-001, AT-REV-002 and
   AT-DEL-001 green, self-review refused, hard filters proven
   non-overridable, and no release without a signature.
```

**المخرجات المتوقعة:** بوابة تجارية بشرطين، صفحة تحقق محدودة ومُحصَّنة، إبطال، نسب الإصدارات.
**التحقق المطلوب:** لا إفراج بلا توقيع وتفويض؛ لا تسريب من السطح العام؛ لا استبدال صامت.
**الاعتمادية التالية:** `P08-01`.

# PHASE-12 — المسح والالتقاط

<!-- phasemeta
id: PHASE-12
depends_on: [PHASE-02, PHASE-06, PHASE-11]
criticality: P1
-->

## الغرض من المرحلة

الورقة 49 تحدد سبعة أنماط التقاط، والورقة 66 تحدد قيودها الهندسية، والورقة 50
تحدد عقود الـAPI والأحداث. والقيد الحاكم في الورقة 57 الصف 6 (`A05`): «قياسات
LiDAR ليست مساحة هندسية معتمدة»، والأثر «مسؤولية الدقة»، والتنفيذ المطلوب:
«عتبات ثقة وتحقق بشري إلزامي».

كما أن الورقة 49 الصف 4 تضع قيداً تقنياً صريحاً: التحليل الحيّ يرسل «إطارات
وأحداث مُعيَّنة، **لا** كل إطار إلى LLM».

## شروط الدخول

- اكتمال `PHASE-02` (خط الأدلة) و`PHASE-06`، وتوافر ضوابط خصوصية المسح من
  `P11-04`.

## شروط الخروج

- مصفوفة أجهزة مُختبَرة.
- الموافقة والحجب والحذف مُثبتة.
- التحليل الحيّ يُعيّن الإطارات داخل ميزانية زمن وتكلفة مقيسة.
- مخرج LiDAR يحمل ثقة وإخلاء مسؤولية صريحاً عن المساحة، مع تحقق بشري إلزامي.

## المتطلبات المغطاة في هذه المرحلة

`REQ-SCN-01`..`REQ-SCN-06`, `REQ-GW-15`, `REQ-SEC-02`

---

## الأوامر التنفيذية

### P12-01 — أنماط الالتقاط والموافقة

<!-- meta
id: P12-01
phase: PHASE-12
title_en: Capture modes, consent and privacy
prereq: [P11-04]
requirements: [REQ-SCN-01, REQ-SCN-02, REQ-SCN-05, REQ-SCN-06]
-->

**ماذا سينفذ هذا الأمر؟** يبني أنماط الالتقاط على الويب: الصورة، والفيديو
الموجَّه، والتحليل الحيّ بتعيين إطارات، والقياس اليدوي — مع الموافقة والحجب
والبدائل.

**لماذا نحتاجه؟** الورقة 54 الصف 6 (`G05`) حاجز إصدار `P0`: «صلاحيات الكاميرا
وPDPL — موافقة، حذف، حجب، DPA». والورقة 49 الصف 8 تحدد لكل نمط «بديلاً» عند تعذر
الصلاحية، فالمنتج يجب أن يعمل على جهاز لا يمنح الكاميرا.

**ما المتطلبات السابقة؟** `P11-04`.

**ما النتيجة المتوقعة؟** أنماط التقاط تعمل على متصفح الجوال بحالات واجهة محددة
وبدائل، مع موافقة مُسجَّلة.

**كيف نتحقق من نجاحه؟** رفض صلاحية الكاميرا يُنتج البديل لا خطأ؛ وسحب الموافقة
يوقف الالتقاط ويحذف ما يلزم.

```text
TASK P12-01 — Capture modes, consent and privacy

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P12-01
   Phase: PHASE-12 (Scan and capture)
   Prerequisites: P11-04 (scan privacy controls and the DPIA template)
   Requirements covered: REQ-SCN-01, REQ-SCN-02, REQ-SCN-05, REQ-SCN-06

B. OBJECTIVE
   Implement the web capture modes — photo, guided video, sampled live
   analysis and manual measures — with their UX states, fallbacks, verification
   and the consent and privacy controls the source makes a P0 release blocker.

   Why this is necessary: sheet 54 row 6 (G05) is a P0 blocker for camera
   permissions and PDPL, requiring consent, deletion, redaction and a DPA.
   Sheet 49 gives every mode an explicit fallback, which means the product must
   work on a device that denies the camera. Sheet 49 row 4 forbids sending
   every frame to a model.

   SCOPE BOUNDARY: the capture surfaces, consent, privacy and the client-side
   pipeline. The evidence API and events are P12-02. Native LiDAR is P12-03.

C. CONTEXT
   Required inputs, sheet 49 rows 2-8, each as mode / entry surface / device
   capability / captured payload / UX states / fallback / verification:
     Photo / mobile web or PWA / camera permission / photo plus filtered EXIF
       plus consent / ready, capture, preview, upload / file picker / upload
       checksum
     Guided video / mobile web / getUserMedia on a supported browser / short
       clips plus timestamps / record, pause, review / video upload / quality
       checklist
     Live analysis / mobile web / video stream plus network / sampled frames
       and events, NOT every frame to an LLM / live, buffering, result /
       store-and-analyze / latency budget plus cost
     LiDAR RoomPlan / native iOS companion / supported Apple LiDAR device /
       USDZ or structured room geometry plus confidence / scan, quality, sync /
       guided capture on web / accuracy disclaimers
     Manual measures / web / any device / typed dimensions plus units plus
       reference / measure, confirm / laser meter upload / unit and
       plausibility
     Evidence package / platform backend / any capture source / project_id,
       tenant_id, consent, provenance / draft, uploaded, validated, locked /
       retry queue / immutable hashes
     Privacy / all capture modes / permission and retention policy / redaction
       plus data region plus access scope / consent, revoke / manual
       submission / PDPL and security review
   And sheet 66 rows 2-3: quick photo uses on-device preview and guided
   capture with the constraint "consent, no implied measurements"; live
   analysis uses sampled frames with websocket or SSE status and the constraint
   "bandwidth and latency budget; no continuous raw stream by default".
   Also sheet 54 row 12 (G11): the customer portal must be RTL, mobile-camera
   capable and accessible.

D. EXECUTION INSTRUCTIONS
   1. Build the capture surface as a mobile-web progressive experience that is
      RTL-first and accessible per sheet 54 row 12, with each mode's exact UX
      states from the register implemented as real states, including the
      buffering state for live analysis.
   2. Implement consent before capture, not after: a mode cannot start without
      an active, purpose-specific consent record from P11-01, covering the
      capture purpose, the retention, the data region and the access scope.
      Revocation stops capture immediately and triggers the deletion path from
      P11-02.
   3. Implement permission handling with the source's fallbacks as first-class
      paths, not error screens: a denied camera permission routes to the file
      picker; an unsupported getUserMedia routes to video upload; a poor
      network routes live analysis to store-and-analyze; an absent laser meter
      routes to typed manual measures. Each fallback is tested.
   4. Implement EXIF filtering per sheet 49 row 2: strip or retain metadata by
      an explicit allowlist. Location data is retained only when it serves a
      declared purpose with consent, because a site photograph's coordinates
      are both operationally valuable and personal data. Record the decision
      per field.
   5. Implement redaction for images that may contain people, per sheet 49
      row 8 and the P11-04 control set: detect and blur faces and other
      identifying features before the image leaves the device where feasible,
      or immediately on ingestion otherwise, keeping the unredacted original
      only where a declared purpose and consent permit and under restricted
      access. Record which path applied.
   6. Implement the no-implied-measurement rule from sheet 66 row 2: the photo
      mode must not present any dimension, area or distance derived from an
      image. The UI states explicitly that photographs are evidence, not
      measurements. Add a test asserting no measurement field is produced by the
      photo path.
   7. Implement live analysis with event and keyframe triggering per sheet 71
      row 8 and sheet 63 row 8:
        - on-device filtering first, so frames that carry no new information
          are never uploaded;
        - sampling driven by events and keyframes, with a configured maximum
          frames per interval;
        - a measured latency budget and a cost budget enforced through the
          P04-06 budget controller, so a live session cannot run away;
        - no continuous raw stream by default, per sheet 66 row 3;
        - a safe disable path per sheet 71 row 8's fallback: AI commentary can
          be turned off without breaking capture.
      Add a test that counts frames sent to the gateway over a session and
      asserts it is bounded and far below the frame rate.
   8. Implement manual measures with unit and plausibility validation per
      sheet 49 row 6: units are mandatory and typed, a reference is recorded,
      and an implausible value against the project context is flagged for
      confirmation rather than silently accepted.
   9. Implement the guided video quality checklist per sheet 49 row 3 and the
      capture quality signal that sheet 50 row 7 defines as the
      capture.quality.updated event, feeding the scan ingestion dashboard
      panel from P10-02.
  10. Implement client-side integrity: a checksum computed before upload and
      verified server-side per sheet 49 row 2's verification column.
  11. Tests:
        a. capture without an active consent -> refused;
        b. consent revocation mid-session -> capture stops, the deletion path
           triggers;
        c. denied camera permission -> the file picker fallback works end to
           end;
        d. unsupported getUserMedia -> the video upload fallback works;
        e. degraded network -> live analysis falls back to store-and-analyze;
        f. EXIF handling -> only allowlisted fields survive; location retained
           only with a declared purpose;
        g. an image containing a face -> redacted per policy, with the applied
           path recorded;
        h. the photo path produces no measurement field;
        i. a live session -> frames sent to the gateway are bounded and the
           cost stays within budget; paste the frame count and the frame rate;
        j. disabling AI commentary -> capture continues working;
        k. a manual measure without a unit -> rejected; an implausible value ->
           flagged;
        l. client checksum mismatch on upload -> rejected;
        m. the surface is RTL and passes the project's accessibility checks.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the RTL-first, accessible mobile-web capture surface with per-mode UX
     states
   - consent-before-capture with immediate revocation effect
   - all five fallback paths as tested first-class flows
   - EXIF allowlist filtering with per-field decisions recorded
   - person redaction with the applied path recorded
   - the enforced no-implied-measurement rule
   - event and keyframe sampled live analysis within measured latency and cost
     budgets, with a safe disable path
   - manual measures with unit and plausibility validation
   - the guided video quality checklist and the quality signal
   - client-side checksums verified server-side
   - tests/scan/capture-*.* covering cases a through m
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all thirteen tests.
   - For case i, paste the session frame count, the camera frame rate and the
     recorded cost, demonstrating that not every frame reached a model.
   - Paste the EXIF before and after field lists.
   - Paste the accessibility and RTL check results.
   - Acceptance criterion: no capture occurs without consent, every fallback
     works, no measurement is implied from a photograph, and live analysis is
     provably bounded.

G. COMPLETION CONTRACT
   Definition of Done: four web capture modes working with consent, privacy,
   fallbacks and bounded live analysis.
   Evidence to report: the thirteen test outputs, the frame-count evidence, the
   EXIF comparison, the accessibility results.
   Remaining blockers: the DPIA requires privacy-owner completion and a DPA is
   owner-owned, both of which gate sheet 54 row 6 (G05) and sheet 76 row 10
   (G09). Report them as outstanding.
   Next prompt: P12-02.
```

**المخرجات المتوقعة:** سطح التقاط RTL متاح، موافقة قبل الالتقاط، بدائل مُختبَرة، تحليل حيّ محدود.
**التحقق المطلوب:** عدد الإطارات المُرسَلة محدود ومُثبت؛ لا قياس مُستنتَج من صورة.
**الاعتمادية التالية:** `P12-02`.

---

### P12-02 — عقود المسح وخط الأدلة

<!-- meta
id: P12-02
phase: PHASE-12
title_en: Scan API contracts and the evidence pipeline
prereq: [P12-01]
requirements: [REQ-SCN-03, REQ-SCN-01, REQ-SEC-02, REQ-API-05]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ العمليات والأحداث الثمانية في الورقة 50، وخط
حزمة الأدلة من المسودة إلى القفل.

**لماذا نحتاجه؟** الورقة 50 تحدد لكل عملية حقولها ومصادقتها وidempotency
وتحققها، وثلاثة أحداث بإصدار `v1`. والورقة 49 الصف 7 تحدد حالات حزمة الأدلة:
`draft` → `uploaded` → `validated` → `locked` مع «retry queue» و«immutable
hashes».

**ما المتطلبات السابقة؟** `P12-01`.

**ما النتيجة المتوقعة؟** ثماني عمليات وأحداث مُنفَّذة، ورفع قابل للاستئناف،
وحزمة أدلة مقفلة.

**كيف نتحقق من نجاحه؟** انقطاع الرفع يُستأنف بلا فقدان ولا تكرار؛ والحزمة المقفلة
بصمتها تُتحقَّق.

```text
TASK P12-02 — Scan API contracts and the evidence pipeline

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P12-02
   Phase: PHASE-12
   Prerequisites: P12-01
   Requirements covered: REQ-SCN-01, REQ-SCN-03, REQ-SEC-02, REQ-API-05

B. OBJECTIVE
   Implement the eight scan operations and events with their exact request
   fields, authorization, idempotency and validation, plus the evidence package
   pipeline from draft to locked with resumable uploads.

   Why this is necessary: sheet 50 specifies each operation's contract
   precisely, including which require an Idempotency-Key and which validate
   entitlement and quota. Sheet 49 row 7 defines the evidence package states
   and requires a retry queue and immutable hashes. Sheet 75 row 8 requires
   resumable encrypted upload with an offline queue and evidence integrity
   verification.

   SCOPE BOUNDARY: the API, the events and the evidence pipeline. Do not
   implement analysis agents — the analysis request dispatches through the
   existing gateway. LiDAR is P12-03.

C. CONTEXT
   Required inputs, sheet 50 rows 2-9, each as operation / method or event /
   request fields / response / auth / idempotency / validation:
     Start capture / POST /v1/projects/{id}/capture-sessions / mode, device,
       consent / session_id, upload_urls / project.write / Idempotency-Key /
       tenant plus consent
     Upload chunk / PUT signed upload URL / file chunk, hash / etag /
       short-lived token / chunk id / size plus MIME plus AV
     Commit evidence / POST /v1/evidence-packages / session_id, manifest,
       hashes / evidence_id, status / evidence.write / Idempotency-Key /
       schema plus provenance
     Analysis request / POST /v1/analysis-runs / evidence_id, agent_bundle /
       run_id, accepted / agent.execute / Idempotency-Key / entitlement plus
       quota
     Progress stream / GET /v1/runs/{id}/events / Last-Event-ID / SSE states
       plus sequence / runs.read / event sequence / auth plus resume
     Capture event / capture.quality.updated v1 / session_id, score, issues /
       quality signal / service auth / event_id / score bounded
     Evidence event / evidence.package.ready v1 / evidence_id, project_id /
       immutable reference / service auth / event_id / tenant scope
     Agent event / agent.run.completed v1 / run_id, version, artifacts /
       signed artifact refs / service auth / event_id / no cross-tenant
   Note on entitlement: the analysis request validates entitlement and quota.
   Entitlement in its full commercial sense is deferred (sheet 68 row 8), so
   implement the quota and the single-tenant entitlement check now, with the
   seam for PHASE-16, and do not build the marketplace.

D. EXECUTION INSTRUCTIONS
   1. Implement capture-session creation with consent and tenant validation,
      returning scoped, short-lived upload targets, under a required
      Idempotency-Key.
   2. Implement chunked upload against signed URLs with per-chunk hashes and
      etags, validating size, declared MIME against real magic bytes, and
      routing every chunk through the AV path from P02-01 before the assembled
      object is readable. An assembled object is never readable before its scan
      passes.
   3. Implement resumability per sheet 75 row 8: an interrupted upload resumes
      from the last confirmed chunk without re-sending confirmed chunks and
      without creating duplicates. Implement an offline queue on the client so
      a capture taken without connectivity is retained and uploaded later, with
      its original capture timestamp preserved and distinguished from the
      upload timestamp.
   4. Implement evidence commit building on P02-03's manifest: the commit
      validates the schema and the provenance, verifies every declared hash
      against the stored bytes, and transitions the package through draft,
      uploaded, validated and locked. Locking uses P02-02 so the package is
      immutable.
   5. Implement the analysis request: validate the evidence package is locked
      and validated, check quota and the tenant entitlement, then dispatch
      through the P04-01 gateway with the appropriate task class from sheet 71
      (live scan narration or extraction). Never call a provider directly.
   6. Implement the progress SSE stream with Last-Event-ID resumption and a
      monotonic per-run sequence, reusing P04-01's redaction so no secrets or
      personal data enter the stream.
   7. Implement the three events with the common envelope from P03-03, their
      declared ordering keys and their validation rules, including the bounded
      score check on capture.quality.updated and the cross-tenant prohibition
      on agent.run.completed.
   8. Implement the retry queue for failed commits per sheet 49 row 7, with
      bounded retries, a DLQ and operator visibility through the P10-03 safe
      actions.
   9. Implement evidence integrity verification as a scheduled check per
      sheet 75 row 8, reusing P02-02's verification sweep, so a corrupted
      evidence object is detected rather than discovered during a review.
  10. Tests:
        a. capture-session creation without consent -> refused;
        b. a chunk whose declared MIME differs from its magic bytes ->
           rejected;
        c. an assembled object is unreadable until its AV scan passes;
        d. an interrupted upload resumes without re-sending confirmed chunks
           and without duplicates;
        e. an offline capture uploads later with its original capture timestamp
           preserved and distinct from the upload timestamp;
        f. a commit whose declared hash does not match stored bytes ->
           rejected, naming the item;
        g. a commit with a repeated Idempotency-Key -> one package, same
           receipt;
        h. an analysis request against an unlocked package -> refused;
        i. an analysis request over quota -> refused with the quota reason;
        j. the SSE stream resumes from Last-Event-ID with no gap and no
           duplicate, and contains no personal data;
        k. all three events conform to the envelope with their ordering keys;
        l. a capture.quality.updated event with an out-of-range score ->
           rejected;
        m. a failed commit -> retried, then DLQ with its history;
        n. the scheduled integrity check detects a corrupted evidence object.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the five operations and three events of sheet 50
   - chunked, scanned, magic-byte-validated upload
   - resumable upload plus a client offline queue with timestamp separation
   - the four-state evidence package pipeline ending in an immutable lock
   - the gateway-dispatched analysis request with quota and entitlement checks
   - the resumable, redacted progress stream
   - the retry queue with DLQ and operator visibility
   - the scheduled evidence integrity check
   - tests/scan/api-*.* covering cases a through n
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all fourteen tests.
   - For case d, paste the chunk list before and after resumption.
   - For case e, paste the two timestamps showing they are distinct.
   - For case j, paste the stream transcript across the resumption point.
   - Acceptance criterion: an interrupted or offline capture never loses or
     duplicates data, nothing is readable before its scan passes, and no
     analysis runs on an unlocked package.

G. COMPLETION CONTRACT
   Definition of Done: the eight contracts implemented, uploads resumable and
   scanned, packages immutable, analysis gateway-routed and quota-checked.
   Evidence to report: the fourteen test outputs, the resumption evidence, the
   timestamp separation, the stream transcript.
   Remaining blockers: commercial entitlement is deferred to PHASE-16. Confirm
   the seam exists without building the marketplace.
   Next prompt: P12-03.
```

**المخرجات المتوقعة:** ثماني عمليات وأحداث، رفع قابل للاستئناف وطابور غير متصل، حزمة أدلة مقفلة.
**التحقق المطلوب:** لا فقدان ولا تكرار عند الانقطاع؛ لا تحليل على حزمة غير مقفلة.
**الاعتمادية التالية:** `P12-03`.

---

### P12-03 — LiDAR والدقة والتحقق البشري الإلزامي

<!-- meta
id: P12-03
phase: PHASE-12
title_en: Optional native LiDAR with confidence and mandatory human validation
prereq: [P12-02]
requirements: [REQ-SCN-04, REQ-GW-15, REQ-SCN-01, REQ-OBS-04]
-->

**ماذا سينفذ هذا الأمر؟** يبني التكامل الاختياري مع تطبيق iOS أصلي لـLiDAR، مع
درجة ثقة وإخلاء مسؤولية صريح وتحقق بشري إلزامي قبل أي استخدام هندسي.

**لماذا نحتاجه؟** الورقة 57 الصف 6 (`A05`) تحدد الأثر: «مسؤولية الدقة»، والدليل
المطلوب: «تقرير تحقق ميداني للجهاز». والورقة 66 الصف 6 صريحة: «ليست مساحة
معتمدة». والورقة 71 الصف 7 تضع القاعدة التقنية: «لا LLM لحقيقة القياس المرجعية»
و«أرسل الهندسة لا الفيديو».

**ما المتطلبات السابقة؟** `P12-02`.

**ما النتيجة المتوقعة؟** مسار LiDAR اختياري يُنتج هندسة بثقة، ولا يُستخدم هندسياً
قبل تحقق بشري.

**كيف نتحقق من نجاحه؟** ثقة منخفضة تُنتج `request rescan` و«provisional»؛ ولا
نموذج يُنتج قياساً مرجعياً.

```text
TASK P12-03 — Optional native LiDAR with confidence and mandatory human validation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P12-03
   Phase: PHASE-12
   Prerequisites: P12-02
   Requirements covered: REQ-SCN-01, REQ-SCN-04, REQ-GW-15, REQ-OBS-04

B. OBJECTIVE
   Implement the optional native iOS LiDAR path producing structured room
   geometry with a confidence score, an explicit non-survey disclaimer, and
   mandatory human validation before any engineering use.

   Why this is necessary: sheet 57 row 6 (A05) names the impact as accuracy
   liability, requires confidence thresholds and mandatory human validation,
   and names the acceptance evidence as a device field validation report.
   Sheet 66 row 6 states the output is "not a certified survey". Sheet 71 row 7
   forbids using an LLM for measurement ground truth and requires sending
   geometry rather than video. Sheet 61 row 7 defines the low-confidence
   support scenario: request a rescan and mark the result provisional, with a
   qualified engineer escalation, before approval.

   SCOPE BOUNDARY: the LiDAR ingestion path, confidence handling, disclaimers
   and validation gating. Shipping a native iOS application is an owner
   decision with its own release process — build the integration contract and
   the server side, and treat the client as an optional companion whose
   availability you report honestly.

C. CONTEXT
   Required inputs:
     - sheet 49 row 5: mode LiDAR RoomPlan; entry surface native iOS
       companion; capability a supported Apple LiDAR device; payload USDZ or
       structured room geometry plus confidence; UX states scan, quality, sync;
       fallback guided capture on web; verification accuracy disclaimers
     - sheet 66 row 4: optional native iOS companion; RoomPlan or ARKit
       compatible devices; output room geometry plus a quality score;
       constraint native entitlement and compatible hardware
     - sheet 54 row 7 (G06): LiDAR precision disclaimers, supported devices,
       confidence and validation, P0, UNVERIFIED, release blocker YES
     - the evidence pipeline from P12-02

D. EXECUTION INSTRUCTIONS
   1. Define the geometry ingestion contract: structured room geometry —
      planes, openings, dimensions and their units — plus a per-element and
      overall confidence, the device model, the OS version, the capture
      duration, the coverage estimate and the scan session reference. Accept
      USDZ or an equivalent structured format; do not accept raw video, per
      sheet 71 row 7's "send geometry not video".
   2. Implement a supported-device allowlist: the server validates the
      reported device against the devices actually field-validated, and an
      unvalidated device's output is accepted only as UNVALIDATED_DEVICE with
      a lower trust class. Sheet 54 row 7 names supported devices as part of
      the gate, so an unknown device cannot silently produce trusted geometry.
   3. Implement confidence thresholds with three outcomes rather than two:
        - above the high threshold: geometry is usable as provisional input,
          still requiring human validation before engineering use;
        - between thresholds: marked PROVISIONAL_LOW with a rescan
          recommendation;
        - below the low threshold: rejected for engineering use, with a rescan
          request per sheet 61 row 7.
      The thresholds are configuration, initially PROPOSED, and must be set
      from the field validation report, not guessed.
   4. Implement mandatory human validation as a hard gate, which is the core of
      A05: LiDAR-derived geometry cannot enter a finding, a quantity, a
      drawing-check or any engineering conclusion until a qualified person has
      validated it against an independent reference — a known dimension, a tape
      measure or a laser reading. Record the validator identity, the reference
      used, the deviation found and the decision. Add a test asserting
      unvalidated geometry cannot be consumed by any engineering path.
   5. Implement the known-dimension check from sheet 71 row 7's quality check:
      the operator supplies at least one independently measured dimension, the
      system compares it to the scan, and records the deviation. A deviation
      beyond tolerance downgrades the scan regardless of its reported
      confidence.
   6. Implement the disclaimer as data, not as UI text alone: every artifact,
      finding, report and delivery package that incorporates LiDAR-derived
      geometry carries a machine-readable non-survey declaration and a human
      readable statement in Arabic and English, stating that the measurement is
      not a certified survey and naming the validation performed. Add a test
      asserting a package containing LiDAR-derived data cannot be released
      without it.
   7. Enforce the no-LLM-for-measurement rule structurally: the measurement
      values come only from the deterministic scan pipeline or a human entry.
      Add a test with a gateway double asserting no model is invoked to produce,
      adjust or interpolate a dimension. A model may describe or classify a
      space; it may not measure it.
   8. Implement the web fallback per sheet 49 row 5: on a device without LiDAR,
      the guided capture path from P12-01 plus manual measures is offered, and
      the resulting evidence is clearly distinguished in type and trust class.
   9. Implement the scan ingestion telemetry from sheet 73 row 8: frame drops,
      upload latency, geometry confidence and scan completion, dimensioned by
      device, OS and project, feeding the P10-02 panel and its low-quality
      alert.
  10. Produce the device field validation report required by A05 and G06, for
      every device you can actually test: the device and OS, the test
      environment, the reference measurements, the scan results, the deviations,
      the derived confidence thresholds and the conclusion. If you can test no
      device, the report records that and the gate stays UNVERIFIED — do not
      derive thresholds from a datasheet.
  11. Tests:
        a. raw video submitted to the geometry endpoint -> rejected;
        b. an unvalidated device -> accepted only as UNVALIDATED_DEVICE with a
           lower trust class;
        c. confidence below the low threshold -> rejected for engineering use
           with a rescan request;
        d. confidence between thresholds -> PROVISIONAL_LOW with a rescan
           recommendation;
        e. unvalidated geometry -> cannot be consumed by any engineering path;
           assert across findings, quantities and reports;
        f. a known-dimension deviation beyond tolerance -> downgrades the scan
           despite high reported confidence;
        g. a package containing LiDAR-derived data without the non-survey
           declaration -> cannot be released;
        h. a gateway double asserts no model was invoked to produce or adjust a
           dimension;
        i. a device without LiDAR -> the web fallback produces evidence with a
           distinct type and trust class;
        j. the scan telemetry panel receives confidence and completion signals
           and the low-quality alert fires.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the structured geometry ingestion contract rejecting raw video
   - the supported-device allowlist with an UNVALIDATED_DEVICE trust class
   - three-tier confidence handling with rescan requests
   - the mandatory human validation gate with recorded reference and deviation
   - the known-dimension comparison with tolerance-based downgrade
   - the machine-readable and bilingual non-survey declaration, enforced at
     release
   - the structurally enforced no-LLM-for-measurement rule
   - the web fallback with a distinct trust class
   - scan ingestion telemetry feeding the dashboard and alert
   - docs/evidence/G06-lidar-field-validation/ with the device report or an
     honest statement that no device was tested
   - tests/scan/lidar-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - Paste case e showing refusal across all three engineering paths.
   - Paste the gateway double assertion from case h.
   - Paste the field validation report, or state plainly that no supported
     device was available and that G06 therefore remains UNVERIFIED.
   - Acceptance criterion: no LiDAR geometry reaches an engineering conclusion
     without human validation, no model produces a measurement, and no package
     ships without the non-survey declaration.

G. COMPLETION CONTRACT
   Definition of Done: the geometry path implemented with confidence tiers and
   a hard validation gate, disclaimers enforced as data, no model measurement,
   telemetry flowing.
   Evidence to report: the ten test outputs, the engineering-path refusals, the
   no-model assertion, the field validation report or its absence.
   Remaining blockers: shipping a native iOS companion, obtaining supported
   devices and running the field validation are owner-owned. Sheet 54 row 7
   (G06) stays a P0 release blocker until the field report exists. Say so.
   Next prompt: P13-01. PHASE-12 exit requires the device matrix tested,
   consent and deletion proven, live analysis bounded, and LiDAR output gated
   behind human validation with its disclaimer.
```

**المخرجات المتوقعة:** عقد هندسة مُنمَّط، ثلاث طبقات ثقة، بوابة تحقق بشري إلزامية، إخلاء مسؤولية كبيانات.
**التحقق المطلوب:** لا هندسة غير مُتحقَّقة تصل إلى استنتاج هندسي؛ لا نموذج يُنتج قياساً.
**الاعتمادية التالية:** `P13-01`.

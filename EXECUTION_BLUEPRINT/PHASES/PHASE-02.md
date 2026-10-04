# PHASE-02 — الأدلة والملفات وسلامة المخرجات

<!-- phasemeta
id: PHASE-02
depends_on: [PHASE-01]
criticality: P0
-->

## الغرض من المرحلة

كل ما تنتجه هذه المنصة يستند إلى ملفات العميل: مخططات، تقارير تربة، نماذج IFC،
صور موقع. وكل قرار مهني سيُوقَّع على **بصمة** نسخة محددة من مخرج محدد. لذلك
نحتاج طبقتين قبل أي ذكاء: بوابة ملفات آمنة، ومخزن مخرجات بإصدارات وبصمات لا
تتغير.

الورقة 02 الصف 7 (ADR-006) هي القيد الحاكم: «قرار المراجع يرتبط بنسخة وبصمة
SHA-256؛ التغيير يعيد الدورة». وبدون بصمة موثوقة لا معنى لتوقيع ولا لتسليم.

## شروط الدخول

- اكتمال `PHASE-01`: الهوية والعزل والسياسة والتدقيق تعمل.

## شروط الخروج

- نجاح `AT-FILE-001`: ملف `EICAR` و`zip bomb` يُحجران بلا أي تحليل وبلا أي نداء
  نموذج، مع تنبيه.
- إصدارات المخرجات مع `SHA-256` وقفل الكائن مُثبتة.
- تغيير بايت واحد في مخرج موقَّع يُكتشف ويُبطل الربط.

## المتطلبات المغطاة في هذه المرحلة

`ADR-006`, `REQ-SEC-02`, `REQ-DAT-05`, `REQ-FND-02`, `REQ-DEL-04`, `REQ-API-01`

## تحذير مهم

لا يُسمح بأي تحليل أو استخراج أو نداء نموذج على ملف قبل أن يمر فحص البرمجيات
الضارة بنجاح. الورقة 16 الصف 14 صريحة: المتوقع هو «لا parsing/LLM + alert».
تنفيذ الفحص بعد التحليل، أو بالتوازي معه، يبطل الضابط.

---

## الأوامر التنفيذية

### P02-01 — بوابة الملفات والحجر الصحي

<!-- meta
id: P02-01
phase: PHASE-02
title_en: File gateway with scanning and quarantine
prereq: [P01-05]
requirements: [REQ-SEC-02, REQ-DAT-05, REQ-API-01]
-->

**ماذا سينفذ هذا الأمر؟** يبني مسار رفع الملفات: رابط رفع مُوقَّع مسبقاً، حدود
حجم ونوع، فحص برمجيات ضارة، تحليل في بيئة معزولة، وحجر صحي عند الاكتشاف.

**لماذا نحتاجه؟** الضابط `SEC-04` و`CTRL-015` بأولوية `CRITICAL`. وبوابة الملفات
هي السطح الأكثر عرضة للهجوم في المنصة: ملف العميل مُدخَل غير موثوق بطبيعته،
وسيُمرَّر لاحقاً إلى مُحلِّلات ونماذج.

**ما المتطلبات السابقة؟** `P01-05`.

**ما النتيجة المتوقعة؟** مسار رفع آمن مع حالات `uploaded`/`quarantined`، وأحداث
`file.uploaded` و`file.quarantined`.

**كيف نتحقق من نجاحه؟** `AT-FILE-001` بملف EICAR وzip bomb: لا تحليل، لا نداء
نموذج، تنبيه مُسجَّل.

```text
TASK P02-01 — File gateway with scanning and quarantine

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P02-01
   Phase: PHASE-02 (Evidence, files and artifact integrity)
   Prerequisites: P01-05 (audit store available for quarantine events)
   Requirements covered: REQ-SEC-02, REQ-DAT-05, REQ-API-01

B. OBJECTIVE
   Build the untrusted-file ingestion path: pre-signed upload, enforced size and
   type limits, malware scan, sandboxed parsing, and quarantine on detection,
   with the absolute rule that nothing parses or reaches a model before the scan
   passes.

   Why this is necessary: sheet 27 row 5 (SEC-04) and sheet 15 row 16
   (CTRL-015) are both CRITICAL. Sheet 16 row 14 (AT-FILE-001) states the
   expected result verbatim as "no parsing/LLM plus alert". The file gateway is
   the platform's largest attack surface: a customer drawing is untrusted input
   by definition and will later be handed to parsers and models.

   SCOPE BOUNDARY: ingestion, scanning, quarantine and the evidence record.
   Do not implement document understanding, OCR, page extraction or any model
   call — that is PHASE-05 behind the gateway. Do not implement the scan and
   capture product surface — that is PHASE-12.

C. CONTEXT
   Required inputs:
     - sheet 26 row 4: POST /v1/uploads/init returns an upload link then scans;
       scope files:write; emits file.uploaded or file.quarantined; responses
       201/413/415
     - sheet 33 row 8: POST /v1/projects/{id}/evidence requires
       Idempotency-Key, signed upload, AV scan, SHA-256 and a retention policy;
       responses 202/400/403/413/422
     - config/registries/data-constraints.json, evidence_assets: required
       id, tenant_id, project_id, sha256, classification; UNIQUE
       (tenant_id, id); invariant "AV scan, immutable hash"
   Tooling the source names: ClamAV for malware scanning, Production decision,
   with the control "with sandbox/CDR where needed" (sheet 22 row 29); Apache
   Tika for text and metadata with the control "sandbox files" (sheet 22
   row 27). These are source-supported choices.

D. EXECUTION INSTRUCTIONS
   1. Implement POST /v1/uploads/init: authorize, derive tenant server-side,
      validate declared content type and declared size against configured
      allowlists, and return a short-lived pre-signed upload target scoped to
      the tenant's object prefix. Reject disallowed types with 415 and
      oversized declarations with 413.
   2. Enforce limits again on the server after upload — never trust the declared
      size or type. Verify the real content type by inspecting magic bytes, not
      the file extension or the client-supplied header.
   3. Implement the scan stage as a mandatory gate:
        - state machine: RECEIVED -> SCANNING -> (CLEAN | QUARANTINED);
        - nothing downstream may read the object while state is not CLEAN;
        - enforce that with authorization, not convention: the parser's
          credentials must not be able to read a non-CLEAN object.
   4. Implement protections beyond signature scanning, because AT-FILE-001
      includes a zip bomb, which an AV signature will not catch:
        - decompression ratio and absolute uncompressed size limits;
        - archive entry count and nesting depth limits;
        - a wall-clock and memory budget on any inspection, enforced by the
          sandbox, so a malicious file cannot exhaust the host.
   5. Run parsing and type inspection inside a sandbox with no network egress,
      a read-only filesystem apart from a scratch area, and a hard resource
      limit. If the sandbox cannot be provided in the local environment, state
      that explicitly and record what production must provide.
   6. On detection: move the object to a quarantine location the application
      role cannot read, write an audit event and a security alert, emit
      file.quarantined, and return a response that does not echo the file's
      content or reveal the detection signature to the uploader.
   7. On success: compute SHA-256 over the stored bytes, create the
      evidence_assets record with tenant_id, project_id, sha256 and
      classification, apply the retention class, and emit file.uploaded.
      The hash is immutable once written — enforce it.
   8. Implement POST /v1/projects/{id}/evidence with a required Idempotency-Key
      per sheet 33 row 8, returning the same receipt for a repeated key rather
      than creating a second record.
   9. Write AT-FILE-001 as an automated test:
        a. upload the standard EICAR test string -> assert QUARANTINED, assert
           no parse was invoked, assert no model client was invoked, assert an
           alert was emitted;
        b. upload a zip bomb fixture -> assert QUARANTINED by ratio or size
           limit, assert the host stayed within its resource budget;
        c. upload a file whose extension says PDF but whose magic bytes say
           otherwise -> assert rejection on real content type;
        d. upload a clean file -> assert CLEAN, assert the SHA-256 matches an
           independently computed digest, assert the evidence record exists;
        e. repeat (d) with the same Idempotency-Key -> assert one record, same
           receipt.
      Assert "no model was invoked" with a test double that fails the test if
      called. Do not assert it by inspection.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - POST /v1/uploads/init and POST /v1/projects/{id}/evidence
   - the RECEIVED/SCANNING/CLEAN/QUARANTINED state machine with authorization
     enforcement
   - malware scanning plus archive-bomb and magic-byte defences
   - sandboxed inspection with resource limits
   - quarantine path with alerting and non-revealing responses
   - evidence_assets records with immutable SHA-256 and retention class
   - tests/security/at-file-001.* covering cases a through e
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-FILE-001 output for all five cases.
   - Paste the test-double assertion proving no parser and no model client was
     invoked for a quarantined file.
   - Show that the parser credential cannot read a QUARANTINED object: paste
     the access denial.
   - Independently compute the SHA-256 of the clean fixture with a separate
     tool and show it matches the stored value.
   - Acceptance criterion: AT-FILE-001 passes in full, and the no-parse/no-model
     guarantee is proven by an assertion that would fail if violated.

G. COMPLETION CONTRACT
   Definition of Done: the gateway rejects or quarantines all four hostile
   fixtures, stores clean files with a verified immutable digest, and is
   idempotent on the evidence endpoint.
   Evidence to report: AT-FILE-001 output, the invocation-guard assertion, the
   independent hash comparison, the quarantine access denial.
   Remaining blockers: sandbox or AV capability unavailable locally — name
   exactly what production must supply and what your local run did not prove.
   Next prompt: P02-02.
```

**المخرجات المتوقعة:** بوابة رفع، حجر صحي، سجلات أدلة ببصمات ثابتة، `AT-FILE-001`.
**التحقق المطلوب:** لا تحليل ولا نداء نموذج لملف محجور — مُثبت بمضاعف اختبار يفشل عند النداء.
**الاعتمادية التالية:** `P02-02`.

---

### P02-02 — إصدارات المخرجات والبصمات والقفل

<!-- meta
id: P02-02
phase: PHASE-02
title_en: Artifact versioning, digests and immutability
prereq: [P02-01]
requirements: [ADR-006, REQ-DEL-04, REQ-DAT-05, REQ-WF-06]
-->

**ماذا سينفذ هذا الأمر؟** يبني مخزن مخرجات بإصدارات: كل مخرج له نسخة وبصمة
`SHA-256`، والنسخة المقفلة لا تتغير، وأي تغيير يُنتج نسخة جديدة وبصمة جديدة.

**لماذا نحتاجه؟** `ADR-006` يربط التوقيع المهني بالبصمة. الورقة 09 الصف 26 تحدد
الانتقال: `SIGNED` + `hash_mismatch` → `INVALIDATED`. والورقة 14 الصف 11: «أي
تغيير بعد التوقيع = نسخة وبصمة جديدة وإعادة مراجعة؛ لا استبدال صامت».

**ما المتطلبات السابقة؟** `P02-01`.

**ما النتيجة المتوقعة؟** كيان `Artifact` بإصدارات وبصمات، وقفل كائن، ومرجع ثابت
صالح للتوقيع.

**كيف نتحقق من نجاحه؟** تغيير بايت في مخرج مقفل يُكتشف؛ ومحاولة الكتابة فوق نسخة
مقفلة تُرفض على مستوى التخزين.

```text
TASK P02-02 — Artifact versioning, digests and immutability

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P02-02
   Phase: PHASE-02
   Prerequisites: P02-01 (clean files land as evidence assets)
   Requirements covered: ADR-006, REQ-DEL-04, REQ-DAT-05, REQ-WF-06

B. OBJECTIVE
   Implement versioned, digest-addressed artifacts whose locked versions are
   immutable, so that a professional signature can bind to exactly the bytes a
   reviewer saw, and any later change is detectable and forces a new review
   cycle.

   Why this is necessary: ADR-006 (sheet 02 row 7) binds the reviewer decision
   to a version and a SHA-256 digest, with the acceptance control "lock before
   decision". Sheet 09 row 26 defines the transition SIGNED plus hash_mismatch
   to INVALIDATED. Sheet 14 row 11 forbids silent replacement. Without a
   trustworthy digest, neither the signature nor the delivery means anything.

   SCOPE BOUNDARY: artifact storage, versioning, digests, locking and
   verification. The review decision and signature flow is PHASE-07. Document
   generation and the delivery package are PHASE-07. Here you build the
   substrate they depend on.

C. CONTEXT
   Required inputs:
     - config/registries/data-entities.json, Artifact entry: keys
       artifact_id, version, hash; purpose "versioned file or output"; control
       "object lock"
     - sheet 09 rows 23-26 (Delivery sub-state machine: CANDIDATE -> LOCKED ->
       SIGNED -> RELEASED, and SIGNED -> INVALIDATED on hash mismatch)
     - sheet 26 row 17: POST /v1/deliveries/{id}/lock, scope deliveries:lock,
       concurrency control by artifact version, emits delivery.locked,
       responses 200/409
   Related invariant: findings carry evidence locators including artifact,
   page, grid, GUID and hash (sheet 10 row 12), so an artifact reference must
   be stable enough to anchor a page and a grid cell.

D. EXECUTION INSTRUCTIONS
   1. Model Artifact and ArtifactVersion. An artifact has an identity; a
      version has an immutable digest, a creation source (upload or
      generation), a content type, a size, a classification and a state of
      CANDIDATE or LOCKED.
   2. Compute SHA-256 over canonical stored bytes on version creation. Store
      the digest with an explicit algorithm prefix, for example
      "sha256:<hex>", so a future algorithm change is unambiguous.
   3. Implement lock:
        - locking transitions CANDIDATE to LOCKED and records who locked it,
          when, and the digest at lock time;
        - a LOCKED version is immutable: enforce it in storage with object
          lock or equivalent immutability, and revoke the application role's
          ability to overwrite or delete that object;
        - lock is idempotent for the same version and returns 409 on a
          concurrent conflicting lock attempt, per sheet 26 row 17.
   4. Implement verification:
        - a routine that re-reads the stored bytes and recomputes the digest;
        - a mismatch is a first-class detected event, not a log line: it emits
          an integrity alert, writes an audit record and marks the version
          INTEGRITY_FAILED so downstream consumers refuse it;
        - a scheduled verification sweep over LOCKED versions, with its
          findings recorded.
   5. Implement immutable references for anchoring: a reference form that names
      artifact, version and digest together, so a finding or a signature can
      cite bytes rather than a mutable pointer. Any consumer resolving a
      reference whose digest no longer matches must fail, not fall back.
   6. Implement supersession rather than mutation: a change produces a new
      version linked to its predecessor with a reason, and never edits the
      predecessor. Expose the lineage.
   7. Apply retention class per version and keep the enforcement hook for
      PHASE-11, including a legal-hold flag that blocks deletion.
   8. Tests:
        a. create version, lock, attempt overwrite -> rejected at storage
           level, not by application code;
        b. attempt delete of a LOCKED version -> rejected;
        c. mutate the stored object out of band by one byte -> verification
           detects it, names the version, emits the alert, marks
           INTEGRITY_FAILED;
        d. a consumer resolving the stale reference -> fails closed;
        e. concurrent lock attempts -> one succeeds, the other gets 409;
        f. supersede -> new version created, predecessor unchanged, lineage
           queryable;
        g. legal hold set -> deletion refused even by the retention job.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - Artifact and ArtifactVersion models and migrations
   - digest computation with algorithm prefix
   - POST /v1/deliveries/{id}/lock with idempotency and 409 semantics
   - storage-level immutability for LOCKED versions
   - a verification routine plus a scheduled sweep
   - immutable reference resolution that fails closed on digest mismatch
   - supersession with queryable lineage
   - tests/integrity/artifact-*.* covering cases a through g
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all seven tests.
   - For case a and b, show the rejection comes from the storage layer: paste
     the storage error, not an application exception you raised.
   - For case c, paste the verification output naming the version and the
     expected versus actual digest.
   - Acceptance criterion: a one-byte change to a locked artifact is always
     detected and always blocks downstream consumption. This is the control
     that AT-DEL-001 in PHASE-07 will build on.

G. COMPLETION CONTRACT
   Definition of Done: locked versions are immutable at the storage layer,
   tampering is detected and named, references fail closed, lineage is
   queryable.
   Evidence to report: the seven test outputs, the storage-level rejection
   proof, the digest mismatch report.
   Remaining blockers: object lock unavailable in the local environment —
   state what production must enable and which of the seven cases your local
   run therefore did not fully prove.
   Next prompt: P02-03.
```

**المخرجات المتوقعة:** كيان مخرجات بإصدارات، قفل تخزين، روتين تحقق، نسب الإصدارات.
**التحقق المطلوب:** رفض الكتابة فوق نسخة مقفلة من طبقة التخزين، وكشف تغيير بايت واحد.
**الاعتمادية التالية:** `P02-03`.

---

### P02-03 — بيان الأدلة وسلسلة المصدر

<!-- meta
id: P02-03
phase: PHASE-02
title_en: Evidence manifest and provenance chain
prereq: [P02-02]
requirements: [REQ-FND-02, REQ-API-05, REQ-DAT-05, REQ-EVL-05]
-->

**ماذا سينفذ هذا الأمر؟** يبني «بيان أدلة» (Evidence Manifest) يربط كل دليل
بمصدره وبصمته وموضعه، ويصدر الحدث `evidence.submitted.v1`.

**لماذا نحتاجه؟** الورقة 37 الصف 10 تجعل `REQ-05 Evidence provenance` متطلباً
بدليل مطلوب: «manifest + checksum test». والورقة 10 الصف 12 تفرض على كل finding
حقل `evidence[]` إلزامياً يحتوي `artifact/page/grid/GUID/hash`. فبدون بيان أدلة
منظم لا يمكن إنتاج finding صالح.

**ما المتطلبات السابقة؟** `P02-02`.

**ما النتيجة المتوقعة؟** كيان بيان أدلة، نقطة نهاية إرساله، وحدث مُصدَر، مع
مُحدِّد موضع قابل للتحقق.

**كيف نتحقق من نجاحه؟** إعادة حساب المجاميع من البيان تطابق المخزون؛ ومُحدِّد
موضع يشير إلى صفحة/شبكة/GUID يُحلّ ويُتحقق منه.

```text
TASK P02-03 — Evidence manifest and provenance chain

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P02-03
   Phase: PHASE-02
   Prerequisites: P02-02 (versioned, digest-addressed artifacts)
   Requirements covered: REQ-FND-02, REQ-API-05, REQ-DAT-05, REQ-EVL-05

B. OBJECTIVE
   Implement the evidence manifest: a structured, verifiable record binding
   each piece of evidence to its source artifact version, its digest and its
   precise locator, and emit the versioned evidence.submitted.v1 event.

   Why this is necessary: sheet 37 row 10 makes evidence provenance a tracked
   requirement whose required proof is "manifest plus checksum test". Sheet 10
   row 12 makes the evidence array mandatory on every finding with locators
   artifact, page, grid, GUID and hash. Without a structured manifest, a valid
   finding cannot be produced at all, so this blocks PHASE-07.

   SCOPE BOUNDARY: the manifest, its locators, its verification and its event.
   Do not extract content from documents, do not detect pages or rooms, and do
   not call a model. Locators here are recorded and verified, not inferred.

C. CONTEXT
   Required inputs:
     - the artifact and version model from P02-02
     - sheet 34 row 7 (EV-02 EvidenceSubmitted, topic
       evidence.submitted.v1, aggregate Evidence, required payload
       manifestId, projectId, hashes, producer Upload service, consumer
       Evidence QA, ordering key manifestId, at-least-once, validation
       "quarantine until scan passes")
     - sheet 34 row 3 (the common envelope: eventId, eventType, schemaVersion,
       tenantId, correlationId, causationId, occurredAt UTC, payload)
     - sheet 28 row 10 (Evidence entity: evidence_id, hash, locator; purpose
       "evidence for a test or a decision"; control "immutable")

D. EXECUTION INSTRUCTIONS
   1. Model EvidenceManifest and EvidenceItem. A manifest belongs to a tenant
      and a project, has an id, a creation actor, a state and a digest over its
      own canonical content. An item references an artifact version by
      artifact, version and digest, and carries a locator.
   2. Implement a typed locator with a discriminated form, so a locator is
      always interpretable:
        - PAGE: page number, plus optional bounding box
        - GRID: page plus grid reference, for example B4
        - IFC_GUID: the GUID plus the model artifact version it belongs to
        - GEO: coordinates plus CRS identifier, never bare coordinates
        - TIME: offset into a media artifact
        - CELL: sheet plus cell, for tabular sources
      Reject a locator that does not resolve against the referenced artifact
      version. A locator pointing at page 40 of a 12-page document is invalid
      data, not a warning.
   3. Compute and store a manifest digest over the canonical serialization of
      its items, so the manifest itself is tamper-evident and citable.
   4. Implement POST /v1/projects/{id}/evidence to accept a manifest with a
      required Idempotency-Key per sheet 33 row 8, returning an EvidenceReceipt
      with 202 on acceptance and 422 on schema or locator failure.
   5. Enforce the source's validation rule: an item referencing an artifact
      that is not CLEAN is refused. The manifest cannot launder a quarantined
      file into the system.
   6. Emit evidence.submitted.v1 using the common envelope of sheet 34 row 3,
      with manifestId as the ordering key, through the transactional outbox
      that PHASE-03 will generalize. If the outbox does not exist yet,
      implement the minimal outbox table now and record that P03-03 generalizes
      it — do not emit directly from the request path, because an at-least-once
      guarantee cannot be made that way.
   7. Implement manifest verification: re-resolve every item, recompute every
      referenced digest, recompute the manifest digest, and report per-item
      PASS or FAIL with the reason. This is the "checksum test" that sheet 37
      row 10 requires as proof.
   8. Expose a provenance query: given a finding or a decision reference,
      return the full chain down to the originating uploaded bytes, with every
      digest in the chain.
   9. Tests:
        a. a manifest with valid locators is accepted, and verification passes
           for every item;
        b. a locator beyond the artifact's extent is rejected with 422 naming
           the item;
        c. a GEO locator without a CRS is rejected;
        d. an item referencing a QUARANTINED artifact is refused;
        e. a repeated Idempotency-Key returns the original receipt and creates
           no second manifest;
        f. tampering with a referenced artifact after submission makes
           verification FAIL for that item and names it;
        g. the emitted event matches the sheet 34 row 3 envelope schema exactly,
           asserted against a schema file;
        h. a provenance query returns an unbroken digest chain to the source
           bytes.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - EvidenceManifest and EvidenceItem models and migrations
   - the typed, resolvable locator implementation
   - POST /v1/projects/{id}/evidence with idempotency and 422 semantics
   - the minimal transactional outbox plus evidence.submitted.v1 emission
   - the manifest verification routine
   - the provenance query
   - tests/evidence/manifest-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eight tests.
   - Paste the event payload for case g beside the envelope schema, showing
     every required field present.
   - For case f, paste the verification report naming the failed item and the
     digest difference.
   - Acceptance criterion: no manifest can reference unscanned bytes, no
     unresolvable locator is accepted, and verification detects post-hoc
     tampering per item.

G. COMPLETION CONTRACT
   Definition of Done: manifests are typed, verifiable and tamper-evident;
   locators resolve or are rejected; the event conforms to the source envelope;
   provenance is queryable end to end.
   Evidence to report: the eight test outputs, the envelope conformance
   comparison, the tamper detection report.
   Remaining blockers: none expected. If the outbox had to be stubbed, say so
   and name P03-03 as the completing prompt.
   Next prompt: P03-01. PHASE-02 exit requires AT-FILE-001 green, artifact
   immutability proven at storage level, and manifest verification working.
```

**المخرجات المتوقعة:** بيان أدلة مُتحقَّق، مُحدِّدات موضع مُحلَّلة، حدث مطابق للمغلف.
**التحقق المطلوب:** رفض الأدلة المرتبطة بملف غير نظيف، وكشف التلاعب لكل عنصر.
**الاعتمادية التالية:** `P03-01`.

# PHASE-11 — الأمن والخصوصية وPDPL

<!-- phasemeta
id: PHASE-11
depends_on: [PHASE-01, PHASE-02, PHASE-10]
criticality: P0
-->

## الغرض من المرحلة

الورقة 27 تحدد خمسة عشر ضابطاً، منها ثمانية بأولوية `CRITICAL`. والورقة 57 الصف 10
(`A09`) تحدد الفجوة الأمنية الأبرز: «حمايات حقن المطالبات وتسريب الأدوات تحتاج
اختبارات خصومية». والورقة 23 الصف 12 تضع المرجع التنظيمي: نظام حماية البيانات
الشخصية (`PDPL`) وحقوقه.

هذه المرحلة تحوّل الضوابط الموصوفة إلى ضوابط مُنفَّذة ومُدلَّلة.

## شروط الدخول

- اكتمال `PHASE-01` (الهوية والتدقيق) و`PHASE-02` (الملفات والأدلة).

## شروط الخروج

- نجاح `AT-PRIV-001` عبر الوصول والتصحيح والإتلاف.
- حذف مُتحقَّق منه مُثبت.
- مجموعة خصومية تغطي حقن المطالبات وتسريب الأدوات والخروج.
- تقييم إقامة البيانات لكل مزود.
- تمرين طاولة لخرق البيانات مُنفَّذ.

## المتطلبات المغطاة في هذه المرحلة

`REQ-SEC-06`..`REQ-SEC-11`, `REQ-GW-19`, `REQ-SCN-05`, `REQ-EVL-08`

---

## الأوامر التنفيذية

### P11-01 — الأساس النظامي وسجل المعالجة والموافقة

<!-- meta
id: P11-01
phase: PHASE-11
title_en: PDPL lawful basis, RoPA, consent and notice
prereq: [P10-04]
requirements: [REQ-SEC-07, REQ-SEC-11]
-->

**ماذا سينفذ هذا الأمر؟** يبني سجل أنشطة المعالجة (`RoPA`)، والأساس النظامي لكل
غرض، وإدارة الموافقة وسحبها، وإشعار الخصوصية.

**لماذا نحتاجه؟** الورقة 27 الصف 9 (`SEC-08`) بأولوية `CRITICAL` ودليله المطلوب:
«RoPA وإشعار». والورقة 28 الصف 19 تحدد كيان `Consent` بـ«purpose/status/time»
وضابطه «withdrawal». الموافقة بلا إمكانية سحب ليست موافقة.

**ما المتطلبات السابقة؟** `P10-04`.

**ما النتيجة المتوقعة؟** سجل معالجة حيّ مرتبط بالكود، وموافقة قابلة للسحب بأثر
فعلي، وإشعار مُصدَر.

**كيف نتحقق من نجاحه؟** سحب الموافقة يوقف المعالجة المعتمدة عليها فعلياً؛ ومعالجة
بلا أساس نظامي مُسجَّل تُرفض.

```text
TASK P11-01 — PDPL lawful basis, RoPA, consent and notice

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P11-01
   Phase: PHASE-11 (Security, privacy and PDPL hardening)
   Prerequisites: P10-04
   Requirements covered: REQ-SEC-07, REQ-SEC-11

B. OBJECTIVE
   Implement the PDPL foundation: a record of processing activities tied to the
   actual code paths, a recorded lawful basis per purpose, consent capture with
   effective withdrawal, and the privacy notice.

   Why this is necessary: sheet 27 row 9 (SEC-08) is CRITICAL with required
   evidence of a RoPA and a notice. Sheet 28 row 19 defines Consent with
   purpose, status and time and its control as withdrawal. Sheet 23 row 12
   names the SDAIA PDPL platform as the regulatory reference covering the
   system and the data subject rights.

   SCOPE BOUNDARY: lawful basis, RoPA, consent and notice. Data subject rights
   execution is P11-02. Retention and deletion are P11-03. This prompt does not
   constitute legal advice and the RoPA requires review by the privacy owner.

C. CONTEXT
   Required inputs:
     - sheet 27 row 9: purpose, lawful basis, consent and notice, recorded in a
       RoPA; owner Privacy
     - sheet 27 row 13 (SEC-12): DPA, subprocessors, due diligence and transfer
       assessment; evidence annual and vendor review
     - sheet 24 row 4 (RAG-SCE): "no PII without purpose"
     - sheet 49 row 8: capture privacy — consent, redaction, data region and
       access scope, with a consent-to-revoke lifecycle
     - docs/discovery/INTEGRATION-ACCESS-AUDIT.md from P00-03 for the actual
       provider and processor set
   Personal data in this system includes, at minimum: client and owner
   identity and contact data; reviewer identity, membership reference,
   experience and performance data; engineer and contractor identities;
   uploaded documents that contain personal data; site photographs that may
   contain people; payment-adjacent identity data; and audit records naming
   actors.

D. EXECUTION INSTRUCTIONS
   1. Build the RoPA as a maintained artifact, with one entry per processing
      purpose containing: the purpose, the data categories, the data subject
      categories, the lawful basis, the retention class, the recipients and
      processors, any cross-border transfer and its basis, the security
      measures, and the code paths or services that perform the processing.
   2. Tie the RoPA to the code so it cannot silently rot: define a
      purpose identifier that processing code must declare, and add a test
      asserting every declared purpose in the code exists in the RoPA and every
      RoPA entry maps to at least one real code path. A RoPA that is a
      standalone document always drifts.
   3. Implement lawful basis enforcement: a processing operation declares its
      purpose; the purpose carries its lawful basis; where the basis is consent,
      the operation requires an active consent record for that subject and
      purpose. Processing with no registered purpose is refused — this is the
      fail-closed principle applied to privacy.
   4. Implement consent per sheet 28 row 19: purpose, status, timestamp,
      version of the notice consented to, and the capture context. Consent is
      per-purpose and granular; a single blanket consent is not implemented.
   5. Implement withdrawal with real effect, which is the hard part: on
      withdrawal, consent-based processing for that purpose stops, in-flight
      operations relying on it halt at their next checkpoint, derived artifacts
      are flagged, and the withdrawal is audited. Add a test that withdraws
      consent and asserts a subsequent consent-dependent operation is refused.
      A withdrawal that only sets a flag is not a withdrawal.
   6. Implement the privacy notice as a versioned artifact, with the version
      recorded on every consent, so you can always establish what a subject was
      told at the time.
   7. Implement the processor register per sheet 27 row 13: every processor and
      subprocessor with its DPA reference, the data categories it receives, its
      location, and its due-diligence review date. Mark a processor with no DPA
      as NOT_PROVIDED, and connect this to the model registry's data_policy
      from P04-02 so an undocumented processor cannot receive restricted data.
   8. Implement transfer assessment per provider and per data classification,
      and enforce it in the policy engine: a route whose destination geography
      is not permitted for that classification is denied. Sheet 77 row 5 forbids
      assuming Saudi residency, so the absence of an assessment means the
      transfer is not permitted.
   9. Implement the no-PII-without-purpose rule for RAG-SCE and generally: an
      ingestion carrying personal data must name its purpose, and the ingestion
      is refused otherwise.
  10. Tests:
        a. a processing operation with no registered purpose -> refused;
        b. a consent-based operation with no active consent -> refused;
        c. withdrawal -> a subsequent consent-dependent operation is refused,
           in-flight work halts, derived artifacts are flagged, the withdrawal
           is audited;
        d. the RoPA-to-code test passes, and fails when a purpose is used in
           code but not registered;
        e. a transfer to a geography with no assessment for that classification
           -> denied by the policy engine;
        f. a processor with NOT_PROVIDED DPA cannot receive restricted data;
        g. an ingestion of personal data with no stated purpose -> refused;
        h. a consent record carries the notice version it was given against.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the RoPA with all listed fields, per purpose
   - purpose declarations in code with the drift test both ways
   - lawful basis enforcement with fail-closed semantics
   - granular per-purpose consent with notice versioning
   - withdrawal with real, tested effect
   - the versioned privacy notice
   - the processor and subprocessor register with DPA references
   - per-provider, per-classification transfer assessment enforced in policy
   - the no-PII-without-purpose rule
   - tests/privacy/basis-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eight tests.
   - Paste the RoPA-to-code drift test both passing and failing.
   - Paste the withdrawal test showing the subsequent refusal.
   - Report how many processors have a DPA on file and how many are
     NOT_PROVIDED.
   - Acceptance criterion: no processing occurs without a registered purpose
     and a valid basis, and withdrawal actually stops processing.

G. COMPLETION CONTRACT
   Definition of Done: the RoPA exists and is code-linked, basis enforced,
   consent granular and withdrawable with effect, processors registered,
   transfers assessed.
   Evidence to report: the eight test outputs, the drift test both ways, the
   processor DPA count.
   Remaining blockers: the RoPA and the notice require review by the privacy
   owner and legal counsel; DPAs are owner-owned procurement items. Report
   both. Do not describe the platform as PDPL compliant on the basis of this
   implementation.
   Next prompt: P11-02.
```

**المخرجات المتوقعة:** `RoPA` مرتبط بالكود، موافقة قابلة للسحب بأثر، سجل معالِجين، تقييم نقل.
**التحقق المطلوب:** لا معالجة بلا غرض مُسجَّل؛ السحب يوقف المعالجة فعلاً.
**الاعتمادية التالية:** `P11-02`.

---

### P11-02 — حقوق صاحب البيانات

<!-- meta
id: P11-02
phase: PHASE-11
title_en: Data subject rights execution
prereq: [P11-01]
requirements: [REQ-SEC-08, REQ-EVL-01]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ حقوق الوصول والتصحيح والإتلاف وسحب الموافقة، مع
التحقق من الهوية وSLA وتسجيل الاستثناءات.

**لماذا نحتاجه؟** `AT-PRIV-001` (الورقة 16 الصف 11) يحدد السيناريو: «Access ثم
correction ثم destruction» والمتوقع «هوية وSLA واستثناءات وأدلة». والورقة 27
الصف 10 (`SEC-09`) دليله: «DSR exercise».

**ما المتطلبات السابقة؟** `P11-01`.

**ما النتيجة المتوقعة؟** مسار طلبات مُنفَّذ بالأربع عمليات، مع استثناءات مُعلَّلة.

**كيف نتحقق من نجاحه؟** `AT-PRIV-001` ناجح؛ وكل استثناء عن الحذف له أساس مُسجَّل
لا رفض صامت.

```text
TASK P11-02 — Data subject rights execution

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P11-02
   Phase: PHASE-11
   Prerequisites: P11-01
   Requirements covered: REQ-SEC-08, REQ-EVL-01

B. OBJECTIVE
   Implement data subject rights — access, correction, destruction and
   withdrawal of consent — with identity verification, a tracked SLA, recorded
   exceptions, and evidence of each exercise.

   Why this is necessary: AT-PRIV-001 (sheet 16 row 11) runs access, then
   correction, then destruction, and expects identity verification, SLA
   tracking, exceptions and evidence. Sheet 27 row 10 (SEC-09) names the
   evidence as a DSR exercise. Sheet 31 row 11 cites the PDPL platform for the
   rights of access, correction, destruction, withdrawal of consent and breach
   notification.

   SCOPE BOUNDARY: the request lifecycle and its four operations. Retention
   schedules and verified deletion mechanics are P11-03, which this prompt
   consumes.

C. CONTEXT
   Required inputs:
     - the RoPA and consent records from P11-01, which tell you where a
       subject's data lives
     - the append-only audit store from P01-05, immutable artifacts from
       P02-02 and the financial ledger from P08-04 — all three constrain
       deletion
     - sheet 27 row 11 (SEC-10): retention schedules, legal hold and verified
       deletion
   Critical tension to handle honestly: several stores are immutable or
   legally retained by design. A reviewer's signed decision, an append-only
   audit record and a financial posting cannot simply be deleted. The correct
   answer is a recorded, legally grounded exception with a defined scope — not
   a silent failure to delete, and not a deletion that destroys an integrity
   chain.

D. EXECUTION INSTRUCTIONS
   1. Implement the request lifecycle: RECEIVED, IDENTITY_PENDING,
      IDENTITY_VERIFIED, IN_PROGRESS, PARTIALLY_FULFILLED, FULFILLED,
      REFUSED, each with timestamps and actors, and an SLA clock from the
      verification point.
   2. Implement identity verification proportionate to the request and
      logged. A destruction request requires stronger verification than an
      access request. Never disclose data to an unverified requester, and never
      use the request itself as a channel to confirm whether a person is in the
      system.
   3. Implement a data discovery routine driven by the RoPA: for a given
      subject identifier, enumerate every store and every record category that
      may hold their data, including the relational stores, the object store,
      the vector indexes, the caches, the traces and logs, the backups, and the
      processor-held copies. A rights process that misses the vector index or
      the trace store is incomplete, and sheet 76 row 6 explicitly includes RAG,
      cache, traces and logs in the isolation scope.
   4. Implement access: produce a structured export of the subject's personal
      data with its sources and purposes, excluding other people's personal
      data and excluding commercially confidential material that is not the
      subject's personal data. Deliver through an authenticated channel, never
      by unauthenticated link.
   5. Implement correction: apply the correction to the authoritative record
      and propagate it, while preserving the audit trail of the prior value.
      Where a record is immutable by design, record the correction as an
      appended correcting entry that any reader of the original will encounter
      — not an edit, and not an unlinked note.
   6. Implement destruction with a defined, honest scope:
        - delete or irreversibly anonymize where the data is deletable;
        - for immutable or legally retained records, apply the exception path:
          record the specific legal or contractual basis, the record category,
          the retention end date, and the scope of what survives;
        - reduce surviving records to the minimum necessary (for example,
          replacing identity with a pseudonymous reference where the integrity
          chain permits);
        - handle backups explicitly: state the backup retention window after
          which the data is gone, and ensure a restore does not resurrect
          deleted data without re-applying the deletion. Implement a deletion
          journal that a restore replays.
        - propagate the deletion request to processors and record their
          confirmation.
   7. Implement withdrawal of consent wired to P11-01's withdrawal effect.
   8. Implement exception recording as a first-class, reviewable output. Every
      partial fulfilment lists exactly what was not done and the basis. Sheet
      16 row 11 names exceptions as an expected part of the result, so a
      process that reports only success is wrong.
   9. Implement evidence capture per request: the request, the verification,
      the discovery result, the actions taken per store, the exceptions, the
      confirmations from processors, and the timestamps. This is the DSR
      exercise evidence.
  10. Tests — AT-PRIV-001 plus the rights suite:
        a. AT-PRIV-001: run access, then correction, then destruction for one
           subject; assert identity verification occurred, the SLA was tracked,
           exceptions were recorded, and evidence was captured for each;
        b. an unverified requester -> no disclosure, and no confirmation of
           existence;
        c. the discovery routine finds the subject's data in the vector index,
           the cache and the trace store, not only the database;
        d. an access export contains no third-party personal data;
        e. a correction on an immutable record -> an appended correcting entry
           that is surfaced with the original;
        f. a destruction request where an audit record must be retained -> a
           recorded exception with its basis and retention end date, and the
           audit digest chain still verifies;
        g. a restore from a backup taken before a deletion -> the deletion
           journal is replayed and the data does not resurrect;
        h. a processor deletion propagation is recorded with its confirmation
           or its absence;
        i. an SLA breach raises an alert.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the request lifecycle with SLA tracking
   - proportionate, logged identity verification with no existence disclosure
   - the RoPA-driven discovery routine covering all nine store categories
   - access export excluding third-party data
   - correction with immutable-record append semantics
   - destruction with scoped exceptions, minimization, a deletion journal and
     processor propagation
   - consent withdrawal wiring
   - first-class exception recording
   - per-request evidence capture
   - tests/privacy/at-priv-001.* plus cases b through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-PRIV-001 output for all three operations with their evidence.
   - Paste the discovery result from case c listing every store searched.
   - Paste the case f exception record and the audit chain verification after
     it.
   - Paste the case g restore showing the deletion journal replay.
   - Acceptance criterion: every store is covered, every exception is recorded
     with a basis, and a restore never resurrects deleted data.

G. COMPLETION CONTRACT
   Definition of Done: AT-PRIV-001 green across all three operations, discovery
   complete, exceptions recorded with bases, deletion durable across restore.
   Evidence to report: AT-PRIV-001 output, the discovery inventory, the
   exception record, the restore journal replay.
   Remaining blockers: the legal bases for retention exceptions require the
   privacy owner's and counsel's confirmation. Report the exception categories
   you implemented and that they need legal sign-off.
   Next prompt: P11-03.
```

**المخرجات المتوقعة:** دورة حياة طلبات بأربع عمليات، اكتشاف شامل للمخازن، استثناءات مُعلَّلة، سجل حذف.
**التحقق المطلوب:** `AT-PRIV-001` ناجح؛ الاسترجاع لا يُعيد بيانات محذوفة.
**الاعتمادية التالية:** `P11-03`.

---

### P11-03 — الحفظ والحجز القانوني والحذف المُتحقَّق

<!-- meta
id: P11-03
phase: PHASE-11
title_en: Retention schedules, legal hold and verified deletion
prereq: [P11-02]
requirements: [REQ-SEC-09, REQ-DAT-01, REQ-SEC-14]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ جداول الحفظ لكل فئة بيانات، والحجز القانوني،
والحذف المُتحقَّق منه بدليل.

**لماذا نحتاجه؟** الورقة 27 الصف 11 (`SEC-10`) دليله: «deletion test». والورقة 28
تحدد لكل كيان من العشرين سياسة حفظ مختلفة — من «دائم» لقوالب مسارات العمل إلى
«حسب السياسة» لتشغيلاتها. تطبيق سياسة واحدة على كل شيء يخالف المصدر.

**ما المتطلبات السابقة؟** `P11-02`.

**ما النتيجة المتوقعة؟** جداول حفظ مُنفَّذة لكل كيان، وحجز قانوني يمنع الحذف،
وحذف مُتحقَّق بدليل قابل للتدقيق.

**كيف نتحقق من نجاحه؟** الحذف يُتحقَّق منه بعد التنفيذ لا قبله؛ والحجز القانوني
يمنع حتى وظيفة الحفظ المجدولة.

```text
TASK P11-03 — Retention schedules, legal hold and verified deletion

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P11-03
   Phase: PHASE-11
   Prerequisites: P11-02
   Requirements covered: REQ-SEC-09, REQ-SEC-14, REQ-DAT-01

B. OBJECTIVE
   Implement per-entity retention schedules, legal hold, and verified deletion
   that produces auditable proof the data is actually gone.

   Why this is necessary: sheet 27 row 11 (SEC-10) names the required evidence
   as a deletion test. Sheet 28 assigns each of the twenty entities its own
   retention rule, from permanent for workflow templates to policy-based for
   runs to long-term evidence for review decisions. Applying one blanket policy
   contradicts the source and would either delete evidence that must be kept or
   keep personal data that must go.

   SCOPE BOUNDARY: retention, hold and deletion mechanics. The rights requests
   that trigger them are P11-02.

C. CONTEXT
   Required inputs:
     - config/registries/data-entities.json with each entity's retention
       column, and data-constraints.json with the retention and handling
       column: projects "retention by approved policy"; workflow_runs "audit
       retention"; agent_executions "redact prompts"; evidence_assets "delete
       by policy"; review_decisions "append-only"; boq_items "versioned
       snapshots"; usage_ledger "finance policy"; outbox_events "delivery
       audit"; idempotency_keys "TTL by operation"
     - the retention class fields already created in P02-01, P02-02 and P01-05
     - sheet 24 metadata including per-collection refresh and risk

D. EXECUTION INSTRUCTIONS
   1. Define a retention schedule per entity and per data class, each with: the
      retention period, the trigger that starts the clock (creation, project
      closure, contract end, last access), the disposition (delete, anonymize,
      archive), the legal or business basis, and the owner. Mark every period
      the source does not specify as PROPOSED and requiring ratification —
      sheet 28 says "by policy" in several places, which means the policy does
      not yet exist.
   2. Implement the retention engine as a scheduled, auditable job that
      evaluates eligibility, respects legal hold, performs the disposition, and
      records a disposition certificate per record or batch.
   3. Implement legal hold as an override that blocks every disposition path,
      including the scheduled job, an operator action and a rights-driven
      deletion. A hold names its authority, scope, reason and review date, and
      its application and release are audited and dual-approved.
   4. Implement prompt redaction for agent_executions per its retention rule:
      prompts are redacted at rest after their operational window while the
      execution record and its lineage survive, so quality investigation
      remains possible without indefinite prompt retention.
   5. Implement idempotency key TTL per operation per the data constraint, and
      document the behavioural consequence: after expiry a replay is no longer
      deduplicated, so the TTL must exceed the longest realistic provider
      retry window. State the chosen values and the reasoning.
   6. Implement verified deletion, which is the deliverable the source's
      evidence requirement actually demands:
        - after a disposition, verify by attempting retrieval through every
          path that could return the data — primary store, replica, object
          store, cache, vector index, search index and trace store;
        - record the verification result per path;
        - a path that still returns the data is a failed deletion, reported as
          such, not retried silently;
        - produce a disposition certificate containing the record identifiers
          or a scoped description, the paths verified, the timestamp, the
          actor and the outcome.
   7. Handle replicas, caches and backups explicitly: state the lag within
      which a replica is purged, invalidate caches as part of the disposition,
      rebuild or purge vector entries, and declare the backup window after
      which the data is irrecoverable, with the deletion journal from P11-02
      covering the interim.
   8. Implement a retention dashboard panel and alert: records overdue for
      disposition, holds past their review date, and failed verifications.
   9. Tests:
        a. an entity reaching its retention end -> disposed per its own
           schedule, with a disposition certificate;
        b. two entities with different schedules -> disposed at different
           times, proving per-entity schedules work;
        c. a legal hold -> blocks the scheduled job, an operator deletion and a
           rights-driven deletion; its application and release are
           dual-approved and audited;
        d. verified deletion -> every path reports not-found, and the
           certificate lists them;
        e. an injected failure where the vector index still returns the data ->
           reported as a failed deletion, not a success;
        f. prompt redaction -> prompts gone, execution lineage intact;
        g. an idempotency key past TTL -> replay no longer deduplicated;
           document that this is expected;
        h. the overdue-disposition alert fires.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - per-entity retention schedules with triggers, dispositions, bases and
     owners, with unspecified periods marked PROPOSED
   - the auditable retention engine with disposition certificates
   - dual-approved, audited legal hold overriding every path
   - prompt redaction preserving lineage
   - documented idempotency TTLs with their reasoning
   - multi-path verified deletion with per-path results
   - explicit replica, cache, index and backup handling
   - the retention dashboard panel and alerts
   - tests/privacy/retention-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eight tests.
   - Paste one disposition certificate showing every verified path.
   - Paste the case e failure report proving a partial deletion is not reported
     as success.
   - List every retention period marked PROPOSED and awaiting ratification.
   - Acceptance criterion: deletion is verified across every retrieval path, a
     partial deletion is reported as a failure, and legal hold blocks
     everything.

G. COMPLETION CONTRACT
   Definition of Done: per-entity schedules implemented, hold enforced
   everywhere, deletion verified and certified, failures reported honestly.
   Evidence to report: the eight test outputs, a disposition certificate, the
   failed-deletion report, the PROPOSED period list.
   Remaining blockers: retention periods the source leaves as "by policy" need
   owner and legal ratification. Report the full list.
   Next prompt: P11-04.
```

**المخرجات المتوقعة:** جداول حفظ لكل كيان، حجز قانوني مانع، حذف مُتحقَّق بشهادات.
**التحقق المطلوب:** الحذف مُتحقَّق عبر كل مسار استرجاع؛ الحذف الجزئي يُبلَّغ كفشل.
**الاعتمادية التالية:** `P11-04`.

---

### P11-04 — البرنامج الخصومي والخرق والإقامة

<!-- meta
id: P11-04
phase: PHASE-11
title_en: Adversarial programme, breach readiness and residency assessment
prereq: [P11-03]
requirements: [REQ-SEC-06, REQ-SEC-10, REQ-GW-19, REQ-SCN-05, REQ-EVL-08]
-->

**ماذا سينفذ هذا الأمر؟** يوسّع المجموعة الخصومية إلى برنامج كامل، ويبني جاهزية
الخرق بتمرين طاولة، ويُنجز تقييم إقامة البيانات لكل مزود.

**لماذا نحتاجه؟** الورقة 57 الصف 10 (`A09`) دليلها المطلوب: «red-team suite».
والورقة 27 الصف 12 (`SEC-11`) بأولوية `CRITICAL` ودليله «Tabletop»، ويحدد
«مُحفِّز إشعار الجهة التنظيمية خلال 72 ساعة حيث ينطبق». والورقة 76 الصف 2 (`G01`)
تطلب «تقييم قانوني لـDPA المزود والاستضافة الإقليمية والنقل».

**ما المتطلبات السابقة؟** `P11-03`.

**ما النتيجة المتوقعة؟** برنامج اختبار خصومي دوري، وخطة خرق مُجرَّبة، وتقييم
إقامة مُوثَّق لكل مزود.

**كيف نتحقق من نجاحه؟** المجموعة الخصومية تُشغَّل في CI وتفشل عند إضعاف ضابط؛
وتمرين الطاولة يُنتج تقريراً بإجراءات ومالكين.

```text
TASK P11-04 — Adversarial programme, breach readiness and residency assessment

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P11-04
   Phase: PHASE-11
   Prerequisites: P11-03
   Requirements covered: REQ-SEC-06, REQ-SEC-10, REQ-GW-19, REQ-SCN-05,
                         REQ-EVL-08

B. OBJECTIVE
   Extend the first adversarial suite into a maintained red-team programme,
   establish and exercise breach readiness including the regulator notification
   trigger, and complete the per-provider residency and transfer assessment.

   Why this is necessary: sheet 57 row 10 (A09) names a red-team suite as the
   acceptance evidence for prompt injection and exfiltration protections.
   Sheet 27 row 12 (SEC-11) is CRITICAL, requires a tabletop exercise, and
   names a 72-hour regulator notification trigger where applicable. Sheet 76
   row 2 (G01) requires a legal assessment of provider DPAs, regional hosting
   and transfers, currently NOT VERIFIED with the blocker "no production
   provider approvals".

   SCOPE BOUNDARY: security testing, breach process and the residency
   assessment. Do not conduct testing against a third party's systems. Do not
   test against production. The residency assessment is a documentation and
   enforcement exercise, not legal advice.

C. CONTEXT
   Required inputs:
     - the first adversarial suite from P05-03
     - the egress allowlist and tool boundary from P04-04 and P05-03
     - the transfer assessment and processor register from P11-01
     - sheet 27 rows 2-16, the fifteen security controls, as the coverage
       checklist
     - sheet 54 rows 6-7 (G05, G06) and sheet 76 rows 6, 10 (G05, G09) for the
       scan privacy and isolation gates

D. EXECUTION INSTRUCTIONS
   1. Build the red-team suite as a maintained, CI-executed test suite covering
      at least these categories, each with multiple cases:
        - prompt injection through document content, OCR text, filenames, EXIF,
          IFC property values and retrieved passages (extending P05-03);
        - tool exfiltration through injected destinations, path traversal in
          tool arguments, and chained tool calls;
        - egress attempts to non-allowlisted hosts from every component that
          makes outbound calls;
        - cross-tenant attempts against every store the source names:
          database, object storage, queues, vector index, prompt cache, traces
          and logs (sheet 76 row 6 lists exactly these);
        - authorization bypass against the sheet 04 deny matrix and the sheet
          59 admin matrix, including privilege escalation through JIT and
          break-glass;
        - the no-AI-approval invariant from P05-04 and P07-05 attacked from
          multiple identities;
        - webhook forgery, replay and amount tampering against P08-03;
        - public surface attacks against the verification endpoint from P07-06,
          including enumeration;
        - file-based attacks extending AT-FILE-001: polyglot files, deeply
          nested archives, malformed PDFs, XXE in any XML or IFC parsing, and
          SSRF through any URL-bearing field;
        - secret disclosure through error messages, traces, logs, SSE streams
          and the client bundle.
   2. Make the suite able to fail: for at least one case per category,
      demonstrate the test failing when the control is weakened, then restore
      it. A suite that has never failed proves nothing.
   3. Map the suite to sheet 27's fifteen controls and report coverage. Name
      any control with no adversarial coverage and why.
   4. Implement the breach process per sheet 27 row 12 as an executable
      runbook: triage with a severity rubric, containment actions reusing the
      safe actions from P10-03, impact assessment including which data subjects
      and categories are affected using the discovery routine from P11-02,
      notification decision logic including the 72-hour regulator trigger where
      applicable with a recorded clock, subject notification drafting, and
      post-incident review.
   5. Run the tabletop exercise with the named roles from the source (Security
      and Privacy own SEC-11), using a realistic scenario — the most relevant
      one being a cross-tenant exposure, since that is the source's only
      zero-target KPI with a Stop-the-line action. Record decisions, timings,
      gaps and assigned follow-up actions with owners.
   6. Complete the residency and transfer assessment per provider: the legal
      entity, the endpoint geography, the data classes permitted, the DPA
      reference, the retention and training terms, the transfer basis, and the
      assessment outcome. Enforce the outcome in the policy engine, so an
      unassessed or non-permitted route is denied rather than merely documented
      as risky. Report how many providers are approved for each data
      classification — if the answer is none for the highest classification,
      say so.
   7. Implement scan privacy controls in advance of PHASE-12, since sheet 54
      row 6 (G05) and sheet 76 row 10 (G09) make camera consent, retention,
      redaction, deletion and a DPIA P0 blockers: the consent model, the
      redaction requirement for images containing people, the data region
      constraint, and the DPIA template with its inputs. PHASE-12 consumes
      these.
   8. Produce a security evidence package for the release gates: the red-team
      suite results, the control coverage map, the tabletop report, the
      residency assessment, and the outstanding findings with owners and dates.
   9. Tests and exercises:
        a. the full red-team suite in CI with its results;
        b. one weakened-control demonstration per category;
        c. the control coverage map against sheet 27's fifteen controls;
        d. the cross-tenant category exercised against all seven stores;
        e. the tabletop exercise report with timings and actions;
        f. the 72-hour notification clock starts on detection and is tracked;
        g. an unassessed provider route -> denied by policy;
        h. the DPIA template completed for the scan use case to the extent
           possible before PHASE-12.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the CI-executed red-team suite across ten categories
   - weakened-control demonstrations proving the suite can fail
   - the coverage map against the fifteen security controls
   - the executable breach runbook with the notification clock
   - the tabletop exercise report with assigned actions
   - the per-provider residency assessment enforced in policy
   - the scan privacy control set and the DPIA template for PHASE-12
   - docs/evidence/security/ with the full evidence package
   - tests/security/red-team/*.* and the exercise records
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the red-team suite results with per-category pass counts.
   - Paste the weakened-control demonstrations.
   - Paste the coverage map naming any uncovered control.
   - Paste the cross-tenant results for all seven stores.
   - Paste the tabletop report summary and the residency approval counts per
     classification.
   - Acceptance criterion: every category is covered and demonstrably able to
     fail; every store is tested for cross-tenant exposure; no unassessed
     provider route is permitted.

G. COMPLETION CONTRACT
   Definition of Done: the red-team programme running in CI and proven able to
   fail, the breach runbook exercised, residency assessed and enforced, scan
   privacy controls prepared.
   Evidence to report: the suite results, the coverage map, the tabletop
   report, the residency counts, the evidence package path.
   Remaining blockers: provider DPAs and an independent penetration test are
   owner-owned. Sheet 38 row 6 (G-01) names a pen test as required evidence,
   and an internally written suite is not an independent pen test — state that
   distinction explicitly rather than presenting the suite as satisfying it.
   Next prompt: P12-01. PHASE-11 exit requires AT-PRIV-001 green, verified
   deletion proven, the red-team suite green and able to fail, residency
   assessed per provider, and the tabletop completed.
```

**المخرجات المتوقعة:** مجموعة خصومية بعشر فئات في CI، كتاب خرق مُجرَّب، تقييم إقامة مفروض بالسياسة.
**التحقق المطلوب:** المجموعة قادرة على الفشل؛ العزل مُختبَر في سبعة مخازن؛ لا مسار مزود غير مُقيَّم.
**الاعتمادية التالية:** `P12-01`.

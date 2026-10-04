# PHASE-06 — المعرفة وحقوق المصادر وRAG

<!-- phasemeta
id: PHASE-06
depends_on: [PHASE-02]
criticality: P0
-->

## الغرض من المرحلة

`ADR-009` قرار معتمد وصريح: «لا embedding أو اقتباس قبل تسجيل حق الاستخدام»،
وضابط قبوله «بوابة حقوق للمصادر». والورقة 25 الصف 2 تسجّل الحقيقة الأخطر في
الملف كله: كود البناء السعودي `SBC 2024` حقوقه كلها `UNKNOWN` — الترخيص والتخزين
والـembedding والاقتباس وإعادة التوزيع — والقرار المسجّل: **`BLOCK until ALLOWED`**.

هذا يعني أن مسار الامتثال السعودي، وهو جوهر المنتج، **محجوب قانونياً** حتى يحسم
المالك والشؤون القانونية حق الاستخدام. هذه المرحلة تبني بوابة الحقوق أولاً حتى
يكون الحجب تقنياً مفروضاً لا اعتماداً على الانتباه.

## شروط الدخول

- اكتمال `PHASE-02`: ملفات نظيفة ومخرجات ببصمات وبيان أدلة.
- وجود مالك قانوني مُسمّى لسجل الحقوق.

## شروط الخروج

- نجاح `AT-RAG-001`: مصدر حقوقه `UNKNOWN` لا يُنتج مقتطفاً ولا embedding.
- كل استشهاد يحمل المصدر والإصدار والمرساة ولقطة الحقوق.
- عزل كل مجموعة مُثبت.

## المتطلبات المغطاة في هذه المرحلة

`ADR-009`, `REQ-KNW-01`..`REQ-KNW-07`, `REQ-INT-02`, `REQ-GW-07`

## تحذير مهم

ترتيب التنفيذ في هذه المرحلة ليس اختيارياً. بوابة الحقوق (`P06-01`) تُبنى **قبل**
أي استيعاب أو فهرسة (`P06-02`). بناء خط الاستيعاب أولاً ثم إضافة البوابة يعني أن
نسخة من مصدر محجوب ستوجد في الفهرس، وهذا بالضبط ما يمنعه `ADR-009`.

---

## الأوامر التنفيذية

### P06-01 — بوابة حقوق المصادر

<!-- meta
id: P06-01
phase: PHASE-06
title_en: Source rights gate
prereq: [P02-03]
requirements: [ADR-009, REQ-KNW-02, REQ-KNW-03]
-->

**ماذا سينفذ هذا الأمر؟** يبني سجل حقوق المصادر وبوابة تمنع تقنياً أي تخزين أو
embedding أو اقتباس من مصدر لم يُسجَّل حقه كـ`ALLOWED`.

**لماذا نحتاجه؟** الورقة 15 الصف 10 (`CTRL-009`) بأولوية `CRITICAL` ودليله
المطلوب: «`UNKNOWN` يحجب الاستدعاء». والورقة 16 الصف 10 (`AT-RAG-001`) تحدد
السيناريو: حقوق `SBC` = `UNKNOWN` ثم محاولة استدعاء، والمتوقع: «حجب بلا
excerpt/embedding».

**ما المتطلبات السابقة؟** `P02-03`.

**ما النتيجة المتوقعة؟** سجل حقوق بثلاثة عشر حقلاً لكل مصدر، وبوابة مفروضة في
ثلاث نقاط: الاستيعاب، والاستدعاء، والمخرج.

**كيف نتحقق من نجاحه؟** `AT-RAG-001` ناجح، ولا يوجد مسار كود يستوعب مصدراً بلا
قرار حقوق.

```text
TASK P06-01 — Source rights gate

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P06-01
   Phase: PHASE-06 (Knowledge, source rights and RAG)
   Prerequisites: P02-03
   Requirements covered: ADR-009, REQ-KNW-02, REQ-KNW-03

B. OBJECTIVE
   Implement the source rights register and a technically enforced gate that
   makes it impossible to store, embed, quote or redistribute content from a
   source whose usage right is not recorded as ALLOWED.

   Why this is necessary: ADR-009 (sheet 02 row 10) is an APPROVED decision
   whose acceptance control is a rights gate on sources, with the stated reason
   of reducing intellectual-property risk. Sheet 15 row 10 (CTRL-009) is
   CRITICAL with the required evidence "UNKNOWN blocks retrieval". Sheet 25
   row 2 records that SBC 2024 has UNKNOWN licence, storage, embedding,
   quotation and redistribution rights, with the decision BLOCK until ALLOWED —
   so the gate must block the platform's most important corpus today.

   SCOPE BOUNDARY: the register, the gate and its enforcement points. Corpus
   ingestion is P06-02 and must be built after this. Do not ingest anything in
   this prompt, including as a test — use synthetic fixtures only.

C. CONTEXT
   Required inputs:
     - config/registries/source-rights.json from P00-02 (sheet 25 rows 2-7,
       thirteen columns per source: Source ID, title, owner, link or contract,
       type, licence, storage, embedding, quotation, redistribution, reviewer,
       last review date, decision)
     - the six registered sources and their decisions: SRC-SBC-2024 —
       everything UNKNOWN, decision BLOCK until ALLOWED; SRC-BALADY-OD —
       conditional storage and embedding, attribution required, decision
       dataset review; SRC-PROJECT — customer files, allowed for service,
       conditional embedding, no training by default, decision tenant
       isolated; SRC-SCE-PUBLIC — link only, brief factual quotation, decision
       no scraping; SRC-ZATCA — reference, citation, no bundle
       redistribution, decision track versions; SRC-OEM — copyrighted,
       conditional, minimal quotation, redistribution prohibited by default,
       decision asset only
     - sheet 23 row 6: SBC is an official source, not an API, and text and
       embedding rights need review; the connection plan is a rights gate plus
       version and effective date
     - sheet 23 row 3: SCE has no proven public verification API; an official
       channel or documented manual review is required and scraping is
       prohibited

D. EXECUTION INSTRUCTIONS
   1. Implement the SourceRights entity with all thirteen fields. Each of the
      five right fields (licence, storage, embedding, quotation,
      redistribution) is an enum: ALLOWED, CONDITIONAL, PROHIBITED, UNKNOWN.
      CONDITIONAL requires a non-empty condition text and a named approver.
      UNKNOWN is the default for a new source, never ALLOWED.
   2. Implement the decision field as the operative control: BLOCK,
      ALLOW_WITH_CONDITIONS or ALLOW, with a reviewer identity and a review
      date. A decision older than a configured review interval reverts to
      requiring re-review, and the gate treats an expired review as UNKNOWN.
   3. Enforce the gate at three independent points, because a single
      checkpoint will eventually be bypassed:
        a. INGESTION: the ingestion API refuses a source whose storage right is
           not ALLOWED or CONDITIONAL-with-conditions-met. There is no code
           path that writes corpus content without passing this check — prove
           it with an architectural test as in P04-01.
        b. RETRIEVAL: a query cannot return a passage from a source whose
           quotation right is not permitted, and cannot use an embedding from a
           source whose embedding right is not permitted. The filter is applied
           in the query construction layer, not in post-processing, so there is
           no window in which blocked content exists in a result set.
        c. OUTPUT: the P04-07 validator already rejects a citation whose rights
           snapshot is not ALLOWED. Wire this register as that check's source
           of truth.
   4. Implement the rights snapshot: when a passage is retrieved or cited, the
      current rights state is captured and travels with it, so a later rights
      change does not retroactively validate a past citation and a past
      citation can be audited against the rights that applied at the time.
   5. Implement per-right granularity. The source distinguishes storage from
      embedding from quotation from redistribution, and a source can permit one
      and forbid another. SRC-OEM permits minimal quotation but prohibits
      redistribution by default; SRC-SCE-PUBLIC permits a link and brief
      factual quotation but not scraping. Collapsing these into one boolean
      loses the model the source specifies — implement all five independently.
   6. Implement the attribution requirement: where the register requires
      attribution (SRC-BALADY-OD), any output quoting that source must carry
      the attribution, and the validator rejects an output that omits it.
   7. Implement a no-training default: SRC-PROJECT records "no training by
      default". Mark corpora with a training-permitted flag defaulting to
      false, and ensure no export path can send flagged content to a provider
      whose data_policy permits training on inputs (the registry field from
      P04-02). Add a test for that interaction.
   8. Implement the scraping prohibition as a technical control, not a policy
      note: the ingestion layer accepts content only from an authorized channel
      (an uploaded licensed file, a contracted API with recorded credentials,
      or an explicitly permitted open-data endpoint). A generic web fetch into
      a corpus is not an available operation.
   9. Tests — AT-RAG-001 plus the gate suite:
        a. AT-RAG-001: register SBC with UNKNOWN rights; attempt retrieval ->
           blocked, with no excerpt returned and no embedding computed or
           stored. Assert "no embedding computed" with a test double on the
           embedding client that fails the test if called;
        b. attempt ingestion of a BLOCK-decision source -> refused at the API
           and unreachable by any other path (architectural test);
        c. a source with ALLOWED storage but PROHIBITED embedding -> content
           stored, embedding refused, retrieval by keyword permitted and
           retrieval by vector refused;
        d. a source with CONDITIONAL quotation and unmet conditions -> quotation
           refused with the condition named;
        e. an expired review date -> treated as UNKNOWN and blocked;
        f. a rights change after a citation was made -> the old citation
           retains its original snapshot and remains auditable; a new citation
           uses the new state;
        g. an output quoting SRC-BALADY-OD without attribution -> rejected by
           the validator;
        h. an attempt to export no-training-flagged content to a
           training-permitting provider -> blocked;
        i. a generic web fetch into a corpus -> not available; assert the
           operation does not exist rather than that it returns an error.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the SourceRights entity with thirteen fields and five independent right
     enums
   - decision semantics with review expiry reverting to UNKNOWN
   - the three enforcement points, with ingestion proven architecturally
   - rights snapshots travelling with retrieved and cited content
   - the attribution requirement wired into output validation
   - the no-training default and its provider-policy interaction check
   - channel-restricted ingestion with no generic web fetch
   - tests/knowledge/at-rag-001.* plus cases b through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-RAG-001 output, including the embedding-client double's assertion
     that it was never called.
   - Paste the architectural test proving no ingestion path bypasses the gate,
     then weaken it, show failure, restore it.
   - Paste the current register state: for each of the six sources, its five
     right values and its decision. State plainly that SBC 2024 is BLOCKED and
     that the Saudi code compliance workflow therefore cannot cite the code
     today.
   - Acceptance criterion: no blocked source yields an excerpt or an embedding
     through any path, and the register's real state is reported without
     softening.

G. COMPLETION CONTRACT
   Definition of Done: the gate enforced at three points, AT-RAG-001 green, the
   register reflecting the source's actual UNKNOWN and BLOCK states.
   Evidence to report: AT-RAG-001 output, the architectural test both ways, the
   six-source rights table.
   Remaining blockers: SRC-SBC-2024 rights are an owner and legal blocker
   (open decision OD-05). This blocks the compliance capability COM-01 and the
   SBC routing class, and therefore constrains PHASE-09's villa path to
   non-code findings until resolved. Report this prominently — it is the single
   largest scope risk in the source.
   Next prompt: P06-02.
```

**المخرجات المتوقعة:** سجل حقوق بثلاثة عشر حقلاً، بوابة بثلاث نقاط فرض، `AT-RAG-001`.
**التحقق المطلوب:** لا مقتطف ولا embedding من مصدر محجوب عبر أي مسار؛ `SBC 2024` محجوب فعلياً.
**الاعتمادية التالية:** `P06-02`.

---

### P06-02 — المجموعات العشر والعزل والاستيعاب

<!-- meta
id: P06-02
phase: PHASE-06
title_en: The ten RAG collections, isolation and ingestion
prereq: [P06-01]
requirements: [REQ-KNW-01, REQ-KNW-04, REQ-GW-07]
-->

**ماذا سينفذ هذا الأمر؟** يبني المجموعات العشر في الورقة 24، كل منها ببياناتها
الوصفية واستراتيجيتها ومالكها ودورة تحديثها ومستوى خطرها، مع عزل صارم.

**لماذا نحتاجه؟** الورقة 24 تحدد لكل مجموعة بيانات وصفية مختلفة جوهرياً:
`RAG-PROJECT` تحتاج `tenant/project/ACL/revision/hash/classification`،
و`RAG-CONTRACT` تحتاج `privilege/party/clause/dates/ACL` وتكون «Restricted؛ لا
تدريب»، و`RAG-GOLDEN` تكون «للتقييم فقط مع ضبط التسريب». خلطها في فهرس واحد يُفقد
كل هذه الضوابط.

**ما المتطلبات السابقة؟** `P06-01` — بوابة الحقوق موجودة ومفروضة.

**ما النتيجة المتوقعة؟** عشر مجموعات معزولة ببياناتها الوصفية الخاصة، وخط
استيعاب يمر إلزامياً عبر بوابة الحقوق.

**كيف نتحقق من نجاحه؟** استعلام في مجموعة لا يعيد أبداً نتيجة من مجموعة أخرى أو
من مستأجر آخر؛ و`RAG-GOLDEN` لا تُستدعى في مسار إنتاج أبداً.

```text
TASK P06-02 — The ten RAG collections, isolation and ingestion

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P06-02
   Phase: PHASE-06
   Prerequisites: P06-01 (the rights gate exists and is enforced)
   Requirements covered: REQ-KNW-01, REQ-KNW-04, REQ-GW-07

B. OBJECTIVE
   Implement the ten knowledge collections with their distinct metadata
   schemas, retrieval strategies, owners, refresh cadences and risk ratings,
   under strict per-collection and per-tenant isolation, with an ingestion
   pipeline that cannot bypass the rights gate.

   Why this is necessary: sheet 24 gives each of the ten collections a
   materially different metadata contract and strategy. RAG-PROJECT needs
   tenant, project, ACL, revision, hash and classification with a
   project-scoped index and no cross-tenant access. RAG-CONTRACT needs
   privilege, party, clause, dates and ACL and is Restricted with no training.
   RAG-GOLDEN is evaluation-only with leakage control. Flattening these into
   one index destroys every one of those controls.

   SCOPE BOUNDARY: collection definitions, isolation, ingestion and retrieval
   plumbing. Citation quality evaluation is PHASE-14. Do not ingest a BLOCKED
   source — the gate will refuse, and that refusal is the correct outcome.

C. CONTEXT
   Required inputs, config/registries/rag-collections.json (sheet 24 rows
   2-11), each as collection / users / metadata / strategy / owner / refresh /
   risk:
     RAG-SBC — SBC codes / COM and disciplines / source, edition, effective
       date, code, section, rights / hybrid plus rules, no ingest before
       ALLOWED / Legal and Compliance / on edition / P3
     RAG-BALADY — requirements and data / COM, STD, INF / city, municipality,
       service, date, URL, licence / structured plus archives where permitted /
       Compliance / monthly / P2-P3
     RAG-SCE — membership policies / REV and Review Ops / version, URL, check
       date / reference, no PII without purpose / Review Ops / monthly / P2
     RAG-PROJECT — project documents / all agents / tenant, project, ACL,
       revision, hash, classification / project-scoped index, no cross-tenant /
       PM / immediate / variable
     RAG-CLIENT — client standards / Design, QA, PMO / tenant-only, approval,
       superseded-by / priority only when delegated / Tenant Admin / on change /
       P2-P3
     RAG-CONTRACT — contracts and correspondence / PMO and Commercial /
       privilege, party, clause, dates, ACL / Restricted, no training / Legal /
       immediate / P3
     RAG-PRICES — prices and suppliers / CST, FIN, EXE / city, currency, date,
       supplier, validity / structured DB plus expiry / Commercial / monthly /
       P2
     RAG-QA-HSE — specs, ITP, HSE / QMS and HSE / project, revision, hold,
       method / rules plus retrieval, block superseded / QA and HSE /
       immediate / P3
     RAG-OEM — O&M and manuals / OPS and HND / asset, model, manufacturer,
       rights, revision / asset-linked / Facilities / on handover / P2
     RAG-GOLDEN — labelled cases / EVAL / consent, right, de-identification,
       label, split / evaluation only, leakage control / AI Gov and Privacy /
       per release / P3

D. EXECUTION INSTRUCTIONS
   1. Implement a Collection abstraction where each collection declares its own
      required metadata schema, its retrieval strategy, its owner role, its
      refresh cadence and its risk rating. Ingesting a document without that
      collection's required metadata fields is rejected.
   2. Enforce isolation on three dimensions simultaneously: collection, tenant
      and ACL. A retrieval request names exactly one collection and carries a
      tenant scope; the query cannot be constructed otherwise (reuse the
      structural guarantee from P04-05 step 5). Cross-collection retrieval
      requires an explicit, policy-approved fan-out that preserves each
      collection's own filters.
   3. Implement the per-collection strategies the source names rather than one
      generic vector search:
        - hybrid plus rules for RAG-SBC (keyword and vector, with a rules
          engine over structured clauses);
        - structured storage with an expiry for RAG-PRICES, where an expired
          price is not returned as current;
        - rules plus retrieval with superseded blocking for RAG-QA-HSE, where a
          superseded specification revision is never returned as applicable;
        - asset-linked retrieval for RAG-OEM;
        - reference-only for RAG-SCE with no PII ingestion absent a recorded
          purpose;
        - priority-only-when-delegated for RAG-CLIENT, meaning a client
          standard outranks a default only when the tenant has delegated that
          precedence.
   4. Implement supersession and effective-date awareness as first-class:
      RAG-SBC entries carry an edition and an effective date and a retrieval is
      resolved against the date applicable to the project, not against the
      newest edition. Sheet 37 row 13 requires the citation to include the
      edition and its applicability, which is only possible if the index stores
      both.
   5. Implement RAG-GOLDEN's leakage control as a hard separation: the
      evaluation collection is in a distinct store or namespace that production
      retrieval credentials cannot read. Add a test asserting a production
      query path cannot reach it. A golden set that leaks into production
      retrieval invalidates every evaluation built on it.
   6. Implement the no-training flags for RAG-CONTRACT and RAG-PROJECT, wired
      to the export check from P06-01 step 7.
   7. Build the ingestion pipeline: authorized channel, rights gate check
      (P06-01), required metadata validation, malware-scanned source artifact
      (P02-01), chunking that preserves locators so a citation can anchor to a
      page, clause or GUID, embedding only where the embedding right permits,
      and an immutable record linking every chunk to its source artifact
      version and digest.
   8. Implement refresh per the declared cadence, with the rule that a refresh
      re-checks rights before re-ingesting. A source whose rights lapsed is not
      silently refreshed.
   9. Implement retrieval observability for PHASE-10's dashboard: RAG hit rate,
      citation coverage, vector latency and ACL-denied counts (sheet 73 row 7).
  10. Tests:
        a. ingesting into RAG-PROJECT without a classification field ->
           rejected;
        b. a retrieval in RAG-PROJECT for tenant A never returns tenant B's
           chunks — attempt directly against the index;
        c. a retrieval naming one collection never returns another
           collection's chunks;
        d. a production credential attempting to query RAG-GOLDEN -> denied;
        e. an expired RAG-PRICES entry is not returned as current;
        f. a superseded RAG-QA-HSE revision is not returned as applicable;
        g. a RAG-SBC retrieval for a project with an earlier applicable edition
           returns that edition, not the newest;
        h. a chunk's citation resolves to its source artifact version and
           digest;
        i. a refresh of a source whose rights lapsed -> refused;
        j. ingestion of a BLOCKED source -> refused by the gate.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the Collection abstraction with per-collection metadata schemas
   - three-dimension isolation with structurally scoped queries
   - the six distinct retrieval strategies the source specifies
   - edition and effective-date resolution with supersession
   - hard separation of RAG-GOLDEN from production credentials
   - no-training flags and their export interaction
   - the rights-gated ingestion pipeline with locator-preserving chunking
   - rights-rechecking refresh
   - retrieval metrics for PHASE-10
   - tests/knowledge/collections-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - For case b and case d, paste the direct index probes.
   - Report, per collection: whether it exists, how many documents it holds,
     its rights decision, and whether it is usable today. Several will be empty
     or blocked; state that accurately.
   - Acceptance criterion: no retrieval crosses a collection, a tenant or an
     ACL; the golden set is unreachable from production; blocked sources remain
     un-ingested.

G. COMPLETION CONTRACT
   Definition of Done: ten collections defined with their own contracts,
   isolation proven by direct probes, strategies implemented, ingestion gated.
   Evidence to report: the ten test outputs, the index probes, the
   per-collection status table.
   Remaining blockers: RAG-SBC stays empty while OD-05 is unresolved;
   RAG-BALADY needs per-dataset licence review (sheet 25 row 3 decision
   "dataset review"); RAG-SCE is reference-only with no verification API
   (sheet 23 row 3). Name all three.
   Next prompt: P06-03.
```

**المخرجات المتوقعة:** عشر مجموعات بعقود بيانات وصفية منفصلة، عزل ثلاثي، خط استيعاب مُبوَّب.
**التحقق المطلوب:** لا استعلام يتجاوز مجموعة أو مستأجراً أو ACL؛ مجموعة التقييم غير قابلة للوصول من الإنتاج.
**الاعتمادية التالية:** `P06-03`.

---

### P06-03 — الاستشهاد المُتحقَّق وقواعد الامتثال

<!-- meta
id: P06-03
phase: PHASE-06
title_en: Verified citations and the compliance rules layer
prereq: [P06-02]
requirements: [REQ-KNW-05, REQ-KNW-06, REQ-GW-14, REQ-INT-02]
-->

**ماذا سينفذ هذا الأمر؟** يبني طبقة الاستشهاد المُتحقَّق: كل ادعاء معياري يحمل
المصدر والإصدار والمرساة والانطباق، مع محرك قواعد للنصوص المهيكلة ومسار توقف عند
غياب الدليل.

**لماذا نحتاجه؟** الورقة 71 الصف 5 تحدد سلوك صنف `SBC compliance`: «استرجاع
أكواد مرخَّصة موثوقة + محرك قواعد»، وفحص الجودة: «استشهادات بالبنود + توقيع
بشري»، وقاعدة البديل: «توقّف إلى البشري إذا غاب الدليل». والورقة 05 الصف 11
(`COM-01`) شروط إيقافها: «حقوق UNKNOWN؛ إصدار مجهول؛ تعارض».

**ما المتطلبات السابقة؟** `P06-02`.

**ما النتيجة المتوقعة؟** استشهادات قابلة للتحقق آلياً، ومحرك قواعد منفصل عن
النموذج، وتوقف صريح لا تخمين.

**كيف نتحقق من نجاحه؟** ادعاء معياري بلا استشهاد صالح يُرفض؛ وغياب الدليل يُنتج
توقفاً بشرياً لا نصاً مُخترَعاً.

```text
TASK P06-03 — Verified citations and the compliance rules layer

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P06-03
   Phase: PHASE-06
   Prerequisites: P06-02
   Requirements covered: REQ-KNW-05, REQ-KNW-06, REQ-GW-14, REQ-INT-02

B. OBJECTIVE
   Implement machine-verifiable citations and a deterministic rules layer for
   structured normative text, so a compliance claim either carries a resolvable,
   edition-correct, rights-cleared citation or does not exist — and absence of
   evidence pauses to a human instead of producing a plausible sentence.

   Why this is necessary: sheet 71 row 5 specifies, for the SBC compliance task
   class, retrieval of licensed authoritative codes plus a rules engine, a
   quality check of clause citations plus human sign-off, and the fallback
   "pause to human if evidence absent". Sheet 05 row 11 lists the compliance
   capability's stop conditions as UNKNOWN rights, unknown edition and
   conflict. Sheet 37 row 13 requires a citation to include the edition and its
   applicability. Sheet 38 row 12 (G-07) makes "no unsupported normative
   citation" a release blocker.

   SCOPE BOUNDARY: citation verification and the rules layer. Do not ingest SBC
   content — it is BLOCKED by P06-01 until OD-05 is resolved. Build and test
   against a synthetic normative corpus that stands in for a licensed code, and
   say so explicitly in your report.

C. CONTEXT
   Required inputs:
     - the rights gate (P06-01) and collections (P06-02)
     - the output validator's citation checks (P04-07 step 3), which this
       prompt supplies with real resolution capability
     - sheet 10 row 13: citations carry source, version, anchor and rights, and
       are required when a claim is made
     - sheet 17 row 4: citation validity is a metric — "the citation accurately
       supports the claim" — owned by Knowledge QA and used as a release gate
     - sheet 23 row 3: SCE membership has no proven public API; no scraping;
       an official channel or documented manual review is required

D. EXECUTION INSTRUCTIONS
   1. Implement the Citation entity per config/registries/data-entities.json:
      source, version, anchor and rights, with a rights snapshot. Add the
      applicability statement sheet 37 row 13 requires: which occupancy, scope
      and jurisdiction the cited clause applies to, and the effective date
      window.
   2. Implement anchor resolution: an anchor names a code, section and clause
      (or a page and span for unstructured sources) and must resolve to real
      stored text in the cited edition. Resolution returns the exact text span,
      so a citation can be checked rather than trusted.
   3. Implement claim-to-citation binding verification. A normative claim
      records which citation supports it, and verification confirms: the anchor
      resolves; the edition is the applicable one for the project's effective
      date; the rights snapshot permits quotation; and the resolved text is
      actually present. An unresolvable or non-applicable citation makes the
      claim invalid.
   4. Implement the applicability determination explicitly, because it is the
      compliance capability's core output (sheet 05 row 11: "determine editions
      and jurisdiction"). Inputs are location, occupancy and date; output is the
      applicable code set with editions and the reason. An indeterminate
      applicability is a stop condition, not a default to the newest edition.
   5. Implement the rules layer as deterministic code over structured clauses,
      separate from any model: a rule has an id, the clause it derives from,
      its parameters, its evaluation logic and its test cases. A rule's finding
      cites the clause it came from. Sheet 05 row 11 describes this as
      converting permitted text into rules and cited findings, and sheet 71
      row 5's cost control is "reuse indexed clauses".
   6. Implement the three stop conditions from sheet 05 row 11 as enforced
      halts:
        - UNKNOWN rights -> halt (already enforced by P06-01; wire the reason
          through so the user sees why);
        - unknown edition -> halt, do not assume;
        - conflict between applicable requirements -> halt and escalate to the
          discipline specialist, recording both conflicting clauses rather than
          silently picking one.
   7. Implement the pause-to-human fallback of sheet 71 row 5: when the
      retrieval returns no supporting evidence for a required claim, the step
      transitions to AWAITING_INFORMATION or escalates to a reviewer. It never
      emits a claim without a citation, and it never emits a citation it could
      not resolve. Add a test with a model double that attempts to return a
      fabricated clause reference and assert the system rejects it.
   8. Implement the citation validity measurement input for sheet 17 row 4: for
      a sample of claims, record whether the cited text actually supports the
      claim, as a human-labelled judgement stored for PHASE-14. Do not compute
      a validity percentage from automated resolution alone and present it as
      the metric — resolution proves the citation exists, not that it supports
      the claim. State that distinction in the implementation.
   9. For reviewer credential verification (sheet 23 row 3), implement a
      verification record abstraction with two permitted modes — an official
      channel integration when one exists, or a documented manual review with
      the evidence attached and the checker named. Scraping is not an available
      mode. PHASE-07 consumes this.
  10. Tests:
        a. a claim whose citation anchor does not resolve -> claim invalid,
           named;
        b. a citation to a non-applicable edition for the project's date ->
           rejected, with the applicable edition named;
        c. a citation whose rights snapshot forbids quotation -> rejected;
        d. a model double returning a fabricated clause reference -> rejected
           at verification, no claim emitted;
        e. indeterminate applicability -> halt, not a newest-edition default;
        f. two conflicting applicable requirements -> halt and escalate, both
           clauses recorded;
        g. no supporting evidence for a required claim -> pause to human, no
           uncited claim emitted;
        h. a rules-layer finding cites the clause it derives from, and the rule
           has passing test cases;
        i. a reviewer verification record cannot be created by a scraping mode.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the Citation entity with applicability and effective-date window
   - anchor resolution returning the exact cited span
   - claim-to-citation verification with four checks
   - applicability determination with indeterminacy as a halt
   - the deterministic rules layer with per-rule test cases
   - the three enforced stop conditions
   - the pause-to-human fallback with fabrication rejection
   - the human-labelled citation validity input for PHASE-14
   - the two-mode reviewer verification record with scraping excluded
   - tests/knowledge/citation-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - For case d, paste the fabricated reference and the rejection — this is the
     control behind release gate G-07.
   - State explicitly that the corpus used was synthetic, not SBC, and that
     G-07 cannot be satisfied for real Saudi code citations until OD-05 is
     resolved.
   - Acceptance criterion: no claim exists without a resolvable, applicable,
     rights-cleared citation; absence of evidence always pauses.

G. COMPLETION CONTRACT
   Definition of Done: citations verifiable end to end, rules layer
   deterministic and clause-linked, stop conditions and pause-to-human
   enforced, fabrication rejected.
   Evidence to report: the nine test outputs, the fabrication rejection, the
   explicit synthetic-corpus statement.
   Remaining blockers: OD-05 (SBC rights) blocks real compliance output.
   PHASE-09's villa path must therefore run without Saudi code citations until
   it is resolved — carry this constraint forward explicitly.
   Next prompt: P07-01. PHASE-06 exit requires AT-RAG-001 green, collection
   isolation proven, and citation verification rejecting fabrication.
```

**المخرجات المتوقعة:** استشهادات مُتحقَّقة بالانطباق والإصدار، محرك قواعد حتمي، توقفات مفروضة.
**التحقق المطلوب:** رفض الاستشهاد المُلفَّق؛ لا ادعاء بلا استشهاد قابل للحل.
**الاعتمادية التالية:** `P07-01`.

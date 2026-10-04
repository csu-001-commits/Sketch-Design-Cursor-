# PHASE-00 — الاكتشاف وجرد الواقع

<!-- phasemeta
id: PHASE-00
depends_on: []
criticality: P0
-->

## الغرض من المرحلة

المصدر يصرّح عن نفسه بأنه «أساس معماري وتشغيلي، ولا يمثل دليلاً على أن المنصة
مبنية أو مختبرة» (الورقة 00، الصف 14)، وبأن «بيئة التشغيل لم يتم الوصول إليها»
(الورقة 68، الصف 9). كما تسجّل الورقة 57 في الصف 2 ملاحظة حرجة: «v9 يصف معمارية
لا تنفيذاً مُتحققاً منه».

لذلك لا يجوز أن تبدأ أي كتابة كود قبل أن نعرف **ما هو الموجود فعلاً**. هذه
المرحلة وظيفتها الإجابة على سؤال واحد بالدليل: ما الذي يوجد اليوم من كود ونشر
وتكاملات وأسرار وبيانات، وما الفرق بين ذلك وبين ما يوصفه المصدر؟

هذه المرحلة **لا تغيّر** أي نظام قائم. كلها قراءة وتوثيق.

## شروط الدخول

- وصول إلى المستودع، وإلى بيئة التشغيل إن كانت موجودة، بتفويض من المالك.
- توافر المصدر: `Sketch_Design_Model_Gateway_Observability_v11.md`.

## شروط الخروج

- جرد مكتوب ومُدلَّل لما يوجد فعلاً (كود، نشر، تكاملات، أسرار، بيانات).
- تسجيل التعارضات الخمسة المرصودة في المصدر في سجل القرارات المفتوحة.
- مصادقة المالك على: الإصدار المرجعي المعتمد، والتسلسل التنفيذي الموفَّق بين
  الورقة 29 والورقة 67.

## المتطلبات المغطاة في هذه المرحلة

`REQ-GOV-05`, `REQ-GOV-06`, `REQ-INT-01`, `REQ-INT-04`, `REQ-OPN-01`,
`REQ-OPN-04`, `REQ-OPN-05`, `REQ-OPN-06`

## تحذير مهم

لا تُنفّذ أي أمر في هذه المرحلة مقابل بيئة إنتاج دون تفويض مكتوب. جرد الأسرار
يعني **تسجيل وجودها وأسمائها ومواضعها**، ولا يعني أبداً طباعة قيمها أو نسخها أو
تدوينها في أي ملف أو سجل.

---

## الأوامر التنفيذية

### P00-01 — جرد واقع المستودع وبيئة التشغيل

<!-- meta
id: P00-01
phase: PHASE-00
title_en: Repository and runtime reality inventory
prereq: []
requirements: [REQ-GOV-05, REQ-OPN-01]
-->

**ماذا سينفذ هذا الأمر؟** يفحص المستودع وبيئة التشغيل (إن وُجدت) ويكتب تقرير جرد
واقعي: ما هي الخدمات القائمة، ما إصداراتها، ما الذي يعمل وما الذي لا يعمل، وما
الفجوة بين الواقع ووصف المصدر.

**لماذا نحتاجه؟** لأن كل خطة لاحقة تعتمد على معرفة نقطة البداية. إن كان المستودع
فارغاً فنحن في مشروع جديد تماماً، وإن كان هناك نشر قائم فعلينا الحفاظ عليه وعدم
استبداله. المصدر نفسه لا يعرف الإجابة، ويطلبها في الورقة 67 الصف 2.

**ما المتطلبات السابقة؟** لا شيء. هذا أول أمر في المكتبة.

**ما النتيجة المتوقعة؟** ملف `docs/discovery/RUNTIME-INVENTORY.md` يحتوي جرداً
مُدلَّلاً، وملف `docs/EXECUTION-LOG.md` بأول مدخلة.

**كيف نتحقق من نجاحه؟** كل سطر في الجرد مرفق بدليل: مخرج أمر، أو مسار ملف، أو
تصريح صريح بأن المعلومة غير متوفرة. لا يُقبل أي سطر تخميني.

```text
TASK P00-01 — Repository and runtime reality inventory

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P00-01
   Phase: PHASE-00 (Discovery and baseline inventory)
   Prerequisites: none — this is the first prompt in the library
   Requirements covered: REQ-GOV-05, REQ-OPN-01

B. OBJECTIVE
   Produce an evidence-backed inventory of what actually exists today for the
   Sketch Design platform, and the delta between that reality and what the
   source workbook describes.

   Why this is necessary: the source states about itself that it is an
   architecture baseline and that the runtime environment was never accessed
   (sheet 00 row 14; sheet 68 row 9; sheet 57 row 2). Every later phase assumes
   a known starting point. Without this, the plan is guesswork.

   SCOPE BOUNDARY: this task is read-only. Do not create, modify, deploy,
   migrate or delete anything except the two report files named in E. Do not
   install dependencies into a shared environment. Do not call any paid API.

C. CONTEXT
   Required inputs:
     - This repository.
     - EXECUTION_BLUEPRINT/_registry/requirements.tsv (requirement registry).
     - EXECUTION_BLUEPRINT/01-DEEP-ANALYSIS.md (intended system description).
   Known constraint: the repository may be empty. That is a valid finding, not
   an error. Report it plainly.
   Known constraint: a deployed runtime may or may not exist. The source cannot
   tell us. Do not assume either way.

D. EXECUTION INSTRUCTIONS
   1. Inventory the repository:
      - List the full file tree, excluding dependency directories.
      - Read every build, dependency and configuration manifest you find
        (package.json, pyproject.toml, go.mod, Cargo.toml, pom.xml,
        Dockerfile, docker-compose.yml, Makefile, CI workflow files).
      - Record: languages, frameworks, declared runtime versions, declared
        services, declared datastores.
   2. Establish whether the project builds and tests:
      - Run the repository's own install, build, lint, typecheck and test
        commands exactly as the manifests define them.
      - Record the exact command, exit code and the final 30 lines of output
        for each. Do not fix failures in this task; record them.
   3. Inventory declared infrastructure:
      - From compose files, CI files, deploy directories and IaC files, list
        every service, port, volume, datastore and external dependency.
      - Mark each as DECLARED (it appears in config) and separately as
        REACHABLE / NOT REACHABLE / NOT CHECKED.
   4. Inventory the database reality, if a datastore is declared and reachable:
      - List schemas, tables, row counts and whether row-level security or
        equivalent tenant isolation is enabled.
      - Do NOT read, export or print row contents. Counts and DDL only.
   5. Inventory secrets by NAME ONLY:
      - List every environment variable name and secret reference the code or
        config expects.
      - For each, record: name, where it is expected, and PRESENT / ABSENT.
      - NEVER print, log, copy or commit a secret value. Not even partially.
   6. Build the delta table. For each of these capability areas from the
      source, record ABSENT / PARTIAL / PRESENT with the file or command that
      proves it:
        tenancy and isolation; identity, MFA and RBAC; policy engine;
        append-only audit; file gateway with AV scan; artifact versioning and
        digests; durable workflow runtime; workflow template registry;
        AI gateway; model registry and router; budget controller and usage
        ledger; agent registry and versioning; RAG and source-rights gate;
        typed findings; reviewer registry and eligibility; delivery lock, sign
        and release; pricing engine; payment webhooks; observability and
        tracing; admin control plane; connector manager and secrets vault;
        scan and capture; evaluation harness.
   7. Write docs/discovery/RUNTIME-INVENTORY.md with these sections:
      Repository inventory; Build and test reality; Declared infrastructure;
      Datastore reality; Expected secrets (names only); Capability delta table;
      What could not be determined and why.
   8. Append your entry to docs/EXECUTION-LOG.md per section 8 of the
      operating contract.

E. DELIVERABLES
   - docs/discovery/RUNTIME-INVENTORY.md
   - docs/EXECUTION-LOG.md (created or appended)
   No source code changes.

F. VERIFICATION
   - Every row of the capability delta table cites either a file path or a
     command output as its evidence, or says "NOT DETERMINED" with a reason.
   - The build and test section contains real exit codes and real output
     excerpts, not summaries.
   - The secrets section contains zero secret values. Grep your own report for
     anything that looks like a key, token or password and confirm it is clean.
   - Acceptance criterion: a reader who has never seen this project can state,
     from your report alone, what exists and what does not.

G. COMPLETION CONTRACT
   Definition of Done: RUNTIME-INVENTORY.md exists, every claim is evidenced,
   and the execution log entry is written.
   Evidence to report: the path to the inventory, the list of commands you ran
   with exit codes, and the count of capability areas marked ABSENT / PARTIAL /
   PRESENT.
   Remaining blockers: list anything you could not inspect, and what access you
   would need. An inaccessible runtime is a legitimate, reportable outcome —
   state it rather than guessing.
   Next prompt: P00-02.
```

**المخرجات المتوقعة:** `docs/discovery/RUNTIME-INVENTORY.md`، `docs/EXECUTION-LOG.md`.
**التحقق المطلوب:** كل صف مُدلَّل، لا قيم أسرار، مخارج أوامر حقيقية.
**الاعتمادية التالية:** `P00-02`.

---

### P00-02 — تحويل سجلات المصدر إلى ملفات مرجعية قابلة للقراءة آلياً

<!-- meta
id: P00-02
phase: PHASE-00
title_en: Import the source registers into machine-readable project files
prereq: [P00-01]
requirements: [REQ-WF-07, REQ-AGT-08, REQ-EVL-01, REQ-EVL-02, REQ-DAT-01]
-->

**ماذا سينفذ هذا الأمر؟** ينقل السجلات الجدولية من المصدر (القدرات الـ44، قوالب
مسارات العمل الثمانية، الضوابط الـ16، اختبارات القبول الـ13، الكيانات الـ20،
مجموعات RAG، مصفوفة الأهلية، أدوار RBAC) إلى ملفات JSON/YAML داخل المشروع
لتصبح مصدر حقيقة واحداً يمكن للكود والاختبارات الرجوع إليه.

**لماذا نحتاجه؟** لأن هذه السجلات ستُستخدم عشرات المرات في المراحل اللاحقة
(سجل القوالب، سجل الوكلاء، مصفوفة الأهلية، لوحة الأدلة). نسخها يدوياً في كل مرة
يُنتج انحرافاً. تحويلها مرة واحدة إلى بيانات يجعل الانحراف قابلاً للاكتشاف آلياً.

**ما المتطلبات السابقة؟** `P00-01` (نعرف هيكل المشروع وأين نضع الملفات).

**ما النتيجة المتوقعة؟** مجلد `config/registries/` يحتوي ملفات بيانات مُتحقَّقاً
من مخططها، مع سكربت تحقق.

**كيف نتحقق من نجاحه؟** عدّاد الصفوف في كل ملف يطابق عدد الصفوف في الورقة
المصدر، وسكربت التحقق يمر بلا أخطاء.

```text
TASK P00-02 — Import the source registers into machine-readable project files

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P00-02
   Phase: PHASE-00
   Prerequisites: P00-01 complete (repository structure known)
   Requirements covered: REQ-WF-07, REQ-AGT-08, REQ-EVL-01, REQ-EVL-02,
                         REQ-DAT-01

B. OBJECTIVE
   Convert the tabular registers in the source workbook into validated,
   machine-readable data files inside this repository, so that later phases
   reference one source of truth instead of re-transcribing the workbook.

   Why this is necessary: these registers are consumed repeatedly downstream
   (template registry in PHASE-03, agent registry in PHASE-05, eligibility
   matrix in PHASE-07, evidence ledger in PHASE-14). Hand-copying them each
   time guarantees drift. Importing once makes drift machine-detectable.

   SCOPE BOUNDARY: transcribe and structure only. Do not invent fields, do not
   fill blanks, do not resolve contradictions, do not add entries that are not
   in the source. Where the source cell is empty or says TBD or UNKNOWN,
   preserve that exactly.

C. CONTEXT
   Required input: the source export
   Sketch_Design_Model_Gateway_Observability_v11.md. If it is not present in the
   repository, request it from the owner and stop — do not reconstruct it from
   memory or from this prompt.
   Reference: EXECUTION_BLUEPRINT/_registry/requirements.tsv maps every register
   to its sheet and rows via the source_ref column.

D. EXECUTION INSTRUCTIONS
   1. Create config/registries/ and produce one file per register. Use JSON
      (or YAML if the repository already standardizes on YAML):

      a. workflow-templates.json       <- sheet 07, rows 2-9 (8 templates)
         fields: workflow_id, name_ar, version, segment, scope_ar,
                 capabilities[], action_risk, professional_consequence,
                 review_requirement_ar, pricing_id, test_suite_id,
                 evidence_state
      b. agent-capabilities.json       <- sheet 05, rows 2-46 (44 capabilities)
         fields: id, domain_ar, capability_ar, description_ar, inputs,
                 outputs, tools, knowledge, action_risk,
                 professional_consequence, human_gate_ar,
                 stop_conditions_ar, workflows, kpis, owner
      c. pmo-capabilities.json         <- sheet 06, rows 2-9 (8 capabilities)
      d. controls.json                 <- sheet 15, rows 2-17 (CTRL-001..016)
         fields: control_id, control, priority, source_state, required_evidence,
                 test_id, owner
      e. acceptance-tests.json         <- sheet 16, rows 2-14 (13 AT-* tests)
         fields: test_id, area, scenario_ar, expected_ar, environment, owner,
                 status
      f. data-entities.json            <- sheet 28, rows 2-21 (20 entities)
      g. data-constraints.json         <- sheet 39, rows 6-14 (9 tables)
         fields: entity, required_fields[], unique_constraint,
                 suggested_indexes[], invariant, retention
      h. rbac-roles.json               <- sheet 04, rows 2-11 (10 roles)
      i. admin-rbac-matrix.json        <- sheet 59, rows 2-10 (9 staff roles)
      j. eligibility-matrix.json       <- sheet 12, rows 2-9 (8 codes)
      k. rag-collections.json          <- sheet 24, rows 2-11 (10 collections)
      l. source-rights.json            <- sheet 25, rows 2-7 (6 sources)
      m. saudi-integrations.json       <- sheet 23, rows 2-16 (15 targets)
      n. model-registry-schema.json    <- sheet 72, rows 2-11 (field spec only,
                                          not model instances)
      o. routing-policies.json         <- sheet 71, rows 2-9 (8 task classes)
      p. release-gates.json            <- sheets 38 (G-01..G-10), 54
                                          (G01..G12), 76 (G01..G10), kept as
                                          three separate named gate sets
                                          because they are three distinct
                                          registers in the source
      q. finding-schema.json           <- sheet 10, rows 2-22 (21 fields)
         fields: field, type, obligation, definition_ar, example

   2. Every file carries a header object:
        { "source": "Sketch_Design_Model_Gateway_Observability_v11.md",
          "sheet": "<sheet name>", "rows": "<row range>",
          "imported_at": "<UTC date>", "row_count": <n>,
          "note": "Transcribed from source. Status words are the source's own
                   and are not readiness claims." }

   3. Write scripts/validate-registries.mjs (or .py, matching the repository's
      language) that asserts:
        - every file parses;
        - row_count equals the actual number of entries;
        - required keys are present on every entry;
        - IDs are unique within each file;
        - every capability ID referenced in workflow-templates.json exists in
          agent-capabilities.json or pmo-capabilities.json;
        - every test_id referenced in controls.json exists in
          acceptance-tests.json;
        - no entry has been silently given a value where the source had TBD,
          UNKNOWN or an empty cell (keep a literal null or the source token).

   4. Wire the validator into the repository's test or CI command so drift
      fails the build.

   5. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - config/registries/*.json (17 files as listed)
   - scripts/validate-registries.* and its wiring into the test command
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Run the validator; paste its real output and exit code.
   - For each file, state the expected row count from the source and the actual
     count, and confirm they match.
   - Acceptance criterion: the validator exits 0, and deliberately corrupting
     one entry (then reverting) makes it exit non-zero. Demonstrate both.

G. COMPLETION CONTRACT
   Definition of Done: all 17 registry files exist, the validator passes, and
   you have demonstrated it also fails on injected drift.
   Evidence to report: validator output, per-file row count table, the injected
   failure output.
   Remaining blockers: any register you could not transcribe faithfully, with
   the exact sheet and row and the ambiguity you hit.
   Next prompt: P00-03.
```

**المخرجات المتوقعة:** `config/registries/` (17 ملفاً)، `scripts/validate-registries.*`.
**التحقق المطلوب:** عدّادات الصفوف مطابقة، المدقّق ينجح ويفشل عند إدخال انحراف مُتعمَّد.
**الاعتمادية التالية:** `P00-03`.

---

### P00-03 — تدقيق صلاحية الوصول للتكاملات ومزودي النماذج

<!-- meta
id: P00-03
phase: PHASE-00
title_en: Integration and provider access audit
prereq: [P00-01, P00-02]
requirements: [REQ-GOV-06, REQ-INT-01, REQ-INT-04, REQ-INT-02, REQ-INT-03, REQ-GW-19]
-->

**ماذا سينفذ هذا الأمر؟** يحوّل قائمة التكاملات السعودية الخمسة عشر ومزودي
النماذج إلى سجل حالة وصول حقيقي: هل يوجد عقد؟ مفاتيح؟ بيئة sandbox؟ هل نجح نداء
تجريبي فعلاً؟

**لماذا نحتاجه؟** لأن المصدر صريح في الورقة 68 الصف 6: «تكاملات الجهات السعودية
تتطلب اتفاقيات رسمية ومفاتيح وتحققاً في بيئة sandbox»، وفي الورقة 57 الصف 5:
«لا يجوز افتراض توافر التكاملات السعودية». بناء ميزة على تكامل غير متاح هو أسرع
طريق إلى وعد مكسور.

**ما المتطلبات السابقة؟** `P00-01`، `P00-02` (سجل التكاملات موجود كبيانات).

**ما النتيجة المتوقعة؟** `docs/discovery/INTEGRATION-ACCESS-AUDIT.md` وتحديث
`config/registries/saudi-integrations.json` بحالة وصول حقيقية لكل هدف.

**كيف نتحقق من نجاحه؟** لا يوجد أي هدف بحالة «متاح» دون دليل: رقم عقد، أو مخرج
نداء sandbox ناجح، أو تصريح بأن الوصول غير متوفر.

```text
TASK P00-03 — Integration and provider access audit

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P00-03
   Phase: PHASE-00
   Prerequisites: P00-01, P00-02
   Requirements covered: REQ-GOV-06, REQ-INT-01, REQ-INT-02, REQ-INT-03,
                         REQ-INT-04, REQ-GW-19

B. OBJECTIVE
   Establish, per integration target and per model provider, whether access
   actually exists today — contract, credentials, sandbox, and a real
   successful call — and record the result as data the router and the
   connector manager can read later.

   Why this is necessary: the source explicitly forbids presuming Saudi
   authority integrations are available (sheet 68 row 6, sheet 57 row 5), and
   explicitly rejects assuming any gateway is Saudi-resident (sheet 77 row 5).
   Several targets are marked VERIFY, PARTNERSHIP or SANDBOX rather than
   available.

   SCOPE BOUNDARY: audit only. Do not sign up for anything, do not provision a
   paid account, do not purchase credits, and do not call a paid production
   endpoint. Sandbox calls are permitted ONLY where a sandbox credential is
   already present in the environment. If a credential is absent, the finding
   is "NO CREDENTIAL" — that is the answer, not a reason to obtain one.

C. CONTEXT
   Required inputs:
     - config/registries/saudi-integrations.json (from P00-02)
     - docs/discovery/RUNTIME-INVENTORY.md secrets section (names only)
   The 15 targets and the source's own status word for each are: Nafath
   (VERIFY), SCE (PARTNERSHIP), Balady Open Data (TEST), Balady Transactions
   (VERIFY), SBC 2024 (RIGHTS REVIEW), Etimad API portal (SANDBOX), ZATCA
   Fatoorah (ONBOARD), SPL National Address (TEST), GEOSA (VERIFY LAYER), Open
   Data Saudi (AVAILABLE), NCA (REFERENCE), SDAIA PDPL (REFERENCE), SAMA PSP
   list (REFERENCE), Saber (VERIFY), Salamah (VERIFY).
   Payment candidates from sheet 21: Moyasar, Geidea, Tamara, bank transfer,
   ZATCA Fatoorah.

D. EXECUTION INSTRUCTIONS
   1. For each of the 15 integration targets, determine and record:
        - access_class: PUBLIC_DATA | PUBLISHED_API | PARTNER_ONLY |
                        REFERENCE_DOCUMENT_ONLY | RIGHTS_REVIEW_REQUIRED
        - contract_status: NONE | REQUESTED | SIGNED  (from the owner; if the
          owner has not told you, record NOT PROVIDED — do not infer)
        - credential_status: ABSENT | SANDBOX_PRESENT | PRODUCTION_PRESENT
        - verified_call: NOT ATTEMPTED | SUCCESS | FAILURE, with the evidence
        - blocking_for: which requirement IDs depend on this target
        - the source's own status word, preserved verbatim
   2. Where a sandbox credential is already present, make ONE minimal
      non-mutating call (a health, metadata or lookup endpoint). Record the
      request path, the HTTP status and a redacted response excerpt. Never send
      real personal data. Never send project data.
   3. For model providers, record per provider: whether a key exists, whether a
      DPA or equivalent agreement is on file, the endpoint region, and the
      stated data-retention and training policy. Mark anything the owner has
      not supplied as NOT PROVIDED. Do not assert a residency claim you cannot
      evidence — this is the explicit prohibition in sheet 77 row 5.
   4. Produce a dependency risk list: every planned capability that would be
      blocked or degraded if a given integration never becomes available, and
      the documented fallback the source names (for example, sheet 23 row 2
      names OTP/MFA as the interim path for identity; sheet 23 row 3 forbids
      scraping and requires an official channel or documented manual review
      for SCE membership).
   5. Update config/registries/saudi-integrations.json with an `access_audit`
      object per target. Keep the original source fields untouched.
   6. Write docs/discovery/INTEGRATION-ACCESS-AUDIT.md.
   7. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - docs/discovery/INTEGRATION-ACCESS-AUDIT.md
   - updated config/registries/saudi-integrations.json with access_audit
   - a dependency risk list inside the audit document
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - No target carries verified_call = SUCCESS without a pasted status code and
     response excerpt.
   - No provider carries a residency or retention claim without a named
     document supplied by the owner.
   - Re-run scripts/validate-registries.* and confirm it still passes.
   - Acceptance criterion: for all 15 targets plus every provider, access state
     is one of the defined enum values, and nothing is left blank.

G. COMPLETION CONTRACT
   Definition of Done: the audit document exists, the registry carries an
   access_audit per target, the validator passes.
   Evidence to report: the count of targets per access_class, the list of
   successful sandbox calls with status codes, and the dependency risk list.
   Remaining blockers: every target whose availability the owner must resolve
   commercially. Name them explicitly — they are inputs to PHASE-15 scope.
   Next prompt: P00-04.
```

**المخرجات المتوقعة:** `docs/discovery/INTEGRATION-ACCESS-AUDIT.md`، تحديث سجل التكاملات.
**التحقق المطلوب:** لا ادعاء توفّر بلا دليل، لا ادعاء إقامة بيانات بلا مستند.
**الاعتمادية التالية:** `P00-04`.

---

### P00-04 — سجل التعارضات والقرارات المفتوحة وتثبيت ADRs

<!-- meta
id: P00-04
phase: PHASE-00
title_en: Contradiction register, open decisions and ADR bootstrap
prereq: [P00-01, P00-02, P00-03]
requirements: [REQ-OPN-04, REQ-OPN-05, REQ-OPN-06, REQ-OPN-02, REQ-OPN-03, ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-010]
-->

**ماذا سينفذ هذا الأمر؟** يثبّت القرارات المعمارية العشرة المعتمدة في المصدر
كملفات ADR داخل المشروع، ويسجّل التعارضات والفراغات التي لا يمكن حلها بلا قرار
من المالك.

**لماذا نحتاجه؟** القرارات العشرة (ADR-001..010) معتمدة في المصدر وحالتها
APPROVED، فهي قيود حاكمة على كل ما يليها ويجب أن تكون قابلة للرجوع إليها من
الكود لا من ملف Excel. وفي المقابل هناك تعارضات حقيقية لا يجوز للعميل البرمجي أن
يحلّها بنفسه، أهمها تعارض تسلسل التنفيذ بين الورقة 29 والورقة 67.

**ما المتطلبات السابقة؟** `P00-01`..`P00-03`.

**ما النتيجة المتوقعة؟** `docs/adr/ADR-001..010` و`docs/OPEN-DECISIONS.md` حيّ
داخل المشروع، ومصادقة مكتوبة من المالك على التسلسل المعتمد.

**كيف نتحقق من نجاحه؟** كل ADR يحتوي ضابط القبول المذكور في المصدر، وكل قرار
مفتوح له مالك وسؤال محدد وأثر معروف على المراحل.

```text
TASK P00-04 — Contradiction register, open decisions and ADR bootstrap

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P00-04
   Phase: PHASE-00
   Prerequisites: P00-01, P00-02, P00-03
   Requirements covered: ADR-001 through ADR-010, REQ-OPN-02, REQ-OPN-03,
                         REQ-OPN-04, REQ-OPN-05, REQ-OPN-06

B. OBJECTIVE
   Two outcomes:
   (1) Record the ten APPROVED architectural decisions from the source as ADR
       files in this repository so that code and reviews can cite them.
   (2) Record every contradiction and missing input that an implementation
       agent must NOT resolve on its own, each with a named owner and a
       specific question.

   Why this is necessary: ADR-001..010 are marked APPROVED in the source
   (sheet 02) and act as hard constraints on every later phase. Separately, the
   source contains contradictions a coding agent could silently paper over —
   above all two different execution sequences (sheet 29 versus sheet 67). The
   governing rule of this platform is evidence-based readiness (ADR-008), which
   is incompatible with quietly guessing.

   SCOPE BOUNDARY: write decision records and the open-questions register.
   Do not resolve an open decision yourself. Do not implement anything.

C. CONTEXT
   Required inputs:
     - the source export, sheet 02 rows 2-11 (the ten ADRs with their
       acceptance control and status)
     - EXECUTION_BLUEPRINT/06-OPEN-DECISIONS.md (the blueprint's own register)
     - docs/discovery/*.md from P00-01 and P00-03

D. EXECUTION INSTRUCTIONS
   1. Create docs/adr/ and write one file per decision, ADR-001 to ADR-010,
      each with: title, status (APPROVED, as the source states), context,
      decision, the acceptance control the source specifies verbatim,
      consequences, and the source reference (sheet 02 row N). The decisions
      are, in source order: Workflow-first; separation of interface from
      engine; multi-tenant isolation; typed findings; two risk axes; signature
      bound to digest; event-driven payment; no READY from database rows;
      RAG rights first; human accountability.
   2. Create docs/OPEN-DECISIONS.md as the live, in-repository register. Seed
      it with these, each as: ID, question, why it blocks, options, owner,
      impact if unresolved, status:
      a. OD-01 Authoritative version. The cover states v6.0 dated 04 October
         2026 while the same artifact carries v7, v8, v9, v10 and v11 content.
         Which version label governs?
      b. OD-02 Execution sequence. Sheet 29 sequences the villa MVP before
         platform expansion; sheet 67 sequences admin console, agent lifecycle,
         connector vault and model routing first; sheet 68 row 5 sets the P0
         priority as security, operations, agent lifecycle, connector vault,
         model routing and evidence. The blueprint reconciles these by building
         the platform spine first and the villa path as the first vertical
         slice. The owner must ratify or replace that reconciliation.
      c. OD-03 Commercial rates. Every rate in the quote calculator is zero
         except VAT (sheet 19 row 54). No commercial quotation is possible
         until the owner supplies an executed rate card.
      d. OD-04 KPI thresholds. Finding precision, finding recall, citation
         validity, workflow failure rate, time to signed delivery and cost per
         workflow are all TBD and may only be set from a measured baseline
         (sheet 30 row 14).
      e. OD-05 SBC 2024 usage rights. Licence, storage, embedding, quotation
         and redistribution rights are all UNKNOWN and the source decision is
         BLOCK until ALLOWED (sheet 25 row 2). Legal must resolve this before
         any compliance workflow can cite the code.
      f. OD-06 Brand identity. The wordmark in the workbook is explicitly
         temporary (sheet 00 row 17).
      g. OD-07 Deployment target and datastore. Not determined by the source;
         must be chosen and recorded as a new ADR before PHASE-01.
      h. OD-08 Deferred commerce. Sheet 68 row 8 defers white-label, external
         tenants and subscription sales. PHASE-16 stays closed until the owner
         reverses this in writing.
      Add any further contradiction you found in P00-01 or P00-03.
   3. For each open decision, state which phases and requirement IDs are
      blocked by it, so the impact is explicit.
   4. Write docs/adr/README.md explaining that ADR-001..010 are inherited from
      the source and APPROVED, while any new ADR created during implementation
      starts as PROPOSED and needs the owner's acceptance.
   5. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - docs/adr/ADR-001.md .. docs/adr/ADR-010.md
   - docs/adr/README.md
   - docs/OPEN-DECISIONS.md with at least OD-01..OD-08
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Each of the ten ADR files cites its source row and reproduces the source's
     acceptance control.
   - Each open decision names an owner role, a specific question, and the
     phases and requirement IDs it blocks.
   - Acceptance criterion: PHASE-01 cannot begin without OD-07 answered, and
     your register makes that dependency explicit.

G. COMPLETION CONTRACT
   Definition of Done: ten ADRs written, the open-decisions register seeded and
   impact-mapped, the execution log updated.
   Evidence to report: the ADR file list, the open-decision table, and which
   decisions block which phases.
   Remaining blockers: OD-01 through OD-08 are, by design, blockers owned by
   the owner and not by you. Report them as the phase exit condition. Do not
   proceed to PHASE-01 until OD-02 and OD-07 are answered.
   Next prompt: P01-01, after OD-02 and OD-07 are answered.
```

**المخرجات المتوقعة:** عشرة ملفات ADR، `docs/OPEN-DECISIONS.md`.
**التحقق المطلوب:** كل ADR يحمل ضابط قبوله من المصدر، وكل قرار مفتوح له مالك وأثر.
**الاعتمادية التالية:** `P01-01` — بعد إجابة `OD-02` و`OD-07` من المالك.

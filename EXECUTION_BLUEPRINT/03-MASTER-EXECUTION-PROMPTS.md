<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Produced by EXECUTION_BLUEPRINT/_tools/build.py from
     EXECUTION_BLUEPRINT/PHASES/*.md and EXECUTION_BLUEPRINT/_registry/*.tsv.
     Edit those sources and re-run the script. -->
# 03 — مكتبة أوامر التنفيذ الكاملة
> هذا هو المُخرَج الأساسي. يحتوي **كل** أوامر التنفيذ بالترتيب الصحيح.
> كل أمر مستقل بذاته وقابل للتنفيذ في جلسة Claude Code جديدة، بشرط توفر
> ملفات المشروع المذكورة فيه.

**تاريخ التوليد:** 2026-10-04 · **عدد المراحل:** 17 · **عدد الأوامر:** 69

## كيف تستخدم هذا الملف

1. اقرأ `EXECUTION_BLUEPRINT/00-START-HERE.md` أولاً.
2. تأكد من أن المتطلبات السابقة لكل أمر مُستوفاة قبل تنفيذه.
3. انسخ **النص الإنجليزي داخل كتلة الكود** كما هو إلى Claude Code.
4. لا تنفّذ أمراً قبل أن يُسجّل الأمر السابق نتيجته في `docs/EXECUTION-LOG.md`.
5. عند انقطاع السياق، اقرأ سجل التنفيذ ثم أعد التحقق من حالة المشروع الفعلية قبل الوثوق بأي ادعاء سابق.

## الفهرس

**PHASE-00 — الاكتشاف وجرد الواقع** (`P0`)
- `P00-01` — جرد واقع المستودع وبيئة التشغيل · المتطلب السابق: —
- `P00-02` — تحويل سجلات المصدر إلى ملفات مرجعية قابلة للقراءة آلياً · المتطلب السابق: `P00-01`
- `P00-03` — تدقيق صلاحية الوصول للتكاملات ومزودي النماذج · المتطلب السابق: `P00-01`, `P00-02`
- `P00-04` — سجل التعارضات والقرارات المفتوحة وتثبيت ADRs · المتطلب السابق: `P00-01`, `P00-02`, `P00-03`

**PHASE-01 — الأساسات: الهوية والعزل والسياسة والتدقيق** (`P0`)
- `P01-01` — هيكل المنصة والمخطط الأساسي وقيوده · المتطلب السابق: `P00-04`
- `P01-02` — عزل المستأجرين في كل الطبقات · المتطلب السابق: `P01-01`
- `P01-03` — الهوية والمصادقة ومصفوفة الأدوار · المتطلب السابق: `P01-02`
- `P01-04` — محرك السياسة الذي يفشل مُغلقاً · المتطلب السابق: `P01-03`
- `P01-05` — سجل التدقيق غير القابل للتعديل · المتطلب السابق: `P01-04`

**PHASE-02 — الأدلة والملفات وسلامة المخرجات** (`P0`)
- `P02-01` — بوابة الملفات والحجر الصحي · المتطلب السابق: `P01-05`
- `P02-02` — إصدارات المخرجات والبصمات والقفل · المتطلب السابق: `P02-01`
- `P02-03` — بيان الأدلة وسلسلة المصدر · المتطلب السابق: `P02-02`

**PHASE-03 — محرك مسارات العمل والعقود** (`P0`)
- `P03-01` — سجل قوالب مسارات العمل وتثبيت الإصدار · المتطلب السابق: `P02-03`
- `P03-02` — التنفيذ الصامد وآلة الحالات · المتطلب السابق: `P03-01`
- `P03-03` — عدم التكرار وصندوق الصادر وعقود الأحداث · المتطلب السابق: `P03-02`
- `P03-04` — سطح الـAPI للمنتج وعقوده · المتطلب السابق: `P03-03`
- `P03-05` — خدمة SLA والمؤقتات والتصعيد · المتطلب السابق: `P03-04`

**PHASE-04 — بوابة الذكاء والتوجيه والميزانية** (`P0`)
- `P04-01` — مدخل البوابة ومغلف المهمة والبث · المتطلب السابق: `P03-05`
- `P04-02` — سجل النماذج وسجل القدرات · المتطلب السابق: `P04-01`
- `P04-03` — الراوتر التكيّفي وسياسات التوجيه · المتطلب السابق: `P04-02`
- `P04-04` — محوّلات المزودين والبديل وقاطع الدائرة · المتطلب السابق: `P04-03`
- `P04-05` — مُجمِّع السياق وذاكرة المطالبات · المتطلب السابق: `P04-04`
- `P04-06` — وحدة الميزانية ودفتر الاستخدام · المتطلب السابق: `P04-05`
- `P04-07` — مُدقِّق المخرجات · المتطلب السابق: `P04-06`

**PHASE-05 — تشغيل الوكلاء والسجل والإصدارات** (`P0`)
- `P05-01` — عقد تشغيل الوكيل بمجالاته العشرة · المتطلب السابق: `P04-07`
- `P05-02` — سجل الوكلاء ودورة حياة الإصدارات · المتطلب السابق: `P05-01`
- `P05-03` — حدود الأدوات ومنع الحقن والتسريب · المتطلب السابق: `P05-02`
- `P05-04` — محرك R/P والبوابات البشرية · المتطلب السابق: `P05-03`

**PHASE-06 — المعرفة وحقوق المصادر وRAG** (`P0`)
- `P06-01` — بوابة حقوق المصادر · المتطلب السابق: `P02-03`
- `P06-02` — المجموعات العشر والعزل والاستيعاب · المتطلب السابق: `P06-01`
- `P06-03` — الاستشهاد المُتحقَّق وقواعد الامتثال · المتطلب السابق: `P06-02`

**PHASE-07 — الملاحظات والمراجعة والأهلية والتسليم** (`P0`)
- `P07-01` — مخطط الملاحظات المُنمَّط · المتطلب السابق: `P06-03`
- `P07-02` — سجل المراجعين ومصفوفة الأهلية · المتطلب السابق: `P07-01`
- `P07-03` — الإسناد: المرشّحات الصلبة وتعارض المصالح والاستقلالية · المتطلب السابق: `P07-02`
- `P07-04` — قرارات المراجعة على مستوى كل ملاحظة · المتطلب السابق: `P07-03`
- `P07-05` — القفل والتوقيع على البصمة وحزمة التسليم · المتطلب السابق: `P07-04`
- `P07-06` — الإفراج وصفحة التحقق والإبطال · المتطلب السابق: `P07-05`

**PHASE-08 — التسعير والدفع والفوترة** (`P0`)
- `P08-01` — محرك التسعير ولقطات المعدلات · المتطلب السابق: `P07-06`
- `P08-02` — دورة حياة عرض السعر والقفل عند القبول · المتطلب السابق: `P08-01`
- `P08-03` — الدفع بالأحداث: تفعيل بـwebhook فقط · المتطلب السابق: `P08-02`
- `P08-04` — الفوترة والمطابقة وZATCA · المتطلب السابق: `P08-03`

**PHASE-09 — المسار الذهبي لمراجعة الفيلا** (`P0`)
- `P09-01` — الاستقبال والتوجيه وفهم الملفات · المتطلب السابق: `P08-04`
- `P09-02` — الامتثال والمسودة المعمارية وبوابة الجودة · المتطلب السابق: `P09-01`
- `P09-03` — التشغيل الكامل من طرف إلى طرف ودليل G01 · المتطلب السابق: `P09-02`

**PHASE-10 — الرصد والموثوقية وFinOps** (`P0`)
- `P10-01` — التتبع الموحد وربط السلسلة · المتطلب السابق: `P09-03`
- `P10-02` — اللوحات التسع والتنبيهات · المتطلب السابق: `P10-01`
- `P10-03` — كتب التشغيل ومسارات الدعم · المتطلب السابق: `P10-02`
- `P10-04` — النسخ الاحتياطي والاسترجاع وRTO/RPO · المتطلب السابق: `P10-03`

**PHASE-11 — الأمن والخصوصية وPDPL** (`P0`)
- `P11-01` — الأساس النظامي وسجل المعالجة والموافقة · المتطلب السابق: `P10-04`
- `P11-02` — حقوق صاحب البيانات · المتطلب السابق: `P11-01`
- `P11-03` — الحفظ والحجز القانوني والحذف المُتحقَّق · المتطلب السابق: `P11-02`
- `P11-04` — البرنامج الخصومي والخرق والإقامة · المتطلب السابق: `P11-03`

**PHASE-12 — المسح والالتقاط** (`P1`)
- `P12-01` — أنماط الالتقاط والموافقة · المتطلب السابق: `P11-04`
- `P12-02` — عقود المسح وخط الأدلة · المتطلب السابق: `P12-01`
- `P12-03` — LiDAR والدقة والتحقق البشري الإلزامي · المتطلب السابق: `P12-02`

**PHASE-13 — لوحة التحكم الإدارية والموصلات والدعم** (`P0`)
- `P13-01` — مستوى التحكم والحد المعماري · المتطلب السابق: `P12-03`
- `P13-02` — دورة حياة الموصلات وخزانة الأسرار · المتطلب السابق: `P13-01`
- `P13-03` — القدرات الإدارية الست عشرة ومصفوفة الصلاحيات · المتطلب السابق: `P13-02`
- `P13-04` — سطح الدعم والتشخيص المُحجَّب · المتطلب السابق: `P13-03`

**PHASE-14 — التقييم والتعلم وبوابات الإصدار** (`P0`)
- `P14-01` — المجموعات الذهبية ومحرك التقييم · المتطلب السابق: `P13-04`
- `P14-02` — قياس النماذج بأبعاده السبعة · المتطلب السابق: `P14-01`
- `P14-03` — بوابة الانحدار الحاجزة · المتطلب السابق: `P14-02`
- `P14-04` — دفتر الأدلة وفرض بوابات الإصدار · المتطلب السابق: `P14-03`
- `P14-05` — دورة التعلم وحكومة الإصدار المستمرة · المتطلب السابق: `P14-04`

**PHASE-15 — التوسع في المسارات التخصصية** (`P1`)
- `P15-01` — بوابة إدخال القوالب الجديدة · المتطلب السابق: `P14-05`
- `P15-02` — مسارات BIM والكميات · المتطلب السابق: `P15-01`
- `P15-03` — MEP والبنية التحتية والموقع وPMO · المتطلب السابق: `P15-02`

**PHASE-16 — التجارة المؤجلة (خارج نطاق الإطلاق)** (`DEFERRED`)
- `P16-01` — بوابة التفويض (الأمر الوحيد القابل للتنفيذ الآن) · المتطلب السابق: `P14-04`
- `P16-02` — تنفيذ التجارة متعددة المستأجرين (مشروط بالتفويض) · المتطلب السابق: `P16-01`


---

# PHASE-00 — الاكتشاف وجرد الواقع


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

---

### `P00-01` — جرد واقع المستودع وبيئة التشغيل

**Phase:** `PHASE-00` · **EN title:** Repository and runtime reality inventory

**المتطلبات السابقة:** —

**المتطلبات المغطاة:** `REQ-GOV-05`, `REQ-OPN-01`

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

---

### `P00-02` — تحويل سجلات المصدر إلى ملفات مرجعية قابلة للقراءة آلياً

**Phase:** `PHASE-00` · **EN title:** Import the source registers into machine-readable project files

**المتطلبات السابقة:** `P00-01`

**المتطلبات المغطاة:** `REQ-WF-07`, `REQ-AGT-08`, `REQ-EVL-01`, `REQ-EVL-02`, `REQ-DAT-01`

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

---

### `P00-03` — تدقيق صلاحية الوصول للتكاملات ومزودي النماذج

**Phase:** `PHASE-00` · **EN title:** Integration and provider access audit

**المتطلبات السابقة:** `P00-01`, `P00-02`

**المتطلبات المغطاة:** `REQ-GOV-06`, `REQ-INT-01`, `REQ-INT-04`, `REQ-INT-02`, `REQ-INT-03`, `REQ-GW-19`

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

---

### `P00-04` — سجل التعارضات والقرارات المفتوحة وتثبيت ADRs

**Phase:** `PHASE-00` · **EN title:** Contradiction register, open decisions and ADR bootstrap

**المتطلبات السابقة:** `P00-01`, `P00-02`, `P00-03`

**المتطلبات المغطاة:** `REQ-OPN-04`, `REQ-OPN-05`, `REQ-OPN-06`, `REQ-OPN-02`, `REQ-OPN-03`, `ADR-001`, `ADR-002`, `ADR-003`, `ADR-004`, `ADR-005`, `ADR-006`, `ADR-007`, `ADR-008`, `ADR-009`, `ADR-010`

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


---

# PHASE-01 — الأساسات: الهوية والعزل والسياسة والتدقيق


## الغرض من المرحلة

بناء العمود الفقري الذي يستحيل إضافته لاحقاً: اشتقاق `tenant_id` من الهوية
وفرضه في كل طبقة، وأدوار محددة بصلاحيات ومنع صريح، ومحرك سياسة يفشل مُغلقاً،
وسجل تدقيق لا يقبل التعديل.

الورقة 02 الصف 4 (ADR-003) تجعل العزل قراراً معتمداً: «`tenant_id` مشتق من
الهوية ويُطبَّق في IAM وDB والتخزين والطوابير وRAG». والورقة 27 الصف 2 تصنّفه
`CRITICAL`. أما الورقة 68 الصف 3 فتحدد نطاق الإطلاق: «تشغيل أحادي المستأجر
مملوك الآن، مع بدائيات واعية بالمستأجر للمستقبل» — أي أننا نبني المخطط واعياً
بالمستأجر من اليوم الأول، لكننا لا نبني تجارة متعددة المستأجرين.

## شروط الدخول

- اكتمال `PHASE-00`.
- إجابة `OD-07` (هدف النشر وقاعدة البيانات) و`OD-02` (التسلسل المعتمد) من المالك.

## شروط الخروج

- نجاح `AT-SEC-001`: محاولة مستأجر A الوصول إلى معرفات وملفات ومتجهات مستأجر B
  تُرفض بـ403/404 بلا تسريب أي بيانات وصفية، مع تنبيه.
- اختبارات سلبية لكل دور من الأدوار العشرة.
- سجل تدقيق مُثبت أنه كاشف للتلاعب.
- ترحيل المخطط الأساسي بقيوده.

## المتطلبات المغطاة في هذه المرحلة

`ADR-003`, `REQ-GOV-01`, `REQ-TEN-01`..`REQ-TEN-09`, `REQ-SEC-03`, `REQ-SEC-04`,
`REQ-DAT-01`, `REQ-DAT-02`, `REQ-API-03`, `REQ-INT-03`

## تحذير مهم

العزل ليس ميزة تُضاف لاحقاً. كل جدول وكل مفتاح تخزين وكل طابور وكل فهرس متجهات
يُنشأ في هذه المرحلة أو بعدها يجب أن يحمل نطاق المستأجر من لحظة إنشائه. إضافة
العزل بأثر رجعي على بيانات قائمة هي من أكثر الهجرات خطورة.

---

## الأوامر التنفيذية

---

### `P01-01` — هيكل المنصة والمخطط الأساسي وقيوده

**Phase:** `PHASE-01` · **EN title:** Platform skeleton and core schema with constraints

**المتطلبات السابقة:** `P00-04`

**المتطلبات المغطاة:** `REQ-DAT-01`, `REQ-DAT-02`, `REQ-SEC-03`, `REQ-GOV-01`, `REQ-TEN-02`, `REQ-TEN-04`

**ماذا سينفذ هذا الأمر؟** يثبّت اختيار المنصة وقاعدة البيانات في ADR جديد، ثم
ينشئ الهيكل الأولي وترحيلات المخطط للكيانات الأساسية مع القيود والفهارس المحددة
في الورقة 39.

**لماذا نحتاجه؟** الورقة 28 تحدد عشرين كياناً أساسياً، والورقة 39 تحدد لكل جدول
حقوله الإلزامية وقيد التفرد وفهارسه والثابت المنطقي وسياسة الحفظ. هذه ليست
تفاصيل لاحقة: قيد `UNIQUE (tenant_id, idempotency_key)` هو ما يمنع الشحن
المزدوج، وقيد `UNIQUE (artifact_id, review_version)` هو ما يحمي سلامة المراجعة.

**ما المتطلبات السابقة؟** `P00-04`، وإجابة `OD-07`.

**ما النتيجة المتوقعة؟** مشروع يبنى ويختبر، وترحيلات تُطبَّق وتُسترجع على قاعدة
بيانات مؤقتة، وقيود مُثبتة بالاختبار.

**كيف نتحقق من نجاحه؟** لكل قيد تفرد في الورقة 39 اختبار يُدخل تكراراً ويتوقع
الرفض. الترحيل يُطبَّق ويُرجَع بلا فقدان.

```text
TASK P01-01 — Platform skeleton and core schema with constraints

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-01
   Phase: PHASE-01 (Foundations)
   Prerequisites: P00-04 complete; open decisions OD-02 and OD-07 answered by
                  the owner and recorded in docs/OPEN-DECISIONS.md
   Requirements covered: REQ-DAT-01, REQ-DAT-02, REQ-SEC-03, REQ-GOV-01

B. OBJECTIVE
   Stand up the project skeleton and the core database schema with the exact
   integrity constraints the source specifies, so that every later phase builds
   on enforced invariants rather than on convention.

   Why this is necessary: sheet 28 defines 20 core entities; sheet 39 defines,
   per table, the required fields, the uniqueness constraint, the suggested
   indexes, the invariant and the retention rule. Those constraints are the
   mechanism behind several P0 controls — UNIQUE (tenant_id, idempotency_key)
   is what prevents a double charge, and UNIQUE (artifact_id, review_version)
   is what protects review integrity.

   SCOPE BOUNDARY: schema, migrations, constraints and the minimum application
   skeleton needed to run them. No business logic, no endpoints beyond a health
   check, no AI, no payment code.

C. CONTEXT
   Required inputs:
     - config/registries/data-entities.json (sheet 28, 20 entities)
     - config/registries/data-constraints.json (sheet 39, 9 tables)
     - docs/OPEN-DECISIONS.md — OD-07 names the chosen datastore
     - docs/discovery/RUNTIME-INVENTORY.md — what already exists
   Constraint from the source: sheet 39 row 3 states these are proposed
   relational constraints and that migration review is required before
   implementation. Treat the constraint set as specified, but review it against
   your chosen engine and report any incompatibility rather than silently
   changing it.
   Constraint: launch scope is single-tenant owned operation with tenant-aware
   primitives (sheet 68 row 3). Every table carries tenant_id from the start
   even though only one tenant exists at launch.

D. EXECUTION INSTRUCTIONS
   1. If a platform or datastore decision is not already an accepted ADR, write
      docs/adr/ADR-011-platform-and-datastore.md as PROPOSED, capturing the
      owner's answer to OD-07, the alternatives considered, and the
      consequences. Do not proceed past step 2 if OD-07 is unanswered.
   2. Create or extend the project skeleton so that install, build, lint,
      typecheck and test all run and pass on an empty-but-valid project. Match
      whatever the repository already uses; if the repository is empty, choose a
      stack consistent with the ADR and justify it there.
   3. Write forward migrations for the 20 entities of sheet 28. Every table:
        - has tenant_id, not nullable, on every tenant-scoped table;
        - has created_at and updated_at in UTC;
        - uses the exact uniqueness constraints from
          config/registries/data-constraints.json where that table appears
          there (projects, workflow_runs, agent_executions, evidence_assets,
          review_decisions, boq_items, usage_ledger, outbox_events,
          idempotency_keys);
        - creates the suggested indexes from that same register.
   4. Implement the invariants from sheet 39 that are expressible in the
      database, as constraints rather than as application checks:
        - idempotency_keys conflicts when the request hash differs for the same
          (tenant_id, key);
        - review_decisions is append-only (no UPDATE, no DELETE) — enforce with
          a rule, trigger or permission, not with a code comment;
        - evidence_assets.sha256 is not nullable;
        - usage_ledger.execution_id is unique, enabling exactly-once posting.
   5. Encryption at rest and in transit per sheet 27 row 6: configure TLS for
      client connections and document the at-rest mechanism (engine-level,
      volume-level or cloud-managed) with the key custodian named. If you cannot
      enable it in the local environment, state that explicitly and record what
      production must configure.
   6. Write a migration test script that, on a throwaway database:
        - applies every migration from empty;
        - asserts every expected table, column, constraint and index exists;
        - for each uniqueness constraint, inserts a duplicate and asserts the
          write is rejected;
        - asserts review_decisions rejects UPDATE and DELETE;
        - rolls back or tears down cleanly.
   7. Wire that script into the repository's test or validation command.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - docs/adr/ADR-011-platform-and-datastore.md
   - migration files for the 20 entities
   - a migration and constraint test script, wired into the test command
   - updated README section describing how to run migrations locally
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Run the full migration from empty on a throwaway database. Paste the real
     output and exit code.
   - Paste the output of the constraint test showing each duplicate insert
     being rejected, naming the constraint.
   - Paste the output showing UPDATE and DELETE rejected on review_decisions.
   - Confirm build, lint, typecheck and test all pass; paste exit codes.
   - Acceptance criterion: every table in data-constraints.json has its stated
     uniqueness constraint proven by a failing duplicate insert. A table whose
     constraint you could not implement is reported as NOT VERIFIED with the
     engine limitation that caused it.

G. COMPLETION CONTRACT
   Definition of Done: migrations apply from empty, every specified constraint
   is proven by test, the project's own checks pass.
   Evidence to report: migration output, constraint test output, the table of
   entity -> constraint -> PROVEN / NOT VERIFIED.
   Remaining blockers: any constraint from sheet 39 that is incompatible with
   the chosen engine — report it, propose the equivalent, and do not silently
   drop it.
   Next prompt: P01-02.
```

**المخرجات المتوقعة:** ترحيلات الكيانات العشرين، سكربت اختبار القيود، `ADR-011`.
**التحقق المطلوب:** كل قيد تفرد مُثبت برفض إدخال مكرر؛ `review_decisions` يرفض التعديل والحذف.
**الاعتمادية التالية:** `P01-02`.

---

---

### `P01-02` — عزل المستأجرين في كل الطبقات

**Phase:** `PHASE-01` · **EN title:** Tenant isolation across every layer

**المتطلبات السابقة:** `P01-01`

**المتطلبات المغطاة:** `ADR-003`, `REQ-TEN-01`, `REQ-TEN-03`, `REQ-TEN-06`, `REQ-API-03`

**ماذا سينفذ هذا الأمر؟** يفرض العزل في قاعدة البيانات (RLS أو تقسيم)، وفي مفاتيح
التخزين، وفي الطوابير، وفي فلاتر المتجهات، ويبني اختبار `AT-SEC-001` السلبي.

**لماذا نحتاجه؟** هذا هو الضابط `CTRL-001` بأولوية `CRITICAL` (الورقة 15 الصف 2)،
والمؤشر الوحيد في الورقة 30 الذي هدفه صفر مطلق مع إجراء «Stop-the-line». كما أن
الورقة 33 الصف 7 تضيف شرطاً دقيقاً: «لا تكشف أبداً وجود كيان لمستأجر آخر» — أي أن
الرد على طلب غير مصرح به يجب ألا يفرّق بين «غير موجود» و«موجود لكن ممنوع».

**ما المتطلبات السابقة؟** `P01-01`.

**ما النتيجة المتوقعة؟** عزل مفروض في أربع طبقات، واختبار سلبي آلي في مجموعة
الاختبارات، وتنبيه عند محاولة الاختراق.

**كيف نتحقق من نجاحه؟** `AT-SEC-001`: مستأجر A يحاول قراءة وكتابة معرفات وملفات
ومتجهات مستأجر B، فيحصل على 403/404 بلا تسريب بيانات وصفية، ويُسجَّل تنبيه.

```text
TASK P01-02 — Tenant isolation across every layer

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-02
   Phase: PHASE-01
   Prerequisites: P01-01 (schema and constraints in place)
   Requirements covered: ADR-003, REQ-TEN-01, REQ-TEN-03, REQ-TEN-06,
                         REQ-API-03

B. OBJECTIVE
   Enforce tenant isolation in all four layers the source names — database,
   object storage, queues and vector indexes — with tenant_id always derived
   from the authenticated identity and never accepted from a client, and prove
   it with the negative test AT-SEC-001.

   Why this is necessary: this is CTRL-001 at CRITICAL priority (sheet 15
   row 2), it is ADR-003 (sheet 02 row 4), and it is the only KPI in the source
   with an absolute target of zero and a Stop-the-line action (sheet 30 row 2).
   Sheet 33 row 7 adds a precise requirement: cross-tenant existence must never
   be revealed, so an unauthorized read must not let the caller distinguish
   "does not exist" from "exists but forbidden".

   SCOPE BOUNDARY: isolation enforcement and its tests. Do not build product
   endpoints. Do not build the AI gateway. Add only the minimal routes needed
   to exercise the isolation test.

C. CONTEXT
   Required inputs:
     - the migrations from P01-01
     - config/registries/data-entities.json
     - config/registries/acceptance-tests.json, entry AT-SEC-001: "Tenant A
       attempts B's IDs, files and vectors" -> expected "403/404 with no
       metadata leak plus alert"
   Constraint: launch is single-tenant (sheet 68 row 3), so the test must
   provision at least two tenants in the test fixture even though production
   runs one. Isolation that is never exercised is isolation that does not work.

D. EXECUTION INSTRUCTIONS
   1. Database layer:
      - Enable row-level security (or the engine's equivalent) on every
        tenant-scoped table, with a default-deny policy.
      - Derive the tenant context from the authenticated session on every
        connection or transaction. Never read tenant_id from a request body,
        query parameter or header.
      - Add a test that asserts a query without a tenant context returns zero
        rows rather than all rows.
   2. Object storage layer:
      - Namespace every object key with the tenant prefix.
      - Scope credentials or signed URLs so a token for tenant A cannot
        construct a readable URL for tenant B's prefix.
   3. Queue layer:
      - Carry tenant_id in every message envelope and assert it on consume.
      - Reject a message whose tenant does not match the consumer's scope, and
        route it to the dead-letter queue with an alert rather than processing
        it.
   4. Vector or search layer:
      - If a vector store exists at this point, enforce a mandatory tenant
        filter at the query-construction layer so a query cannot be issued
        without it. If no vector store exists yet, write the enforcement
        interface and a failing-by-default stub, and record that PHASE-06 will
        complete it.
   5. Response shaping:
      - Implement a single authorization helper that returns an identical
        response shape for "not found" and "forbidden" on cross-tenant access,
        so no metadata, existence hint, ID echo or timing difference leaks.
   6. Alerting:
      - Emit a structured security event on every cross-tenant attempt, with
        actor, target, decision and correlation id, into the audit path that
        P01-05 will harden. Never put the attempted payload in the event.
   7. Implement AT-SEC-001 as an automated test that, for tenants A and B:
        - attempts a cross-tenant read by ID on every tenant-scoped entity;
        - attempts a cross-tenant write;
        - attempts a cross-tenant object fetch;
        - attempts a cross-tenant vector or search query;
        - asserts 403 or 404 with an identical body shape in every case;
        - asserts no response contains B's identifiers or counts;
        - asserts a security event was emitted for each attempt.
   8. Wire AT-SEC-001 into the test command and mark it non-skippable.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - RLS or equivalent policies in migrations
   - tenant-context derivation middleware
   - object key namespacing and scoped credential issuance
   - queue envelope tenant assertion with DLQ routing
   - vector or search mandatory tenant filter (or enforced stub)
   - the uniform not-found/forbidden authorization helper
   - tests/security/at-sec-001.* implementing the full negative suite
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Run AT-SEC-001. Paste the real output showing every assertion.
   - Demonstrate the test actually catches a regression: temporarily disable
     one isolation layer, show the test failing, restore it, show it passing.
     Paste both outputs.
   - Confirm no response body differs between forbidden and missing.
   - Acceptance criterion: AT-SEC-001 passes, and its deliberate-regression
     run fails. Both are required — a test that cannot fail proves nothing.

G. COMPLETION CONTRACT
   Definition of Done: isolation enforced in all four layers, AT-SEC-001
   passing and proven able to fail, security events emitted.
   Evidence to report: AT-SEC-001 output, the deliberate-regression output, and
   a table of layer -> mechanism -> test that covers it.
   Remaining blockers: any layer not yet present in the project (for example a
   vector store before PHASE-06) — name it and name the prompt that completes
   it.
   Next prompt: P01-03.
```

**المخرجات المتوقعة:** سياسات RLS، وسيط سياق المستأجر، اختبار `AT-SEC-001`.
**التحقق المطلوب:** الاختبار ينجح، ويفشل عند تعطيل طبقة عزل متعمداً.
**الاعتمادية التالية:** `P01-03`.

---

---

### `P01-03` — الهوية والمصادقة ومصفوفة الأدوار

**Phase:** `PHASE-01` · **EN title:** Identity, authentication strength and the role matrix

**المتطلبات السابقة:** `P01-02`

**المتطلبات المغطاة:** `REQ-TEN-05`, `REQ-TEN-07`, `REQ-TEN-08`, `REQ-TEN-09`, `REQ-INT-03`

**ماذا سينفذ هذا الأمر؟** يبني الهوية (OIDC)، ودرجات المصادقة المطلوبة لكل دور
(MFA، step-up، JIT، break-glass)، ومصفوفة الأدوار العشرة بما تسمح وما تحظر وما
نطاق بياناتها.

**لماذا نحتاجه؟** الورقة 04 لا تكتفي بتسمية الأدوار، بل تحدد لكل دور عموداً
«يحظر» — وهذا هو الجزء الذي يُنسى عادة. مثال: `EXECUTION_ENGINEER` يُحظر عليه
«مراجعة مستقلة لعمله»، و`FINANCE` يُحظر عليه «تغيير delivery hash»،
و`SUPPORT_L2` يُحظر عليه «قرار reviewer أو payment status يدوياً». هذه محظورات
يجب أن تكون مفروضة بالكود ومُختبرة سلبياً.

**ما المتطلبات السابقة؟** `P01-02`.

**ما النتيجة المتوقعة؟** مصادقة عاملة بدرجات، ومصفوفة أدوار مفروضة، واختبار سلبي
لكل محظور في الورقة 04.

**كيف نتحقق من نجاحه؟** لكل صف في الورقة 04 اختبار يحاول الفعل المحظور ويتوقع
الرفض مع تسجيل تدقيقي.

```text
TASK P01-03 — Identity, authentication strength and the role matrix

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-03
   Phase: PHASE-01
   Prerequisites: P01-02 (tenant isolation enforced)
   Requirements covered: REQ-TEN-05, REQ-TEN-07, REQ-TEN-08, REQ-TEN-09,
                         REQ-INT-03

B. OBJECTIVE
   Implement identity and authorization: OIDC-based authentication, the
   per-role authentication strength the source specifies, and the ten-role
   matrix with its allow list, data scope and — critically — its explicit deny
   list, each deny proven by a negative test.

   Why this is necessary: sheet 04 specifies for all ten roles not only what
   they may do but what they are forbidden to do. Those denials carry the real
   safety value and are the ones implementations usually omit. Examples from
   the source: EXECUTION_ENGINEER is forbidden from independently reviewing
   their own work; FINANCE is forbidden from changing a delivery hash;
   SUPPORT_L2 is forbidden from manually setting a reviewer decision or a
   payment status; PLATFORM_OWNER is forbidden from a discipline signature
   without eligibility and from disabling audit.

   SCOPE BOUNDARY: authentication, authorization and the role matrix. The
   policy engine itself is P01-04. Reviewer eligibility logic is PHASE-07 —
   here you implement only the role-level gate.

C. CONTEXT
   Required inputs:
     - config/registries/rbac-roles.json (sheet 04, 10 roles with allow, data
       scope, deny, authentication strength and review cadence)
     - config/registries/admin-rbac-matrix.json (sheet 59, staff roles)
     - sheet 03 (ten access surfaces and their access boundaries)
   Constraint from the source: Nafath is not a public API and is conditional on
   enterprise onboarding; OTP and MFA are the documented interim identity path
   (sheet 23 row 2). Implement the interim path and leave a clean seam for
   Nafath. Do not claim Nafath integration.
   Authentication strengths the source specifies: strong MFA plus PAM for
   PLATFORM_OWNER; MFA for TENANT_ADMIN, PROJECT_MANAGER, EXECUTION_ENGINEER,
   PMO_CONTROLLER, AUDITOR; MFA plus step-up for QUALIFIED_REVIEWER; MFA plus
   dual approval for FINANCE; MFA plus JIT for SUPPORT_L2; secret or mTLS for
   API_CLIENT with 90-day rotation.

D. EXECUTION INSTRUCTIONS
   1. Implement OIDC authentication. Session or token claims must carry: subject,
      tenant_id (server-derived), roles, authentication strength achieved, and
      the time of the last step-up.
   2. Implement authentication strength as a first-class, checkable property:
        - MFA achieved or not;
        - step-up performed within a configured freshness window;
        - JIT elevation with an explicit expiry timestamp;
        - break-glass as a separate, time-boxed, dual-approved grant that
          expires automatically and cannot be renewed silently.
   3. Implement the role matrix from the register as data-driven authorization,
      not as scattered conditionals. One authorization decision point, fed by
      the registry file, so that sheet 04 and the code cannot drift.
   4. Implement the deny list explicitly. A role's absence of permission and a
      role's explicit prohibition are different states, and the prohibition
      must be auditable. Record a denial event naming the role, action and rule.
   5. Implement API_CLIENT credentials with scopes bound to exactly one tenant
      and a 90-day rotation policy, with rotation implemented (not just
      documented) and the old credential revocable.
   6. Map the ten access surfaces of sheet 03 to route groups with their stated
      access boundaries, including that the public surface has no operational
      data and no direct engine connection.
   7. Write a negative authorization test suite that, for every role in
      sheet 04, attempts every action in that role's deny column and asserts
      rejection plus an audit event. This suite is the deliverable that proves
      the phase, so it must be exhaustive against the register, not a sample.
   8. Add a test asserting that an expired JIT grant and an expired break-glass
      grant both stop working without any explicit revocation call.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - OIDC authentication with strength-aware claims
   - step-up, JIT and auto-expiring dual-approved break-glass
   - a single data-driven authorization decision point reading rbac-roles.json
   - API client credentials with scopes, tenant binding and working rotation
   - route grouping for the ten access surfaces
   - tests/security/rbac-negative.* covering every deny cell in sheet 04
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Run the negative authorization suite. Paste real output, and state the
     count of deny cells in the register versus the count of assertions you
     wrote. They must match.
   - Paste the test output for JIT and break-glass expiry.
   - Demonstrate credential rotation: issue, rotate, confirm the old credential
     is rejected.
   - Acceptance criterion: every deny cell in sheet 04 has a passing negative
     test; every elevated grant expires without intervention.

G. COMPLETION CONTRACT
   Definition of Done: authentication with strengths, data-driven authorization,
   exhaustive negative tests passing, expiry proven.
   Evidence to report: deny-cell coverage count, negative suite output, expiry
   test output, rotation demonstration.
   Remaining blockers: Nafath and any enterprise SSO that needs a provider
   agreement — report as blocked on the owner, with the interim path working.
   Next prompt: P01-04.
```

**المخرجات المتوقعة:** مصادقة بدرجات، نقطة قرار تفويض واحدة، مجموعة اختبارات سلبية كاملة.
**التحقق المطلوب:** تطابق عدد خلايا «يحظر» مع عدد التأكيدات؛ انتهاء صلاحية JIT وbreak-glass مُثبت.
**الاعتمادية التالية:** `P01-04`.

---

---

### `P01-04` — محرك السياسة الذي يفشل مُغلقاً

**Phase:** `PHASE-01` · **EN title:** Fail-closed policy engine with complete decision logging

**المتطلبات السابقة:** `P01-03`

**المتطلبات المغطاة:** `REQ-GW-02`, `REQ-TEN-05`, `REQ-GOV-03`

**ماذا سينفذ هذا الأمر؟** يبني محرك سياسة مركزياً يُصنّف ويقرر قبل كل عملية
حساسة، يفشل مُغلقاً عند أي شك، ويسجّل 100% من قراراته.

**لماذا نحتاجه؟** الورقة 70 الصف 3 تحدد «محرك سياسة ما قبل التنفيذ» يصنّف
البيانات والجغرافيا والموافقة والأدوات المسموحة ومخاطر المهمة، و«يفشل مُغلقاً»،
وضابط قبوله: «تسجيل 100% من قرارات السياسة». بناء هذا الآن — قبل البوابة
والوكلاء — يجعل كل المراحل اللاحقة تستهلك نقطة قرار واحدة لا عشرة شروط متناثرة.

**ما المتطلبات السابقة؟** `P01-03`.

**ما النتيجة المتوقعة؟** خدمة سياسة مُصدَرة بإصدار، قابلة للاختبار، مع سجل قرارات
كامل، ووضع افتراضي رافض.

**كيف نتحقق من نجاحه؟** اختبار يُزيل حزمة السياسة فيصبح كل قرار رفضاً لا سماحاً؛
واختبار يؤكد أن عدد القرارات المسجلة يساوي عدد الطلبات.

```text
TASK P01-04 — Fail-closed policy engine with complete decision logging

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-04
   Phase: PHASE-01
   Prerequisites: P01-03 (identity and roles available as policy input)
   Requirements covered: REQ-GW-02, REQ-TEN-05, REQ-GOV-03

B. OBJECTIVE
   Build one central, versioned policy decision service that every sensitive
   operation consults before acting. It classifies the request, decides, fails
   closed on any uncertainty, and logs 100 percent of its decisions.

   Why this is necessary: sheet 70 row 3 specifies a preflight policy engine
   that classifies data, geography, consent, allowed tools and task risk, that
   fails closed, and whose acceptance gate is that 100 percent of policy
   decisions are logged. Building it here — before the gateway and the agents —
   means later phases consume one decision point instead of scattering
   conditionals that drift.

   SCOPE BOUNDARY: the policy service, its input contract, its decision log and
   its tests. Do not implement the gateway, the router or agent execution. Do
   not encode pricing or payment rules here.

C. CONTEXT
   Required inputs:
     - config/registries/rbac-roles.json and admin-rbac-matrix.json
     - config/registries/routing-policies.json (task classes, for the risk
       classification vocabulary only)
     - sheet 70 row 3 (the engine's responsibilities)
     - sheet 68 row 4 (the control path: console -> platform API -> policy and
       approval -> runtime; never browser-to-agent, never browser-to-database)
   The two risk axes come from ADR-005 (sheet 02 row 6): Action Risk R0-R4 is
   authority to act; Professional Consequence P0-P3 is impact of error. They
   are independent inputs, not one score. P3 requires a specialist; R4 requires
   delegated authority.
   Policy-as-code is a source recommendation: sheet 22 row 30 lists Open Policy
   Agent as Recommended with the control "version and test bundles". Using it
   is justified by the source; if you choose otherwise, record an ADR.

D. EXECUTION INSTRUCTIONS
   1. Define the decision request contract. At minimum: actor identity, roles,
      authentication strength, tenant, project, action, resource class, data
      classification, declared task_type, action_risk (R0-R4), professional
      consequence (P0-P3), requested tools, destination geography, consent
      state, and a correlation id.
   2. Define the decision response contract: ALLOW | DENY | ALLOW_WITH_GATE,
      the matched rule id, the policy bundle version, the human gate required
      (if any), and a machine-readable reason code. Never return a bare boolean.
   3. Implement fail-closed semantics, exhaustively:
        - unknown action, unknown resource class or unknown classification ->
          DENY;
        - missing or unparseable policy bundle -> DENY (never ALLOW);
        - policy service unreachable or timed out -> the CALLER denies;
        - a required input field absent -> DENY with a reason code naming it.
      Each of these five cases needs its own test.
   4. Version the policy bundle. Every decision records the bundle version that
      produced it. Bundles are tested artifacts: add a bundle test suite that
      runs in CI, per the control in sheet 22 row 30.
   5. Implement the decision log:
        - one record per decision, written on the ALLOW path as well as the
          DENY path;
        - fields: correlation id, actor, tenant, action, decision, rule id,
          bundle version, timestamp UTC, latency;
        - no secrets, no payload content, no PII beyond identifiers;
        - written to the append-only store that P01-05 hardens.
   6. Encode the two risk axes as independent policy inputs with their source
      semantics: an R4 action requires a recorded delegation; a P3 consequence
      requires a specialist human gate. Do not collapse them into one number.
   7. Add an architectural guard test asserting the control path of sheet 68
      row 4: there is no route by which a browser-originated request reaches an
      agent runtime or the database without passing the platform API and the
      policy service. Implement this as a real test over the route table or
      dependency graph, not as documentation.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the policy decision service with versioned bundles
   - request and response contracts as typed schemas
   - the five fail-closed tests
   - the decision log writer
   - a policy bundle test suite in CI
   - the architectural control-path guard test
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of the five fail-closed tests.
   - Prove log completeness: run N mixed requests, assert exactly N decision
     records exist, and paste the count comparison.
   - Remove the policy bundle and show every decision becomes DENY. Paste it.
   - Confirm no decision record contains a secret or payload content: grep the
     log fixture and paste the result.
   - Acceptance criterion: decisions logged equals decisions made, with no
     exceptions; every uncertainty path denies.

G. COMPLETION CONTRACT
   Definition of Done: fail-closed policy service, 100 percent decision
   logging proven by count, control-path guard test passing.
   Evidence to report: fail-closed test output, the N-requests-to-N-records
   proof, the missing-bundle denial output.
   Remaining blockers: any classification vocabulary that depends on an
   unresolved open decision — name it and default it to DENY, never to ALLOW.
   Next prompt: P01-05.
```

**المخرجات المتوقعة:** خدمة سياسة بإصدارات، اختبارات الفشل المُغلق الخمسة، سجل قرارات كامل.
**التحقق المطلوب:** عدد القرارات المسجلة = عدد القرارات المتخذة؛ إزالة الحزمة تُنتج رفضاً شاملاً.
**الاعتمادية التالية:** `P01-05`.

---

---

### `P01-05` — سجل التدقيق غير القابل للتعديل

**Phase:** `PHASE-01` · **EN title:** Append-only, tamper-evident audit store

**المتطلبات السابقة:** `P01-04`

**المتطلبات المغطاة:** `REQ-SEC-04`, `REQ-DAT-01`, `REQ-TEN-08`

**ماذا سينفذ هذا الأمر؟** يبني مخزن تدقيق إضافي فقط (append-only/WORM) يسجّل
الفاعل والفعل وقيمة ما قبل وما بعد والزمن ومعرف الارتباط، ويُثبت أنه كاشف
للتلاعب.

**لماذا نحتاجه؟** الضابط `CTRL`/`SEC-06` في الورقة 27 الصف 7 بأولوية `CRITICAL`،
ودليله المطلوب: «اختبار تلاعب واسترجاع». والورقة 04 الصف 2 تحظر على مالك المنصة
نفسه «تعطيل audit» — أي أن السجل يجب أن يكون محمياً من أعلى صلاحية في النظام.

**ما المتطلبات السابقة؟** `P01-04`.

**ما النتيجة المتوقعة؟** مخزن تدقيق مُثبت، واستعلام استرجاع بنطاق مستأجر،
واختبار تلاعب يفشل الكشف إن عُطّل.

**كيف نتحقق من نجاحه؟** محاولة تعديل أو حذف سجل تدقيق تُرفض؛ تعديل مباشر في
المخزن يُكتشف بسلسلة تحقق.

```text
TASK P01-05 — Append-only, tamper-evident audit store

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P01-05
   Phase: PHASE-01
   Prerequisites: P01-04 (policy decisions are a primary audit producer)
   Requirements covered: REQ-SEC-04, REQ-DAT-01, REQ-TEN-08

B. OBJECTIVE
   Implement the audit and evidence store as append-only or WORM, recording
   actor, action, before and after values, timestamp and correlation id, and
   prove it is tamper-evident and retrievable.

   Why this is necessary: sheet 27 row 7 marks this control CRITICAL and names
   the required evidence as a tamper and retrieval test. Sheet 04 row 2
   forbids even PLATFORM_OWNER from disabling audit, so the store must be
   protected against the system's highest privilege. Sheet 28 row 20 defines
   AuditEvent as append-only by contract.

   SCOPE BOUNDARY: the audit store, its write path, its retrieval API and its
   integrity verification. Observability dashboards are PHASE-10. Retention and
   legal hold policy execution is PHASE-11; here you implement the retention
   field and the enforcement hook, not the PDPL workflow.

C. CONTEXT
   Required inputs:
     - the policy decision log writer from P01-04
     - the security events from P01-02
     - config/registries/data-entities.json, AuditEvent entry
   Producers that must write audit events, per the source: all services
   (sheet 28 row 20). At this point that means authentication, authorization
   denials, policy decisions, cross-tenant attempts, credential rotation and
   break-glass grants.

D. EXECUTION INSTRUCTIONS
   1. Implement the audit event schema: event_id, tenant_id, actor (subject and
      role), action, resource reference, before value, after value, decision,
      reason code, correlation id, causation id, occurred_at in UTC,
      recorded_at in UTC, and a retention class.
   2. Enforce append-only at the storage layer, not in application code:
        - revoke UPDATE and DELETE from the application role;
        - if the engine supports it, use an immutability or WORM feature;
        - if the store is object-based, enable object lock.
      Document precisely which mechanism you used and what privilege could
      still bypass it — then restrict that privilege and record who holds it.
   3. Implement tamper evidence: chain each record to the previous one with a
      cryptographic digest over the record's canonical form plus the previous
      digest, per tenant stream. Provide a verification routine that walks a
      stream and reports the first broken link.
   4. Redaction on write: secrets, tokens, PAN-like strings and raw payloads
      must never enter the store. Implement a redaction filter on the write
      path and test it with representative strings.
   5. Retrieval: a tenant-scoped, role-gated query API supporting filter by
      actor, action, resource, correlation id and time range, with cursor
      pagination. AUDITOR role is read-only with no bulk export beyond a
      configured limit (sheet 04 row 11 forbids excessive download).
   6. Protect against privileged disablement: adding a configuration flag that
      turns auditing off is prohibited. If a maintenance path must exist, it
      requires dual approval, is itself audited to a separate stream, and
      expires. Prove this with a test.
   7. Write the integrity tests:
        a. an UPDATE attempt on an audit record is rejected;
        b. a DELETE attempt is rejected;
        c. an out-of-band modification directly in the store is detected by the
           verification routine, which names the broken record;
        d. retrieval by correlation id returns the full causal chain for a
           multi-service request;
        e. the redaction filter strips every representative secret pattern;
        f. a cross-tenant audit read is denied (reuse the P01-02 helper).
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - audit event schema and migration
   - storage-level append-only enforcement with the mechanism documented
   - digest-chain tamper evidence plus a verification routine
   - a write-path redaction filter
   - a tenant-scoped, role-gated retrieval API with pagination
   - tests/security/audit-integrity.* covering cases a through f
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all six integrity tests.
   - For case c, show the verification routine naming the exact tampered
     record.
   - State which privilege could still bypass append-only, who holds it, and
     how that is controlled. If the answer is "none", prove it.
   - Acceptance criterion: a tamper is always detected and named; no audit
     write path can be disabled without dual approval and its own audit trail.

G. COMPLETION CONTRACT
   Definition of Done: append-only enforced at storage level, tamper detection
   working and demonstrated, retrieval scoped and paginated, redaction tested.
   Evidence to report: the six test outputs, the tamper-detection output, and
   the privilege analysis.
   Remaining blockers: any WORM or object-lock capability unavailable in the
   local environment — state what production must enable, and what the local
   fallback proves and does not prove.
   Next prompt: P02-01. PHASE-01 exit requires AT-SEC-001 green, the sheet-04
   deny suite green, and audit tamper detection demonstrated.
```

**المخرجات المتوقعة:** مخزن تدقيق إضافي فقط، سلسلة بصمات، API استرجاع، مرشّح حجب.
**التحقق المطلوب:** رفض التعديل والحذف، كشف التلاعب بتسمية السجل، حجب الأسرار.
**الاعتمادية التالية:** `P02-01`.


---

# PHASE-02 — الأدلة والملفات وسلامة المخرجات


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

---

### `P02-01` — بوابة الملفات والحجر الصحي

**Phase:** `PHASE-02` · **EN title:** File gateway with scanning and quarantine

**المتطلبات السابقة:** `P01-05`

**المتطلبات المغطاة:** `REQ-SEC-02`, `REQ-DAT-05`, `REQ-API-01`

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

---

### `P02-02` — إصدارات المخرجات والبصمات والقفل

**Phase:** `PHASE-02` · **EN title:** Artifact versioning, digests and immutability

**المتطلبات السابقة:** `P02-01`

**المتطلبات المغطاة:** `ADR-006`, `REQ-DEL-04`, `REQ-DAT-05`, `REQ-WF-06`

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

---

### `P02-03` — بيان الأدلة وسلسلة المصدر

**Phase:** `PHASE-02` · **EN title:** Evidence manifest and provenance chain

**المتطلبات السابقة:** `P02-02`

**المتطلبات المغطاة:** `REQ-FND-02`, `REQ-API-05`, `REQ-DAT-05`, `REQ-EVL-05`

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


---

# PHASE-03 — محرك مسارات العمل والعقود


## الغرض من المرحلة

`ADR-001` هو القرار الحاكم للمنتج كله: «المنتج هو Workflow Template محدد الإصدار
والمدخلات والمخرجات والمخاطر والتسعير والاختبارات. الوكلاء قدرات تنفذ خطوات داخل
القالب، وليسوا فريقاً حراً يؤلف مساراً جديداً لكل طلب» (الورقة 00 الصف 20،
والورقة 02 الصف 2).

هذا يعني أن محرك مسارات العمل يُبنى **قبل** الوكلاء وقبل بوابة الذكاء، لأنه هو من
يملك السلطة على ما يُنفَّذ ومتى. وهذه المرحلة تبني أيضاً الضمانات التي يستحيل
إضافتها لاحقاً: تثبيت الإصدار، والصمود أمام إعادة تشغيل العامل، وعدم تكرار الأثر
الجانبي.

## شروط الدخول

- اكتمال `PHASE-02`: مخرجات بإصدارات وبصمات، وبيان أدلة.

## شروط الخروج

- نجاح `AT-WF-001` (الفشل والإلغاء والانتهاء كحالات منفصلة بلا مهام معلقة).
- نجاح `AT-WF-002` (تثبيت الإصدار: التشغيل القديم يبقى على `v1.0`).
- إعادة تشغيل العامل لا تُفقد أي مهمة.
- تكرار `Idempotency-Key` لا يُنتج أثراً جانبياً مكرراً.
- صندوق الصادر يوصل مع إزالة تكرار؛ القوالب المسحوبة ومخططات غير الصالحة تُرفض.

## المتطلبات المغطاة في هذه المرحلة

`ADR-001`, `REQ-WF-01`..`REQ-WF-04`, `REQ-WF-07`, `REQ-WF-09`, `REQ-WF-10`,
`REQ-DAT-03`, `REQ-DAT-09`, `REQ-DAT-10`, `REQ-API-01`, `REQ-API-02`,
`REQ-API-04`, `REQ-API-05`

## تحذير مهم

الورقة 22 الصف 20 تقول عن LangGraph: «لا graph حر للإنتاج». واستخدام أي محرك
تنسيق (الورقة 22 الصف 19 توصي بـTemporal) مشروط بضوابطه المذكورة:
«Determinism/versioning/idempotency». أي تنفيذ يسمح للنموذج بتأليف خطوات جديدة
في وقت التشغيل يخالف `ADR-001` مباشرة.

---

## الأوامر التنفيذية

---

### `P03-01` — سجل قوالب مسارات العمل وتثبيت الإصدار

**Phase:** `PHASE-03` · **EN title:** Workflow template registry with immutable versions and routing

**المتطلبات السابقة:** `P02-03`

**المتطلبات المغطاة:** `ADR-001`, `REQ-WF-02`, `REQ-WF-07`, `REQ-WF-10`

**ماذا سينفذ هذا الأمر؟** يبني سجل قوالب غير قابل للتعديل بإصدارات دلالية، وراوتر
يختار قالباً معتمداً بالسياسة، ويرفض القوالب المسحوبة والمخططات غير الصالحة،
ويحوّل غياب التطابق إلى فرز بشري لا إلى مسار مُؤلَّف.

**لماذا نحتاجه؟** هذا هو `ADR-001` بالكود. والورقة 15 الصف 4 (`CTRL-003`) تطلب
دليلاً: «التشغيل يرجع إلى إصدار محدد بالضبط». والورقة 16 الصف 3 (`AT-WF-002`)
تحدد السيناريو: شغّل `v1.0` ثم انشر `v1.1`، فالقديم يبقى على `v1.0`.

**ما المتطلبات السابقة؟** `P02-03`.

**ما النتيجة المتوقعة؟** سجل قوالب مُحمَّل من `config/registries/workflow-templates.json`،
وراوتر بسياسة، ونجاح `AT-WF-002`.

**كيف نتحقق من نجاحه؟** نشر إصدار جديد أثناء تشغيل جارٍ لا يُغيّر إصدار ذلك
التشغيل؛ ومحاولة بدء قالب `retired` تُرفض.

```text
TASK P03-01 — Workflow template registry with immutable versions and routing

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-01
   Phase: PHASE-03 (Workflow runtime and contracts)
   Prerequisites: P02-03
   Requirements covered: ADR-001, REQ-WF-02, REQ-WF-07, REQ-WF-10

B. OBJECTIVE
   Implement the workflow template registry as immutable, semantically
   versioned, policy-gated definitions, plus a router that selects an approved
   template version and never composes a new path.

   Why this is necessary: this is ADR-001 expressed in code — the governing
   product decision of the whole platform (sheet 00 row 20, sheet 02 row 2).
   Sheet 15 row 4 (CTRL-003) requires the evidence "run references exact
   version". Sheet 16 row 3 (AT-WF-002) defines the test: start v1.0, publish
   v1.1, and the already-running instance stays on v1.0.

   SCOPE BOUNDARY: the registry, versioning, publication lifecycle and routing
   decision. Do not implement step execution, durability or the state machine —
   that is P03-02. Do not implement agents or model calls.

C. CONTEXT
   Required inputs:
     - config/registries/workflow-templates.json (sheet 07: 8 templates with
       workflow_id, version, segment, scope, capabilities, R, P, review
       requirement, pricing id, test suite id, evidence state)
     - the policy service from P01-04
   The eight templates and their source versions: WF-VILLA-REVIEW 1.0.0
   (PILOT TARGET), WF-BIM-COORD 0.9.0, WF-QTO 0.9.0, WF-SITE-REPORT 0.9.0,
   WF-MEP-REVIEW 0.8.0, WF-INFRA-REVIEW 0.8.0 (all DEFINED), WF-PAYMENT 1.0.0
   and WF-REVIEW-DELIVERY 1.0.0 (DESIGNED).
   Source constraint (sheet 05 row 3, CTL-02): the router selects by brief,
   policy and registry; no match yields manual triage; it halts on no template,
   a retired version, or an invalid schema.
   Source constraint (sheet 02 row 2) acceptance control: a template is valid
   only with owner, schema, tests, pricing and approval.

D. EXECUTION INSTRUCTIONS
   1. Model WorkflowTemplate and WorkflowTemplateVersion. Per
      config/registries/data-entities.json the keys are id, version and status,
      the purpose is an immutable versioned template, and the control is
      semantic versioning.
   2. Enforce the five-part validity gate from ADR-001's acceptance control. A
      version cannot reach status ACTIVE unless it has: a named owner, a valid
      input and output schema, a referenced test suite id, a referenced pricing
      id, and a recorded approval actor and timestamp. Reject publication
      otherwise, naming the missing part.
   3. Implement the version lifecycle: DRAFT -> ACTIVE -> DEPRECATED ->
      RETIRED. An ACTIVE or later version is immutable — editing it is
      impossible; a change produces a new semantic version. Enforce immutability
      with a database constraint or trigger, not application logic alone.
   4. Implement version pinning. Starting a run resolves the template version
      once, stores the exact resolved version on the run record, and every
      later step reads the pinned version. There is no code path that resolves
      "latest" after a run has started. Add a test that would fail if such a
      path existed.
   5. Implement the router:
        - input: a validated brief plus tenant policy;
        - output: either an exact template and version, or MANUAL_TRIAGE with a
          machine-readable reason;
        - it consults the policy service from P01-04 and records the policy
          bundle version in its decision;
        - it refuses to start a RETIRED version, refuses a brief failing the
          template's input schema, and refuses when no template matches;
        - it never synthesizes a capability list, a step order or a new
          template. Assert that the set of capabilities for a run is read from
          the pinned version and is not computed.
   6. Record a routing decision record for every routing attempt, including the
      rejected ones, with the reason. Sheet 05 row 3 tracks routing accuracy and
      misroutes as KPIs, which requires this record to exist.
   7. Load the eight templates from the registry file at startup, validating
      them against a schema. A registry file that fails validation prevents
      startup rather than degrading silently.
   8. Tests:
        a. AT-WF-002: start a run on v1.0.0; publish v1.1.0; assert the running
           instance still reports v1.0.0 and executes v1.0.0's capability list;
           assert a new run gets v1.1.0 according to the rollout policy;
        b. attempt to edit an ACTIVE version -> rejected at the database level;
        c. attempt to publish a version missing a test suite id -> rejected,
           naming the missing part; repeat for owner, schema, pricing and
           approval;
        d. attempt to start a RETIRED version -> rejected;
        e. submit a brief that matches no template -> MANUAL_TRIAGE with a
           reason, and no run created;
        f. submit a brief failing the input schema -> rejected with the
           validation detail;
        g. corrupt workflow-templates.json -> startup fails loudly.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - WorkflowTemplate and WorkflowTemplateVersion models and migrations
   - the five-part publication gate
   - the DRAFT/ACTIVE/DEPRECATED/RETIRED lifecycle with enforced immutability
   - version pinning on run creation
   - the policy-consulting router with MANUAL_TRIAGE output
   - routing decision records
   - startup-time registry validation
   - tests/workflow/at-wf-002.* plus cases b through g
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-WF-002 output showing the running instance pinned to v1.0.0 after
     v1.1.0 is published.
   - Paste the database-level rejection for case b.
   - Paste all five publication-gate rejections for case c.
   - Acceptance criterion: no code path resolves a template version after a run
     has started, and every routing attempt leaves a decision record.

G. COMPLETION CONTRACT
   Definition of Done: immutable versioned templates, enforced publication
   gate, proven version pinning, policy-gated routing with manual triage.
   Evidence to report: AT-WF-002 output, the seven test results, and the count
   of templates loaded versus the eight in the source.
   Remaining blockers: templates whose pricing id or test suite id does not yet
   exist — the source marks several DEFINED rather than built. Record them as
   publishable only in PHASE-15, and keep WF-VILLA-REVIEW as the PILOT TARGET.
   Next prompt: P03-02.
```

**المخرجات المتوقعة:** سجل قوالب غير قابل للتعديل، بوابة نشر خمسية، راوتر بسياسة.
**التحقق المطلوب:** `AT-WF-002` ناجح، ولا مسار كود يحلّ «الأحدث» بعد بدء التشغيل.
**الاعتمادية التالية:** `P03-02`.

---

---

### `P03-02` — التنفيذ الصامد وآلة الحالات

**Phase:** `PHASE-03` · **EN title:** Durable execution and the workflow state machine

**المتطلبات السابقة:** `P03-01`

**المتطلبات المغطاة:** `REQ-WF-01`, `REQ-WF-03`, `REQ-WF-09`, `REQ-DAT-03`

**ماذا سينفذ هذا الأمر؟** يبني محرك تنفيذ صامد وآلة الحالات الكاملة للورقة 09:
سبع عشرة حالة للمسار مع أحداثها وانتقالاتها وفاعليها وضوابطها.

**لماذا نحتاجه؟** الورقة 15 الصف 3 (`CTRL-002`) تجعل حالات الفشل والإلغاء
والانتهاء ضابطاً بأولوية `HIGH`، و`AT-WF-001` يطلب أن تكون «منفصلة ولا مهام
معلقة». الخلط بين `FAILED` و`CANCELLED` و`EXPIRED` يخفي الأعطال ويجعل مقياس
`Workflow failure rate` بلا معنى.

**ما المتطلبات السابقة؟** `P03-01`.

**ما النتيجة المتوقعة؟** محرك تنفيذ صامد، وآلة حالات مُنفَّذة كبيانات، ونجاح
`AT-WF-001`.

**كيف نتحقق من نجاحه؟** قتل العامل أثناء تشغيل لا يفقد مهمة؛ والانتقالات غير
المسموحة تُرفض؛ ولا تبقى مهمة معلقة بعد حالة نهائية.

```text
TASK P03-02 — Durable execution and the workflow state machine

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-02
   Phase: PHASE-03
   Prerequisites: P03-01 (pinned template versions)
   Requirements covered: REQ-WF-01, REQ-WF-03, REQ-WF-09, REQ-DAT-03

B. OBJECTIVE
   Implement durable workflow execution that survives worker restart with no
   lost work, and the full state machine the source specifies, with every
   terminal and exceptional state distinct.

   Why this is necessary: sheet 15 row 3 (CTRL-002) makes failure, cancel and
   expire states a HIGH control whose evidence is state tests plus event
   history. AT-WF-001 (sheet 16 row 2) requires that FAILED, CANCELLED and
   EXPIRED be separate with no dangling tasks. Collapsing them hides faults and
   makes the workflow failure rate KPI (sheet 30 row 7) meaningless. Sheet 37
   row 7 requires that restarting a worker mid-job loses nothing.

   SCOPE BOUNDARY: orchestration, state machine, tasks, timers and human
   waits. Idempotency and the outbox are P03-03. Agent and model execution are
   PHASE-04 and PHASE-05 — here a step is a typed, pluggable unit with a test
   double.

C. CONTEXT
   Required inputs:
     - sheet 09 rows 2-16 for the Workflow entity: states DRAFT, QUOTED,
       AWAITING_PAYMENT, PAYMENT_VERIFIED, QUEUED, RUNNING,
       AWAITING_INFORMATION, AWAITING_REVIEW, AWAITING_SECOND_REVIEW,
       AWAITING_CLIENT_DECISION, DELIVERED, ARCHIVED, plus the exceptional and
       terminal states FAILED, CANCELLED, EXPIRED, SUSPENDED and
       PARTIALLY_COMPLETED; each row names the event, the target state, the
       actor and the control
     - config/registries/data-constraints.json, workflow_runs: UNIQUE
       (tenant_id, idempotency_key), indexes project_id, status, created_at,
       invariant "state machine / retries"
     - sheet 05 row 4 (CTL-03): tasks, deadlines, dependencies, waits and
       retries under a state machine; halt when idempotency cannot be
       guaranteed or the retry budget is exceeded
   Tooling: sheet 22 row 19 recommends Temporal for durable execution, retries,
   timers, history and human waits, with the control
   "determinism/versioning/idempotency". Sheet 22 row 20 permits LangGraph for
   in-step human-in-the-loop barriers but states "no free graph for
   production". Choosing Temporal is source-supported; choosing otherwise
   requires an ADR and must still deliver durability, timers and replay.

D. EXECUTION INSTRUCTIONS
   1. Implement the state machine as data, derived from sheet 09, not as
      scattered conditionals. One transition table of
      (entity, from_state, event) -> (to_state, required_actor, guard). Load it
      from a registry file so the source and the code cannot drift.
   2. Enforce that an undeclared transition is impossible. Attempting one is an
      error with a reason code, never a silent no-op and never a fallthrough to
      a default state.
   3. Keep the exceptional states genuinely distinct, each with its own cause
      field:
        - FAILED carries an error class and the retry budget state;
        - CANCELLED carries the authorizing actor and a compensation record;
        - EXPIRED carries which timer fired and the reopen policy;
        - SUSPENDED carries the security, compliance, payment or COI reason and
          requires manual clearance to leave;
        - PARTIALLY_COMPLETED carries the explicit scope that succeeded and the
          scope that did not, per sheet 09 row 16.
   4. Implement durable orchestration:
        - run state and history are persisted, not held in memory;
        - a worker crash or restart resumes from persisted state;
        - every step is at-least-once with a declared side-effect class
          (SAFE_RETRYABLE, UNSAFE_RETRYABLE, IRREVERSIBLE) per sheet 36 row 10;
        - an IRREVERSIBLE step requires a manual gate and is never auto-retried.
   5. Implement tasks per config/registries/data-entities.json: task_id,
      run_id, assignee; a task is a human or machine step with a retry policy
      and a lease. A lease expiring returns the task to the queue rather than
      stranding it.
   6. Implement timers and human waits: quote expiry, payment expiry,
      assignment offer expiry and RFI waits, each producing the correct EXPIRED
      transition from sheet 09 row 14.
   7. Implement structured RFI: entering AWAITING_INFORMATION records what is
      missing, from whom, and the deadline — per sheet 09 row 7, the control is
      "structured RFI", not a free-text note.
   8. Guarantee no dangling tasks: reaching any terminal state cancels or closes
      every outstanding task and timer for that run. Add an invariant check that
      asserts zero open tasks and zero armed timers for a terminal run, and run
      it as part of the test suite.
   9. Implement retry budgets. Exceeding the budget transitions to FAILED with
      the budget state recorded; it never loops. Sheet 05 row 4 names exceeding
      retry as a stop condition.
  10. Tests — AT-WF-001 plus the state machine suite:
        a. force a parser step to fail -> FAILED, distinct, with error class,
           no open tasks, no armed timers;
        b. cancel a running run -> CANCELLED with authorizing actor and a
           compensation record, no open tasks;
        c. let an assignment offer expire -> EXPIRED naming the timer, no open
           tasks;
        d. assert the three outcomes above are distinguishable in both the run
           record and the event history;
        e. kill the worker process mid-run, restart it, assert the run resumes
           and completes with no duplicated step and no lost step;
        f. attempt an undeclared transition -> rejected with a reason code;
        g. suspend a run -> SUSPENDED, and assert it cannot leave that state
           without a recorded manual clearance;
        h. exceed the retry budget -> FAILED with budget state, no infinite
           loop;
        i. assert the terminal-state invariant (zero open tasks, zero armed
           timers) for every terminal state.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the data-driven transition table plus its registry file
   - durable run and task persistence with resume-after-restart
   - distinct exceptional states with their cause fields
   - tasks with leases, timers, human waits and structured RFI
   - side-effect classes with IRREVERSIBLE gating
   - retry budgets
   - the terminal-state invariant check
   - tests/workflow/at-wf-001.* plus cases e through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-WF-001 output showing FAILED, CANCELLED and EXPIRED as distinct
     outcomes with no dangling tasks.
   - Paste the worker-kill test output showing the run resuming and completing,
     with step execution counts proving no duplication and no loss.
   - Paste the undeclared-transition rejection.
   - State the count of transitions in sheet 09 versus the count in your
     transition table. They must match.
   - Acceptance criterion: AT-WF-001 green; restart loses nothing; no terminal
     run holds an open task or an armed timer.

G. COMPLETION CONTRACT
   Definition of Done: durable execution proven by worker kill, full state
   machine enforced from data, exceptional states distinct, no dangling work.
   Evidence to report: AT-WF-001 output, the restart test output, the
   transition count comparison, the invariant check output.
   Remaining blockers: any state in sheet 09 whose triggering event belongs to
   a later phase (payment, review, delivery) — implement the transition and
   drive it with a test double now, and name the phase that wires the real
   producer.
   Next prompt: P03-03.
```

**المخرجات المتوقعة:** جدول انتقالات مُحمَّل من بيانات، تنفيذ صامد، حالات استثنائية مميّزة.
**التحقق المطلوب:** `AT-WF-001` ناجح؛ قتل العامل لا يفقد ولا يكرر؛ ثابت الحالة النهائية مُتحقَّق.
**الاعتمادية التالية:** `P03-03`.

---

---

### `P03-03` — عدم التكرار وصندوق الصادر وعقود الأحداث

**Phase:** `PHASE-03` · **EN title:** Idempotency, transactional outbox and event contracts

**المتطلبات السابقة:** `P03-02`

**المتطلبات المغطاة:** `REQ-WF-04`, `REQ-DAT-09`, `REQ-DAT-10`, `REQ-API-04`, `REQ-API-05`

**ماذا سينفذ هذا الأمر؟** يبني مفاتيح عدم التكرار، وصندوق صادر معاملاتي، وطابور
رسائل ميتة، ومغلف الأحداث الموحد للورقة 34 بأحداثه الثمانية.

**لماذا نحتاجه؟** الورقة 38 الصف 9 (`G-04 Side-effect safety`) ضابط حاجز للإصدار:
«لا شحن مكرر ولا إرسال مكرر»، ودليله «DB constraint + replay test». والورقة 37
الصف 8 تجعلها متطلباً مُتتبَّعاً. وبدون صندوق صادر معاملاتي لا يمكن تحقيق
«at-least-once» المذكورة في كل صفوف الورقة 34.

**ما المتطلبات السابقة؟** `P03-02`.

**ما النتيجة المتوقعة؟** عدم تكرار مفروض بقيد قاعدة بيانات، وصندوق صادر مع إعادة
محاولة وDLQ، وأحداث مطابقة للمغلف.

**كيف نتحقق من نجاحه؟** إعادة إرسال نفس المفتاح لا تُنتج أثراً ثانياً؛ وإعادة
تشغيل الأحداث خارج الترتيب ومكررة لا تُنتج حالة خاطئة.

```text
TASK P03-03 — Idempotency, transactional outbox and event contracts

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-03
   Phase: PHASE-03
   Prerequisites: P03-02 (durable runs and tasks)
   Requirements covered: REQ-WF-04, REQ-DAT-09, REQ-DAT-10, REQ-API-04,
                         REQ-API-05

B. OBJECTIVE
   Make side effects exactly-once observable: database-enforced idempotency
   keys, a transactional outbox with retry and dead-letter handling, and the
   source's common event envelope with its eight versioned domain events.

   Why this is necessary: sheet 38 row 9 (G-04) is a release blocker whose pass
   criterion is "no duplicate charges or dispatch" and whose required evidence
   is "DB constraint plus replay test". Sheet 37 row 8 tracks it as a
   requirement. Every event row in sheet 34 specifies at-least-once delivery,
   which is only honest if an outbox and consumer-side dedupe exist.

   SCOPE BOUNDARY: idempotency, the outbox, delivery semantics and event
   schemas. Payment-specific webhook verification is PHASE-08 and builds on
   this. Do not implement business handlers beyond what the tests need.

C. CONTEXT
   Required inputs:
     - config/registries/data-constraints.json: idempotency_keys with
       tenant_id, key, request_hash, response_ref; UNIQUE (tenant_id, key);
       index expires_at; invariant "conflict on hash mismatch"; retention
       "TTL by operation". outbox_events with event_id, tenant_id,
       aggregate_id, payload, status; UNIQUE event_id; index status,
       next_attempt_at; invariant "transactional outbox"
     - sheet 34 row 3: the common envelope — eventId UUID, eventType,
       schemaVersion, tenantId, correlationId, causationId, occurredAt UTC,
       payload
     - sheet 34 rows 6-13: EV-01 ProjectCreated project.created.v1; EV-02
       EvidenceSubmitted evidence.submitted.v1; EV-03 WorkflowRequested
       workflow.requested.v1; EV-04 AgentStepCompleted
       agent.step.completed.v1; EV-05 ReviewDecisionRecorded review.decision.v1;
       EV-06 EstimateIssued estimate.issued.v1; EV-07 DeliverableReleased
       deliverable.released.v1; EV-08 UsageRecorded usage.recorded.v1 — each
       with aggregate, required payload fields, producer, consumer, ordering
       key, delivery and a validation rule
     - the minimal outbox stub from P02-03, which this prompt generalizes

D. EXECUTION INSTRUCTIONS
   1. Implement idempotency as a request-level mechanism:
        - operations that sheet 26 and sheet 33 mark as requiring an
          Idempotency-Key reject the request with 400 when it is absent;
        - the first request records (tenant_id, key, request_hash,
          response_ref) in the same transaction as its effect;
        - a replay with the same key and the same request hash returns the
          stored response, and performs no new effect;
        - a replay with the same key but a different request hash returns 409
          and performs no effect — this is the "conflict on hash mismatch"
          invariant;
        - keys expire by a per-operation TTL, and expiry is a documented
          behaviour change, not a silent window.
   2. Implement the transactional outbox:
        - the domain change and the outbox row are written in one transaction,
          so an event cannot exist without its effect and vice versa;
        - a separate dispatcher reads PENDING rows ordered by
          next_attempt_at, publishes, and marks them SENT;
        - failures use bounded exponential backoff with jitter and a maximum
          attempt count, then move to the dead-letter queue with the full
          failure history;
        - the dispatcher is safe to run in multiple instances: use row-level
          locking or equivalent so one event is dispatched once.
   3. Implement the envelope exactly as sheet 34 row 3 specifies, as a schema
      file that every producer validates against before the outbox write. A
      non-conforming event fails at write time, not at consume time.
   4. Implement the eight events of sheet 34 as versioned schemas with their
      required payload fields and their declared ordering keys. Ordering is
      guaranteed per ordering key, not globally — implement and document it that
      way rather than implying total ordering you cannot provide.
   5. Implement consumer-side dedupe by eventId, because delivery is
      at-least-once. Provide one shared, tested dedupe helper so every consumer
      is protected identically.
   6. Implement the dead-letter queue with: a reason, the attempt history, the
      original envelope, a tenant scope, and an operator replay path that is
      itself idempotent and audited.
   7. Tests — the replay suite:
        a. repeat a create request with the same key and body -> one entity,
           identical response, no second event;
        b. repeat with the same key and a changed body -> 409, no effect;
        c. omit a required Idempotency-Key -> 400;
        d. crash the process between the domain write and the dispatch ->
           restart and assert the event is still delivered exactly once;
        e. deliver the same event twice to a consumer -> the effect applies
           once;
        f. deliver two events for one ordering key out of order -> assert the
           consumer reaches the correct final state, and that an older event
           cannot overwrite a newer state;
        g. exhaust retries -> the event lands in the DLQ with its history, and
           no partial effect remains;
        h. replay from the DLQ -> idempotent, audited, no duplicate effect;
        i. emit an event missing a required envelope field -> rejected at write
           time;
        j. run two dispatcher instances concurrently -> assert each event is
           published exactly once.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - idempotency_keys table, middleware and 409-on-hash-mismatch semantics
   - the transactional outbox with a concurrency-safe dispatcher
   - the envelope schema file plus the eight event schemas
   - the shared consumer dedupe helper
   - the DLQ with an idempotent, audited replay path
   - tests/events/replay-suite.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the replay suite output for all ten cases.
   - For case a, show the database constraint doing the work: paste the unique
     violation that your handler converts into the stored response.
   - For case d, show the crash point and the post-restart delivery count.
   - For case j, paste the per-event publish counts from the concurrent run.
   - Acceptance criterion: no duplicate effect in any of the ten cases, and the
     guarantee rests on a database constraint rather than on application timing.

G. COMPLETION CONTRACT
   Definition of Done: idempotency enforced by constraint, outbox delivering
   exactly-once-observably, all eight event schemas conforming to the envelope,
   DLQ working with audited replay.
   Evidence to report: the ten test outputs, the constraint violation proof,
   the concurrent dispatcher counts.
   Remaining blockers: events whose producer belongs to a later phase (EV-04
   from the gateway, EV-05 from review, EV-06 from costing, EV-07 from
   delivery, EV-08 from usage) — define the schema and test it with a producer
   double now, and name the phase that wires the real producer.
   Next prompt: P03-04.
```

**المخرجات المتوقعة:** مفاتيح عدم تكرار، صندوق صادر، مغلف وثمانية أحداث، DLQ.
**التحقق المطلوب:** عشر حالات إعادة تشغيل بلا أثر مكرر، والضمان من قيد قاعدة بيانات.
**الاعتمادية التالية:** `P03-04`.

---

---

### `P03-04` — سطح الـAPI للمنتج وعقوده

**Phase:** `PHASE-03` · **EN title:** Product API surface and contract tests

**المتطلبات السابقة:** `P03-03`

**المتطلبات المغطاة:** `REQ-API-01`, `REQ-API-02`, `REQ-API-03`, `REQ-WF-01`

**ماذا سينفذ هذا الأمر؟** ينفّذ سطح الـAPI للمنتج: تسع عشرة عملية في الورقة 26،
وعشرة عقود مُسمّاة في الورقة 33، مع اختبارات عقود حقيقية.

**لماذا نحتاجه؟** الورقة 38 الصف 6 (`G-01 API security`) حاجز إصدار بمعيار نجاح
«صفر تسريب بين المستأجرين»، والورقة 40 الصف 8 تقول صراحة إن عقود الـAPI
«موثقة» لكن حالتها `UNVERIFIED` وتحتاج «runtime contract tests». هذا الأمر يحوّل
الوثيقة إلى عقد مُختبَر.

**ما المتطلبات السابقة؟** `P03-03`.

**ما النتيجة المتوقعة؟** مواصفة OpenAPI مُولَّدة أو مُؤلَّفة، ونقاط نهاية مُنفَّذة،
واختبارات عقود تتحقق من رموز الحالة والنطاقات والأحداث.

**كيف نتحقق من نجاحه؟** لكل عملية اختبار يتحقق من: النطاق المطلوب، رموز الحالة
المذكورة، الحدث المُصدَر، وسلوك عدم التكرار.

```text
TASK P03-04 — Product API surface and contract tests

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-04
   Phase: PHASE-03
   Prerequisites: P03-03 (idempotency and events)
   Requirements covered: REQ-API-01, REQ-API-02, REQ-API-03, REQ-WF-01

B. OBJECTIVE
   Implement the product API surface the source specifies and prove it with
   runtime contract tests covering scope, status codes, emitted events and
   idempotency behaviour.

   Why this is necessary: sheet 38 row 6 (G-01) is a release blocker whose pass
   criterion is zero cross-tenant leaks, with required evidence of a CI report
   and a penetration test. Sheet 40 row 8 states plainly that API contracts are
   "Documented" but their verdict is UNVERIFIED and runtime contract tests are
   required. This prompt converts documentation into a tested contract.

   SCOPE BOUNDARY: the operations listed below, their authorization, their
   status codes, their events and their idempotency. Business logic that belongs
   to a later phase is implemented as a validated, authorized endpoint whose
   handler delegates to a clearly marked not-yet-implemented boundary that
   returns 501 — never a fake success.

C. CONTEXT
   Required inputs:
     - sheet 26 rows 2-20, nineteen operations with purpose, scope,
       idempotency or concurrency control, event and response codes:
       POST /v1/projects (projects:write, Idempotency-Key, project.created,
       201/400/403/409); POST /v1/requests (requests:write, request.created,
       201/422); POST /v1/uploads/init (files:write,
       file.uploaded|quarantined, 201/413/415); POST /v1/quotes (quotes:write,
       quote.created, 201/422); POST /v1/quotes/{id}/accept (quotes:accept,
       version/etag, quote.accepted, 200/409/410); POST
       /v1/payments/sessions (payments:write, Idempotency-Key,
       payment.initiated, 201/422); POST /v1/webhooks/payments/{provider}
       (provider signature, payment.*, 200/400/401); POST /v1/workflow-runs
       (runs:write, Idempotency-Key, workflow.queued, 202/409/422); GET
       /v1/workflow-runs/{id} (runs:read, ETag, 200/403/404); POST
       /v1/workflow-runs/{id}/cancel (runs:cancel, workflow.cancelled,
       202/409); POST /v1/workflow-runs/{id}/retry (runs:retry,
       task.retry_scheduled, 202/409); POST /v1/workflow-runs/{id}/resume
       (runs:resume, workflow.resumed, 202/409); GET /v1/findings
       (findings:read, cursor, 200); POST /v1/reviews/{id}/decisions
       (reviews:decide, review hash/etag, review.decision_recorded,
       200/409/422); POST /v1/reviews/{id}/return (reviews:decide,
       review.returned, 202); POST /v1/deliveries/{id}/lock (deliveries:lock,
       delivery.locked, 200/409); POST /v1/deliveries/{id}/sign
       (deliveries:sign, delivery.signed, 202/409); POST
       /v1/deliveries/{id}/release (deliveries:release, delivery.released,
       202/409); GET /v1/verify/{token} (public token, rate limit,
       verification.viewed, 200/404/410)
     - sheet 33 rows 6-15, the ten named contracts API-01..API-10 with request
       and response schema names, scopes, retry semantics, status codes, events
       and security invariants
   Cross-cutting invariant from sheet 33 row 7: never reveal cross-tenant
   existence. Reuse the uniform authorization helper from P01-02.

D. EXECUTION INSTRUCTIONS
   1. Author an OpenAPI document covering every operation above, with named
      request and response schemas matching sheet 33's names
      (CreateProjectRequest, ProjectResponse, EvidenceManifestRequest,
      EvidenceReceipt, StartWorkflowRequest, WorkflowRun, ReviewDecisionRequest,
      ReviewDecision, EstimateRequest, EstimateResponse, DeliverableManifest,
      UsageQuery, UsagePage, WebhookSubscriptionRequest, Subscription).
   2. Implement request validation from the schema, returning 422 with a
      machine-readable field-level detail. Validation happens before
      authorization side effects and before any state change.
   3. Enforce scopes exactly as listed. A token lacking the scope gets 403; a
      token for another tenant gets the uniform not-found/forbidden response
      from P01-02.
   4. Implement concurrency control where the source specifies it: ETag on GET
      /v1/workflow-runs/{id}; version or etag on quote accept; review hash or
      etag on review decisions; artifact version on delivery lock. A stale
      precondition returns 409; a gone resource returns 410 where the source
      lists it.
   5. Implement cursor pagination on GET /v1/findings and GET /v1/usage, with
      an opaque, tamper-resistant cursor that encodes the tenant scope so a
      cursor cannot be replayed across tenants.
   6. Rate-limit GET /v1/verify/{token} per the source's control, and keep the
      verification response minimal: digest and status only. It is a public
      surface, so it must not leak project, client or reviewer identity.
   7. Emit the specified event for each operation through the outbox from
      P03-03, never directly.
   8. For operations whose domain logic belongs to a later phase, return 501
      from a single clearly named boundary function with the owning phase in
      the response detail. Record the list. A stubbed endpoint must never return
      200 with invented data — that is the fabrication this project's
      governance model exists to prevent.
   9. Write the contract test suite. For every operation assert: the success
      path and code; every documented error code is reachable by a real
      condition; missing scope gives 403; cross-tenant gives the uniform
      response with no leakage; the documented event is emitted exactly once;
      idempotency behaves per P03-03 where a key is required; the response
      validates against the OpenAPI schema.
  10. Add a contract-drift test asserting every route in the application
      appears in the OpenAPI document and vice versa, so the document cannot
      rot.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the OpenAPI document with sheet 33's schema names
   - the nineteen implemented operations with scopes, codes and events
   - ETag and precondition handling, cursor pagination, verify rate limiting
   - the single 501 boundary with its documented inventory
   - tests/contract/*.* covering every operation
   - the contract-drift test
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the contract suite output with the per-operation pass list.
   - State the operation count: nineteen from sheet 26 plus the ten named
     contracts from sheet 33, and how your implementation maps to both (several
     overlap — show the mapping explicitly rather than double-counting).
   - Paste a cross-tenant attempt for three different operations showing
     identical response shapes.
   - List every endpoint currently returning 501 with its owning phase.
   - Acceptance criterion: every documented status code is reachable by a real
     test, no endpoint returns fabricated success data, and the drift test
     passes.

G. COMPLETION CONTRACT
   Definition of Done: the API surface implemented and contract-tested, drift
   test green, stubs honestly returning 501.
   Evidence to report: contract suite output, the sheet 26 to sheet 33 mapping
   table, the cross-tenant uniformity proof, the 501 inventory.
   Remaining blockers: the 501 list is the expected blocker set. Each entry
   must name the phase that completes it.
   Next prompt: P03-05.
```

**المخرجات المتوقعة:** مواصفة OpenAPI، تسع عشرة عملية، اختبارات عقود، اختبار انحراف.
**التحقق المطلوب:** كل رمز حالة موثق قابل للوصول باختبار حقيقي؛ لا نقطة نهاية ترجع نجاحاً مُلفَّقاً.
**الاعتمادية التالية:** `P03-05`.

---

---

### `P03-05` — خدمة SLA والمؤقتات والتصعيد

**Phase:** `PHASE-03` · **EN title:** SLA service, timers and escalation

**المتطلبات السابقة:** `P03-04`

**المتطلبات المغطاة:** `REQ-WF-09`, `REQ-WF-01`, `REQ-OBS-05`

**ماذا سينفذ هذا الأمر؟** يبني خدمة SLA: مواعيد لكل خطوة، تذكيرات، تصعيد، وتسجيل
زمن دقيق لقياس «Time to signed delivery».

**لماذا نحتاجه؟** الورقة 05 الصف 4 تحدد مخرجات `CTL-03` بأنها
«tasks/timers/escalations»، ومؤشراتها «SLA؛ stuck runs؛ recovery». والورقة 17
الصف 9 تعرّف مقياساً زمنياً محدداً: من `payment verified` إلى `release`. بدون
مؤقتات وأحداث زمنية موثوقة لا يمكن قياس هذا ولا اكتشاف التشغيل المتوقف.

**ما المتطلبات السابقة؟** `P03-04`.

**ما النتيجة المتوقعة؟** مؤقتات صامدة، تصعيد مُسجَّل، وكشف للتشغيل المتوقف.

**كيف نتحقق من نجاحه؟** تشغيل بلا نبض يُكتشف ويُصعَّد؛ والمقياس الزمني يُحسب من
أحداث حقيقية لا من حقول مُحدَّثة يدوياً.

```text
TASK P03-05 — SLA service, timers and escalation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P03-05
   Phase: PHASE-03
   Prerequisites: P03-04
   Requirements covered: REQ-WF-09, REQ-WF-01, REQ-OBS-05

B. OBJECTIVE
   Implement durable SLA timers, reminders, escalation and stuck-run detection,
   and derive the source's time metrics from real event history rather than from
   hand-maintained fields.

   Why this is necessary: sheet 05 row 4 defines CTL-03's outputs as tasks,
   timers and escalations with KPIs for SLA, stuck runs and recovery. Sheet 17
   row 9 defines "time to signed delivery" precisely as payment verified to
   release. Sheet 61 row 3 defines the stuck-workflow support scenario with
   detection by missing heartbeat. None of these are measurable without durable
   timers and a trustworthy event history.

   SCOPE BOUNDARY: timers, deadlines, reminders, escalation routing and
   stuck-run detection, plus the metric derivation query. Dashboards and alert
   delivery are PHASE-10. Do not build notification channels beyond an
   abstracted dispatch interface with a test double.

C. CONTEXT
   Required inputs:
     - the durable runtime from P03-02 and the outbox from P03-03
     - sheet 09 row 14: TIME_BOUND entities expire on timer.expired with a
       reopen policy — quote, payment and assignment expiry
     - sheet 13 row 10: SLA handling is reminder, then expiry, then
       reassignment, and must never bypass a hard filter
     - sheet 17 rows 8-9: workflow failure segmented by step, tool and tenant
       (daily, SRE, SLO); time to signed delivery segmented by service and
       complexity
     - sheet 61 row 3: workflow stuck, trigger "no heartbeat", first response
       "inspect task and lease", safe action "pause or requeue idempotently"

D. EXECUTION INSTRUCTIONS
   1. Implement deadlines as first-class durable records: subject reference,
      deadline in UTC, purpose, reminder schedule, escalation target and
      current state. They survive restart because they live in the datastore,
      not in an in-process scheduler.
   2. Implement the reminder-then-expiry ladder of sheet 13 row 10: configurable
      reminders before the deadline, then the EXPIRED transition, then the
      reassignment or reopen action the source specifies for that subject.
      Expiry must never relax a hard filter — assert that in a test.
   3. Implement escalation routing: on breach, route to the role the source
      names for that subject (for example Review Ops for an assignment offer,
      Finance for a payment exception, PM for a scope change), record the
      escalation, and emit an event. Escalation is recorded even when nobody
      acts, so the record cannot be lost.
   4. Implement heartbeat and lease monitoring: a running task renews a lease;
      a missing heartbeat beyond a threshold marks the run STUCK_SUSPECTED,
      records the task and lease state for the operator per sheet 61 row 3, and
      offers the idempotent pause-or-requeue action. Detection does not itself
      mutate the run beyond the suspicion marker.
   5. Derive metrics from event history, not from mutable columns:
        - time to signed delivery as the interval between the
          payment-verified event and the delivery-released event for a run;
        - workflow failure rate segmented by step, tool and tenant;
        - stuck-run count and recovery time.
      Implement them as queries over the event store so a value can always be
      recomputed and audited. Do not maintain a denormalized metric column that
      can silently diverge.
   6. Make the metric outputs explicitly unthresholded. Sheet 30 row 14 forbids
      populating current values from anything but documented operational
      sources, and sheet 30 rows 3-9 mark these targets TBD. Your API returns
      the measured value and the literal state PENDING for the target, never a
      placeholder target that would make a dashboard look green.
   7. Tests:
        a. a deadline fires after restart of the process -> timer durability
           proven;
        b. the reminder ladder fires in order, then expiry, then the configured
           reopen or reassignment action;
        c. an expiry cannot bypass a hard filter -> reassignment still applies
           every filter;
        d. a breach produces an escalation record and event even with no
           handler subscribed;
        e. a task stops heartbeating -> STUCK_SUSPECTED with task and lease
           state captured; the requeue action is idempotent when applied twice;
        f. time to signed delivery computed from a synthetic event history
           matches a hand-calculated expected value;
        g. a metric with a TBD target returns PENDING, never a number.
   8. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - durable deadline and reminder records with escalation routing
   - heartbeat and lease monitoring with stuck-run detection
   - event-derived metric queries for the source's time and failure metrics
   - the PENDING-target semantics for unthresholded KPIs
   - an abstracted notification dispatch interface with a test double
   - tests/sla/*.* covering cases a through g
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all seven tests.
   - For case a, show the process restart and the timer still firing.
   - For case f, show the synthetic history, your computed value and the
     hand-calculated expectation side by side.
   - For case g, paste the API response showing PENDING rather than a number.
   - Acceptance criterion: timers survive restart, escalations are never lost,
     and no metric reports a target the source has not set.

G. COMPLETION CONTRACT
   Definition of Done: durable timers, working escalation, stuck-run detection,
   event-derived metrics with honest PENDING targets.
   Evidence to report: the seven test outputs, the restart proof, the metric
   calculation comparison.
   Remaining blockers: KPI targets remain owner-owned (open decision OD-04).
   Report that the measurement path is ready and the thresholds are not set.
   Next prompt: P04-01. PHASE-03 exit requires AT-WF-001 and AT-WF-002 green,
   the replay suite green, and the contract-drift test green.
```

**المخرجات المتوقعة:** مؤقتات صامدة، تصعيد مُسجَّل، مقاييس مشتقة من الأحداث.
**التحقق المطلوب:** المؤقتات تصمد لإعادة التشغيل؛ لا مقياس يُظهر هدفاً لم يحدده المصدر.
**الاعتمادية التالية:** `P04-01`.


---

# PHASE-04 — بوابة الذكاء والتوجيه والميزانية


## الغرض من المرحلة

هذه المرحلة تُنفّذ الطبقة الجديدة في الإصدار v11: الأوراق 70 إلى 77. وهي تحوّل
`ADR-002` («كل اتصال بالنماذج والأدوات Backend-to-Backend خلف API Gateway») إلى
مكوّن فعلي بثلاث عشرة مسؤولية محددة في الورقة 70.

القرار الحاكم في الورقة 77 الصف 2: «مزودون متعددون عبر بوابة مستقلة» مع رفض
صريح لـ«الارتباط الصلب بـOpenRouter». والورقة 77 الصف 4: «أهلية حتمية ← درجة
وتكلفة مقيسة ← canary» مع رفض «روليت النماذج المجانية المعتم». أي أن التوجيه يجب
أن يكون قابلاً للتدقيق، لا ذكياً وغامضاً.

## شروط الدخول

- اكتمال `PHASE-03`: محرك مسارات العمل يستطيع إرسال مهام مُنمَّطة.
- وجود خزانة أسرار (من `P01-04`/`P13-02` إن سبقت) أو خزانة بديلة موثقة.

## شروط الخروج

- محرك السياسة يسجّل 100% من القرارات ويفشل مُغلقاً.
- مزودان مستقلان على الأقل مُشغَّلان فعلاً.
- اختبارات فوضى (429/5xx/timeout/stalled stream) تُنتج بديلاً مُحدَّداً ومُختبراً.
- حد الميزانية يوقف حلقة جارية.
- دفتر الاستخدام يُسجّل مرة واحدة بالضبط ويُطابَق.

## المتطلبات المغطاة في هذه المرحلة

`ADR-002`, `REQ-GW-01`..`REQ-GW-14`, `REQ-GW-17`, `REQ-GW-20`, `REQ-API-06`,
`REQ-API-07`, `REQ-API-08`, `REQ-DAT-08`, `REQ-COM-10`

## تحذير مهم

الورقة 71 الصف 7 قاعدة غير قابلة للتفاوض: «لا LLM لحقيقة القياس المرجعية»
(No LLM for measurement ground truth). والورقة 71 الصف 9: في مسائل السلامة
والإنشاءات «LLM يساعد فقط» و«fail closed». أي توجيه يسمح لنموذج بإنتاج قياس أو
حكم سلامة نهائي يخالف المصدر.

---

## الأوامر التنفيذية

---

### `P04-01` — مدخل البوابة ومغلف المهمة والبث

**Phase:** `PHASE-04` · **EN title:** Gateway ingress, typed task envelope and streaming

**المتطلبات السابقة:** `P03-05`

**المتطلبات المغطاة:** `ADR-002`, `REQ-GW-01`, `REQ-GW-02`, `REQ-API-06`, `REQ-API-07`, `REQ-API-08`

**ماذا سينفذ هذا الأمر؟** يبني نقطة دخول واحدة `/v1/ai/execute` بمغلف مهمة
مُنمَّط وبث SSE، خلف مصادقة خدمة وRBAC وidempotency، مع اشتقاق المستأجر من الخادم.

**لماذا نحتاجه؟** الورقة 74 الصف 2 تحدد الشرط الحاسم: «المستأجر مشتق من الخادم؛
لا تثق أبداً بـ`tenant_id` من العميل». والورقة 74 الصف 4 تمنع ظهور أي أسرار أو
بيانات شخصية في البث. هذه البوابة هي المكان الوحيد الذي يُسمح فيه بالوصول إلى
النماذج، فأي مسار جانبي يُبطل `ADR-002`.

**ما المتطلبات السابقة؟** `P03-05`.

**ما النتيجة المتوقعة؟** نقطة تنفيذ واحدة، ونقطتا قراءة (حالة وبث)، واختبار
معماري يمنع أي مسار مباشر إلى مزود.

**كيف نتحقق من نجاحه؟** اختبار يؤكد عدم وجود أي استدعاء لمزود خارج البوابة؛
واختبار يرسل `tenant_id` كاذباً في الطلب ويتأكد من تجاهله.

```text
TASK P04-01 — Gateway ingress, typed task envelope and streaming

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-01
   Phase: PHASE-04 (AI gateway, model registry, routing and budget)
   Prerequisites: P03-05
   Requirements covered: ADR-002, REQ-GW-01, REQ-API-06, REQ-API-07

B. OBJECTIVE
   Build the private AI gateway: one entry point POST /v1/ai/execute taking a
   typed task envelope, plus execution read and SSE event endpoints, behind
   service OIDC authentication, tenant and project RBAC, WAF and idempotency —
   and make it the only path to any model provider.

   Why this is necessary: ADR-002 (sheet 02 row 3) requires every model and
   tool call to be backend-to-backend behind a gateway with no keys in the
   browser. Sheet 70 row 2 specifies this component. Sheet 74 row 2 adds the
   decisive rule: tenant is server-derived and a client-supplied tenant_id is
   never trusted. Sheet 74 row 4 forbids secrets or PII in the stream.

   SCOPE BOUNDARY: ingress, envelope, authorization, idempotency, streaming and
   the architectural guard. Model selection is P04-03. Provider calls are
   P04-04. Budget enforcement is P04-06. Output validation is P04-07. Here, a
   routed execution is dispatched to a test double.

C. CONTEXT
   Required inputs:
     - sheet 74 row 2: POST /v1/ai/execute request fields tenant_id,
       project_id, task_type, risk, modality, input_refs, budget,
       idempotency_key; response execution_id, state, trace_id
     - sheet 74 row 3: GET /v1/ai/executions/{id} returns state, spans, costs,
       model versions, evidence_refs; role-scoped
     - sheet 74 row 4: GET /v1/ai/executions/{id}/events takes last_event_id
       and returns SSE progress, agent events and partial artifacts, with no
       secrets or PII in streams
     - sheet 70 row 2: SLO note "p95 overhead under 150ms target; measure"
     - the policy service from P01-04 and the idempotency layer from P03-03
   Note on the SLO: the source states a target and explicitly instructs to
   measure it. Do not report a latency number you have not measured, and do not
   treat 150ms as achieved because it is written down.

D. EXECUTION INSTRUCTIONS
   1. Define the task envelope as a typed schema with: tenant_id (accepted in
      the payload for client convenience but IGNORED and overwritten from the
      authenticated principal), project_id, task_type, action_risk (R0-R4),
      professional_consequence (P0-P3), modality, input_refs (artifact and
      version and digest references only — never inline content), budget hints,
      and idempotency_key.
   2. Implement server-derived tenancy explicitly: resolve tenant from the
      authenticated principal, compare it against any client-supplied value,
      and on mismatch reject with 403 and emit a security event. Never silently
      accept the client value, and never silently ignore the mismatch.
   3. Enforce service OIDC authentication for internal callers and tenant plus
      project RBAC for user-originated calls, through the existing
      authorization point from P01-03. Consult the policy service from P01-04
      before dispatch; a DENY returns 403 with the reason code, an
      ALLOW_WITH_GATE returns a pending state that names the required human
      gate.
   4. Implement idempotency on execute per P03-03: a repeated key with the same
      request hash returns the original execution_id and creates no second
      execution.
   5. Validate input_refs: every reference must resolve to a CLEAN, existing
      artifact version whose digest matches, using the fail-closed resolver
      from P02-02. Inline payload content is rejected so that provenance is
      always preserved.
   6. Implement the execution record with state, trace_id, span references,
      cost references, resolved model versions and evidence refs, and expose it
      via GET /v1/ai/executions/{id} with role scoping.
   7. Implement the SSE endpoint with resumability by last_event_id and a
      monotonic sequence per execution. Apply a redaction filter on every
      emitted frame; the stream carries progress, state and artifact references,
      never raw prompts, provider responses, secrets or personal data.
   8. Emit ai.execution.completed and ai.execution.failed v1 through the outbox
      per sheet 74 rows 8-9, with consumer dedupe and DLQ.
   9. Implement the architectural guard, which is the most important deliverable
      of this prompt. Write a test that fails if any module outside the gateway
      package imports a provider SDK, constructs a provider HTTP client, or
      reads a provider credential. Enforce it with a dependency or import rule
      so a future contributor cannot bypass the gateway by accident. Also assert
      no client-side bundle can reach a provider: scan the browser build output
      for provider hostnames and credential names.
  10. Instrument gateway overhead: measure the time the gateway adds around the
      downstream call and record p50 and p95 as real measurements. Report the
      numbers you observe against the source's stated target. If you cannot
      produce a representative measurement, say so rather than quoting the
      target.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the typed task envelope schema
   - POST /v1/ai/execute, GET /v1/ai/executions/{id}, GET
     /v1/ai/executions/{id}/events
   - server-derived tenancy with mismatch rejection and security event
   - policy consultation before dispatch
   - input_ref resolution that fails closed
   - resumable, redacted SSE with per-execution sequencing
   - the two gateway events through the outbox
   - tests/architecture/no-provider-bypass.* plus the client bundle scan
   - gateway overhead instrumentation with measured p50 and p95
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the no-provider-bypass test output, then deliberately add a provider
     import outside the gateway, show the test failing, and remove it. Both
     outputs are required.
   - Paste the client bundle scan result.
   - Send a request whose body claims another tenant; paste the 403 and the
     security event.
   - Paste an SSE transcript showing resumption from last_event_id and showing
     a redacted field where a prompt would otherwise appear.
   - Paste the measured p50 and p95 gateway overhead with the sample size, and
     state plainly whether it meets the source's 150ms target or is not yet
     representative.
   - Acceptance criterion: no code path outside the gateway can reach a
     provider, and the test proving it can actually fail.

G. COMPLETION CONTRACT
   Definition of Done: single gateway entry with typed envelope, server-derived
   tenancy, redacted resumable streaming, and an enforced architectural guard
   proven able to fail.
   Evidence to report: both guard outputs, the bundle scan, the tenant-mismatch
   rejection, the SSE transcript, the measured overhead.
   Remaining blockers: none expected. If no real provider is configured yet,
   state that dispatch ran against a double and name P04-04.
   Next prompt: P04-02.
```

**المخرجات المتوقعة:** بوابة بنقطة دخول واحدة، بث مُحجَّب قابل للاستئناف، حارس معماري.
**التحقق المطلوب:** الحارس يفشل عند إضافة استيراد مزود خارج البوابة؛ رفض `tenant_id` الكاذب.
**الاعتمادية التالية:** `P04-02`.

---

---

### `P04-02` — سجل النماذج وسجل القدرات

**Phase:** `PHASE-04` · **EN title:** Model registry and capability registry

**المتطلبات السابقة:** `P04-01`

**المتطلبات المغطاة:** `REQ-GW-03`, `REQ-GW-13`, `REQ-GW-19`, `REQ-GW-20`

**ماذا سينفذ هذا الأمر؟** يبني سجل نماذج بالحقول الأحد عشر في الورقة 72، وسجل
قدرات يختار النماذج المؤهلة بحسب القدرة والنمط ودعم العربية ونافذة السياق
والتوافر، مع قائمة سماح بحسب تصنيف البيانات.

**لماذا نحتاجه؟** الورقة 72 الصف 6 تضع قاعدة دقيقة: `quality_score` يكون «لكل
مهمة بقياس offline/online؛ ولا يكون أبداً درجة عامة شاملة». وهذا يمنع الخطأ
الشائع: ترتيب النماذج بدرجة واحدة ثم اعتبارها صالحة لكل مهمة.

**ما المتطلبات السابقة؟** `P04-01`.

**ما النتيجة المتوقعة؟** سجل نماذج بإصدارات وحالة إصدار وحالة دائرة، وسجل قدرات
يُنتج مجموعة مؤهلين قابلة للتفسير.

**كيف نتحقق من نجاحه؟** لا نموذج يدخل مجموعة المؤهلين لتصنيف بيانات غير مسموح
له؛ ولا نموذج له درجة عامة.

```text
TASK P04-02 — Model registry and capability registry

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-02
   Phase: PHASE-04
   Prerequisites: P04-01
   Requirements covered: REQ-GW-03, REQ-GW-13, REQ-GW-19, REQ-GW-20

B. OBJECTIVE
   Implement the model registry with the eleven fields the source specifies,
   and the capability registry that produces an explainable eligible-model set
   filtered by verified capability, modality, Arabic support, context window,
   availability and data classification allowlist.

   Why this is necessary: sheet 72 sets a precise rule in row 6 — quality_score
   is per-task from offline and online benchmarks and is "never a global
   generic score". Sheet 70 row 4 requires selection by verified capability
   with an allowlist by classification and no unapproved provider. Sheet 77
   row 5 forbids assuming any gateway is Saudi-resident, so region and data
   policy are registry facts, not assumptions.

   SCOPE BOUNDARY: the two registries and eligibility computation. Scoring and
   final selection are P04-03. Benchmarks that populate quality_score are
   PHASE-14 — here you build the field, its provenance and the rule that an
   unpopulated score cannot be treated as good.

C. CONTEXT
   Required inputs:
     - config/registries/model-registry-schema.json from P00-02 (sheet 72
       rows 2-11): model_id (immutable provider/model/version id, owner AI
       platform); provider and region (legal entity and endpoint geography,
       owner Security); capabilities (reasoning, Arabic, vision, tool, JSON,
       context; owner Evaluation); data_policy (approved classes, retention,
       training, transfer; owner Legal); quality_score (per-task, owner QA);
       p50/p95 latency (per task, modality and load; owner SRE); cost_in/out
       (currency per million tokens, effective rate including cache, tools and
       taxes; owner FinOps); limits (RPM, TPM, concurrency, timeout, context;
       owner SRE); health/circuit (healthy, degraded, open, half-open; owner
       Runtime); release_status (candidate, canary, approved, blocked, retired;
       owner Governance)
     - docs/discovery/INTEGRATION-ACCESS-AUDIT.md from P00-03 for what each
       provider's agreement and region actually are
     - sheet 51 rows 2-9 for the nine SLA policy controls and their owners

D. EXECUTION INSTRUCTIONS
   1. Implement the model registry with all eleven fields. model_id is
      immutable and includes the provider, model and version so a route is
      always reproducible. A model entry is a versioned record; changing a
      field creates a new revision with an actor and timestamp.
   2. Make data_policy authoritative and sourced: approved data classes,
      retention period, whether provider training on inputs is permitted, and
      permitted transfer geographies. Each field records the document that
      establishes it (a DPA reference or contract id from P00-03). A field with
      no establishing document is NOT_PROVIDED, and a model with a
      NOT_PROVIDED data policy is ineligible for anything above the lowest
      classification. Do not infer a policy from a provider's marketing page.
   3. Implement quality_score strictly per task: a map from task class to a
      scored result with the evaluation run reference, the dataset reference and
      the measurement date. Reject any attempt to write a scalar global score —
      make it a type error, not a convention. An absent score for a task class
      means INELIGIBLE for quality-first routing in P04-03, never "assume
      acceptable".
   4. Implement release_status with its five values and enforce the lifecycle:
      candidate -> canary -> approved, and blocked or retired as terminal.
      Only approved models serve production traffic; canary serves only the
      configured canary share; blocked and retired serve nothing.
   5. Implement health and circuit state as runtime-owned fields updated by
      P04-04, with the four states the source names.
   6. Implement the capability registry: given a task_type, modality, required
      capabilities, required context window, data classification and tenant
      policy, return the eligible model set plus, for every excluded model, the
      specific exclusion reason. An eligibility result is explainable by
      construction — this is what makes sheet 77 row 4's "auditable decisions"
      achievable.
   7. Enforce the classification allowlist as a hard gate: a model whose
      data_policy does not include the request's data classification is
      excluded regardless of score, cost or availability. Likewise a model
      whose region is outside the permitted transfer geographies for that
      classification.
   8. Treat Arabic support as a verified capability, not an assumption. Sheet 64
      row 4 defines Arabic quality as an evaluation dimension with reviewer
      acceptance, currently NOT TESTED. Until an evaluation exists, the Arabic
      capability flag is UNVERIFIED and routing must surface that.
   9. Record every eligibility computation with its inputs, result and the
      registry revision used, so a past routing decision can be reconstructed.
  10. Tests:
        a. a model with NOT_PROVIDED data policy is excluded for a restricted
           classification, with the reason given;
        b. a model whose region is outside permitted transfer is excluded;
        c. a model with no quality_score for the requested task class is
           excluded from quality-first eligibility, with the reason;
        d. writing a scalar global quality score fails;
        e. a candidate or blocked or retired model never appears in a
           production eligible set;
        f. changing a registry field creates a new revision and leaves the old
           one intact;
        g. an eligibility result lists an exclusion reason for every excluded
           model, with none unexplained;
        h. a context window smaller than the request's requirement excludes the
           model.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the model registry with eleven fields, revisioned, with sourced
     data_policy
   - per-task quality_score typing that rejects a global score
   - release_status lifecycle enforcement
   - runtime health and circuit fields
   - the capability registry returning an explainable eligible set
   - the classification and region hard gates
   - eligibility computation audit records
   - tests/gateway/registry-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eight tests.
   - Paste one full eligibility result showing every model and its include or
     exclude reason.
   - List every registered model with its data_policy provenance document, or
     NOT_PROVIDED. State how many models are currently eligible for the highest
     data classification; if the answer is zero, say so plainly.
   - Acceptance criterion: no model is eligible without an establishing data
     policy document, and no eligibility result contains an unexplained
     exclusion.

G. COMPLETION CONTRACT
   Definition of Done: both registries implemented with the source's exact
   fields and rules; eligibility explainable; hard gates enforced.
   Evidence to report: the eight test outputs, a sample eligibility
   explanation, the model-to-data-policy provenance table.
   Remaining blockers: quality_score is empty until PHASE-14 benchmarks run,
   and the Arabic capability stays UNVERIFIED until then. Report both as
   expected, and confirm the registry refuses to pretend otherwise.
   Next prompt: P04-03.
```

**المخرجات المتوقعة:** سجل نماذج بأحد عشر حقلاً، سجل قدرات بأهلية مُفسَّرة.
**التحقق المطلوب:** رفض الدرجة العامة؛ استبعاد كل نموذج بلا مستند سياسة بيانات.
**الاعتمادية التالية:** `P04-03`.

---

---

### `P04-03` — الراوتر التكيّفي وسياسات التوجيه

**Phase:** `PHASE-04` · **EN title:** Adaptive router and the eight routing policies

**المتطلبات السابقة:** `P04-02`

**المتطلبات المغطاة:** `REQ-GW-04`, `REQ-GW-14`, `REQ-GW-15`, `REQ-GW-16`, `REQ-GW-17`

**ماذا سينفذ هذا الأمر؟** يبني الراوتر: قواعد حتمية أولاً، ثم درجة وتكلفة مقيسة،
ثم canary؛ وينفّذ سياسات التوجيه الثماني في الورقة 71 بأرضية جودة لكل صنف مهمة.

**لماذا نحتاجه؟** الورقة 77 الصف 4 ترفض «روليت النماذج المجانية المعتم» وتطلب
«قرارات قابلة للتدقيق». والورقة 70 الصف 5 تشترط: «قواعد حتمية أولاً؛ contextual
bandit فقط بعد التقييم». والورقة 71 تضع لكل صنف مهمة استراتيجية وفحص جودة وقاعدة
بديل وضابط تكلفة.

**ما المتطلبات السابقة؟** `P04-02`.

**ما النتيجة المتوقعة؟** راوتر حتمي قابل للتفسير والإعادة، وثماني سياسات مُنفَّذة،
وأرضية جودة تمنع التدهور الصامت.

**كيف نتحقق من نجاحه؟** إعادة نفس الطلب بنفس حالة السجل تُنتج نفس القرار؛ ومهام
القياس والسلامة لا تُوجَّه إلى نموذج أبداً.

```text
TASK P04-03 — Adaptive router and the eight routing policies

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-03
   Phase: PHASE-04
   Prerequisites: P04-02 (eligible model sets available)
   Requirements covered: REQ-GW-04, REQ-GW-14, REQ-GW-15, REQ-GW-16,
                         REQ-GW-17

B. OBJECTIVE
   Implement the adaptive router — quality-first for high-risk tasks, least-cost
   within a validated tier for routine tasks, deterministic rules before any
   learning — and the eight per-task-class routing policies with their quality
   checks, fallback rules and cost controls.

   Why this is necessary: sheet 70 row 5 requires deterministic rules first and
   permits a contextual bandit only after evaluation, with a quality floor per
   task. Sheet 77 row 4 adopts "deterministic eligibility, then measured score
   and cost, then canary" and explicitly rejects "opaque free-model roulette",
   because the rationale is auditable decisions.

   SCOPE BOUNDARY: selection logic and policy enforcement. Provider invocation
   and failover execution are P04-04. Do not implement a bandit or any online
   learning in this prompt — the source gates that behind evaluation evidence
   that does not exist yet.

C. CONTEXT
   Required inputs:
     - config/registries/routing-policies.json (sheet 71 rows 2-9), the eight
       task classes with candidate tier, route strategy, quality check,
       fallback rule and cost control:
       1. OCR/extraction — document vision verified; benchmark Arabic docs and
          plans, OCR deterministic first; check field accuracy and confidence;
          fallback a different approved vision model; cost control crop pages,
          only changed regions
       2. Routine support — fast low-cost; approved small model with RAG; check
          citation and answer grounding; fallback mid-tier approved; cost
          control max output tokens
       3. Architectural reasoning — high-quality reasoning; approved reasoning
          model; check constraint and evidence; fallback peer-quality approved;
          cost control bounded multi-step
       4. SBC compliance — high-quality plus rules; retrieve licensed
          authoritative codes and a rules engine; check clause citations plus
          human sign-off; fallback pause to human if evidence absent; cost
          control reuse indexed clauses
       5. BOQ/costing — deterministic engine plus LLM; LLM extracts only,
          calculators price; check unit, quantities, audit trail; fallback
          manual review if confidence low; cost control no repeated
          full-document context
       6. LiDAR geometry — native RoomPlan or CAD tools; NO LLM for measurement
          ground truth; check scan confidence plus known dimension; fallback
          manual tape or reference; cost control send geometry not video
       7. Live scan narration — small multimodal only as needed;
          event/keyframe triggered; check grounding and latency; fallback
          disable AI commentary safely; cost control frame sampling and local
          filtering
       8. Safety/structural — engineering deterministic plus expert; LLM
          assists only; check licensed reviewer approval; fallback fail closed;
          cost control premium route only when justified
     - sheet 63 rows 2-8, the parallel task-class table with escalation
       triggers, which refines the above
     - the eligible-set computation from P04-02

D. EXECUTION INSTRUCTIONS
   1. Implement routing as an ordered, auditable pipeline:
        stage 1 hard eligibility (from P04-02; classification, region,
                 capability, context, release_status) — non-negotiable;
        stage 2 policy strategy for the task class (from the register);
        stage 3 measured score and cost ranking within the validated tier;
        stage 4 canary share application.
      Each stage records what it removed and why. The final decision carries
      the full chain.
   2. Implement quality-first versus least-cost by risk: when action_risk or
      professional_consequence is high (R3-R4 or P2-P3), rank by measured
      quality for that task class and never substitute a cheaper model that
      lacks a score. For routine classes, rank by cost within the tier whose
      quality has been validated.
   3. Implement the per-class quality floor. A model with no measured score for
      the class cannot satisfy a floor. If no model clears the floor, the router
      returns NO_ELIGIBLE_ROUTE with the reason — it does not fall back to an
      unscored model. Sheet 70 row 5's gate is "quality floor per task"; an
      unscored route silently taken is exactly the failure this prevents.
   4. Implement the two deterministic-first classes as code paths that do not
      call a model at all:
        - LiDAR geometry (sheet 71 row 7): measurement ground truth comes from
          the native scan or CAD tool. The router must refuse to route a
          measurement-truth task to any model. Make this a hard assertion.
        - BOQ/costing (sheet 71 row 6): the model may extract, but pricing is
          computed by the calculator. The router marks the step EXTRACT_ONLY
          and the pricing path rejects a model-produced price.
   5. Implement fail-closed for safety and structural (sheet 71 row 9): the
      route is assist-only, the output cannot be final, and a licensed reviewer
      approval is a required downstream gate. If that gate is unavailable, the
      task does not run.
   6. Implement the pause-to-human fallback for SBC compliance when source
      evidence is absent (sheet 71 row 5), wired to the AWAITING_INFORMATION or
      AWAITING_REVIEW transition from P03-02 rather than to a guess.
   7. Implement multi-provider topology per sheet 77 row 2: the router must be
      able to select across at least two independent providers, and no code path
      may hard-depend on one aggregator. Add a test that removes one provider
      entirely and asserts the router still produces routes for the classes
      where another approved model is eligible.
   8. Implement canary: a configured share of eligible traffic for a canary
      model, with the share recorded on every decision, and an immediate
      rollback switch that takes effect without a deploy.
   9. Make decisions reproducible: given the same request and the same registry
      revision and policy version, the decision is identical. Record the
      registry revision, policy version and random seed (for canary assignment)
      on every decision.
  10. Tests:
        a. an R4/P3 task routes by measured quality and never to an unscored
           model;
        b. no model clears the floor -> NO_ELIGIBLE_ROUTE with the reason, and
           no call is made;
        c. a measurement-truth LiDAR task -> the router refuses any model
           route; assert with a model-client double that fails if called;
        d. a BOQ task -> marked EXTRACT_ONLY, and a model-produced price is
           rejected by the pricing path;
        e. a safety/structural task with no reviewer gate available -> does not
           run;
        f. an SBC compliance task with absent source evidence -> pauses to
           human, no fabricated citation;
        g. remove one provider -> routes still produced where another approved
           model is eligible;
        h. same request plus same registry revision plus same policy version ->
           byte-identical decision, twice;
        i. canary share honoured over a large sample within tolerance, and the
           rollback switch immediately stops canary assignment;
        j. the decision record for any route explains every stage's exclusions.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the four-stage auditable routing pipeline
   - risk-driven quality-first versus cost-first ranking
   - per-class quality floors with NO_ELIGIBLE_ROUTE semantics
   - the two deterministic-first paths with model routing hard-refused
   - fail-closed safety routing and pause-to-human compliance fallback
   - multi-provider selection with no single-aggregator dependency
   - canary with recorded share and instant rollback
   - reproducible decisions with registry revision, policy version and seed
   - tests/gateway/router-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - For case c, paste the double's assertion proving no model client was
     constructed or called.
   - For case h, paste both decision records and show they are identical.
   - Paste one full decision record showing stage-by-stage exclusions.
   - Acceptance criterion: no unscored model ever serves a high-risk task, no
     model ever produces measurement ground truth, and every decision is
     reproducible and explainable.

G. COMPLETION CONTRACT
   Definition of Done: deterministic, reproducible, explainable routing with
   enforced quality floors and the two no-model paths.
   Evidence to report: the ten test outputs, the no-call assertion, the
   reproducibility proof, a sample decision record.
   Remaining blockers: quality floors cannot be set numerically until PHASE-14
   produces benchmarks (open decision OD-04). Until then the floor
   configuration is empty and the router correctly returns NO_ELIGIBLE_ROUTE
   for quality-first classes. Report that as the expected, honest state — do
   not populate a placeholder floor to make routing appear to work.
   Next prompt: P04-04.
```

**المخرجات المتوقعة:** خط توجيه رباعي المراحل، أرضيات جودة، مسارا «بلا نموذج»، canary.
**التحقق المطلوب:** لا نموذج بلا درجة لمهمة عالية الخطر؛ لا نموذج لحقيقة القياس؛ قرار قابل للإعادة.
**الاعتمادية التالية:** `P04-04`.

---

---

### `P04-04` — محوّلات المزودين والبديل وقاطع الدائرة

**Phase:** `PHASE-04` · **EN title:** Provider adapters, fallback controller and circuit breaker

**المتطلبات السابقة:** `P04-03`

**المتطلبات المغطاة:** `REQ-GW-05`, `REQ-GW-06`, `REQ-GW-17`, `REQ-SEC-01`, `REQ-OBS-03`

**ماذا سينفذ هذا الأمر؟** يبني محوّلات مزودين تُطبّع العقد، مع مهل وإعادة محاولة
وقاطع دائرة، ووحدة تحكم بديل لا تُنزل الجودة صامتة.

**لماذا نحتاجه؟** الورقة 70 الصف 7 تضع القيد الحاسم: «لا تُنزل أبداً تحقق الهندسة
الحرج بصمت». والورقة 38 الصف 8 (`G-03`) حاجز إصدار يتطلب إثبات
«429/timeout/stalled stream» بـ«fault injection traces».

**ما المتطلبات السابقة؟** `P04-04` يعتمد على `P04-03`.

**ما النتيجة المتوقعة؟** محوّلان لمزودين مستقلين على الأقل، وبديل مُختبَر، وقاطع
دائرة بحالات أربع.

**كيف نتحقق من نجاحه؟** حقن أعطال 429 و5xx وtimeout وبث متوقف يُنتج سلوكاً
مُحدَّداً ومُسجَّلاً، لا تعليقاً ولا نجاحاً زائفاً.

```text
TASK P04-04 — Provider adapters, fallback controller and circuit breaker

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-04
   Phase: PHASE-04
   Prerequisites: P04-03 (routing decisions produced)
   Requirements covered: REQ-GW-05, REQ-GW-06, REQ-GW-17, REQ-SEC-01,
                         REQ-OBS-03

B. OBJECTIVE
   Implement provider adapters with a normalized contract, secrets from a
   vault, an egress allowlist, timeouts, bounded retries and a circuit breaker;
   plus a fallback controller that stays inside the approved region and data
   classification, preserves quality equivalence, and never silently downgrades
   critical engineering verification.

   Why this is necessary: sheet 70 row 6 specifies adapters with a normalized
   contract, vault secrets, egress allowlist and no browser keys. Sheet 70
   row 7 specifies the fallback controller and its hard rule against silent
   downgrade. Sheet 38 row 8 (G-03) is a release blocker requiring fault
   injection traces for 429, timeout and stalled stream. Sheet 76 row 5 (G04)
   requires chaos evidence.

   SCOPE BOUNDARY: provider invocation, resilience and failover. Do not change
   routing logic. Do not implement budget enforcement (P04-06) or output
   validation (P04-07).

C. CONTEXT
   Required inputs:
     - the routing decision from P04-03, which names model_id and a
       fallback chain
     - sheet 70 row 6 providers named as candidates: OpenAI, Anthropic, Google,
       with OpenRouter optional. Sheet 77 row 2 adopts multi-provider through an
       independent gateway and rejects hard lock-in to OpenRouter.
     - sheet 75 rows 2-3: the 429 runbook (bounded exponential jitter,
       backpressure, route to an approved alternate) and the provider outage
       runbook (stop retries, open circuit, fail over to allowed)
     - sheet 51 row 6: reliability control with timeouts, circuit breaker and
       retry jitter, metric p95 and error rate, fallback provider failover,
       proof chaos tests
   Credential reality: use only credentials already present in the environment,
   per the audit from P00-03. If none exist, implement against a contract-
   conformant local fake and report that no real provider was exercised. Do not
   create accounts and do not spend money.

D. EXECUTION INSTRUCTIONS
   1. Define one normalized adapter interface covering: text and multimodal
      completion, streaming, tool or function calling, structured JSON output,
      token accounting, and error classification. Every provider implements the
      same interface so the router is provider-agnostic.
   2. Implement a provider-independent error taxonomy mapping each provider's
      errors into the classes sheet 36 row 15 requires: errorCode, retryable,
      providerFailure, partialArtifacts. At minimum: RATE_LIMITED,
      TIMEOUT, STALLED_STREAM, SERVER_ERROR, INVALID_REQUEST,
      CONTENT_FILTERED, CONTEXT_EXCEEDED, AUTH_FAILED, QUOTA_EXCEEDED.
   3. Load credentials from the vault only, at call time, never into logs,
      traces, error messages or the SSE stream. Add a test asserting a forced
      adapter error does not include the credential anywhere in its message or
      stack.
   4. Enforce an egress allowlist at the network layer for the gateway process:
      only approved provider hostnames are reachable. Add a test asserting a
      call to a non-allowlisted host fails. This is the control that limits
      tool-based exfiltration (sheet 27 row 8).
   5. Implement timeouts at three levels: connection, first token, and total
      wall clock. A stalled stream is a distinct, detected failure — a stream
      that stops producing tokens must trip the first-token or inter-token
      timeout rather than hanging until the total budget expires.
   6. Implement bounded retries with exponential backoff and jitter per
      sheet 75 row 2, with a maximum attempt count and a maximum total added
      latency. Retry only errors classified retryable, and only steps whose
      side-effect class is SAFE_RETRYABLE per P03-02.
   7. Implement the circuit breaker with the four states sheet 72 row 10 names:
      healthy, degraded, open, half-open. Opening stops retries immediately
      (sheet 75 row 3). Half-open admits a probe. State changes update the model
      registry's health field and emit an event.
   8. Implement the fallback controller with the source's constraints:
        - a fallback candidate must be within the approved region and data
          classification for the request — never widen either to find capacity;
        - it must be quality-equivalent for the task class, using the per-class
          scores from P04-02;
        - for critical engineering verification (high P, and the
          safety/structural and SBC compliance classes), a downgrade is
          forbidden. If no equivalent route exists, the execution fails closed
          with FALLBACK_UNAVAILABLE. It does not quietly use a weaker model.
        - every fallback is recorded on the execution with the original model,
          the fallback model, the trigger and the equivalence justification.
   9. Implement backpressure: when providers are saturated, shed or queue by
      priority rather than amplifying load with retries. Sheet 73 row 2's
      action for a p95 breach is "shed low-priority load" — implement a
      priority signal so that is possible.
  10. Build the chaos test harness with a fault-injecting fake provider, and
      write the tests:
        a. 429 -> bounded jittered retry, then route to an approved alternate;
           assert attempt count and total added latency are within bounds;
        b. repeated 5xx -> circuit opens, retries stop immediately, registry
           health becomes open, event emitted;
        c. half-open probe succeeds -> state returns to healthy; probe fails ->
           back to open;
        d. stalled stream -> detected by the inter-token timeout, not by the
           total budget; execution ends with STALLED_STREAM and a partial
           artifact record if any;
        e. connection timeout -> classified TIMEOUT, retried per policy;
        f. fallback that would cross a region or classification boundary ->
           refused, execution fails closed;
        g. a high-P critical task with no quality-equivalent fallback ->
           FALLBACK_UNAVAILABLE, no downgrade;
        h. a forced adapter error -> no credential appears in the message,
           stack, log or stream;
        i. egress to a non-allowlisted host -> blocked;
        j. saturation -> low-priority load shed, high-priority served, no
           retry amplification.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the normalized adapter interface and at least two provider
     implementations (real where credentials exist, contract-conformant fakes
     otherwise, clearly labelled)
   - the provider-independent error taxonomy
   - vault-only credential loading with leak tests
   - the network egress allowlist
   - three-level timeouts including inter-token stall detection
   - bounded jittered retries limited to safe-retryable steps
   - the four-state circuit breaker wired to registry health
   - the fallback controller with region, classification and equivalence
     constraints and FALLBACK_UNAVAILABLE semantics
   - priority-based backpressure and load shedding
   - tests/chaos/*.* covering cases a through j, with traces retained as
     evidence for release gate G-03
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten chaos tests.
   - Retain and reference the fault-injection traces; sheet 38 row 8 names
     them as the required evidence for G-03, so they must be stored where the
     evidence ledger can cite them.
   - For case g, paste the FALLBACK_UNAVAILABLE outcome and show no provider
     call was made to a lower-quality model.
   - For case h, paste the grep over the error output proving no credential
     material.
   - State plainly which providers were exercised with real credentials and
     which with fakes.
   - Acceptance criterion: every one of the four fault classes in G-03 produces
     a bounded, recorded, non-hanging outcome, and no critical task is ever
     silently downgraded.

G. COMPLETION CONTRACT
   Definition of Done: two adapters behind one interface, chaos suite green,
   circuit breaker and fallback behaving per the source's constraints, traces
   retained.
   Evidence to report: the ten test outputs, the trace storage location, the
   real-versus-fake provider statement, the credential leak grep.
   Remaining blockers: providers without an agreement or credential (from
   P00-03) cannot be exercised for real. Name them; this is an owner-owned
   commercial blocker and a direct input to release gate G01 on sheet 76.
   Next prompt: P04-05.
```

**المخرجات المتوقعة:** محوّلان بواجهة واحدة، تصنيف أخطاء، قاطع دائرة، وحدة بديل.
**التحقق المطلوب:** أربع فئات أعطال بنتائج محدودة ومُسجَّلة؛ لا تدهور صامت لمهمة حرجة.
**الاعتمادية التالية:** `P04-05`.

---

---

### `P04-05` — مُجمِّع السياق وذاكرة المطالبات

**Phase:** `PHASE-04` · **EN title:** Context compiler and prompt cache

**المتطلبات السابقة:** `P04-04`

**المتطلبات المغطاة:** `REQ-GW-07`, `REQ-GW-08`, `REQ-KNW-04`

**ماذا سينفذ هذا الأمر؟** يبني مُجمِّع سياق محدود بالمهمة مع استشهادات وإزالة
تكرار دلالي واستدعاء مُفلتَر بنطاق المستأجر، وذاكرة مطالبات معزولة.

**لماذا نحتاجه؟** الورقة 77 الصف 6 تعتمد «RAG وميزانيات سياق وذاكرة وkeyframes
وأدوات أولاً»، وترفض «ضغط أدلة الهندسة بشكل أعمى»، والسبب المذكور: «الحفاظ على
المصدرية». والورقة 76 الصف 6 (`G05`) تجعل عزل المستأجر شاملاً للذاكرة والآثار
والسجلات، لا قاعدة البيانات وحدها.

**ما المتطلبات السابقة؟** `P04-04`.

**ما النتيجة المتوقعة؟** مُجمِّع سياق يقيس التوفير، وذاكرة معزولة بثلاثة أبعاد،
واستدعاء لا يمكن إصداره بلا فلتر مستأجر.

**كيف نتحقق من نجاحه؟** اختبار يؤكد أن ذاكرة مستأجر لا تخدم مستأجراً آخر أبداً؛
واختبار يؤكد أن الضغط لا يحذف استشهاداً أو مُحدِّد موضع.

```text
TASK P04-05 — Context compiler and prompt cache

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-05
   Phase: PHASE-04
   Prerequisites: P04-04
   Requirements covered: REQ-GW-07, REQ-GW-08, REQ-KNW-04

B. OBJECTIVE
   Implement the context compiler — task-scoped context with citations,
   semantic de-duplication and tenant-scoped ACL-filtered retrieval, reporting
   tokens saved against a baseline — and a prompt cache isolated by tenant,
   data classification and model version.

   Why this is necessary: sheet 70 rows 8-9 specify both components and their
   gates (tokens saved versus baseline; cache hit rate; isolation by tenant,
   classification and model version with no cross-tenant leakage). Sheet 77
   row 6 adopts context budgets and caching but explicitly rejects blindly
   compressing engineering evidence, because provenance must be preserved.
   Sheet 76 row 6 extends tenant isolation to cache, traces and logs.

   SCOPE BOUNDARY: context assembly and caching. The RAG corpora, their rights
   gate and their ingestion are PHASE-06 — here you build the retrieval
   interface with mandatory tenant filtering and consume whatever index exists.

C. CONTEXT
   Required inputs:
     - the mandatory-tenant-filter retrieval interface from P01-02 step 4
     - sheet 24 row 5 (RAG-PROJECT): metadata tenant, project, ACL, revision,
       hash, classification; strategy project-scoped index, no cross-tenant
     - sheet 71 cost controls per class: crop pages and only changed regions
       for extraction; max output tokens for routine; bounded multi-step for
       reasoning; reuse indexed clauses for compliance; no repeated
       full-document context for BOQ; send geometry not video for LiDAR; frame
       sampling for live narration

D. EXECUTION INSTRUCTIONS
   1. Implement a context budget per task class, read from configuration, with
      the per-class cost controls above encoded as assembly rules rather than as
      advice.
   2. Implement task-scoped assembly: the compiler receives the task envelope
      and returns a context package carrying, for every included element, its
      provenance — artifact, version, digest and locator, or source, version
      and anchor for a knowledge citation. An element with no provenance cannot
      enter the package. This is the mechanism that makes sheet 77 row 6's
      "preserve provenance" enforceable rather than aspirational.
   3. Implement semantic de-duplication that removes redundant passages but
      never removes a citation, a locator or a unit. Add a test asserting that
      de-duplication preserves the full citation set and every numeric value
      with its unit. Dropping a unit from engineering evidence is a correctness
      failure, not a size optimization.
   4. Implement budget overflow handling explicitly: when the assembled context
      exceeds the budget, the compiler reduces by the class's declared strategy
      (crop to changed regions, reuse indexed clauses, bound the step count) and
      records what it dropped. If it cannot fit within budget without dropping
      evidence that the task's quality check requires, it returns
      CONTEXT_BUDGET_EXCEEDED rather than silently truncating. Truncating
      engineering evidence silently is the failure sheet 77 row 6 rejects.
   5. Enforce mandatory tenant filtering structurally: the retrieval call cannot
      be constructed without a tenant scope. Make the unfiltered form
      unrepresentable in the type system or guarded by a single checked
      constructor, and test that bypassing it fails.
   6. Implement the prompt cache:
        - the cache key includes tenant, data classification, model id and
          version, prompt template version, and a digest of the stable prefix;
        - entries never cross any of those dimensions;
        - a classification change invalidates;
        - a model version change invalidates;
        - cache content is encrypted at rest and excluded from logs and traces.
   7. Measure and expose: tokens saved versus an uncompiled baseline, cache hit
      rate, and context assembly latency — as measured values feeding the
      PHASE-10 dashboards. Report real measurements only.
   8. Tests:
        a. tenant A's cached entry is never served to tenant B — attempt it
           directly against the cache and assert a miss;
        b. the same prompt under two classifications produces two entries;
        c. a model version bump invalidates;
        d. de-duplication preserves every citation and every value-with-unit;
        e. an element without provenance is refused entry to the package;
        f. a retrieval call cannot be built without a tenant scope;
        g. budget overflow that would drop required evidence returns
           CONTEXT_BUDGET_EXCEEDED rather than truncating;
        h. cache content does not appear in logs, traces or the SSE stream;
        i. measured tokens saved and hit rate are produced from real runs, with
           the sample size reported.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - per-class context budgets with the source's cost-control strategies
   - the provenance-carrying context package with refusal of unprovenanced
     elements
   - citation-and-unit-preserving semantic de-duplication
   - CONTEXT_BUDGET_EXCEEDED semantics instead of silent truncation
   - structurally mandatory tenant-scoped retrieval
   - the three-dimension isolated, encrypted prompt cache
   - measured tokens-saved, hit-rate and latency metrics
   - tests/gateway/context-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - For case a, paste the direct cache probe showing a miss across tenants.
   - For case d, paste the before and after context showing citations and units
     intact.
   - Paste the measured tokens-saved and hit-rate figures with sample sizes. If
     the sample is too small to be meaningful, say so rather than publishing it.
   - Acceptance criterion: no cache entry crosses tenant, classification or
     model version; no compression removes provenance; overflow fails loudly.

G. COMPLETION CONTRACT
   Definition of Done: context compiled within budget with provenance intact,
   cache isolated on all three dimensions, savings measured honestly.
   Evidence to report: the nine test outputs, the cross-tenant cache probe, the
   de-duplication comparison, the measured savings with sample size.
   Remaining blockers: real retrieval quality depends on PHASE-06 corpora,
   which are themselves blocked on source rights (OD-05). Report that the
   interface is complete and the corpora are not.
   Next prompt: P04-06.
```

**المخرجات المتوقعة:** مُجمِّع سياق بمصدرية محفوظة، ذاكرة معزولة بثلاثة أبعاد، قياسات حقيقية.
**التحقق المطلوب:** لا تجاوز ذاكرة بين المستأجرين؛ لا ضغط يحذف مصدرية؛ الفائض يفشل بصوت عالٍ.
**الاعتمادية التالية:** `P04-06`.

---

---

### `P04-06` — وحدة الميزانية ودفتر الاستخدام

**Phase:** `PHASE-04` · **EN title:** Budget controller and exactly-once usage ledger

**المتطلبات السابقة:** `P04-05`

**المتطلبات المغطاة:** `REQ-GW-09`, `REQ-GW-11`, `REQ-DAT-08`, `REQ-COM-10`, `REQ-AGT-01`

**ماذا سينفذ هذا الأمر؟** يبني وحدة ميزانية بتقدير مُسبق وحدود يومية وشهرية لكل
مهمة ومستأجر، ودفتر استخدام يُسجّل مرة واحدة بالضبط لكل تنفيذ.

**لماذا نحتاجه؟** الورقة 70 الصف 10 ضابطها: «لا نداء فوق الميزانية بلا تفويض».
والورقة 15 الصف 15 (`CTRL-014`) دليلها: «حد الميزانية يوقف الحلقة». والورقة 36
الصف 13 (`RT-08`) تشترط «الحفظ مرة واحدة بالضبط لكل تنفيذ». والورقة 39 الصف 12
تفرض `execution_id UNIQUE`.

**ما المتطلبات السابقة؟** `P04-05`.

**ما النتيجة المتوقعة؟** تقدير مُسبق يمنع التجاوز، وإيقاف صلب للحلقات الجارية،
ودفتر قابل للمطابقة.

**كيف نتحقق من نجاحه؟** حلقة تستهلك بلا حد تتوقف عند السقف؛ وإعادة محاولة لا
تُنتج سجل استخدام ثانياً.

```text
TASK P04-06 — Budget controller and exactly-once usage ledger

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-06
   Phase: PHASE-04
   Prerequisites: P04-05
   Requirements covered: REQ-GW-09, REQ-GW-11, REQ-DAT-08, REQ-COM-10,
                         REQ-AGT-01

B. OBJECTIVE
   Implement the budget controller — per-task, per-tenant daily and monthly
   token and SAR caps with a preflight estimate, a hard stop and approval
   thresholds — and the usage ledger that posts exactly once per execution and
   can be reconciled.

   Why this is necessary: sheet 70 row 10's gate is "no over-budget
   unauthorized calls". Sheet 15 row 15 (CTRL-014) requires the evidence
   "budget cap stops loop". Sheet 36 row 13 (RT-08) requires usage persisted
   exactly once per execution and reconciled with credits. Sheet 39 row 12
   enforces it with execution_id UNIQUE. Sheet 05 row 36 (FIN-03) requires
   attribution to tenant and workflow and prevention of runaway loops.

   SCOPE BOUNDARY: budget enforcement, usage recording and reconciliation
   inputs. Customer-facing pricing is PHASE-08. Cost dashboards are PHASE-10.

C. CONTEXT
   Required inputs:
     - config/registries/data-constraints.json, usage_ledger: required
       execution_id, tenant_id, input_tokens, output_tokens, cost;
       execution_id UNIQUE; index tenant_id, created_at; invariant
       "exactly-once posting"; retention "finance policy"
     - sheet 34 row 13: EV-08 UsageRecorded usage.recorded.v1, aggregate AI
       Core, required payload executionId, inputTokens, outputTokens, producer
       AI Core, consumer billing and observability, ordering key executionId,
       at-least-once, validation "reconcile ledger; no double-charge"
     - sheet 72 row 8: cost_in/out is the effective rate per million tokens
       including cache, tools and taxes
     - sheet 61 row 8: cost spike scenario — throttle and downgrade safe tasks,
       hard tenant and project cap, evidence usage ledger
   Important: all commercial rates in the source calculator are zero except
   VAT (sheet 19 row 54). Provider rates in the model registry must come from
   real contracts. If a rate is absent, the cost field is UNPRICED, and an
   UNPRICED execution still records tokens. Never invent a rate to make a cost
   number appear.

D. EXECUTION INSTRUCTIONS
   1. Implement budget scopes with independent caps: per execution, per task,
      per project, per tenant per day, and per tenant per month, in both tokens
      and currency.
   2. Implement the preflight estimate before dispatch: estimate input tokens
      from the assembled context and output tokens from the task class ceiling,
      price them from the model registry's effective rates, and compare against
      every applicable remaining cap. Over-cap requests are denied before any
      provider call, with a reason naming which cap was hit.
   3. Implement approval thresholds: a configurable band where the request is
      not denied but requires an explicit authorization, returning the
      ALLOW_WITH_GATE pending state from P04-01 rather than proceeding.
   4. Implement the hard stop during execution, which is the control CTRL-014
      requires evidence for. A multi-step or agentic execution re-checks the
      remaining budget before every step and before every provider call, and
      terminates with BUDGET_EXHAUSTED when the cap is reached. Termination
      records the partial artifacts produced so work is not lost silently.
   5. Implement the usage ledger:
        - one row per execution, keyed by execution_id with the UNIQUE
          constraint doing the enforcement;
        - fields: tenant_id, project_id, workflow_run_id, execution_id, model
          id and version, provider, input tokens, output tokens, cached tokens,
          tool units, cost with currency, rate revision used, and UNPRICED flag
          when a rate was absent;
        - writing is idempotent: a retry of the same execution updates nothing
          and inserts nothing new;
        - a provider retry inside one execution adds attempts to the same row's
          accounting rather than creating a second row, so attribution stays
          one-to-one with executions.
   6. Attribute usage to tenant and workflow per sheet 05 row 36, so cost per
      workflow (sheet 17 row 10) is computable without guesswork.
   7. Emit usage.recorded.v1 through the outbox with executionId as the
      ordering key, and implement the reconciliation input: a daily aggregate
      per provider that PHASE-10 compares against the provider's own billing.
   8. Implement graceful degradation per sheet 61 row 8: on approaching a cap,
      throttle and downgrade only tasks whose class permits it — never a
      critical engineering verification class, which must fail closed instead
      (consistent with P04-04).
   9. Tests:
        a. a preflight estimate over a cap -> denied before any provider call;
           assert with a provider double that fails if called;
        b. a request in the approval band -> pending with the gate named, no
           call made;
        c. a runaway multi-step loop -> BUDGET_EXHAUSTED at the cap, with the
           step count bounded and partial artifacts recorded. This is the
           CTRL-014 evidence;
        d. retry the same execution -> exactly one ledger row, unchanged;
        e. three provider attempts within one execution -> one row whose
           accounting includes all three attempts;
        f. concurrent executions for one tenant racing the same cap -> the cap
           is not exceeded; assert with a concurrency test, because a
           read-then-write check without locking will fail here;
        g. a model with no configured rate -> tokens recorded, cost UNPRICED,
           no invented number;
        h. daily and monthly caps roll over correctly across a boundary, in UTC;
        i. approaching a cap -> a routine class is downgraded, a critical class
           fails closed rather than being downgraded;
        j. the emitted usage event conforms to the sheet 34 envelope and carries
           executionId as the ordering key.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - budget scopes and caps in tokens and currency
   - the preflight estimator with pre-dispatch denial
   - approval-threshold banding wired to ALLOW_WITH_GATE
   - the in-execution hard stop with partial artifact recording
   - the usage ledger with execution_id UNIQUE and idempotent writes
   - tenant and workflow attribution
   - usage.recorded.v1 emission and the daily reconciliation aggregate
   - class-aware degradation that never downgrades critical verification
   - tests/finops/budget-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten tests.
   - For case c, paste the loop termination showing the cap, the step count and
     the recorded partial artifacts. Retain this as the CTRL-014 evidence.
   - For case f, paste the concurrency test result and state the mechanism
     preventing the race (lock, atomic decrement, or serialized reservation).
   - For case g, paste the ledger row showing UNPRICED.
   - Acceptance criterion: no provider call happens over a cap, no execution
     produces two ledger rows, and no cost number exists without a real rate.

G. COMPLETION CONTRACT
   Definition of Done: budgets enforced before and during execution, ledger
   exactly-once under retry and concurrency, attribution complete, no invented
   rates.
   Evidence to report: the ten test outputs, the CTRL-014 loop-stop evidence,
   the concurrency mechanism, the UNPRICED row.
   Remaining blockers: provider rates are owner-owned (open decision OD-03).
   Report how many registered models currently have a real rate and how many
   are UNPRICED.
   Next prompt: P04-07.
```

**المخرجات المتوقعة:** حدود ميزانية بتقدير مُسبق، إيقاف صلب أثناء التنفيذ، دفتر استخدام مرة واحدة.
**التحقق المطلوب:** الحلقة الجارية تتوقف عند السقف؛ لا سجل استخدام مكرر؛ لا تكلفة بلا معدل حقيقي.
**الاعتمادية التالية:** `P04-07`.

---

---

### `P04-07` — مُدقِّق المخرجات

**Phase:** `PHASE-04` · **EN title:** Output validator with provenance and deterministic checks

**المتطلبات السابقة:** `P04-06`

**المتطلبات المغطاة:** `REQ-GW-10`, `REQ-GW-16`, `REQ-AGT-04`, `REQ-KNW-05`

**ماذا سينفذ هذا الأمر؟** يبني مُدقِّق مخرجات يفرض مخطط JSON، ومصدرية المصادر،
وفحوصات حسابية وهندسية حتمية، ويطلب اعتماداً بشرياً للاستنتاجات الحرجة للسلامة.

**لماذا نحتاجه؟** الورقة 70 الصف 11 تحدد هذه المسؤولية بدقة، والورقة 36 الصف 11
(`RT-06`) تضيف: «يفشل مُغلقاً عند مخرج غير صالح». والورقة 37 الصف 11 تجعل
«رفض المخرج المُشوَّه» متطلباً مُتتبَّعاً بدليل «schema test + trace».

**ما المتطلبات السابقة؟** `P04-06`.

**ما النتيجة المتوقعة؟** مُدقِّق إلزامي على كل مخرج قبل أن يصبح مستهلَكاً، مع فشل
مُغلق ومسار تصعيد بشري.

**كيف نتحقق من نجاحه؟** مخرج غير مطابق للمخطط يُرفض؛ واستشهاد بلا إصدار يُرفض؛
وحساب غير متسق يُكتشف بحاسبة حتمية لا بنموذج.

```text
TASK P04-07 — Output validator with provenance and deterministic checks

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P04-07
   Phase: PHASE-04
   Prerequisites: P04-06
   Requirements covered: REQ-GW-10, REQ-GW-16, REQ-AGT-04, REQ-KNW-05

B. OBJECTIVE
   Implement the mandatory output validator: JSON schema enforcement, source
   provenance verification, deterministic math and CAD checks, and a required
   human approval path for safety-critical conclusions — with fail-closed
   behaviour on any invalid output.

   Why this is necessary: sheet 70 row 11 specifies exactly these four
   responsibilities with the gate "eval pass-rate by class". Sheet 36 row 11
   (RT-06) requires the result envelope to be JSON-schema validated and to fail
   closed on invalid output. Sheet 37 row 11 tracks "malformed result rejected"
   as a requirement whose proof is a schema test plus a trace. Sheet 10 row 13
   requires citations to carry source, version, anchor and rights.

   SCOPE BOUNDARY: validation of model and agent output inside the gateway. The
   findings schema and the review workflow are PHASE-07. The evaluation harness
   is PHASE-14. Here you enforce structure, provenance and arithmetic.

C. CONTEXT
   Required inputs:
     - sheet 36 row 11: result envelope fields status, structuredOutput,
       artifactRefs, citations, confidence; validation "JSON schema validated";
       failure action "fail closed on invalid output"
     - sheet 10 rows 13-14: citations carry source, version, anchor and rights
       and are required when a claim is made; confidence is a calibrated score
       for the machine and is explicitly "not an approval"
     - sheet 71 quality checks per class: field accuracy and confidence for
       extraction; citation and answer grounding for routine; constraint and
       evidence checks for architectural reasoning; clause citations plus human
       sign-off for SBC compliance; unit, quantities and audit trail for BOQ;
       scan confidence plus known dimension for LiDAR; grounding and latency for
       live narration; licensed reviewer approval for safety and structural
     - sheet 63 row 2: extraction uses grounding and schema as its quality gate

D. EXECUTION INSTRUCTIONS
   1. Implement the result envelope as a strict schema and validate every
      output against it before the output becomes visible to any consumer or to
      the SSE stream. Validation failure is terminal for that attempt: the
      execution records INVALID_OUTPUT with the validation detail and the
      trace, and does not emit a partial success.
   2. Implement structured-output enforcement per task class, each with its own
      output schema loaded from configuration, so a new task class cannot run
      without a declared output contract.
   3. Implement provenance verification on citations:
        - every citation must carry source, version, anchor and a rights
          snapshot;
        - the anchor must resolve against the cited source version — an
          unresolvable anchor is an invalid citation, not a warning;
        - the rights snapshot must say ALLOWED. A citation to a source whose
          rights are UNKNOWN is rejected, enforcing ADR-009 at the output
          boundary as well as at the retrieval boundary;
        - a claim requiring a citation that has none is rejected per sheet 10
          row 13.
      This is the mechanism behind sheet 37 row 13's requirement that a
      citation include the code edition and its applicability.
   4. Implement artifact reference verification: every artifactRef resolves to
      an existing version whose digest matches, using the fail-closed resolver
      from P02-02.
   5. Implement deterministic checks, run by code and never by a model:
        - unit consistency and dimensional analysis on every numeric claim with
          a unit; a value without a unit where the schema requires one is
          invalid;
        - arithmetic re-computation: any total, sum, area or quantity the output
          asserts is recomputed from its components, and a mismatch beyond a
          declared tolerance is a validation failure;
        - range and plausibility bounds per field from configuration;
        - geometry checks for CAD and scan outputs where the task class
          declares them.
      Sheet 71 row 6 is explicit that calculators price and the model only
      extracts, so a model-asserted price or total is rejected here.
   6. Implement confidence handling per sheet 10 row 14: confidence is recorded,
      is required to be within 0..1, and is never treated as an approval or as a
      substitute for a quality check. Add a test asserting that a high
      confidence value does not bypass any validation.
   7. Implement the human approval requirement for safety-critical conclusions:
      for the safety/structural and SBC compliance classes, and for any output
      with professional consequence P3, the validator marks the output
      PENDING_HUMAN_APPROVAL and the output cannot be consumed as final. It is
      routed to the review path that PHASE-07 implements. Until that path
      exists, the state is terminal-pending, never auto-approved.
   8. Record validation results per class so PHASE-14 can compute the
      "eval pass-rate by class" gate sheet 70 row 11 names.
   9. Tests:
        a. output violating the envelope schema -> INVALID_OUTPUT with detail
           and trace, nothing emitted to the stream;
        b. a claim with no citation -> rejected;
        c. a citation missing version or anchor -> rejected;
        d. a citation whose anchor does not resolve -> rejected, naming it;
        e. a citation to a source with UNKNOWN rights -> rejected (ADR-009 at
           the output boundary);
        f. an artifactRef whose digest no longer matches -> rejected;
        g. a numeric claim missing a required unit -> rejected;
        h. a total that does not equal the sum of its components beyond
           tolerance -> rejected, showing expected versus asserted;
        i. a model-asserted price in a BOQ-class output -> rejected;
        j. confidence 0.99 on a schema-invalid output -> still rejected;
        k. a P3 output -> PENDING_HUMAN_APPROVAL, not consumable as final;
        l. validation outcomes are recorded per class and queryable.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the strict result envelope schema and mandatory pre-emission validation
   - per-class output schemas loaded from configuration
   - citation provenance verification including rights and anchor resolution
   - artifact reference digest verification
   - deterministic unit, arithmetic, range and geometry checks
   - confidence recording with no approval semantics
   - PENDING_HUMAN_APPROVAL for safety-critical and P3 outputs
   - per-class validation result recording for the PHASE-14 gate
   - tests/gateway/validator-*.* covering cases a through l
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all twelve tests.
   - For case h, paste the expected-versus-asserted arithmetic comparison.
   - For case e, paste the rejection and the rights snapshot that caused it.
   - For case a, confirm from the SSE transcript that nothing was emitted
     before validation completed.
   - Acceptance criterion: no invalid, unprovenanced or arithmetically
     inconsistent output can reach a consumer, and no confidence value can
     bypass validation.

G. COMPLETION CONTRACT
   Definition of Done: mandatory validation with fail-closed semantics,
   provenance and rights enforced at the output boundary, deterministic checks
   catching arithmetic and unit errors, P3 held pending human approval.
   Evidence to report: the twelve test outputs, the arithmetic comparison, the
   rights rejection, the stream-ordering confirmation.
   Remaining blockers: the human approval path completes in PHASE-07; until
   then PENDING_HUMAN_APPROVAL is terminal. Confirm it is never auto-cleared.
   Next prompt: P05-01. PHASE-04 exit requires the chaos suite green, the
   budget loop-stop evidence retained, exactly-once ledger proven, and the
   no-provider-bypass guard green.
```

**المخرجات المتوقعة:** مُدقِّق إلزامي، تحقق مصدرية واستشهادات، فحوصات حتمية، حالة انتظار اعتماد بشري.
**التحقق المطلوب:** لا مخرج غير صالح أو بلا مصدرية يصل مستهلكاً؛ الثقة لا تتجاوز التحقق.
**الاعتمادية التالية:** `P05-01`.


---

# PHASE-05 — تشغيل الوكلاء والسجل والإصدارات


## الغرض من المرحلة

المصدر يحسم طبيعة الوكلاء في الورقة 00 الصف 20: «الوكلاء قدرات تنفذ خطوات داخل
القالب، وليسوا فريقاً حراً يؤلف مساراً جديداً لكل طلب». وفي الورقة 57 الصف 4
ملاحظة حرجة: «قدرات السجل ليست مكافئة لإصدارات وكلاء قابلة للنشر» — أي أن وجود
44 قدرة في جدول لا يعني وجود 44 وكيلاً جاهزاً.

لذلك هذه المرحلة تبني عقد التشغيل العشاري في الورقة 36، ودورة حياة الإصدارات في
الورقة 62، وحدود الأدوات ودفاعات الحقن.

## شروط الدخول

- اكتمال `PHASE-04`: البوابة تفرض السياسة والتوجيه والميزانية والتحقق.

## شروط الخروج

- أداة غير مُسجَّلة تُحجَب عند الإرسال.
- مغلف نتيجة مُشوَّه يفشل مُغلقاً.
- إصدارات وكلاء غير قابلة للتعديل مع canary ورجوع مُثبت.
- اختبار عزل حزمة السياق ناجح.

## المتطلبات المغطاة في هذه المرحلة

`ADR-005`, `REQ-AGT-01`..`REQ-AGT-08`, `REQ-SEC-05`, `REQ-DAT-04`, `REQ-API-05`

## تحذير مهم

الورقة 62 الصف 2 تقول صراحة: «لا أدوات عشوائية ديناميكية» (No dynamic arbitrary
tools). وأي قدرة في الورقة 05 لها عمود «شروط الإيقاف» — وهذه الشروط ليست
توصيات، بل هي نقاط توقف إلزامية.

---

## الأوامر التنفيذية

---

### `P05-01` — عقد تشغيل الوكيل بمجالاته العشرة

**Phase:** `PHASE-05` · **EN title:** Agent runtime contract RT-01..RT-10

**المتطلبات السابقة:** `P04-07`

**المتطلبات المغطاة:** `REQ-AGT-01`, `REQ-AGT-02`, `REQ-AGT-04`, `REQ-AGT-05`, `REQ-DAT-04`

**ماذا سينفذ هذا الأمر؟** ينفّذ عقد تشغيل الوكلاء في الورقة 36: هوية التنفيذ،
تعريف الوكيل، حزمة السياق، توجيه النموذج، ضوابط التنفيذ، مغلف النتيجة، الأدلة
والتدقيق، دفتر الاستخدام، تصعيد HITL، وتصنيف الفشل — كل مجال بثابته وبإجراء فشله.

**لماذا نحتاجه؟** الورقة 36 الصف 3 تصف نفسها بأنها «مواصفة تصميم لا مُتحقَّقاً
منها في التشغيل»، وتشترط أن «كل تنفيذ يجب أن يكون قابلاً للإسناد والإعادة
ومحدوداً بالسياسة». هذه الثلاثة تحتاج بنية لا نوايا.

**ما المتطلبات السابقة؟** `P04-07`.

**ما النتيجة المتوقعة؟** عقد تنفيذ مُنفَّذ بعشرة مجالات، كل منها بثابت مفروض
واختبار لإجراء الفشل.

**كيف نتحقق من نجاحه؟** لكل صف من `RT-01` إلى `RT-10` اختبار يُفعّل إجراء الفشل
المذكور في المصدر.

```text
TASK P05-01 — Agent runtime contract RT-01..RT-10

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-01
   Phase: PHASE-05 (Agent runtime, registry and versioning)
   Prerequisites: P04-07
   Requirements covered: REQ-AGT-01, REQ-AGT-02, REQ-AGT-04, REQ-AGT-05,
                         REQ-DAT-04

B. OBJECTIVE
   Implement the ten agent runtime contract areas with their fields,
   invariants and failure actions exactly as the source specifies, so every
   execution is attributable, reproducible and policy-constrained.

   Why this is necessary: sheet 36 row 3 states the contract's purpose in those
   three words and declares itself a design specification that is not
   runtime-verified. This prompt is what makes it verified. Each row names a
   failure action, and a failure action that is not implemented is not a
   contract.

   SCOPE BOUNDARY: the execution contract and its enforcement. The agent
   catalogue and versioning lifecycle are P05-02. Tool safety hardening is
   P05-03. The individual 44 capabilities are not implemented here — PHASE-09
   and PHASE-15 implement them behind this contract.

C. CONTEXT
   Required inputs, sheet 36 rows 6-15, each as area / fields / invariant /
   failure action:
     RT-01 Execution identity — executionId, tenantId, projectId,
       workflowRunId, stepId / required UUIDs, tenant-scoped / reject before
       dispatch
     RT-02 Agent definition — agentId, registryVersion, capabilities,
       toolAllowlist / pinned immutable version / block unregistered tools
     RT-03 Context package — projectSnapshot, evidenceRefs, knowledgeRefs,
       policyVersion / least privilege, signed refs / never mix projects or
       tenants
     RT-04 Model routing — capability, classification, budget, maxLatency,
       fallbackChain / no model bypass of policy / escalate on uncertainty
     RT-05 Execution controls — timeout, retryPolicy, idempotencyKey,
       sideEffectClass / retry only safe operations / manual gate for
       irreversible effects
     RT-06 Result envelope — status, structuredOutput, artifactRefs, citations,
       confidence / JSON schema validated / fail closed on invalid output
     RT-07 Evidence and audit — traceId, promptVersion, toolCalls,
       reviewDecision / redact secrets, immutable trace / audit every action
     RT-08 Usage ledger — inputTokens, outputTokens, cost, provider,
       executionId / persist exactly once per execution / reconcile with
       credits
     RT-09 HITL escalation — reason, reviewerRole, deadline, decision /
       qualified reviewer, explicit decision / no self-approval
     RT-10 Failure taxonomy — errorCode, retryable, providerFailure,
       partialArtifacts / circuit breaker plus dead-letter queue / no silent
       success
   Also required: config/registries/data-constraints.json, agent_executions:
   UNIQUE (run_id, step_id, attempt); invariant "trace/model lineage";
   retention "redact prompts".
   Already built and to be reused, not reimplemented: the validator (P04-07)
   satisfies RT-06; the ledger (P04-06) satisfies RT-08; the circuit breaker
   (P04-04) is half of RT-10; the policy service (P01-04) backs RT-04.

D. EXECUTION INSTRUCTIONS
   1. Implement the execution identity record with all five RT-01 fields as
      required, tenant-scoped UUIDs. A dispatch missing any of them is rejected
      before anything runs — not logged and continued.
   2. Implement agent_executions per the data constraint, with UNIQUE
      (run_id, step_id, attempt) so attempts are distinguishable and
      countable, and with prompt redaction at rest per the retention rule.
   3. Implement the context package builder (RT-03) on top of P04-05, adding:
        - least privilege: the package contains only what the step's declared
          inputs require, and the builder refuses a request for a broader
          scope;
        - signed references: evidenceRefs and knowledgeRefs are
          integrity-checked at use time;
        - the hard invariant "never mix projects or tenants": the package is
          constructed for exactly one (tenant, project) pair and a second pair
          cannot be added. Enforce structurally and test it.
   4. Implement RT-04's invariant: a step cannot select a model outside the
      policy decision. There is no parameter by which a caller can name a model
      directly and bypass P04-03. Add a test asserting a caller-supplied model
      id is ignored or rejected. "Escalate on uncertainty" means that when the
      router returns NO_ELIGIBLE_ROUTE the step escalates to HITL rather than
      proceeding.
   5. Implement RT-05's side-effect classes and gating, reusing P03-02's
      classes. An IRREVERSIBLE step requires a recorded manual gate before
      execution and is never retried automatically.
   6. Implement RT-07: a trace id links the whole execution; promptVersion and
      every tool call are recorded; the trace is immutable and secret-redacted;
      every action produces an audit record in the P01-05 store.
   7. Implement RT-09 HITL escalation with its four fields and its two
      invariants: the escalation names a qualified reviewer role and requires
      an explicit decision, and self-approval is impossible — the actor who
      produced the output cannot be the actor who approves it. Enforce the
      self-approval prohibition here as well as in PHASE-07, because the
      runtime must not be able to request it.
   8. Implement RT-10's taxonomy completely, with the explicit rule "no silent
      success": an execution that produced partial artifacts and then failed
      reports FAILED with the partial artifacts referenced, never a success
      status with missing output. Add the dead-letter path for executions that
      cannot be completed.
   9. Implement reproducibility: given the same execution identity, agent
      version, context package digest, policy version and model version, the
      execution is replayable and its inputs are reconstructable from the
      trace. Provide a replay command that reconstructs and re-runs an
      execution for debugging, clearly marked as producing a new execution id.
  10. Tests — one per contract area, driving the source's failure action:
        a. RT-01: dispatch missing projectId -> rejected before dispatch, no
           provider call;
        b. RT-02: a step requesting a tool outside the allowlist -> blocked;
        c. RT-03: attempt to add a second project's evidence to a package ->
           impossible or rejected; attempt a broader scope than declared ->
           refused;
        d. RT-04: caller supplies a model id -> ignored or rejected;
           NO_ELIGIBLE_ROUTE -> escalates to HITL, does not proceed;
        e. RT-05: an IRREVERSIBLE step without a manual gate -> does not run;
           it is never auto-retried;
        f. RT-06: invalid envelope -> fails closed (reuse the P04-07 suite);
        g. RT-07: a forced failure -> the trace exists, contains no secret, and
           cannot be mutated;
        h. RT-08: exactly-once ledger (reuse the P04-06 suite);
        i. RT-09: the producing actor attempts to approve -> refused;
        j. RT-10: partial-then-failed execution -> FAILED with partial
           artifacts, never success; an uncompletable execution reaches the
           DLQ.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the execution identity record with required-field rejection
   - agent_executions with its uniqueness constraint and prompt redaction
   - the least-privilege, single-tenant-single-project context package builder
   - policy-bound model selection with no caller override
   - side-effect class gating for irreversible steps
   - immutable, redacted traces with full tool-call recording
   - HITL escalation with enforced no-self-approval
   - the complete failure taxonomy with no-silent-success and a DLQ path
   - the replay command
   - tests/agent/rt-*.* with one test per contract area
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten contract-area tests.
   - State the mapping of RT-01..RT-10 to the test that proves each failure
     action. All ten must be covered.
   - For case c, show that mixing tenants is structurally impossible rather
     than merely checked.
   - For case j, paste the FAILED-with-partials record.
   - Acceptance criterion: every one of the ten failure actions in sheet 36 is
     exercised by a passing test.

G. COMPLETION CONTRACT
   Definition of Done: all ten contract areas enforced, each failure action
   tested, executions attributable, reproducible and policy-constrained.
   Evidence to report: the ten test outputs, the RT-to-test mapping table, the
   structural isolation demonstration.
   Remaining blockers: none expected. If a contract area depends on a later
   phase (RT-09's reviewer registry is PHASE-07), enforce the runtime half now
   and name the completing prompt.
   Next prompt: P05-02.
```

**المخرجات المتوقعة:** عقد تنفيذ بعشرة مجالات مفروضة، تتبّع غير قابل للتعديل، مسار DLQ.
**التحقق المطلوب:** كل إجراء فشل في الورقة 36 مُفعَّل باختبار ناجح.
**الاعتمادية التالية:** `P05-02`.

---

---

### `P05-02` — سجل الوكلاء ودورة حياة الإصدارات

**Phase:** `PHASE-05` · **EN title:** Agent registry, versioning lifecycle, canary and rollback

**المتطلبات السابقة:** `P05-01`

**المتطلبات المغطاة:** `REQ-AGT-03`, `REQ-AGT-06`, `REQ-AGT-07`, `REQ-AGT-08`

**ماذا سينفذ هذا الأمر؟** يبني الكيانات الخمسة في الورقة 62
(`AgentDefinition`, `AgentVersion`, `AgentDeployment`, `AgentRun`,
`AgentOutput`) مع بوابة إصدار وقاعدة رجوع لكل منها.

**لماذا نحتاجه؟** الورقة 57 الصف 4 تحدد الفجوة بدقة: السجل ليس إصدارات قابلة
للنشر، والأثر «إصدارات غير مُتحكَّم بها»، والدليل المطلوب «إثبات رجوع». والورقة 58
الصف 4 تجعل تفعيل أو تعطيل إصدار وكيل في الإنتاج يحتاج «موافقة مزدوجة» و«canary +
rollback».

**ما المتطلبات السابقة؟** `P05-01`.

**ما النتيجة المتوقعة؟** سجل وكلاء بإصدارات غير قابلة للتعديل، ونشر تدريجي،
ورجوع مُثبت.

**كيف نتحقق من نجاحه؟** نشر إصدار ثم الرجوع عنه يُنتج دليلاً مُسجَّلاً؛ وتعديل
إصدار منشور مستحيل.

```text
TASK P05-02 — Agent registry, versioning lifecycle, canary and rollback

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-02
   Phase: PHASE-05
   Prerequisites: P05-01
   Requirements covered: REQ-AGT-03, REQ-AGT-06, REQ-AGT-07, REQ-AGT-08

B. OBJECTIVE
   Implement the five agent lifecycle objects with their mandatory fields,
   release gates and rollback rules, so a capability in a table becomes a
   deployable, versioned, reversible artifact.

   Why this is necessary: sheet 57 row 4 names the gap precisely — registry
   capabilities are not equivalent to deployable agent versions, the impact is
   uncontrolled releases, and the required acceptance evidence is rollback
   proof. Sheet 58 row 4 requires dual approval plus canary and rollback to
   enable or disable an agent version in production. Sheet 62 row 2 forbids
   dynamic arbitrary tools.

   SCOPE BOUNDARY: the registry, versioning, deployment and rollback. The
   tool-safety controls are P05-03. The evaluation suites that gate releases
   are PHASE-14 — here you build the gate and the hook, and an unpopulated
   eval suite must block, not pass.

C. CONTEXT
   Required inputs, sheet 62 rows 2-6, each as object / mandatory fields /
   release gate / rollback / notes:
     AgentDefinition — agent_id, capability, domain, input_schema,
       output_schema / owner approved / keep prior version / no dynamic
       arbitrary tools
     AgentVersion — version, prompt_hash, tools, model_policy, eval_suite /
       golden-set pass / pin previous version / immutable
     AgentDeployment — environment, traffic percentage, concurrency, budget /
       canary and shadow / traffic switch / per-project visibility
     AgentRun — execution_id, tenant_id, project_id, task_id, evidence_refs /
       idempotent task / compensate only / audit immutable
     AgentOutput — schema_version, provenance, confidence, citations,
       reviewer_state / validation plus policy / re-run as new version / no
       unsupported engineering signoff
   Also: config/registries/agent-capabilities.json and pmo-capabilities.json
   from P00-02 (the 44 plus 8 capability definitions, each with R, P, human
   gate, stop conditions, workflows, KPIs and owner).

D. EXECUTION INSTRUCTIONS
   1. Implement AgentDefinition with its five mandatory fields. input_schema
      and output_schema are required and validated — a definition without them
      cannot be created. The owner-approved gate means a definition is DRAFT
      until a recorded owner approval exists.
   2. Implement AgentVersion as immutable after publication, with prompt_hash
      computed over the canonical prompt template, the explicit tool list, the
      model policy reference and the eval_suite reference. Enforce immutability
      at the database level as in P03-01.
   3. Implement the golden-set release gate: publishing an AgentVersion
      requires a passing evaluation run reference for its eval_suite. If no
      evaluation exists, publication is BLOCKED. Do not provide an override
      that silently bypasses the gate; if a break-glass path is required, it
      needs dual approval, an expiry and its own audit stream, consistent with
      P01-03.
   4. Implement AgentDeployment with environment, traffic percentage,
      concurrency limit and budget, including shadow mode (the version runs and
      is scored but its output is not consumed) and canary mode (a traffic
      share consumes it). Per-project visibility means a deployment can be
      scoped to named projects.
   5. Implement dual approval for production deployment changes per sheet 58
      row 4: two distinct approver identities, neither of whom is the author.
      Enforce distinctness; a single person holding two roles cannot satisfy it.
   6. Implement rollback as a first-class operation: a traffic switch back to
      the pinned previous version that takes effect without a deploy, records
      who, when and why, and emits an event. The previous version is always
      retained per the AgentDefinition rollback rule.
   7. Implement AgentRun per the source: idempotent task, compensate-only (no
      destructive undo), immutable audit. Reuse P03-03's idempotency and
      P01-05's audit store.
   8. Implement AgentOutput with schema_version, provenance, confidence,
      citations and reviewer_state, and enforce the note "no unsupported
      engineering signoff": an output cannot carry an approved reviewer_state
      unless a real review decision from PHASE-07 exists. Until PHASE-07,
      reviewer_state can only be NONE or PENDING.
   9. Map the capability registers to definitions: generate or validate an
      AgentDefinition per capability in agent-capabilities.json, carrying that
      capability's R rating, P rating, human gate and stop conditions as
      definition metadata. Record clearly which definitions have a published,
      eval-passing version (expected: none at this stage) and which are
      definition-only. This is the explicit correction of the sheet 57 row 4
      gap, and the honest answer at the end of this prompt is that 52
      capabilities are defined and few or none are deployable.
  10. Implement stop conditions as enforced preconditions: each capability's
      stop conditions from the register become machine-checkable guards that
      halt the step with a named reason. Where a stop condition cannot be
      expressed mechanically, record it as a required human gate instead of
      discarding it.
  11. Tests:
        a. create a definition without an output schema -> rejected;
        b. publish a version with no passing evaluation -> BLOCKED, naming the
           missing eval;
        c. edit a published version -> rejected at the database level;
        d. production deployment with one approver -> rejected; with two
           distinct non-author approvers -> accepted;
        e. canary at a configured share -> traffic distribution within
           tolerance; shadow mode -> output scored but not consumed, proven by
           asserting no consumer received it;
        f. rollback -> previous version serving within the switch window,
           recorded with actor and reason, event emitted. Retain this as the
           sheet 57 row 4 rollback proof;
        g. an output claiming an approved reviewer_state with no review
           decision -> rejected;
        h. a capability whose stop condition is triggered -> step halts with
           the named reason;
        i. a step requesting a tool not in its version's tool list -> blocked
           (reinforcing RT-02).
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the five lifecycle objects with mandatory fields and migrations
   - immutable published versions with prompt_hash
   - the golden-set publication gate that blocks without evaluation evidence
   - deployments with canary, shadow, concurrency and budget
   - dual approval with enforced approver distinctness
   - rollback as a recorded, deploy-free traffic switch
   - capability-to-definition mapping with an honest deployability report
   - stop conditions as enforced guards or recorded human gates
   - tests/agent/registry-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - Paste the rollback evidence from case f — this is a named acceptance
     requirement in sheet 57 row 4.
   - Report the deployability table: total capabilities defined, versions
     created, versions with a passing evaluation, versions deployed. State the
     real numbers even when they are zero.
   - Acceptance criterion: no version publishes without evaluation evidence, no
     published version is mutable, and rollback is demonstrated end to end.

G. COMPLETION CONTRACT
   Definition of Done: five objects implemented, publication gated on
   evaluation, dual approval and rollback proven, capabilities mapped with an
   honest deployability count.
   Evidence to report: the nine test outputs, the rollback proof, the
   deployability table.
   Remaining blockers: evaluation suites and golden sets arrive in PHASE-14, so
   the number of publishable versions is expected to be zero or near zero now.
   Report that as correct behaviour rather than working around the gate.
   Next prompt: P05-03.
```

**المخرجات المتوقعة:** خمسة كيانات دورة حياة، بوابة تقييم، canary وshadow، رجوع مُثبت.
**التحقق المطلوب:** لا نشر بلا دليل تقييم؛ لا تعديل لإصدار منشور؛ رجوع مُثبت من طرف إلى طرف.
**الاعتمادية التالية:** `P05-03`.

---

---

### `P05-03` — حدود الأدوات ومنع الحقن والتسريب

**Phase:** `PHASE-05` · **EN title:** Tool boundary, injection defence and egress control

**المتطلبات السابقة:** `P05-02`

**المتطلبات المغطاة:** `REQ-SEC-05`, `REQ-SEC-06`, `REQ-AGT-03`, `REQ-AGT-02`

**ماذا سينفذ هذا الأمر؟** يبني حدود الأدوات: قائمة سماح، أقل صلاحية، تسميات ثقة
للمدخلات، منع خروج غير مصرح به، ودفاعات ضد حقن المطالبات.

**لماذا نحتاجه؟** الورقة 27 الصف 8 (`SEC-07`) بأولوية `CRITICAL` ودليلها
«اختبارات خصومية». والورقة 57 الصف 10 (`A09`) تحدد الأثر: «تسريب بيانات»،
والتنفيذ المطلوب: «tool allowlist, egress policy, input trust labels»، والدليل:
«red-team suite». ملف العميل مُدخَل غير موثوق بطبيعته، وسيصل إلى نموذج له أدوات.

**ما المتطلبات السابقة؟** `P05-02`.

**ما النتيجة المتوقعة؟** طبقة أدوات مُقيَّدة بقائمة سماح لكل إصدار وكيل، وتسميات
ثقة مُنفَّذة، ومنع خروج مفروض.

**كيف نتحقق من نجاحه؟** محاولة استخراج سر عبر تعليمات مزروعة في ملف عميل تفشل
وتُسجَّل؛ ونداء خروج غير مُدرج يُحجَب.

```text
TASK P05-03 — Tool boundary, injection defence and egress control

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-03
   Phase: PHASE-05
   Prerequisites: P05-02
   Requirements covered: REQ-SEC-05, REQ-SEC-06, REQ-AGT-02, REQ-AGT-03

B. OBJECTIVE
   Implement the tool execution boundary: a per-agent-version tool allowlist,
   least-privilege tool credentials, input trust labels, enforced egress
   control, and defences against prompt injection and tool-based exfiltration.

   Why this is necessary: sheet 27 row 8 (SEC-07) is CRITICAL with required
   evidence of adversarial tests. Sheet 57 row 10 (A09) names the impact as
   data leakage, the required implementation as tool allowlist plus egress
   policy plus input trust labels, and the acceptance evidence as a red-team
   suite. A customer drawing is untrusted input by construction, and it will
   reach a model that holds tools.

   SCOPE BOUNDARY: the tool boundary and its adversarial tests. The full
   red-team programme and its reporting are PHASE-11; this prompt builds the
   controls and a first adversarial suite that PHASE-11 extends.

C. CONTEXT
   Required inputs:
     - the AgentVersion tool list from P05-02 and RT-02 from P05-01
     - the network egress allowlist from P04-04 step 4
     - sheet 36 row 7: block unregistered tools
     - sheet 62 row 2: no dynamic arbitrary tools
     - sheet 45 row 7 and sheet 05 agent rows: each capability names a human
       gate
   Threat model note: the attacker's input arrives as document content,
   filenames, metadata, OCR text, EXIF fields, IFC property values and
   retrieved knowledge passages. All of these are untrusted. Instructions found
   inside them are data, never commands.

D. EXECUTION INSTRUCTIONS
   1. Implement the tool registry: every tool has an id, a version, a typed
      input and output schema, a declared side-effect class, a declared egress
      requirement and an owner. A tool not in the registry cannot be invoked by
      any path. Tool construction from a model-produced name is prohibited —
      resolution happens only against the registry.
   2. Enforce the per-version allowlist: the set of callable tools for a step
      is the intersection of the agent version's declared tool list and the
      policy decision's permitted tools. An invocation outside that set is
      blocked and recorded as a security event, not merely refused.
   3. Implement least-privilege tool credentials: each tool receives a
      credential scoped to the current tenant, project and operation, minted at
      invocation time with a short lifetime. A tool never receives a broad or
      long-lived credential, and never receives the provider credentials.
   4. Implement input trust labels: every element entering a context package
      carries a trust label (SYSTEM, OPERATOR, TENANT_CONFIG,
      UNTRUSTED_DOCUMENT, UNTRUSTED_RETRIEVAL, UNTRUSTED_EXTERNAL). The label
      travels with the element. Rules:
        - no instruction from an UNTRUSTED_* element may change the step's tool
          set, its policy decision, its budget, its destination or its output
          schema;
        - a tool invocation whose arguments derive from an UNTRUSTED_* element
          is checked against the tool's schema and its argument allowlist, and
          free-form passthrough of untrusted text into a tool argument that
          controls a destination (a URL, a path, a recipient, a query target)
          is prohibited;
        - the system prompt and the untrusted content are structurally
          separated in the request to the provider, and the model is instructed
          that document content is data.
   5. Enforce egress control at the tool layer in addition to the network
      layer: a tool that performs a network call declares its permitted
      destinations, and a destination derived from untrusted content is
      rejected. This blocks the classic exfiltration path where injected text
      supplies a callback URL.
   6. Implement output-side leak prevention: scan tool results and model output
      for credential-shaped strings and for content belonging to another
      tenant's namespace before they enter the context or the stream. A hit is
      an incident, not a redaction-and-continue.
   7. Implement the human gate for tool calls where the capability register
      demands it, and for any tool whose side-effect class is IRREVERSIBLE,
      reusing P03-02's gating.
   8. Build the first adversarial suite. These tests use planted hostile
      content inside otherwise normal fixtures:
        a. a PDF whose text instructs the agent to reveal its system prompt ->
           no system prompt in output, event recorded;
        b. a PDF instructing the agent to call a tool not in its allowlist ->
           blocked, event recorded;
        c. a PDF supplying an external URL and instructing an upload -> egress
           refused at both the tool and network layers;
        d. an IFC property value containing an injection payload -> treated as
           data, no behaviour change;
        e. a retrieved knowledge passage containing an injection payload ->
           treated as data;
        f. a filename and EXIF field containing injection payloads -> treated
           as data;
        g. an attempt to widen the tool set at runtime through a model-produced
           tool name -> resolution fails against the registry;
        h. a tool argument built from untrusted text that names a path outside
           the tenant prefix -> rejected;
        i. a tool result containing a credential-shaped string -> flagged as an
           incident and not propagated;
        j. a tool result containing another tenant's identifier -> flagged as
           an incident.
      Every one of these assertions must be able to fail: demonstrate at least
      three by temporarily weakening the control.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the tool registry with typed schemas and declared egress
   - per-version allowlist intersection enforcement with security events
   - short-lived, narrowly scoped tool credentials
   - the input trust label system with its four prohibition rules
   - tool-layer egress destination control
   - output-side credential and cross-tenant leak detection
   - human gating for declared and irreversible tool calls
   - tests/security/red-team-agents.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all ten adversarial tests.
   - For at least three cases, paste the weakened-control run showing the test
     failing, then the restored run showing it passing.
   - Paste the security events generated by cases a, b and c.
   - Acceptance criterion: no planted instruction in untrusted content changes
     tool set, destination, budget or schema; every attempt is recorded.

G. COMPLETION CONTRACT
   Definition of Done: tool boundary enforced, trust labels implemented with
   their prohibitions, egress controlled at two layers, adversarial suite
   passing and proven able to fail.
   Evidence to report: the ten test outputs, the three weakened-control
   demonstrations, the security event records.
   Remaining blockers: this is a first suite, not a complete programme.
   PHASE-11 extends it; say so rather than implying completeness.
   Next prompt: P05-04.
```

**المخرجات المتوقعة:** سجل أدوات، قائمة سماح لكل إصدار، تسميات ثقة، تحكم خروج بطبقتين.
**التحقق المطلوب:** عشر حالات خصومية ناجحة، وثلاث منها مُثبت قدرتها على الفشل.
**الاعتمادية التالية:** `P05-04`.

---

---

### `P05-04` — محرك R/P والبوابات البشرية

**Phase:** `PHASE-05` · **EN title:** Two-axis risk engine and human gates

**المتطلبات السابقة:** `P05-03`

**المتطلبات المغطاة:** `ADR-005`, `REQ-AGT-08`, `REQ-AGT-09`, `REQ-SVC-02`

**ماذا سينفذ هذا الأمر؟** ينفّذ `ADR-005`: محور `Action Risk R0-R4` منفصلاً عن
محور `Professional Consequence P0-P3`، ويربط كل مستوى ببوابته البشرية.

**لماذا نحتاجه؟** `ADR-005` ضابط قبوله: «P3 لمتخصص؛ R4 بتفويض». والورقة 35 الصف 6
تضع الحارس الأشد: «لا اعتماد مُرخَّص من الذكاء الاصطناعي». وبدون محرك يفرض هذين
المحورين بشكل منفصل، ستختلط صلاحية الفعل بأثر الخطأ، وهو بالضبط ما يحذّر منه
المصدر.

**ما المتطلبات السابقة؟** `P05-03`.

**ما النتيجة المتوقعة؟** محرك مخاطر بمحورين مستقلين، وبوابات بشرية إلزامية لكل
قدرة بحسب تصنيفها في الورقة 05.

**كيف نتحقق من نجاحه؟** قدرة `P3` لا تُنتج مخرجاً نهائياً بلا متخصص؛ وفعل `R4`
لا يُنفَّذ بلا تفويض مُسجَّل.

```text
TASK P05-04 — Two-axis risk engine and human gates

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P05-04
   Phase: PHASE-05
   Prerequisites: P05-03
   Requirements covered: ADR-005, REQ-AGT-08, REQ-AGT-09, REQ-SVC-02

B. OBJECTIVE
   Implement the two independent risk axes and the human gates they imply:
   Action Risk R0-R4 governing authority to act, and Professional Consequence
   P0-P3 governing the impact of an error, with the source's acceptance control
   enforced — P3 requires a specialist and R4 requires delegated authority.

   Why this is necessary: ADR-005 (sheet 02 row 6) exists precisely to stop the
   two being conflated, and its stated reason is to separate authority to act
   from the consequence of error. Sheet 35 row 6 sets the absolute guardrail:
   no licensed approval by AI. Every one of the 52 capability rows in sheets 05
   and 06 carries an R value, a P value and a named human gate, so the engine
   is what makes those columns operative.

   SCOPE BOUNDARY: the risk engine, gate resolution and enforcement at the
   runtime boundary. Reviewer eligibility matching, assignment and signature
   are PHASE-07. Here, a required specialist gate is resolved to a role and
   held pending; PHASE-07 fills it with a real qualified person.

C. CONTEXT
   Required inputs:
     - config/registries/agent-capabilities.json and pmo-capabilities.json:
       every capability's action_risk, professional_consequence,
       human_gate_ar and stop_conditions_ar
     - ADR-005 acceptance control: "P3 requires a specialist; R4 requires
       delegation"
     - sheet 05 examples showing the axes are genuinely independent: DOC-01 is
       R4/P3; FIN-02 is R4/P2; GOV-01 is R3/P3; DAT-01 is R1/P2; CTL-01 is
       R1/P1
     - sheet 35 row 6 guardrail: no licensed approval by AI

D. EXECUTION INSTRUCTIONS
   1. Implement the two axes as separate, non-collapsible values on every step
      and every output. Reject any code that derives one from the other or
      combines them into a single score. The independence is the whole point of
      the ADR.
   2. Define, in configuration, the gate policy per axis level:
        - Action Risk: R0 and R1 proceed; R2 requires a named approver role;
          R3 requires an approver plus a recorded rationale; R4 requires a
          recorded delegation of authority naming the delegator, the delegate,
          the scope and the expiry.
        - Professional Consequence: P0 and P1 need no specialist; P2 requires a
          qualified reviewer in scope; P3 requires a qualified specialist in
          the matching discipline, and, where the capability register says so,
          a second review.
      Implement both ladders independently, and resolve a step's requirement as
      the union of both — the stricter requirement on each axis applies, and
      satisfying one axis never satisfies the other.
   3. Implement R4 delegation as a real, auditable object: delegator identity,
      delegate identity, scope, validity window, and a revocation path. An R4
      action without an active, in-scope delegation does not execute.
   4. Implement the P3 specialist requirement as a blocking gate that resolves
      to a discipline-specific role and holds the output in the
      PENDING_HUMAN_APPROVAL state from P04-07. No automatic clearance, no
      timeout-based approval, no default approve.
   5. Implement the absolute guardrail of sheet 35 row 6 as an enforced
      invariant: no system actor other than a qualified human reviewer can set
      an output to an approved or certified state. Add a test that attempts it
      as the highest-privileged service identity and asserts refusal. This is
      the same prohibition sheet 04 row 2 places on PLATFORM_OWNER.
   6. Implement the human gates named in the capability register as resolved
      role requirements, so each capability's gate column becomes a machine
      requirement rather than prose. Where the register's gate names a
      function (for example Quality Lead, QS or Cost Manager, HSE Officer, BIM
      Coordinator), map it to a role in the RBAC register and fail loudly on an
      unmapped gate rather than defaulting to no gate.
   7. Implement the second-review trigger: where a capability or the
      eligibility matrix requires a second review (sheet 12 names triggers per
      code, such as every P3 for fire review), the engine requires two distinct
      qualified reviewers and records both.
   8. Make the risk classification visible on outputs and in the trace, so a
      downstream consumer cannot treat a P3 output as routine.
   9. Tests:
        a. an R4 step with no delegation -> does not execute, reason recorded;
        b. an R4 step with an expired or out-of-scope delegation -> does not
           execute;
        c. an R4/P1 step with a valid delegation -> executes, and no specialist
           gate is demanded (proving axis independence in one direction);
        d. an R1/P3 step -> executes but its output is held
           PENDING_HUMAN_APPROVAL for a specialist (proving independence in the
           other direction);
        e. a service identity, including the highest-privileged one, attempts
           to approve a P3 output -> refused;
        f. a capability whose human gate is unmapped -> the step fails loudly
           at configuration load, not silently at runtime;
        g. a P3 capability with a second-review trigger -> two distinct
           reviewers required, one is insufficient;
        h. an attempt to store a single combined risk score -> rejected;
        i. the risk classification appears on the output and in the trace.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the two independent axes with a type-level prohibition on collapsing them
   - the two gate ladders in configuration, resolved as a union
   - R4 delegation objects with scope, expiry and revocation
   - P3 specialist gating with no automatic clearance
   - the no-AI-approval invariant enforced against all service identities
   - capability human gates mapped to RBAC roles with loud failure on gaps
   - the second-review trigger
   - risk classification surfaced on outputs and traces
   - tests/agent/risk-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - For cases c and d, state explicitly how they prove the axes are
     independent.
   - For case e, paste the refusal with the identity that attempted it.
   - Report how many of the 52 capabilities have a gate that maps cleanly to an
     RBAC role and how many do not. An unmapped gate is a real finding to
     report, not a gap to paper over.
   - Acceptance criterion: no R4 action without delegation, no P3 output
     approved by any non-human, and the axes provably independent.

G. COMPLETION CONTRACT
   Definition of Done: both axes enforced independently, delegation and
   specialist gating working, the no-AI-approval invariant proven, gates mapped.
   Evidence to report: the nine test outputs, the independence argument, the
   gate mapping coverage count.
   Remaining blockers: real qualified reviewers do not exist until PHASE-07, so
   every P3 output is expected to sit PENDING_HUMAN_APPROVAL. Confirm nothing
   auto-clears it.
   Next prompt: P06-01. PHASE-05 exit requires the RT suite green, rollback
   proven, the adversarial suite green, and the no-AI-approval invariant proven.
```

**المخرجات المتوقعة:** محرك مخاطر بمحورين مستقلين، تفويضات R4، بوابات P3، حارس «لا اعتماد من الذكاء».
**التحقق المطلوب:** استقلال المحورين مُثبت؛ لا هوية خدمة تستطيع اعتماد مخرج P3.
**الاعتمادية التالية:** `P06-01`.


---

# PHASE-06 — المعرفة وحقوق المصادر وRAG


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

---

### `P06-01` — بوابة حقوق المصادر

**Phase:** `PHASE-06` · **EN title:** Source rights gate

**المتطلبات السابقة:** `P02-03`

**المتطلبات المغطاة:** `ADR-009`, `REQ-KNW-02`, `REQ-KNW-03`

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

---

### `P06-02` — المجموعات العشر والعزل والاستيعاب

**Phase:** `PHASE-06` · **EN title:** The ten RAG collections, isolation and ingestion

**المتطلبات السابقة:** `P06-01`

**المتطلبات المغطاة:** `REQ-KNW-01`, `REQ-KNW-04`, `REQ-GW-07`

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

---

### `P06-03` — الاستشهاد المُتحقَّق وقواعد الامتثال

**Phase:** `PHASE-06` · **EN title:** Verified citations and the compliance rules layer

**المتطلبات السابقة:** `P06-02`

**المتطلبات المغطاة:** `REQ-KNW-05`, `REQ-KNW-06`, `REQ-GW-14`, `REQ-INT-02`

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


---

# PHASE-07 — الملاحظات والمراجعة والأهلية والتسليم


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

---

### `P07-01` — مخطط الملاحظات المُنمَّط

**Phase:** `PHASE-07` · **EN title:** Typed findings schema

**المتطلبات السابقة:** `P06-03`

**المتطلبات المغطاة:** `ADR-004`, `REQ-FND-01`, `REQ-FND-02`, `REQ-FND-03`

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

---

### `P07-02` — سجل المراجعين ومصفوفة الأهلية

**Phase:** `PHASE-07` · **EN title:** Reviewer registry and eligibility matrix

**المتطلبات السابقة:** `P07-01`

**المتطلبات المغطاة:** `REQ-REV-01`, `REQ-REV-02`, `REQ-INT-02`, `ADR-010`

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

---

### `P07-03` — الإسناد: المرشّحات الصلبة وتعارض المصالح والاستقلالية

**Phase:** `PHASE-07` · **EN title:** Assignment with hard filters, COI and independence

**المتطلبات السابقة:** `P07-02`

**المتطلبات المغطاة:** `REQ-REV-03`, `REQ-REV-04`, `REQ-REV-05`, `REQ-REV-06`, `REQ-WF-05`

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

---

### `P07-04` — قرارات المراجعة على مستوى كل ملاحظة

**Phase:** `PHASE-07` · **EN title:** Item-level review decisions and reason codes

**المتطلبات السابقة:** `P07-03`

**المتطلبات المغطاة:** `ADR-004`, `REQ-FND-01`, `REQ-DAT-06`, `REQ-WF-05`, `REQ-API-05`

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

---

### `P07-05` — القفل والتوقيع على البصمة وحزمة التسليم

**Phase:** `PHASE-07` · **EN title:** Lock, hash-bound signature and the delivery package

**المتطلبات السابقة:** `P07-04`

**المتطلبات المغطاة:** `ADR-006`, `ADR-010`, `REQ-DEL-01`, `REQ-DEL-05`, `REQ-SEC-13`, `REQ-SVC-02`, `REQ-WF-06`

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

---

### `P07-06` — الإفراج وصفحة التحقق والإبطال

**Phase:** `PHASE-07` · **EN title:** Release, public verification and revocation

**المتطلبات السابقة:** `P07-05`

**المتطلبات المغطاة:** `REQ-DEL-02`, `REQ-DEL-03`, `REQ-DEL-04`, `REQ-API-01`, `REQ-API-05`

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


---

# PHASE-08 — التسعير والدفع والفوترة


## الغرض من المرحلة

`ADR-007` قرار معتمد: «لا يبدأ العمل من redirect؛ webhook موثق واستعلام خادمي
وidempotency»، وضابط قبوله «اختبار replay/order». هذه هي أكثر نقطة في المنصة
عرضة للخطأ المالي، ولذلك يفصل المصدر بين الحالات السبع للدفع ويشترط المطابقة.

## تحذير اقتصادي حاكم

الورقة 19 الصف 54 تحذير صريح: «كل معدلات التكلفة صفر باستثناء VAT. أدخل القيم
الفعلية من العقود قبل أي عرض تجاري». والورقة 01 الصف 11 تؤكد: «الأسعار والمعادلات
نموذج تخطيط قابل للتعديل وليست عرضاً تجارياً».

لذلك هذه المرحلة تبني **المحرك** ولا تُنتج **سعراً**. أي نظام يُصدر عرض سعر من
معدلات صفرية يُنتج رقماً بلا معنى، وقد يُنتج التزاماً تعاقدياً خاطئاً. محرك
التسعير يجب أن يرفض إصدار عرض عندما تكون المعدلات غائبة.

## شروط الدخول

- اكتمال `PHASE-03` و`PHASE-07`.
- إما بطاقة معدلات مُوقَّعة من المالك، أو تعليم البيئة صراحة كـ«غير تجارية».

## شروط الخروج

- نجاح `AT-PRICE-001` (نفس اللقطات = نفس العرض).
- نجاح `AT-PAY-001` (redirect بلا webhook لا يُفعّل شيئاً).
- نجاح `AT-PAY-002` (أحداث مكررة وخارج الترتيب تبقى idempotent).
- لا تخزين لأي `PAN` أو `CVV` في أي موضع.

## المتطلبات المغطاة في هذه المرحلة

`ADR-007`, `REQ-COM-01`..`REQ-COM-09`, `REQ-SEC-12`, `REQ-SEC-15`,
`REQ-DEL-02`, `REQ-OPN-03`

---

## الأوامر التنفيذية

---

### `P08-01` — محرك التسعير ولقطات المعدلات

**Phase:** `PHASE-08` · **EN title:** Pricing engine with rate snapshots and reproducibility

**المتطلبات السابقة:** `P07-06`

**المتطلبات المغطاة:** `REQ-COM-01`, `REQ-COM-02`, `REQ-COM-03`, `REQ-COM-04`, `REQ-OPN-03`

**ماذا سينفذ هذا الأمر؟** ينفّذ مكونات التسعير الاثني عشر في الورقة 18 وسلسلة
الحساب في الورقة 19، مع لقطات معدلات تجعل العرض قابلاً للإعادة بالضبط.

**لماذا نحتاجه؟** الورقة 15 الصف 14 (`CTRL-013`) دليله: «نفس اللقطات نفس العرض».
والورقة 18 تفصل بوضوح بين تكلفة الذكاء وتكلفة الأدوات وأجر المراجع وتكلفة PMO —
والورقة 18 الصف 9 صريحة: «لا يخف داخل AI» أي لا يُدمج أجر PMO في تكلفة الذكاء.

**ما المتطلبات السابقة؟** `P07-06`.

**ما النتيجة المتوقعة؟** محرك تسعير مُنفَّذ بمعادلاته، ولقطات معدلات، ورفض صريح
عند غياب معدل.

**كيف نتحقق من نجاحه؟** `AT-PRICE-001` ناجح؛ ومحرك يرفض إنتاج سعر عندما يكون
معدل مطلوب غائباً أو صفراً غير مقصود.

```text
TASK P08-01 — Pricing engine with rate snapshots and reproducibility

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-01
   Phase: PHASE-08 (Pricing, payment and billing)
   Prerequisites: P07-06
   Requirements covered: REQ-COM-01, REQ-COM-02, REQ-COM-03, REQ-COM-04,
                         REQ-OPN-03

B. OBJECTIVE
   Implement the twelve-component pricing engine and the quote computation
   chain with immutable rate snapshots, so a quote is exactly reproducible —
   and so the engine refuses to produce a commercial price when a required rate
   is absent.

   Why this is necessary: sheet 15 row 14 (CTRL-013) requires the evidence
   "same snapshots same quote". Sheet 18 separates AI inference, document AI,
   engineering tools, reviewer fee and PMO cost as distinct components, and
   row 9 states explicitly that PMO cost must not be hidden inside the AI cost.
   Sheet 19 row 54 warns that every rate is zero except VAT and that actual
   contract values must be entered before any commercial quotation.

   SCOPE BOUNDARY: the pricing engine, rate snapshots and the computation
   chain. The quote lifecycle is P08-02. Payment is P08-03. Do not set any
   commercial rate yourself.

C. CONTEXT
   Required inputs, sheet 18 rows 2-13, the twelve components as component /
   formula / source / control:
     Scope base / base fee / rate card version / not a market price
     Size / quantity times unit rate / scope / per-workflow driver
     Complexity / multiplier or line items / rules / explained to the client
     AI inference / million tokens times rate / provider contract / usually
       internal
     Document AI / usage times rate / tool contract / linked to the run
     Engineering tools / usage times rate / vendor contract / includes a
       minimum charge
     Reviewer / hourly, fixed or share / reviewer contract / second review is
       independent
     PMO / hours times rate or fixed / internal rate / never hidden inside AI
     Risk reserve / eligible cost times percentage / workflow policy /
       reconciled after pilot
     Payment fees / percentage plus fixed / PSP agreement / do not assume fees
     Target margin / gross-up denominator / commercial policy / approval below
       the floor
     VAT / price times VAT / ZATCA or advisor / 15 percent for the standard
       taxable case
   And the computation chain, sheet 19 rows 39-52, which must be reproduced
   exactly:
     size cost = area * area_rate + pages * page_rate + disciplines *
       discipline_fee
     ai cost = input_mtokens * input_rate + output_mtokens * output_rate
     tool cost = bim_hours * bim_rate + fixed_tool_cost
     direct reviewer fee = (HOURLY: r1_hours * r1_rate | FIXED:
       reviewer_fixed_fee | SHARE: 0) + r2_hours * r2_rate
     pmo cost = pmo_hours * pmo_rate
     direct cost = base_fee + size + ai + tool + reviewer + pmo
     reserve = direct_cost * risk_reserve_pct
     revenue share = (SHARE: reviewer_share_pct | else 0)
     price before VAT = IF(1 - psp_pct - target_margin - revenue_share <= 0,
       "CHECK INPUTS", (direct_cost + reserve + psp_fixed) /
       (1 - psp_pct - target_margin - revenue_share))
     final reviewer payout = (SHARE: price_before_vat * reviewer_share_pct |
       else direct_reviewer_fee)
     vat amount = price_before_vat * vat_rate
     total = price_before_vat + vat_amount
     expected profit = price_before_vat - (direct_cost + reserve +
       final_reviewer_payout + price_before_vat * psp_pct + psp_fixed)
     margin pct = IF(price_before_vat = 0, 0, expected_profit /
       price_before_vat)
   Source values: VAT is 0.15 for the standard taxable case (sheet 19 row 35,
   sheet 31 row 5); every other rate in the source is 0.

D. EXECUTION INSTRUCTIONS
   1. Implement each of the twelve components as a named, separately reported
      line item. The breakdown is a deliverable, not an internal detail —
      sheet 05 row 34 names the output as "quote, breakdown, sensitivity", and
      sheet 18 row 4 requires complexity to be explainable to the client.
   2. Implement the computation chain exactly as specified above, including the
      CHECK INPUTS guard: when 1 minus the PSP percentage minus the target
      margin minus the revenue share is less than or equal to zero, the engine
      returns a structured INVALID_PRICING_INPUTS error naming the offending
      inputs. It must never divide by a non-positive denominator and never
      return a negative or infinite price.
   3. Implement reviewer compensation as three mutually exclusive methods
      (HOURLY, FIXED, SHARE) with the source's exact asymmetry: under SHARE the
      direct fee contributes zero to direct cost, the share enters the gross-up
      denominator, and the final payout is computed from the pre-VAT price.
      Reproduce that behaviour and test all three methods.
   4. Keep the second reviewer's fee an independent line per sheet 18 row 8,
      and keep PMO cost its own line per row 9. Add a test asserting the
      breakdown contains distinct, non-zero-able PMO and AI lines so one cannot
      absorb the other.
   5. Implement rate snapshots: a quote captures, immutably, every rate it used
      with that rate's source, version, effective date and currency. Rates live
      in versioned rate cards — provider contract rates (from the model
      registry in P04-02), tool vendor rates, reviewer contract rates (from the
      restricted rate cards in P07-02), internal PMO rates, PSP fees and the
      VAT rate.
   6. Implement the absent-rate refusal, which is the most important behaviour
      in this prompt. Classify every rate as REQUIRED or OPTIONAL for a given
      workflow. If a REQUIRED rate has no value from a contract source, the
      engine returns RATE_CARD_INCOMPLETE listing every missing rate and
      refuses to produce a commercial quote. It may produce a clearly labelled
      PLANNING_ESTIMATE with zeros, which carries a machine-readable
      non_commercial flag and cannot be attached to a quote a client can
      accept. Sheet 19 row 54 and sheet 01 row 11 both demand this separation.
   7. Implement AI and tool cost from measured usage where available: the usage
      ledger from P04-06 provides actuals per run, so a quote can use an
      estimate before the run and the ledger can be compared to it afterwards.
      Record which inputs were estimated and which were measured.
   8. Implement VAT applicability rather than a hardcoded 15 percent: the rate
      and its applicability depend on the taxpayer and the supply (sheet 18
      row 13). Default to the source's standard taxable case value of 0.15,
      record the applicability determination and its basis, and allow a
      zero-rated or exempt determination with a recorded reason.
   9. Implement sensitivity output per sheet 05 row 34: show how the price moves
      with the main drivers, so the breakdown is reviewable.
  10. Implement reproducibility: pricing is a pure function of (inputs, rate
      snapshot, engine version). Record all three on every computation. The same
      triple must produce a byte-identical result.
  11. Tests — AT-PRICE-001 plus the engine suite:
        a. AT-PRICE-001: compute a quote, then recompute with the same inputs
           and the same rate snapshot -> byte-identical result, including every
           breakdown line;
        b. a REQUIRED rate missing -> RATE_CARD_INCOMPLETE listing it, no
           commercial quote produced;
        c. a PLANNING_ESTIMATE carries the non_commercial flag and cannot be
           attached to an acceptable quote;
        d. the CHECK INPUTS condition -> INVALID_PRICING_INPUTS, no division;
        e. all three reviewer methods produce the source's expected asymmetry;
           under SHARE the payout derives from the pre-VAT price;
        f. the breakdown contains distinct AI and PMO lines;
        g. a rate card version change -> a new quote differs, and the old
           quote's snapshot still reproduces the old price;
        h. measured usage from the ledger versus the estimate -> both recorded
           and comparable;
        i. a zero-rated VAT determination -> recorded with its reason, and the
           total reflects it;
        j. engine version change -> flagged on the computation record so an old
           quote is not silently recomputed under new logic.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the twelve components as separately reported line items
   - the exact computation chain with the CHECK INPUTS guard
   - the three reviewer compensation methods with correct asymmetry
   - immutable rate snapshots with source, version, effective date and currency
   - RATE_CARD_INCOMPLETE refusal and the PLANNING_ESTIMATE separation
   - estimate-versus-measured usage recording
   - VAT applicability determination with a recorded basis
   - sensitivity output
   - reproducibility over (inputs, snapshot, engine version)
   - tests/pricing/at-price-001.* plus cases b through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-PRICE-001 output showing two identical computations line by line.
   - Paste the RATE_CARD_INCOMPLETE output listing the missing rates. Given the
     source, this is the expected default state — report how many REQUIRED
     rates are currently absent.
   - Paste the three reviewer-method computations with their inputs.
   - Acceptance criterion: identical inputs and snapshot always give an
     identical quote, and no commercial quote is producible while a required
     rate is missing.

G. COMPLETION CONTRACT
   Definition of Done: the engine reproduces the source's formulas exactly, is
   reproducible, and refuses commercial output on an incomplete rate card.
   Evidence to report: AT-PRICE-001 output, the missing-rate count, the ten
   test results.
   Remaining blockers: the entire rate card is an owner blocker (open decision
   OD-03). The honest completion state is that the engine works and no
   commercial quote can be issued. Do not fill in rates to make the engine
   appear complete.
   Next prompt: P08-02.
```

**المخرجات المتوقعة:** محرك بمكونات اثني عشر، لقطات معدلات، رفض عند نقص المعدلات.
**التحقق المطلوب:** `AT-PRICE-001` ناجح؛ لا عرض تجاري مع معدل مطلوب غائب.
**الاعتمادية التالية:** `P08-02`.

---

---

### `P08-02` — دورة حياة عرض السعر والقفل عند القبول

**Phase:** `PHASE-08` · **EN title:** Quote lifecycle and lock on acceptance

**المتطلبات السابقة:** `P08-01`

**المتطلبات المغطاة:** `REQ-COM-05`, `REQ-WF-01`, `REQ-API-01`, `REQ-API-05`

**ماذا سينفذ هذا الأمر؟** ينفّذ دورة حياة عرض السعر: إنشاء من لقطات، صلاحية،
قبول يقفل العرض، وانتقال `QUOTED` → `AWAITING_PAYMENT`.

**لماذا نحتاجه؟** الورقة 09 الصف 3 تحدد ضابط حالة `QUOTED`: «Freeze quote» عند
القبول. والورقة 28 الصف 16 تحدد كيان `Quote` بـ«inputs/rate snapshots/expiry»
وضابطه «locked on accept». وبدون قفل، يمكن أن يتغير السعر بعد قبول العميل.

**ما المتطلبات السابقة؟** `P08-01`.

**ما النتيجة المتوقعة؟** عروض بصلاحية وقفل، ونقاط نهاية مطابقة للورقة 26.

**كيف نتحقق من نجاحه؟** قبول عرض يقفله ولا يتأثر بتغيير بطاقة المعدلات بعده؛
وعرض منتهي الصلاحية يُرفض قبوله بـ410.

```text
TASK P08-02 — Quote lifecycle and lock on acceptance

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-02
   Phase: PHASE-08
   Prerequisites: P08-01
   Requirements covered: REQ-COM-05, REQ-WF-01, REQ-API-01, REQ-API-05

B. OBJECTIVE
   Implement the quote lifecycle — creation from immutable snapshots, a defined
   validity window, acceptance that freezes the quote, and the workflow
   transition into AWAITING_PAYMENT.

   Why this is necessary: sheet 09 row 3 names the control on the QUOTED state
   as "freeze quote" on acceptance. Sheet 28 row 16 defines Quote with inputs,
   rate snapshots and expiry, and its control as "locked on accept". Without
   the freeze, a rate card change after a client accepts would silently alter
   what they agreed to.

   SCOPE BOUNDARY: the quote entity, its lifecycle and its endpoints. Payment
   session creation is P08-03.

C. CONTEXT
   Required inputs:
     - sheet 26 row 5: POST /v1/quotes, scope quotes:write, control "pricing
       snapshot", emits quote.created, responses 201/422
     - sheet 26 row 6: POST /v1/quotes/{id}/accept, scope quotes:accept,
       control version or etag, emits quote.accepted, responses 200/409/410
     - sheet 09 rows 2-4: DRAFT plus submit_for_quote -> QUOTED (control
       validate schema); QUOTED plus accept_quote -> AWAITING_PAYMENT (control
       freeze quote); AWAITING_PAYMENT plus payment.verified ->
       PAYMENT_VERIFIED (control webhook plus fetch)
     - sheet 09 row 14: a time-bound entity expiring on timer.expired with a
       reopen policy — this covers quote expiry
     - the pricing engine and snapshots from P08-01

D. EXECUTION INSTRUCTIONS
   1. Implement the Quote entity with: the workflow and pinned template
      version, the priced inputs, the immutable rate snapshot reference, the
      computed breakdown, the validity window, the state, and the acceptance
      record.
   2. Implement quote states: DRAFT, ISSUED, ACCEPTED, EXPIRED, WITHDRAWN,
      SUPERSEDED. Only an ISSUED quote inside its validity window is
      acceptable.
   3. Enforce that a quote cannot be ISSUED from a PLANNING_ESTIMATE or while
      RATE_CARD_INCOMPLETE holds. This is the gate that prevents the source's
      zero rates from reaching a client as an offer.
   4. Implement the freeze on acceptance: acceptance copies the full computed
      result and the snapshot reference into an immutable accepted-quote record
      and makes the quote non-recomputable. Enforce immutability in storage.
      Add a test that changes the rate card after acceptance and asserts the
      accepted amount is unchanged.
   5. Implement expiry using the P03-05 timers, producing EXPIRED and returning
      410 on an acceptance attempt per the source's response codes, with the
      reopen policy recorded.
   6. Implement optimistic concurrency with a version or etag per sheet 26
      row 6, returning 409 on a stale acceptance attempt, so a client cannot
      accept a quote they have not actually seen.
   7. Implement supersession: issuing a revised quote marks the prior one
      SUPERSEDED with a link, so the client's history is intact and no quote is
      silently replaced.
   8. Wire the workflow transition: acceptance moves the run from QUOTED to
      AWAITING_PAYMENT, and emits quote.accepted through the outbox.
   9. Record the acceptance act with the accepting identity, timestamp, the
      exact amount and currency, and the terms version, so the commercial gate
      in P07-06 has a verifiable authorization trail.
  10. Tests:
        a. issuing a quote while a required rate is missing -> refused;
        b. accepting an ISSUED quote -> frozen; a subsequent rate card change
           does not alter the accepted amount;
        c. an attempt to modify an accepted quote -> refused at the storage
           level;
        d. accepting an expired quote -> 410;
        e. accepting with a stale etag -> 409;
        f. issuing a revision -> the prior quote is SUPERSEDED with a link, not
           deleted;
        g. acceptance drives the run to AWAITING_PAYMENT and emits
           quote.accepted exactly once;
        h. a quote built from a PLANNING_ESTIMATE cannot be issued or accepted.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the Quote entity with snapshot reference and validity window
   - the six-state lifecycle with issuance gating
   - storage-enforced freeze on acceptance
   - timer-driven expiry with 410 semantics
   - etag concurrency with 409 semantics
   - supersession with linkage
   - the workflow transition and quote.accepted emission
   - the acceptance authorization record
   - tests/pricing/quote-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eight tests.
   - For case b, paste the accepted amount before and after the rate card
     change, showing no drift.
   - Paste the storage-level refusal from case c.
   - Acceptance criterion: an accepted quote is immutable and
   unaffected by any later rate change, and no incomplete-rate quote can be
   issued.

G. COMPLETION CONTRACT
   Definition of Done: the lifecycle implemented, freeze proven immutable,
   expiry and concurrency semantics correct, supersession preserving history.
   Evidence to report: the eight test outputs, the no-drift proof.
   Remaining blockers: no quote can actually be issued while OD-03 is
   unresolved. Confirm the gate holds rather than bypassing it for testing —
   use a test-only rate card fixture clearly marked as such and say so.
   Next prompt: P08-03.
```

**المخرجات المتوقعة:** كيان عرض بست حالات، قفل مفروض عند القبول، صلاحية ومهلة.
**التحقق المطلوب:** العرض المقبول لا يتأثر بتغيير المعدلات؛ لا إصدار عرض بمعدلات ناقصة.
**الاعتمادية التالية:** `P08-03`.

---

---

### `P08-03` — الدفع بالأحداث: تفعيل بـwebhook فقط

**Phase:** `PHASE-08` · **EN title:** Event-driven payment with webhook-only activation

**المتطلبات السابقة:** `P08-02`

**المتطلبات المغطاة:** `ADR-007`, `REQ-COM-06`, `REQ-COM-07`, `REQ-COM-08`, `REQ-SEC-12`, `REQ-SEC-15`

**ماذا سينفذ هذا الأمر؟** ينفّذ `ADR-007`: جلسة دفع مُستضافة، تفعيل من webhook
موثق فقط مع استعلام خادمي، وidempotency، وسبع حالات دفع.

**لماذا نحتاجه؟** `AT-PAY-001` (الورقة 16 الصف 8) يحدد السيناريو: «success
redirect بلا webhook ثم webhook صحيح» والمتوقع «لا تفعيل ثم تفعيل مرة واحدة».
و`AT-PAY-002` يختبر «duplicate وout-of-order events» والمتوقع «Idempotent ولا
رجوع خاطئ». والورقة 21 الصف 8 تمنع تخزين `PAN/CVV` مطلقاً.

**ما المتطلبات السابقة؟** `P08-02`.

**ما النتيجة المتوقعة؟** مسار دفع لا يُفعّل من redirect، ومعالجة أحداث idempotent،
وحدود PCI واضحة.

**كيف نتحقق من نجاحه؟** `AT-PAY-001` و`AT-PAY-002` ناجحان؛ ولا بيانات بطاقة في
أي مخزن أو سجل.

```text
TASK P08-03 — Event-driven payment with webhook-only activation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-03
   Phase: PHASE-08
   Prerequisites: P08-02
   Requirements covered: ADR-007, REQ-COM-06, REQ-COM-07, REQ-COM-08,
                         REQ-SEC-12, REQ-SEC-15

B. OBJECTIVE
   Implement payment as an event-driven flow: a hosted or tokenized checkout
   session, activation only from a signature-verified webhook corroborated by a
   server-side fetch, full idempotency, and the seven-state payment lifecycle —
   with no card data ever entering the platform.

   Why this is necessary: ADR-007 (sheet 02 row 8) is an APPROVED decision
   whose reason is preventing fake or duplicate activation and whose acceptance
   control is a replay and ordering test. AT-PAY-001 (sheet 16 row 8) requires
   that a success redirect without a webhook activates nothing. AT-PAY-002
   requires idempotency under duplicate and out-of-order events. Sheet 21 row 8
   forbids storing PAN or CVV and requires an explicit PCI scope.

   SCOPE BOUNDARY: checkout sessions, webhook ingestion, verification,
   idempotent state transitions and milestone activation. Invoicing and
   reconciliation are P08-04. Do not integrate a provider for which no sandbox
   credential already exists — build to the normalized interface and use a
   contract-conformant fake, clearly labelled.

C. CONTEXT
   Required inputs:
     - sheet 26 row 7: POST /v1/payments/sessions, scope payments:write,
       Idempotency-Key, emits payment.initiated, responses 201/422
     - sheet 26 row 8: POST /v1/webhooks/payments/{provider}, authorized by
       provider signature, keyed by event id, emits payment.*, responses
       200/400/401
     - sheet 21 row 7 (PAY-EVT): the seven states INITIATED, AUTHORIZED, PAID,
       FAILED, EXPIRED, REFUNDED, CHARGEBACK; integration "signed webhook plus
       fetch plus idempotency"; control "a redirect does not open the service";
       note "audit transitions"
     - sheet 21 row 8 (PAY-SEC): no PAN or CVV storage; vault, TLS, WAF,
       signature; define the PCI scope; least scope
     - sheet 21 rows 2-5: Moyasar (hosted or tokenized, verify provider and
       contract), Geidea (hosted checkout preferred, no PAN or CVV, 3DS,
       server-to-server), Tamara BNPL (eligibility is not a guarantee, test the
       states), bank transfer (virtual IBAN, reference, reconcile; a transfer
       image never opens a milestone)
     - sheet 09 rows 4-5 and row 22: AWAITING_PAYMENT plus payment.verified ->
       PAYMENT_VERIFIED with the control "webhook plus fetch"; PAYMENT_VERIFIED
       plus enqueue -> QUEUED with the control idempotency; Payment INITIATED
       plus a provider event -> AUTHORIZED, PAID, FAILED or EXPIRED with the
       control verify

D. EXECUTION INSTRUCTIONS
   1. Define a normalized payment provider interface covering: create hosted
      session, fetch authoritative payment status, verify webhook signature,
      refund, and map provider states to the seven canonical states.
   2. Implement session creation with a required Idempotency-Key, bound to the
      accepted quote, its exact amount and currency, and the milestone it
      funds. Return only the hosted redirect or tokenized handle — never
      anything that could carry card data into the platform.
   3. Implement the PCI boundary explicitly and provably: the platform receives
      no PAN, no CVV, no expiry and no track data on any path. Add a test that
      submits card-shaped data to every payment endpoint and asserts rejection,
      plus a storage and log scan asserting no card-shaped string is persisted
      anywhere. Document the resulting PCI scope statement as a deliverable.
   4. Implement the redirect handler as informational only. It may show the
      user a status page; it may not change any state, activate any milestone,
      or mark any payment verified. Make that structurally true: the redirect
      handler has no write access to payment state. This is the core of
      AT-PAY-001.
   5. Implement webhook ingestion with layered verification, in this order:
        a. verify the provider signature over the raw request body, using a
           constant-time comparison, before parsing;
        b. reject an unsigned or badly signed event with 401 and no state
           change;
        c. enforce a replay window and reject stale timestamps;
        d. dedupe by provider event id using the idempotency store from
           P03-03;
        e. perform an independent server-side fetch of the authoritative
           payment status from the provider, and trust the fetch over the
           webhook payload;
        f. verify that the fetched amount, currency and reference match the
           quote exactly — a mismatch suspends rather than activates, per
           sheet 05 row 35's stop conditions (signature, amount, duplicate,
           fraud).
   6. Implement ordering tolerance: events may arrive out of order. Implement a
      state machine with a monotonic provider-side sequence or timestamp so an
      older event cannot regress a newer state (for example a late AUTHORIZED
      must not overwrite PAID, and a late PAID must not overwrite REFUNDED).
      This is the "no wrong regression" clause of AT-PAY-002.
   7. Implement milestone activation exactly once: the transition to
      PAYMENT_VERIFIED and the resulting enqueue are idempotent, so repeated
      webhooks for the same payment activate one milestone. Track the duplicate
      activation KPI from sheet 30 row 11, whose target is zero.
   8. Implement refund and chargeback as first-class states with their
      consequences recorded, requiring the FINANCE role with dual approval per
      sheet 04 row 8, and never silently reversing a delivered milestone — the
      compensation path is recorded for human handling.
   9. Implement bank transfer handling per sheet 21 row 5: a virtual IBAN and
      reference with automated reconciliation. An uploaded transfer image is
      explicitly not evidence and cannot activate a milestone — add a test.
  10. Implement BNPL eligibility handling per sheet 21 row 4: eligibility is not
      a payment guarantee, so activation still requires the PAID state through
      the same verification path.
  11. Audit every payment state transition per sheet 21 row 7, into the
      append-only store.
  12. Tests — AT-PAY-001 and AT-PAY-002 plus the payment suite:
        a. AT-PAY-001: hit the success redirect with no webhook -> nothing
           activated, run still AWAITING_PAYMENT; then deliver a valid webhook
           -> activated exactly once. Paste both halves;
        b. AT-PAY-002: deliver the same webhook event three times -> one
           activation; deliver AUTHORIZED after PAID -> no regression; deliver
           PAID after REFUNDED -> no regression;
        c. an unsigned webhook -> 401, no state change;
        d. a tampered body with a valid-looking signature -> rejected;
        e. a stale timestamp outside the replay window -> rejected;
        f. a fetched amount that differs from the quote -> suspended, not
           activated, with the reason recorded;
        g. card-shaped data submitted to every payment endpoint -> rejected;
           the storage and log scan finds no card-shaped string;
        h. the redirect handler has no write path to payment state — assert
           architecturally;
        i. a transfer image upload -> does not activate a milestone;
        j. BNPL eligibility granted but not PAID -> no activation;
        k. a refund attempt with a single approver -> refused; with dual
           approval -> recorded, with the compensation path logged;
        l. every state transition appears in the audit store.
  13. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the normalized payment provider interface with at least one
     contract-conformant implementation
   - idempotent session creation bound to quote, amount, currency and milestone
   - the proven PCI boundary and a written PCI scope statement
   - a write-incapable redirect handler
   - six-layer webhook verification including an independent server-side fetch
   - order-tolerant state machine with regression prevention
   - exactly-once milestone activation with the duplicate-activation metric
   - refund and chargeback with dual approval and recorded compensation
   - bank transfer reconciliation with image evidence explicitly rejected
   - BNPL eligibility handling
   - full transition auditing
   - tests/payment/at-pay-001.*, at-pay-002.* plus cases c through l
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste both halves of AT-PAY-001 and all three parts of AT-PAY-002.
   - Paste the card-shaped data rejections and the storage and log scan output
     from case g.
   - Paste the architectural assertion from case h.
   - State which provider was exercised with a real sandbox credential and
     which with a fake.
   - Acceptance criterion: no redirect ever activates anything, duplicate and
     out-of-order events never cause a wrong state, and no card data exists
     anywhere in the platform.

G. COMPLETION CONTRACT
   Definition of Done: AT-PAY-001 and AT-PAY-002 green, PCI boundary proven,
   activation exactly once, no state regression.
   Evidence to report: both acceptance tests, the card-data scans, the
   architectural proof, the real-versus-fake provider statement.
   Remaining blockers: provider contracts and merchant accounts are owner
   blockers (sheet 23 and P00-03). Sheet 31 row 16 requires verifying the PSP
   against the SAMA licensed list — report whether that check was done and by
   whom.
   Next prompt: P08-04.
```

**المخرجات المتوقعة:** واجهة مزود مُطبَّعة، تحقق webhook بست طبقات، تفعيل مرة واحدة، حدود PCI مُثبتة.
**التحقق المطلوب:** `AT-PAY-001` و`AT-PAY-002` ناجحان؛ لا بيانات بطاقة في أي مخزن أو سجل.
**الاعتمادية التالية:** `P08-04`.

---

---

### `P08-04` — الفوترة والمطابقة وZATCA

**Phase:** `PHASE-08` · **EN title:** Invoicing, ZATCA e-invoicing and reconciliation

**المتطلبات السابقة:** `P08-03`

**المتطلبات المغطاة:** `REQ-COM-09`, `REQ-COM-11`, `REQ-SEC-12`, `REQ-DEL-02`, `REQ-INT-01`

**ماذا سينفذ هذا الأمر؟** يبني الفوترة والمطابقة المالية، وتهيئة ZATCA للفاتورة
الإلكترونية، ودفتر مدفوعات قابل للتسوية.

**لماذا نحتاجه؟** الورقة 38 الصف 10 (`G-05 Credits persistence`) حاجز إصدار
بمعيار «لا خصم سلبي أو مزدوج». والورقة 57 الصف 11 (`A10`) تحدد الأثر: «تسرّب
الهامش»، والتنفيذ المطلوب: «ledger idempotency ومطابقة يومية». والورقة 21 الصف 6
تنبّه أن ZATCA «ليست بوابة دفع».

**ما المتطلبات السابقة؟** `P08-03`.

**ما النتيجة المتوقعة؟** دفتر مالي مُطابَق، وفوترة متوافقة مع التهيئة المطلوبة،
وتقرير مطابقة يومي.

**كيف نتحقق من نجاحه؟** مطابقة يومية تكشف أي فرق بين الدفتر والمزود؛ ولا خصم
مزدوج أو سلبي ممكن.

```text
TASK P08-04 — Invoicing, ZATCA e-invoicing and reconciliation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-04
   Phase: PHASE-08
   Prerequisites: P08-03
   Requirements covered: REQ-COM-09, REQ-COM-11, REQ-SEC-12, REQ-DEL-02,
                         REQ-INT-01

B. OBJECTIVE
   Implement the financial ledger with daily reconciliation against provider
   records, invoice generation, and the ZATCA e-invoicing integration path —
   with no possibility of a negative or double debit.

   Why this is necessary: sheet 38 row 10 (G-05) is a release blocker whose
   pass criterion is "no negative or double debit" with required evidence of a
   ledger test. Sheet 57 row 11 (A10) names the impact as margin leakage and
   requires ledger idempotency plus daily reconciliation, evidenced by a
   reconciliation run. Sheet 21 row 6 cautions that ZATCA Fatoorah is an
   e-invoicing system, not a payment gateway.

   SCOPE BOUNDARY: the ledger, reconciliation, invoice generation and the ZATCA
   onboarding path. Do not submit a real invoice to ZATCA production. Use the
   official sandbox only if a credential already exists; otherwise build to the
   interface and report that it is unexercised.

C. CONTEXT
   Required inputs:
     - sheet 23 row 8 (KSA-07): ZATCA Fatoorah, XML and QR invoicing with an
       SDK; portal and official sandbox exist; the connection plan is EGS
       registration, certificates, secrets and tests; status ONBOARD
     - sheet 21 row 6 (INV-01): XML and QR, phase two where applicable;
       portal, SDK, validator and sandbox; not a payment gateway; tax advice
       required
     - sheet 31 row 5 (SRC-004): ZATCA standard VAT is 15 percent where
       applicable
     - sheet 05 row 35 (FIN-02): invoice and checkout, link the milestone after
       a verified webhook and reconciliation; no PAN or CVV and no manual
       adjustment
     - sheet 28 row 17: Payment entity with provider, event, state and amount;
       control idempotent
     - the usage ledger from P04-06 and the payment states from P08-03

D. EXECUTION INSTRUCTIONS
   1. Implement a double-entry or equivalent financial ledger where every
      posting is immutable and every correction is a new compensating entry.
      Deleting or editing a posting is impossible. This is what makes "no
      negative or double debit" provable rather than hoped for.
   2. Enforce posting idempotency on the provider event id and on the internal
      operation id, so a retried webhook or a retried job posts once. Reuse the
      P03-03 idempotency store.
   3. Implement balance invariants as database-level constraints or checked
      invariants: no balance may go negative where the account type forbids it,
      and the sum of entries per transaction must be zero in a double-entry
      model. Add a test attempting to create an unbalanced or
      negative-forbidden posting.
   4. Implement invoice generation from the accepted quote and the delivered
      milestones, with: the invoice number series, the issue date, the supplier
      and customer tax details, the line items from the pricing breakdown, the
      VAT determination and its basis from P08-01, and the total. The invoice
      is an artifact version with a digest, locked on issue (P02-02).
   5. Implement the ZATCA integration path to the point the source supports —
      EGS unit registration, certificate handling via the secrets vault, XML
      generation to the required schema, QR generation, and validation against
      the official validator or sandbox. Each step records whether it was
      actually exercised. Do not claim compliance; the source marks this
      ONBOARD and requires tax advice.
   6. Implement the no-manual-adjustment rule from sheet 05 row 35: there is no
      endpoint or admin action that edits a payment state or an invoice amount
      by hand. Corrections flow through credit notes and compensating entries,
      with FINANCE dual approval per sheet 04 row 8. Add a test asserting no
      manual-adjustment path exists, and recall that sheet 04 row 9 forbids
      SUPPORT_L2 from setting a payment status manually.
   7. Implement daily reconciliation with three legs:
        a. platform ledger versus provider settlement records;
        b. platform usage ledger (P04-06) versus provider usage or billing
           records, which is the margin-leakage control in A10;
        c. invoiced amounts versus accepted quote amounts versus received
           payments.
      Each run produces a dated report listing every discrepancy with its
      amount and suspected cause, and a discrepancy above a threshold raises an
      alert rather than being absorbed.
   8. Implement the unit-economics inputs for sheet 17 rows 10-11: cost per
      workflow and gross margin, computed from the ledger and the usage ledger,
      returning PENDING where a required rate is absent rather than a
      misleading number.
   9. Implement retention and records handling per the Payment and Delivery
      entity retention classes, with the legal-hold interaction from P02-02.
  10. Tests:
        a. a repeated webhook -> one posting;
        b. an unbalanced posting -> rejected;
        c. a posting that would drive a forbidden balance negative -> rejected;
        d. a double debit attempt -> rejected, satisfying G-05's criterion;
        e. no manual-adjustment endpoint exists -> assert architecturally;
        f. a correction flows as a compensating entry with dual approval;
        g. a reconciliation run with an injected provider discrepancy ->
           detected, reported with the amount, alerted;
        h. a reconciliation run with no discrepancy -> clean report, retained
           as the A10 evidence;
        i. an invoice is locked on issue and its digest verifies;
        j. the ZATCA XML validates against the schema (sandbox or validator) if
           a credential exists; otherwise the step reports NOT EXERCISED;
        k. cost per workflow and gross margin return PENDING when a required
           rate is absent.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the immutable financial ledger with compensating-entry corrections
   - event-id and operation-id posting idempotency
   - database-level balance invariants
   - invoice generation, locked with a digest
   - the ZATCA path with per-step exercised or not-exercised status
   - the architecturally enforced no-manual-adjustment rule
   - three-leg daily reconciliation with dated reports and alerting
   - unit-economics inputs with honest PENDING semantics
   - tests/finance/ledger-*.* covering cases a through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eleven tests.
   - Paste the double-debit rejection for case d — this is the G-05 evidence.
   - Paste both reconciliation reports from cases g and h; retain the clean run
     as the A10 evidence.
   - State explicitly which ZATCA steps were actually exercised and which were
     not.
   - Acceptance criterion: a double or negative debit is impossible, every
     discrepancy is detected and reported, and no manual adjustment path
     exists.

G. COMPLETION CONTRACT
   Definition of Done: ledger immutable and invariant-protected, reconciliation
   running and detecting injected discrepancies, invoices locked, ZATCA path
   built with honest exercise status.
   Evidence to report: the eleven test outputs, the G-05 and A10 evidence
   artifacts, the ZATCA exercise statement.
   Remaining blockers: ZATCA onboarding, tax advice and a merchant account are
   owner blockers. Report them. Do not describe the platform as ZATCA compliant.
   Next prompt: P09-01. PHASE-08 exit requires AT-PRICE-001, AT-PAY-001 and
   AT-PAY-002 green, the PCI scan clean, and a clean reconciliation run
   retained.
```

**المخرجات المتوقعة:** دفتر مالي ثابت، مطابقة ثلاثية يومية، فواتير مقفلة، مسار ZATCA.
**التحقق المطلوب:** لا خصم مزدوج أو سلبي؛ كل فرق مكتشَف ومُبلَّغ؛ لا مسار تعديل يدوي.
**الاعتمادية التالية:** `P09-01`.


---

# PHASE-09 — المسار الذهبي لمراجعة الفيلا


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

---

### `P09-01` — الاستقبال والتوجيه وفهم الملفات

**Phase:** `PHASE-09` · **EN title:** Villa path stages 1-4 — intake, routing, quote and file intelligence

**المتطلبات السابقة:** `P08-04`

**المتطلبات المغطاة:** `REQ-WF-08`, `REQ-AGT-08`

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

---

### `P09-02` — الامتثال والمسودة المعمارية وبوابة الجودة

**Phase:** `PHASE-09` · **EN title:** Villa path stages 5-7 — compliance, architectural draft, quality gate

**المتطلبات السابقة:** `P09-01`

**المتطلبات المغطاة:** `REQ-WF-08`, `REQ-AGT-08`, `REQ-KNW-06`, `REQ-SVC-02`

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

---

### `P09-03` — التشغيل الكامل من طرف إلى طرف ودليل G01

**Phase:** `PHASE-09` · **EN title:** Full end-to-end villa run and the G01 evidence record

**المتطلبات السابقة:** `P09-02`

**المتطلبات المغطاة:** `REQ-WF-08`, `REQ-EVL-07`, `REQ-SVC-01`, `REQ-GOV-04`

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


---

# PHASE-10 — الرصد والموثوقية وFinOps


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

---

### `P10-01` — التتبع الموحد وربط السلسلة

**Phase:** `PHASE-10` · **EN title:** Unified tracing and the six-level linkage

**المتطلبات السابقة:** `P09-03`

**المتطلبات المغطاة:** `REQ-OBS-02`, `REQ-GW-11`, `REQ-SEC-04`

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

---

### `P10-02` — اللوحات التسع والتنبيهات

**Phase:** `PHASE-10` · **EN title:** The nine dashboards and tested alerts

**المتطلبات السابقة:** `P10-01`

**المتطلبات المغطاة:** `REQ-OBS-01`, `REQ-OBS-05`, `REQ-GW-11`

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

---

### `P10-03` — كتب التشغيل ومسارات الدعم

**Phase:** `PHASE-10` · **EN title:** SRE runbooks and support operations

**المتطلبات السابقة:** `P10-02`

**المتطلبات المغطاة:** `REQ-OBS-03`, `REQ-OBS-04`, `REQ-COM-11`

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

---

### `P10-04` — النسخ الاحتياطي والاسترجاع وRTO/RPO

**Phase:** `PHASE-10` · **EN title:** Backup, disaster recovery and the RTO/RPO drill

**المتطلبات السابقة:** `P10-03`

**المتطلبات المغطاة:** `REQ-SEC-14`, `REQ-SEC-03`, `REQ-EVL-08`

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


---

# PHASE-11 — الأمن والخصوصية وPDPL


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

---

### `P11-01` — الأساس النظامي وسجل المعالجة والموافقة

**Phase:** `PHASE-11` · **EN title:** PDPL lawful basis, RoPA, consent and notice

**المتطلبات السابقة:** `P10-04`

**المتطلبات المغطاة:** `REQ-SEC-07`, `REQ-SEC-11`

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

---

### `P11-02` — حقوق صاحب البيانات

**Phase:** `PHASE-11` · **EN title:** Data subject rights execution

**المتطلبات السابقة:** `P11-01`

**المتطلبات المغطاة:** `REQ-SEC-08`, `REQ-EVL-01`

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

---

### `P11-03` — الحفظ والحجز القانوني والحذف المُتحقَّق

**Phase:** `PHASE-11` · **EN title:** Retention schedules, legal hold and verified deletion

**المتطلبات السابقة:** `P11-02`

**المتطلبات المغطاة:** `REQ-SEC-09`, `REQ-DAT-01`, `REQ-SEC-14`

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

---

### `P11-04` — البرنامج الخصومي والخرق والإقامة

**Phase:** `PHASE-11` · **EN title:** Adversarial programme, breach readiness and residency assessment

**المتطلبات السابقة:** `P11-03`

**المتطلبات المغطاة:** `REQ-SEC-06`, `REQ-SEC-10`, `REQ-GW-19`, `REQ-SCN-05`, `REQ-EVL-08`

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


---

# PHASE-12 — المسح والالتقاط


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

---

### `P12-01` — أنماط الالتقاط والموافقة

**Phase:** `PHASE-12` · **EN title:** Capture modes, consent and privacy

**المتطلبات السابقة:** `P11-04`

**المتطلبات المغطاة:** `REQ-SCN-01`, `REQ-SCN-02`, `REQ-SCN-05`, `REQ-SCN-06`

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

---

### `P12-02` — عقود المسح وخط الأدلة

**Phase:** `PHASE-12` · **EN title:** Scan API contracts and the evidence pipeline

**المتطلبات السابقة:** `P12-01`

**المتطلبات المغطاة:** `REQ-SCN-03`, `REQ-SCN-01`, `REQ-SEC-02`, `REQ-API-05`

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

---

### `P12-03` — LiDAR والدقة والتحقق البشري الإلزامي

**Phase:** `PHASE-12` · **EN title:** Optional native LiDAR with confidence and mandatory human validation

**المتطلبات السابقة:** `P12-02`

**المتطلبات المغطاة:** `REQ-SCN-04`, `REQ-GW-15`, `REQ-SCN-01`, `REQ-OBS-04`

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


---

# PHASE-13 — لوحة التحكم الإدارية والموصلات والدعم


## الغرض من المرحلة

الورقة 68 الصف 4 تحدد المعمارية الحاكمة للإدارة بعبارة لا تقبل التأويل:
«Admin Console → authenticated Platform API → policy/approval → workflow/agent
runtime. Never direct browser-to-agent or database».

والورقة 57 الصف 3 (`A02`) تسجّل الفجوة بأولوية `CRITICAL`: «عمليات الإدارة تفتقر
إلى عقود تفويض وتدقيق كاملة»، والأثر «إساءة استخدام الصلاحية». والورقة 67 الصف 3
تضع المرحلة الأولى في خطة الإصدار: «لوحة تحكم إدارية للقراءة فقط + تدقيق».

## شروط الدخول

- اكتمال `PHASE-01` (الهوية والسياسة والتدقيق) و`PHASE-04` (البوابة).

## شروط الخروج

- عدم وجود أي مسار مباشر من المتصفح إلى وكيل أو قاعدة بيانات.
- مصفوفة RBAC الإدارية مفروضة باختبارات سلبية.
- تحكم مزدوج على أسرار وسياسات الإنتاج.
- تسجيل واختبار وتدوير وإبطال الموصلات مُثبت.
- انتهاء break-glass آلياً.

## المتطلبات المغطاة في هذه المرحلة

`REQ-GOV-03`, `REQ-ADM-01`..`REQ-ADM-07`, `REQ-API-09`, `REQ-SEC-01`,
`REQ-GW-12`, `REQ-OBS-04`

---

## الأوامر التنفيذية

---

### `P13-01` — مستوى التحكم والحد المعماري

**Phase:** `PHASE-13` · **EN title:** Admin control plane and the architectural boundary

**المتطلبات السابقة:** `P12-03`

**المتطلبات المغطاة:** `REQ-GOV-03`, `REQ-ADM-03`, `REQ-ADM-06`, `REQ-API-09`

**ماذا سينفذ هذا الأمر؟** يبني مستوى التحكم الإداري بوصفه طبقة أوامر خلف الـAPI
والسياسة، ويفرض الحد المعماري باختبار يفشل عند أي خرق.

**لماذا نحتاجه؟** الورقة 52 الصف 7 تحدد الشرط: «لا نداءات وكيل مباشرة من
المتصفح»، والورقة 52 الصف 7 تضيف «orchestrator via commands» — أي أن الإدارة
تُصدر أوامر لا تستدعي المحرك مباشرة. والورقة 67 الصف 3 تبدأ بقراءة فقط عن قصد:
عرض بلا تعريض.

**ما المتطلبات السابقة؟** `P12-03`.

**ما النتيجة المتوقعة؟** مستوى تحكم بأوامر مُنمَّطة، وقراءة مُحجَّبة، وحد معماري
مفروض.

**كيف نتحقق من نجاحه؟** اختبار معماري يفشل إن وُجد مسار من واجهة الإدارة إلى
الوكيل أو قاعدة البيانات مباشرة.

```text
TASK P13-01 — Admin control plane and the architectural boundary

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-01
   Phase: PHASE-13 (Admin control plane, connectors and support operations)
   Prerequisites: P12-03
   Requirements covered: REQ-GOV-03, REQ-ADM-03, REQ-ADM-06, REQ-API-09

B. OBJECTIVE
   Build the admin control plane as a command layer behind the authenticated
   platform API and the policy service, with read access masked by default, and
   enforce the architectural boundary with a test that fails on any violation.

   Why this is necessary: sheet 68 row 4 states the control path as console to
   platform API to policy and approval to runtime, and forbids
   browser-to-agent and browser-to-database. Sheet 52 row 7 requires the
   orchestrator be reached via commands and forbids direct browser agent calls.
   Sheet 57 row 3 (A02) records that admin operations currently lack complete
   authorization and audit contracts, with the impact of privilege abuse.
   Sheet 67 row 3 deliberately starts with a read-only console so staff can
   inspect without exposure.

   SCOPE BOUNDARY: the control plane, the command pattern, the read surface and
   the boundary test. The sixteen admin capabilities are P13-03. Connectors are
   P13-02.

C. CONTEXT
   Required inputs, sheet 52 rows 2-9, each as area / admin frontend action /
   backend authority / agent-layer relation / audit and security / acceptance:
     Organizations / create, approve, suspend / Org service / none direct /
       admin scoped plus audit / suspension blocks new runs
     Sales and contracts / lead to quote to contract / CRM and billing /
       entitlement provision only / dual approval / a signed contract gates
     Agent licenses / grant and revoke SKUs / Entitlement service / runtime
       checks policy / audit grants / an unlicensed run is denied
     Branding / review logo, theme, domain / Branding service / none / domain
       verification / theme scoped
     Knowledge / approve uploaded corpora / Knowledge service / RAG namespace
       by tenant / source license check / no tenant crossover
     Operations / view runs, errors, usage / Observability API / orchestrator
       via commands / RBAC plus redaction / no direct browser agent calls
     Quality / approve human review / Review service / agent output only /
       signed decisions / traceable signoff
     Billing / quotas, invoices, credits / Billing service / budget preflight /
       reconciliation / accurate usage
   Note: the Organizations, Sales, Agent licenses and Branding areas belong to
   the deferred commerce scope (sheet 68 row 8). Implement their read surfaces
   and the command contracts where they serve single-tenant operation, and
   leave the multi-tenant commercial behaviour to PHASE-16 without building it.

D. EXECUTION INSTRUCTIONS
   1. Implement the command pattern: every administrative mutation is a typed
      command with a name, a payload schema, a required authority, an approval
      requirement, an idempotency key and an audit contract. Commands are
      submitted to the platform API, authorized, policy-checked, recorded, and
      then dispatched to the owning service. A command's effect is never
      performed inline in a request handler that also renders a view.
   2. Implement the command log as part of the append-only audit store: who
      submitted, what, when, under which approval, with the before and after
      state and the correlation id. Sheet 58 marks nearly every admin action as
      audited, so this is the mechanism.
   3. Implement the read surface read-only and masked by default, per sheet 67
      row 3's exit criterion "staff can inspect without exposure":
        - personal data masked unless the role and the justification permit it;
        - secrets never returned, in any form, including partially;
        - cross-tenant reads denied through the P01-02 helper;
        - a justification required for any access to customer data, recorded
          with the read (sheet 58 row 3 requires a ticket and "scoped access
          plus justification").
   4. Implement the architectural boundary test, the central deliverable here:
        - assert no admin frontend asset makes a request to anything other than
          the platform API origin;
        - assert no admin backend route reaches the agent runtime or the
          database without passing the authorization and policy middleware —
          implement as a route-table or dependency-graph assertion, extending
          the P01-04 guard;
        - assert the browser bundle contains no database connection string, no
          provider credential and no direct runtime endpoint;
        - make the test fail when a violating path is introduced, and
          demonstrate it.
   5. Implement suspension semantics per sheet 52 row 2: suspending an
      organization blocks new runs immediately while leaving in-flight work and
      records intact. Add a test.
   6. Implement the operations read surface over the P10-01 traces and P10-02
      signals, with redaction, so support can diagnose without raw data access.
   7. Implement the admin API operations from sheet 65 that belong to this
      prompt: GET /v1/admin/health (ops:read, emits health.degraded) and GET
      /v1/admin/audit (audit:read, emits audit.accessed). Note that audit
      access itself emits an event — reading the audit trail is an audited act.
   8. Implement a session model for admin users with short lifetimes,
      re-authentication for sensitive reads, and no long-lived tokens.
   9. Tests:
        a. the architectural boundary test passes; then introduce a direct
           database call in an admin route and show it failing; restore it;
        b. the browser bundle scan finds no credential or direct endpoint;
        c. a customer-data read without a justification -> refused; with one ->
           permitted and the justification recorded;
        d. a secret is never returned by any admin read, including a masked
           form that would leak length or prefix;
        e. a cross-tenant admin read -> denied uniformly;
        f. suspending an organization -> new runs blocked, in-flight work
           untouched;
        g. every command produces an audit record with before and after state;
        h. reading the audit trail emits audit.accessed;
        i. a command submitted without its required approval -> refused;
        j. an admin session expires and a sensitive read requires
           re-authentication.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the typed command pattern with authority, approval, idempotency and audit
     contracts
   - the command log in the append-only store
   - the masked, justification-gated read surface
   - the architectural boundary test with its bundle scan
   - organization suspension semantics
   - the redacted operations read surface over traces and signals
   - GET /v1/admin/health and GET /v1/admin/audit with audit.accessed
   - short-lived admin sessions with re-authentication for sensitive reads
   - tests/admin/boundary-*.* covering cases a through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the boundary test passing, then failing on the injected violation,
     then passing again.
   - Paste the bundle scan output.
   - Paste the case d result showing no secret is returned in any form.
   - Acceptance criterion: no path exists from the admin browser to an agent or
     the database, and the test proving it can fail.

G. COMPLETION CONTRACT
   Definition of Done: the command plane working, reads masked and justified,
   the boundary enforced and provably testable.
   Evidence to report: the three boundary test runs, the bundle scan, the
   masking proof, the command audit sample.
   Remaining blockers: the commerce-related admin areas remain deferred per
   sheet 68 row 8. Confirm you built only their single-tenant read surfaces.
   Next prompt: P13-02.
```

**المخرجات المتوقعة:** نمط أوامر مُنمَّط، سطح قراءة مُحجَّب، اختبار حد معماري قادر على الفشل.
**التحقق المطلوب:** لا مسار من المتصفح إلى وكيل أو قاعدة بيانات؛ لا سر يُرجَع بأي صورة.
**الاعتمادية التالية:** `P13-02`.

---

---

### `P13-02` — دورة حياة الموصلات وخزانة الأسرار

**Phase:** `PHASE-13` · **EN title:** Connector lifecycle and secrets vault

**المتطلبات السابقة:** `P13-01`

**المتطلبات المغطاة:** `REQ-ADM-04`, `REQ-ADM-05`, `REQ-SEC-01`, `REQ-INT-04`

**ماذا سينفذ هذا الأمر؟** ينفّذ مراحل الموصل الست في الورقة 60 — التسجيل
والمصادقة والتحقق والتنفيذ والفشل والإيقاف — مع خزانة أسرار وتدوير وإبطال.

**لماذا نحتاجه؟** الورقة 67 الصف 5 تضع «مدير الموصلات + خزانة الأسرار» مرحلة
`P0` بمعيار خروج: «Register/test/rotate/revoke». والورقة 58 الصف 8 تشترط «الأسرار
لا تُرجَع أبداً» وتحكماً مزدوجاً للتدوير. والورقة 60 الصف 4 تضيف ضابطاً أمنياً
محدداً: «حماية SSRF وTLS».

**ما المتطلبات السابقة؟** `P13-01`.

**ما النتيجة المتوقعة؟** مدير موصلات كامل الدورة، وخزانة أسرار لا تُرجِع قيمة
أبداً.

**كيف نتحقق من نجاحه؟** اختبار إبطال يُثبت توقف الموصل فوراً؛ واختبار SSRF يُحجَب؛
ولا قيمة سر تظهر في أي استجابة أو سجل.

```text
TASK P13-02 — Connector lifecycle and secrets vault

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-02
   Phase: PHASE-13
   Prerequisites: P13-01
   Requirements covered: REQ-ADM-04, REQ-ADM-05, REQ-SEC-01, REQ-INT-04

B. OBJECTIVE
   Implement the six-stage connector lifecycle with its security,
   observability and verification requirements, backed by a secrets vault that
   never returns a secret value.

   Why this is necessary: sheet 67 row 5 makes the connector manager and
   secrets vault a P0 phase whose exit criterion is register, test, rotate and
   revoke. Sheet 58 row 8 requires dual approval for credential rotation and
   states the secret is never returned. Sheet 60 row 4 requires SSRF protection
   and TLS at the validation stage. Sheet 57 row 5 (A04) requires per-provider
   credential, licensing and contract verification with provider sandbox
   success as evidence.

   SCOPE BOUNDARY: the connector manager and the vault integration. Do not
   onboard a provider that has no agreement — registration without a
   credential is a valid, reportable state.

C. CONTEXT
   Required inputs, sheet 60 rows 2-7, each as step / contract and behavior /
   security / observability / verification:
     Register / connector id, version, base URL, scopes, region, owner /
       allowlisted domains / audit registration / schema test
     Authenticate / OAuth2 client credentials or a signed service account /
       vault-managed keys with rotation / expiry alerts / no secrets in logs
     Validate / OpenAPI schema, test endpoint, quota / SSRF protection, TLS /
       synthetic probe / sandbox contract tests
     Execute / idempotency key, timeout, retry and backoff / least-privilege
       egress / trace and request id / provider response fixture
     Fail / circuit breaker, DLQ, fallback / no silent data transfer / error
       budget / failure injection
     Retire / disable, revoke, delete credentials / revoke token / audit trail
       / revocation test
   And sheet 65 rows 4-5: POST /v1/admin/connectors (integrations:write,
   idempotency required, emits connector.created) and POST
   /v1/admin/connectors/{id}/test (integrations:test, idempotency required,
   emits connector.tested) — note the test probe is described in sheet 65 as
   "credential-safe".

D. EXECUTION INSTRUCTIONS
   1. Implement the Connector entity with the register-stage fields: id,
      version, base URL, scopes, region, owner, plus its lifecycle state
      (REGISTERED, AUTHENTICATED, VALIDATED, ACTIVE, DEGRADED, DISABLED,
      RETIRED) and the contract and licensing references from P00-03.
   2. Enforce a domain allowlist at registration: a base URL outside the
      allowlist is rejected. The allowlist is itself a dual-approved,
      audited configuration change, not a free-text field on the connector.
   3. Integrate the secrets vault with a strict interface: write-only from the
      admin path, read-only at call time by the owning service, and no
      read-back path at all for a human or an API. The vault returns a handle
      to the admin surface, never a value. Add a test asserting no endpoint,
      log, trace, error or export returns a secret value or a prefix of one.
   4. Implement rotation with dual approval per sheet 58 row 8: two distinct
      approvers, overlapping validity so rotation is not an outage, and
      automatic revocation of the previous credential after the overlap. Record
      the rotation and emit an event. Implement expiry alerts per the
      authenticate stage's observability requirement.
   5. Implement validation with the source's three checks and two controls:
        - the connector's OpenAPI schema is fetched or supplied and validated;
        - a credential-safe test endpoint probe runs (one minimal, non-mutating
          call) and its result is recorded;
        - quota and rate limits are recorded;
        - SSRF protection: resolve and validate the target address, block
          private, loopback, link-local and metadata address ranges, re-validate
          after redirects, and pin the resolved address for the request;
        - TLS verification is mandatory and non-disableable.
      Add an explicit SSRF test suite, since a connector manager that accepts a
      base URL is the classic SSRF entry point.
   6. Implement execution through one connector client providing idempotency
      keys, timeouts, bounded retry with backoff, least-privilege egress
      (reusing the P04-04 allowlist), and trace and request id propagation.
   7. Implement the failure stage with the circuit breaker, DLQ and fallback,
      and the rule "no silent data transfer": a partial or failed transfer is
      recorded and surfaced, never dropped. Track an error budget per connector.
   8. Implement retirement: disable, revoke the token at the provider where the
      provider supports it, delete the vault entry, and keep the audit trail.
      Add the revocation test the source names: after retirement, a call attempt
      fails immediately and no cached credential works.
   9. Implement synthetic probes per the validate stage's observability
      requirement, running on a schedule and feeding the P10-02 reliability
      dashboard, so a connector that silently stopped working is detected
      before a customer finds out.
  10. Record, per connector, the A04 evidence: the agreement reference, the
      licensing basis, the credential status and the sandbox probe result.
      Report how many connectors have all four and how many do not.
  11. Tests:
        a. registration with a base URL outside the allowlist -> rejected;
        b. no path returns a secret value or prefix — assert across endpoints,
           logs, traces, errors and exports;
        c. rotation with one approver -> refused; with two -> succeeds with an
           overlap, then the old credential stops working;
        d. an expiring credential -> an alert fires;
        e. the SSRF suite: private, loopback, link-local and cloud metadata
           addresses all blocked, including after a redirect;
        f. TLS verification cannot be disabled by configuration;
        g. a schema-invalid connector -> not promoted to VALIDATED;
        h. the credential-safe probe performs exactly one non-mutating call;
        i. a connector failure -> circuit opens, DLQ records it, no silent
           drop;
        j. retirement -> immediate call failure, vault entry gone, audit trail
           intact;
        k. a synthetic probe failure -> the reliability dashboard reflects it
           and an alert fires.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the Connector entity with its seven-state lifecycle
   - the dual-approved domain allowlist
   - vault integration with no read-back path
   - dual-approved rotation with overlap and automatic old-credential
     revocation, plus expiry alerts
   - validation with schema check, credential-safe probe, quota, SSRF
     protection and mandatory TLS
   - the single connector client with idempotency, timeouts, retries and egress
     control
   - circuit breaker, DLQ, error budget and no-silent-drop handling
   - retirement with provider revocation and the revocation test
   - scheduled synthetic probes feeding the dashboard
   - the per-connector A04 evidence table
   - tests/admin/connector-*.* covering cases a through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eleven tests.
   - Paste the full SSRF suite results naming each blocked address class.
   - Paste the secret non-disclosure assertion across all five surfaces.
   - Paste the A04 evidence table with the counts.
   - Acceptance criterion: register, test, rotate and revoke all work and are
     tested; no secret is ever returned; SSRF is blocked including after
     redirects.

G. COMPLETION CONTRACT
   Definition of Done: the six stages implemented with their controls, the
   vault read-back-free, rotation and revocation proven, SSRF blocked.
   Evidence to report: the eleven test outputs, the SSRF results, the secret
   non-disclosure proof, the A04 table.
   Remaining blockers: connectors without an agreement or credential cannot
   reach VALIDATED. That is the correct state; list them and name the owner.
   Next prompt: P13-03.
```

**المخرجات المتوقعة:** دورة موصل بسبع حالات، خزانة بلا مسار قراءة، حماية SSRF، اختبار إبطال.
**التحقق المطلوب:** التسجيل والاختبار والتدوير والإبطال كلها مُختبَرة؛ لا سر يُرجَع.
**الاعتمادية التالية:** `P13-03`.

---

---

### `P13-03` — القدرات الإدارية الست عشرة ومصفوفة الصلاحيات

**Phase:** `PHASE-13` · **EN title:** The sixteen admin capabilities, RBAC matrix and dual control

**المتطلبات السابقة:** `P13-02`

**المتطلبات المغطاة:** `REQ-ADM-01`, `REQ-ADM-02`, `REQ-ADM-07`, `REQ-GW-12`

**ماذا سينفذ هذا الأمر؟** ينفّذ القدرات الست عشرة في الورقة 58 ومصفوفة الصلاحيات
في الورقة 59، بتحكم مزدوج وbreak-glass منتهي الصلاحية.

**لماذا نحتاجه؟** الورقة 58 تحدد لكل قدرة دورها وموافقتها وAPIها وحدها الآمن
وأولويتها. والورقة 59 تضع مصفوفة تسعة أدوار × ثمانية أفعال بقيم دقيقة مثل
`Scoped`, `Redacted`, `Ticketed`, `Policy`, `Emergency`, `Draft`, `Approve` —
وهذه ليست نعم/لا، بل حالات وسطى يجب تنفيذها كما هي.

**ما المتطلبات السابقة؟** `P13-02`.

**ما النتيجة المتوقعة؟** ست عشرة قدرة مُنفَّذة بحدودها، ومصفوفة مفروضة باختبارات
سلبية، وbreak-glass ينتهي آلياً.

**كيف نتحقق من نجاحه؟** لكل خلية في الورقة 59 اختبار؛ وتعديل نموذج في الإنتاج
بموافقة واحدة يُرفض.

```text
TASK P13-03 — The sixteen admin capabilities, RBAC matrix and dual control

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-03
   Phase: PHASE-13
   Prerequisites: P13-02
   Requirements covered: REQ-ADM-01, REQ-ADM-02, REQ-ADM-07, REQ-GW-12

B. OBJECTIVE
   Implement the sixteen admin capabilities with their roles, approval
   requirements, APIs, safety boundaries and launch priorities, and enforce the
   nine-role by eight-action authorization matrix with its intermediate states
   — plus dual control and auto-expiring break-glass.

   Why this is necessary: sheet 58 specifies each capability's exact approval
   requirement and safety boundary. Sheet 59's matrix uses graded values —
   Scoped, Redacted, Ticketed, Policy, Emergency, Draft, Approve, Project,
   Summary — which are distinct authorization states, not yes-or-no. Sheet 70
   row 13 requires four-eyes control for production secrets and policies.
   Sheet 57 row 3 (A02) requires RBAC plus ABAC with dual control and
   append-only audit.

   SCOPE BOUNDARY: the capabilities and the matrix. The underlying services
   already exist from earlier phases; here you expose them as authorized,
   approved, audited commands and enforce the matrix.

C. CONTEXT
   Required inputs, sheet 58 rows 2-17, each as area / action / role /
   approval / API / audit / safety boundary / launch:
     Dashboard / inspect system health / Support L1 / no / GET /admin/health /
       read access / redact PII / P0
     Tenants / view own organization and projects / Support L2 / ticket / GET
       /admin/tenants/{id} / yes / scoped access plus justification / P0
     Agents / enable or disable an agent version / Platform operator / dual
       approval in production / POST /admin/agents/{id}/rollouts / yes /
       canary plus rollback / P0
     Agents / edit prompt or tool policy / AI engineer / peer approval / POST
       /admin/agent-versions / yes / version immutable after publish / P0
     Models / change model route and budget / AI operator / dual approval /
       POST /admin/model-policies / yes / shadow eval plus rollback / P0
     Integrations / register an API connector / Integration engineer / security
       approval / POST /admin/connectors / yes / secret vault, no raw secrets
       in UI / P0
     Integrations / rotate or revoke a credential / Security admin / dual
       approval / POST /admin/connectors/{id}/rotate / yes / the secret is
       never returned / P0
     Workflows / pause or resume the queue / SRE / incident / POST
       /admin/workflows/pause / yes / idempotent, drain in-flight / P0
     Execution / retry a failed task / Support L2 / policy / POST
       /admin/executions/{id}/retry / yes / no duplicate side effects / P0
     Execution / cancel an unsafe task / SRE / incident / POST
       /admin/executions/{id}/cancel / yes / compensating action / P0
     Knowledge / publish a code or standard revision / Knowledge steward /
       reviewer approval / POST /admin/knowledge/releases / yes / license plus
       source version / P0
     Support / view traces and sanitized logs / Support L2 / ticket / GET
       /admin/traces/{id} / yes / no cross-tenant access / P0
     Security / manage staff roles / Security admin / dual approval / POST
       /admin/role-assignments / yes / break-glass expires / P0
     Billing / view token spend and invoices / Finance / no / GET /admin/usage
       / yes / immutable usage ledger / P0
     Scan / inspect evidence and scan quality / Qualified reviewer / project
       authorization / GET /projects/{id}/evidence / yes / consent and
       retention / P0
     Commerce / provision a partner agent package / Sales ops / contract
       approval / POST /admin/entitlements / yes / FUTURE FEATURE / P2
   And sheet 59 rows 2-10, the matrix of nine roles against eight actions:
   view health, view customer PII, edit agent, edit API, change model, retry
   jobs, billing, approve release — with values including Yes, No, Scoped,
   Redacted, Policy, Emergency, Draft, Approve, Ticketed, Summary, Project.

D. EXECUTION INSTRUCTIONS
   1. Implement each of the sixteen capabilities as a command or a scoped read
      per P13-01, carrying exactly the role, approval requirement, API path and
      safety boundary the source assigns. Do not simplify an approval
      requirement, and do not merge two capabilities whose approvals differ
      (enabling an agent version needs dual approval in production, while
      editing a prompt needs peer approval — these are different gates).
   2. Implement the approval types as distinct mechanisms:
        - none;
        - ticket: a referenced support ticket plus a justification;
        - policy: the action is permitted only within a configured policy
          envelope, checked by the policy service;
        - incident: an open incident reference;
        - peer approval: one other qualified person, not the author;
        - dual approval: two distinct approvers, neither the author;
        - security approval: a security-role approver;
        - reviewer approval: a qualified reviewer in scope;
        - project authorization: authorization on that specific project;
        - contract approval: a signed contract reference (deferred scope).
   3. Implement the matrix from sheet 59 with its graded values as a
      data-driven policy, extending the P01-03 decision point. Each graded
      value has precise semantics you must implement:
        - Scoped: limited to the records within the actor's assignment, plus a
          justification;
        - Redacted: the data is returned with sensitive fields masked;
        - Ticketed: requires a ticket reference;
        - Policy: permitted within the configured envelope only;
        - Emergency: permitted only with an open incident, time-boxed and
          audited (SRE changing a model route);
        - Draft: may create or modify a draft but may not publish;
        - Approve: may approve another actor's draft but, per the peer and dual
          rules, not their own;
        - Project: limited to an authorized project;
        - Summary: aggregate figures only, no record-level data.
   4. Implement the separation that makes Draft and Approve meaningful: an AI
      engineer drafts an agent version and a model policy change but cannot
      approve either; a Security admin approves but, where they also drafted,
      cannot approve their own draft. Add tests for both directions.
   5. Implement break-glass per sheet 58 row 14's boundary "break-glass
      expires": dual-approved, time-boxed, scoped to named resources,
      automatically expiring without any revocation call, non-renewable
      silently, and audited to a separate stream. Reuse and verify the P01-03
      implementation.
   6. Implement the production-specific gates: enabling or disabling an agent
      version requires dual approval in production specifically, with canary
      and rollback available (reusing P05-02). A model policy change requires
      dual approval and a shadow evaluation plus rollback (reusing P04-02 and
      P04-03).
   7. Implement the safety boundaries as enforced behaviour, not notes:
      idempotent pause with in-flight drain; retry with no duplicate side
      effects (reusing P03-03); cancel with a compensating action; immutability
      after publish; license and source version checks on knowledge publication
      (reusing P06-01); no cross-tenant trace access; consent and retention
      checks on evidence inspection.
   8. Mark the Commerce capability as the source does — FUTURE FEATURE, P2 —
      and leave it unimplemented behind the PHASE-16 gate. Implement nothing of
      its behaviour.
   9. Write the negative authorization suite covering the full matrix: for
      every one of the seventy-two role-action cells, a test asserting the
      implemented behaviour matches the source's value, including the graded
      semantics. This is the A02 evidence and the sheet 59 enforcement proof.
  10. Tests:
        a. the seventy-two-cell matrix suite;
        b. an AI engineer attempting to approve their own agent version draft
           -> refused; a Security admin approving it -> permitted;
        c. a production agent rollout with one approver -> refused; with two
           distinct non-author approvers -> permitted with canary available;
        d. a model policy change without a shadow evaluation reference ->
           refused;
        e. an SRE emergency model change without an open incident -> refused;
           with one -> permitted, time-boxed and audited;
        f. break-glass expires with no revocation call and cannot be silently
           renewed;
        g. a Support L2 customer-data read without a ticket -> refused; with
           one -> Scoped and justified;
        h. a Finance billing read returns Summary-level data for roles limited
           to Summary;
        i. pause applied twice -> idempotent with in-flight drained;
        j. a knowledge publication without a license check -> refused;
        k. the Commerce entitlement endpoint -> returns a clear not-available
           response, implements nothing.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the sixteen capabilities as commands or scoped reads with their exact
     approvals and boundaries
   - the ten distinct approval mechanisms
   - the data-driven sheet 59 matrix with all nine graded value semantics
   - Draft and Approve separation enforced in both directions
   - verified auto-expiring, scoped, dual-approved break-glass
   - production-specific dual approval with canary, shadow eval and rollback
   - enforced safety boundaries reusing the earlier phases' guarantees
   - the Commerce capability left unimplemented behind the PHASE-16 gate
   - tests/admin/rbac-matrix-72.* and cases b through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the seventy-two-cell suite summary and the full cell-by-cell result
     table.
   - Paste cases b, c, e and f in full.
   - State the count: sixteen capabilities implemented or deliberately not
     implemented, and seventy-two matrix cells asserted.
   - Acceptance criterion: every matrix cell behaves exactly as the source
     specifies, no actor approves their own draft, and break-glass expires on
     its own.

G. COMPLETION CONTRACT
   Definition of Done: sixteen capabilities with correct approvals, the full
   matrix enforced and tested cell by cell, break-glass expiry verified.
   Evidence to report: the matrix result table, the named test outputs, the
   capability implementation status list.
   Remaining blockers: the Commerce capability stays deferred. Confirm it is
   inert.
   Next prompt: P13-04.
```

**المخرجات المتوقعة:** ست عشرة قدرة بموافقاتها، مصفوفة 72 خلية مفروضة، break-glass منتهٍ آلياً.
**التحقق المطلوب:** كل خلية مُختبَرة؛ لا أحد يعتمد مسودته؛ الصلاحية الطارئة تنتهي بنفسها.
**الاعتمادية التالية:** `P13-04`.

---

---

### `P13-04` — سطح الدعم والتشخيص المُحجَّب

**Phase:** `PHASE-13` · **EN title:** Support surfaces, masked diagnostics and the ops API

**المتطلبات السابقة:** `P13-03`

**المتطلبات المغطاة:** `REQ-OBS-04`, `REQ-ADM-01`, `REQ-API-09`, `REQ-TEN-07`

**ماذا سينفذ هذا الأمر؟** يبني سطح الدعم: تذاكر وتشخيص مُحجَّب ووصول JIT وإعادة
محاولة عبر runbook، ويُكمل عمليات الـAPI الإدارية في الورقة 65.

**لماذا نحتاجه؟** الورقة 03 الصف 9 تحدد بوابة الدعم: «بيانات حساسة JIT»،
و«Masking وapproval للـbreak-glass»، وحدها: «لا يغيّر قرار مراجعة أو دفع». وهذا
الحد الأخير جوهري: الدعم يُشخّص ولا يُقرّر.

**ما المتطلبات السابقة؟** `P13-03`.

**ما النتيجة المتوقعة؟** سطح دعم فعّال بلا تعريض، وحدود صلبة تمنع تغيير قرارات
المراجعة والدفع.

**كيف نتحقق من نجاحه؟** محاولة `SUPPORT_L2` تغيير قرار مراجعة أو حالة دفع تُرفض؛
والوصول JIT ينتهي آلياً.

```text
TASK P13-04 — Support surfaces, masked diagnostics and the ops API

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P13-04
   Phase: PHASE-13
   Prerequisites: P13-03
   Requirements covered: REQ-ADM-01, REQ-API-09, REQ-OBS-04, REQ-TEN-07

B. OBJECTIVE
   Build the support surface — tickets, masked diagnostics, JIT access to
   sensitive data, and runbook-driven retry — and complete the admin operations
   API, with the source's hard boundary that support can diagnose but never
   change a review decision or a payment status.

   Why this is necessary: sheet 03 row 9 defines the support portal with JIT
   sensitive data, masking and break-glass approval, and the access limit "does
   not change a review decision or payment". Sheet 04 row 9 repeats it for
   SUPPORT_L2, forbidding manually setting a reviewer decision or payment
   status. That boundary is what keeps professional and financial
   accountability intact, and it is easy to erode through a well-meaning
   support tool.

   SCOPE BOUNDARY: the support surface and the remaining sheet 65 operations.
   The runbooks themselves are P10-03; here they are exposed to support with
   the right authorization and masking.

C. CONTEXT
   Required inputs:
     - sheet 03 row 9: users L1, L2 and SRE; functions tickets, diagnosis and
       retry via runbook; sensitive data JIT; identity masking and break-glass
       approval; limit "does not change a review decision or payment"
     - sheet 04 row 9: SUPPORT_L2 may see limited logs and retry; data scope
       temporary JIT; forbidden from manually setting a reviewer decision or
       payment status; MFA plus JIT; monthly access review
     - sheet 61 rows 2-8, the seven support scenarios from P10-03
     - sheet 65 rows 2-9, the eight admin operations, of which P13-01 and
       P13-02 covered health, audit and connectors; this prompt completes:
       POST /v1/admin/agents/{id}/deployments (agents:deploy, idempotency
       required, emits agent.deployed); POST /v1/admin/executions/{id}/retry
       (executions:retry, idempotency required, emits
       execution.retry_requested); POST /v1/admin/model-policies (models:write,
       idempotency required, emits model.policy_changed); GET
       /v1/projects/{id}/scan-sessions (scan:read, emits
       scan.quality_changed)

D. EXECUTION INSTRUCTIONS
   1. Implement the ticket linkage: a support action requiring a ticket
      validates the reference against the ticketing source of truth, or, where
      none is integrated, against an internal ticket record created by a
      support lead. A free-text ticket string is not a reference — make the
      validation real or state plainly that no ticketing integration exists and
      that the internal record is the control.
   2. Implement masked diagnostics as the default and only view: a support user
      sees run state, step outcomes, error classes, timings, policy and routing
      decisions, and sanitized logs and traces — never raw customer documents,
      raw prompts, personal data beyond identifiers, or secrets. Reuse the
      P10-01 redaction so masking is applied at the data layer.
   3. Implement JIT elevation for genuinely necessary sensitive access:
      requested with a reason and a ticket, approved per the matrix,
      time-boxed, scoped to named records, auto-expiring, and audited with
      every record accessed under it recorded individually. An elevation that
      logs only its grant and not its use is insufficient for the monthly
      access review sheet 04 row 9 requires.
   4. Implement the hard boundary as a structural prohibition, which is the
      central deliverable: there is no code path, endpoint, command or script
      by which a support identity can set a reviewer decision, alter a finding
      status, set a payment state, change an invoice amount or alter a delivery
      hash. Implement it as an architectural test over the command registry and
      the route table, and demonstrate it failing when a violating command is
      introduced. Sheet 04 row 8 adds the related prohibition that FINANCE
      cannot change a delivery hash — assert that too.
   5. Implement runbook-driven retry: support invokes the P10-03 safe actions
      within its policy envelope. A retry is idempotent, records the
      justification, and cannot bypass a business gate — retrying a payment
      verification does not verify a payment, it re-runs the verification
      against the provider.
   6. Implement the remaining four sheet 65 operations with their scopes,
      idempotency requirements and events, wiring them to the existing
      capabilities: agent deployment to P05-02, execution retry to P03-03 and
      P10-03, model policy change to P04-02 and P04-03, and scan session read
      to P12-02 with consent and retention checks.
   7. Implement the monthly access review per sheet 04 row 9: a report of every
      JIT elevation, every record accessed under it, every break-glass grant,
      and every support action taken, for review by the security owner. Make it
      generated, not manual.
   8. Implement the support view of the seven scenarios from sheet 61: for each
      scenario, the surface shows the trigger, the current state, the available
      safe action within the user's authority, the escalation path and the
      evidence to capture, so the runbook is followed in the tool rather than
      from memory.
   9. Tests:
        a. a support action requiring a ticket without a valid reference ->
           refused;
        b. a diagnostic view contains no raw document, prompt, secret or
           personal data beyond identifiers — assert field-by-field against an
           allowlist;
        c. JIT elevation -> time-boxed, scoped, auto-expiring, and every record
           accessed under it individually audited;
        d. the structural prohibition test: no support path can set a reviewer
           decision, a finding status, a payment state, an invoice amount or a
           delivery hash; introduce a violating command, show the test failing,
           remove it;
        e. FINANCE cannot change a delivery hash;
        f. a support retry is idempotent and does not bypass a business gate —
           retrying payment verification re-queries the provider rather than
           marking it paid;
        g. the four sheet 65 operations enforce their scopes, idempotency and
           events;
        h. a scan session read without consent or past retention -> refused;
        i. the monthly access review report is generated and includes
           elevations, accessed records, break-glass grants and actions.
  10. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - validated ticket linkage, or an honest statement of its absence
   - data-layer masked diagnostics with an allowlisted field set
   - JIT elevation with per-record access auditing
   - the architectural prohibition on support changing review, finance or
     delivery state, with its failing demonstration
   - runbook-driven idempotent retry that cannot bypass a business gate
   - the four remaining sheet 65 operations
   - the generated monthly access review report
   - the scenario-guided support surface for sheet 61's seven cases
   - tests/admin/support-*.* covering cases a through i
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all nine tests.
   - Paste the case d prohibition test passing, failing on the injected
     command, and passing again.
   - Paste the masked diagnostic view beside its field allowlist.
   - Paste a sample monthly access review report.
   - Acceptance criterion: support can diagnose everything it needs and change
     nothing it must not, and the test proving that can fail.

G. COMPLETION CONTRACT
   Definition of Done: support surfaces working under masking and JIT, the
   structural prohibition enforced and provably testable, the ops API complete,
   access review generated.
   Evidence to report: the nine test outputs, the three prohibition test runs,
   the allowlist comparison, the review report sample.
   Remaining blockers: a ticketing integration may be absent; say so if the
   internal record is the only control. SLO targets for support response
   remain unestablished per sheet 61's "SLO pending".
   Next prompt: P14-01. PHASE-13 exit requires the boundary test green, the
   seventy-two-cell matrix green, dual control on production secrets and
   policies, connector revocation proven, and break-glass expiry verified.
```

**المخرجات المتوقعة:** تشخيص مُحجَّب، JIT بتدقيق لكل سجل، حظر بنيوي على تغيير المراجعة والدفع والتسليم.
**التحقق المطلوب:** الدعم يُشخّص ولا يُقرّر — مُثبت باختبار معماري قادر على الفشل.
**الاعتمادية التالية:** `P14-01`.


---

# PHASE-14 — التقييم والتعلم وبوابات الإصدار


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

---

### `P14-01` — المجموعات الذهبية ومحرك التقييم

**Phase:** `PHASE-14` · **EN title:** Golden datasets and the evaluation harness

**المتطلبات السابقة:** `P13-04`

**المتطلبات المغطاة:** `REQ-KNW-07`, `REQ-EVL-04`, `REQ-OBS-06`

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

---

### `P14-02` — قياس النماذج بأبعاده السبعة

**Phase:** `PHASE-14` · **EN title:** Model benchmarking across the seven evaluation dimensions

**المتطلبات السابقة:** `P14-01`

**المتطلبات المغطاة:** `REQ-EVL-04`, `REQ-GW-18`, `REQ-GW-13`, `REQ-OPN-07`

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

---

### `P14-03` — بوابة الانحدار الحاجزة

**Phase:** `PHASE-14` · **EN title:** The blocking regression gate

**المتطلبات السابقة:** `P14-02`

**المتطلبات المغطاة:** `REQ-EVL-03`, `REQ-AGT-06`, `REQ-OBS-06`, `REQ-OPN-02`

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

---

### `P14-04` — دفتر الأدلة وفرض بوابات الإصدار

**Phase:** `PHASE-14` · **EN title:** Evidence ledger and enforced release gates

**المتطلبات السابقة:** `P14-03`

**المتطلبات المغطاة:** `ADR-008`, `REQ-GOV-04`, `REQ-GOV-07`, `REQ-GOV-08`, `REQ-EVL-01`, `REQ-EVL-02`, `REQ-EVL-05`, `REQ-EVL-06`, `REQ-EVL-07`, `REQ-EVL-08`, `REQ-EVL-09`, `REQ-EVL-10`

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

---

### `P14-05` — دورة التعلم وحكومة الإصدار المستمرة

**Phase:** `PHASE-14` · **EN title:** Continuous learning loop and ongoing release governance

**المتطلبات السابقة:** `P14-04`

**المتطلبات المغطاة:** `REQ-OBS-06`, `REQ-OBS-07`, `REQ-REV-07`, `REQ-EVL-05`, `REQ-OPN-02`

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


---

# PHASE-15 — التوسع في المسارات التخصصية


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

---

### `P15-01` — بوابة إدخال القوالب الجديدة

**Phase:** `PHASE-15` · **EN title:** The workflow onboarding gate

**المتطلبات السابقة:** `P14-05`

**المتطلبات المغطاة:** `REQ-EXP-07`, `REQ-EXP-06`, `REQ-SVC-01`

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

---

### `P15-02` — مسارات BIM والكميات

**Phase:** `PHASE-15` · **EN title:** BIM coordination and quantity take-off workflows

**المتطلبات السابقة:** `P15-01`

**المتطلبات المغطاة:** `REQ-EXP-01`, `REQ-EXP-02`, `REQ-DAT-07`, `REQ-INT-05`

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

---

### `P15-03` — MEP والبنية التحتية والموقع وPMO

**Phase:** `PHASE-15` · **EN title:** MEP, infrastructure, site report and the PMO capabilities

**المتطلبات السابقة:** `P15-02`

**المتطلبات المغطاة:** `REQ-EXP-03`, `REQ-EXP-04`, `REQ-EXP-05`, `REQ-AGT-09`, `REQ-EXP-07`

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


---

# PHASE-16 — التجارة المؤجلة (خارج نطاق الإطلاق)


## حالة هذه المرحلة: مُغلقة

المصدر يؤجّل هذا النطاق صراحةً. الورقة 68 الصف 8:

> «White-label، والمستأجرون الخارجيون، وبيع الاشتراكات **مؤجلة صراحةً**»
> (Commercialization: White-label, external tenants and subscription sales are
> explicitly deferred).

والورقة 68 الصف 3 تحدد نطاق الإطلاق: «تشغيل أحادي المستأجر مملوك الآن؛ بدائيات
واعية بالمستأجر للمستقبل». والورقة 57 الصف 9 (`A08`) تصنّف الأثر إن تجاهلنا ذلك:
«Scope creep»، والتنفيذ المطلوب: «مستأجر واحد أولاً مع فرض سياق المستأجر».

لذلك هذه المرحلة **لا تُنفَّذ** إلا بتفويض مكتوب من المالك يرفع هذا التأجيل.

## لماذا تُدرَج المرحلة إذاً؟

لأن المصدر يحتوي ستة أوراق كاملة من المواصفات التجارية (43 إلى 48 و53 و55)،
وتجاهلها كان سيُنتج مكتبة أوامر ناقصة التغطية. وجودها هنا — مُعلَّمة ومُبوَّبة —
يحقق أمرين: تغطية كاملة للمصدر، ومنع التنفيذ غير المصرح به.

## الأوراق المُغطاة ولم تُنفَّذ

| الورقة                  | المحتوى                                                 | حالة المصدر               |
| ----------------------- | ------------------------------------------------------- | ------------------------- |
| `43_COMMERCE_OVERVIEW`  | ثماني قدرات تجارية `COM-01..COM-08`                     | `DESIGN ONLY`             |
| `44_TENANT_BLUEPRINT`   | ثمانية كيانات مستأجرين (جزء منها مُنفَّذ في `PHASE-01`) | `DESIGN ONLY`             |
| `45_AGENT_MARKETPLACE`  | تسعة حقول كتالوج الوكلاء                                | `SPEC`                    |
| `46_AGENT_STUDIO`       | ثماني مراحل استوديو الوكلاء                             | `SPEC`                    |
| `47_WHITE_LABEL_PORTAL` | خمسة أنماط تسليم بعلامة بيضاء                           | `SPEC`                    |
| `48_BILLING_CONTRACTS`  | ستة SKUs للفوترة                                        | `SPEC`                    |
| `53_B2B_API_CONTRACT`   | تسع عمليات API للأعمال                                  | `SPEC`                    |
| `55_REQUIREMENTS_DELTA` | عشرة فروق `D01..D10`                                    | `P0` داخل نطاق B2B المؤجل |

## ما نُفِّذ فعلاً من هذه الأوراق في مراحل أخرى

لتجنّب الالتباس: الأجزاء التي تخدم التشغيل أحادي المستأجر **نُفِّذت** في مراحل
سابقة، لأن المصدر يطلب «بدائيات واعية بالمستأجر»:

- `tenant_id` والعزل والـRLS: `PHASE-01` (`REQ-TEN-01`..`REQ-TEN-09`).
- كيانات `Organization`, `Tenant`, `Workspace`, `Membership`, `Project`,
  `EvidencePackage`, `AuditEvent` من الورقة 44: `PHASE-01`.
- عدادات الاستخدام ودفتره (`COM-07`): `PHASE-04` و`PHASE-08`.
- تصدير البيانات وحذفها (`COM-08`): `PHASE-11`.
- سطوح القراءة الإدارية للمناطق التجارية: `PHASE-13`.

**غير المُنفَّذ** هو السلوك التجاري متعدد المستأجرين: الكتالوج، والاستحقاقات،
والاشتراكات، والعلامة البيضاء، والدومينات المخصصة، والتضمين، وبيع الحزم.

## شروط الدخول

تفويض مكتوب من المالك يرفع التأجيل المسجَّل في الورقة 68 الصف 8، مُسجَّل في
`docs/OPEN-DECISIONS.md` ضد `OD-08`.

## شروط الخروج

لا تنطبق أثناء التأجيل. إن صدر التفويض: اجتياز اختبارات الاستحقاق والعلامة
والدومين والتضمين ومطابقة الفوترة، تحت دليل عزل متعدد المستأجرين.

## المتطلبات المغطاة في هذه المرحلة

`REQ-GOV-02`, `REQ-DEF-01`..`REQ-DEF-06`, `REQ-AGT-10`, `REQ-AGT-11`

---

## الأوامر التنفيذية

---

### `P16-01` — بوابة التفويض (الأمر الوحيد القابل للتنفيذ الآن)

**Phase:** `PHASE-16` · **EN title:** Commerce authorization gate and scope assessment

**المتطلبات السابقة:** `P14-04`

**المتطلبات المغطاة:** `REQ-GOV-02`, `REQ-DEF-05`, `REQ-DEF-06`

**ماذا سينفذ هذا الأمر؟** لا يبني أي ميزة تجارية. يُنتج تقييم نطاق وتفويضاً
صريحاً: ما الذي يلزم فعلاً لرفع التأجيل، وما تكلفته، وما مخاطره.

**لماذا نحتاجه؟** لأن القرار بين «مستأجر واحد الآن» و«تجارة متعددة المستأجرين»
قرار تجاري للمالك، لا قرار هندسي. والورقة 55 تحدد عشرة فروق `D01..D10` كلها
`P0` **داخل نطاق B2B** — وهذه الصياغة بالضبط هي ما يجعل تجاهلها خطأً وتنفيذها
بلا تفويض خطأً أيضاً.

**ما المتطلبات السابقة؟** `P14-04` — دفتر الأدلة يعمل، فنعرف الحالة الحقيقية
قبل إضافة نطاق.

**ما النتيجة المتوقعة؟** وثيقة تقييم نطاق وقرار مُسجَّل: إما تفويض مكتوب، أو
إبقاء التأجيل.

**كيف نتحقق من نجاحه؟** لا كود تجاري مُضاف؛ ووثيقة التقييم تربط كل فرق من
العشرة بتكلفته وأثره الأمني.

```text
TASK P16-01 — Commerce authorization gate and scope assessment

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P16-01
   Phase: PHASE-16 (Deferred commerce — explicitly out of launch scope)
   Prerequisites: P14-04 (the evidence ledger reflects the real platform state)
   Requirements covered: REQ-GOV-02, REQ-DEF-05, REQ-DEF-06

B. OBJECTIVE
   Produce a scope and risk assessment for lifting the commerce deferral, and
   record the owner's explicit decision. Build no commercial feature.

   Why this is necessary: sheet 68 row 8 explicitly defers white-label,
   external tenants and subscription sales. Sheet 68 row 3 scopes the launch to
   single-tenant owned operation with tenant-aware primitives. Sheet 57 row 9
   (A08) names the risk of ignoring that as scope creep. Sheet 55 marks its ten
   deltas P0 — but P0 within the B2B scope, which is precisely the phrasing
   that makes both ignoring them and implementing them without authorization
   wrong. The decision is commercial and belongs to the owner.

   SCOPE BOUNDARY: assessment and decision recording only. Do not create a
   catalog, an entitlement service, a branding service, a custom domain path,
   an embed token, a subscription or a B2B endpoint. Do not add a database
   table for any of them. If you find yourself writing commercial logic, stop.

C. CONTEXT
   Required inputs:
     - sheet 43 rows 2-9 (COM-01..COM-08, all DESIGN ONLY)
     - sheet 44 rows 2-9 (tenant blueprint entities; note which are already
       implemented in PHASE-01)
     - sheet 45 rows 2-10 (marketplace catalog fields, SPEC)
     - sheet 46 rows 2-9 (agent studio stages, SPEC)
     - sheet 47 rows 2-6 (five white-label delivery modes, SPEC)
     - sheet 48 rows 2-7 (six billing SKUs, SPEC, with the explicit caveat that
       prices are to be set commercially)
     - sheet 53 rows 2-10 (nine B2B API operations, SPEC)
     - sheet 55 rows 2-11 (ten deltas D01..D10 with owners, reference sheets
       and validation methods)
     - sheet 54 rows 2-11 for the go-live gates that are specifically B2B:
       G02 agent entitlement, G03 B2B billing and metering, G04 custom domain
       and SSO, G09 white-label security — all P0 release blockers, all
       UNVERIFIED
     - docs/evidence/GATE-ASSESSMENT.md from P14-04 for the platform's real
       current state

D. EXECUTION INSTRUCTIONS
   1. Write docs/commerce/SCOPE-ASSESSMENT.md. For each of the ten deltas
      D01..D10 from sheet 55, record:
        - the delta as the source states it;
        - what already exists from the earlier phases (several are partly
          satisfied: tenant isolation from PHASE-01, usage metering from
          PHASE-04 and PHASE-08, data export and deletion from PHASE-11, RAG
          tenant isolation from PHASE-06);
        - what remains genuinely unbuilt;
        - its security implications, especially for the four B2B go-live gates;
        - an engineering effort estimate with its basis;
        - its dependency on other unresolved open decisions.
   2. Assess the security surface that multi-tenant commerce adds, honestly and
      specifically:
        - custom domains and SSO introduce DNS verification, certificate
          management, CORS and token-scoping risk (sheet 47 row 3 requires DNS
          TXT proof, TLS and CORS; sheet 54 row 5 makes it a P0 gate);
        - the embedded widget introduces frame-ancestors, origin checking and
          signed short-lived token risk (sheet 47 row 4; sheet 43 row 6 states
          iframe permissions must not be bypassable);
        - white-label branding introduces an HTML and CSS injection surface
          (sheet 46 row 5 restricts it to safe HTML and CSS tokens only, and
          sheet 54 row 10 makes white-label security a P0 gate);
        - the agent studio introduces tenant-supplied prompt and tool
          configuration, which is an injection and privilege surface (sheet 45
          row 8 requires signed versioned config and that customization cannot
          break protection);
        - tenant-supplied knowledge corpora multiply the rights-gate and
          isolation surface (sheet 46 row 4);
        - entitlement becomes a security control, not a billing nicety: sheet
          45 row 10 requires that revocation immediately rejects new requests.
      State plainly that each of these is a new attack surface on a platform
      whose P0 security gates are not yet all green.
   3. Assess the operational surface: per-tenant quotas and fairness (sheet 45
      row 9, sheet 54 row 8), support for tenants you do not control, billing
      disputes and reconciliation across tenants (sheet 48, sheet 54 row 4),
      and the sales-to-provisioning process (sheet 43 row 7, which forbids
      automatically creating a paid subscription without a contract).
   4. State the prerequisite position clearly: which currently-open P0 gates
      must be PASS before multi-tenant commerce is responsible to ship. At
      minimum, tenant isolation (sheet 54 G01), engineer sign-off (G10) and
      disaster recovery (G12) should be evidenced before adding external
      tenants, because a multi-tenant failure is a multi-customer failure.
   5. Record the commercial inputs the owner must supply, which are entirely
      absent from the source: the pricing for every SKU in sheet 48 (the source
      says prices are to be set commercially), the contract templates, the
      trademark and IP terms for white-label (sheet 48 row 5 names them), and
      the tax treatment of subscriptions.
   6. Present the decision options neutrally, with their consequences:
        a. keep the deferral — the blueprint's execution scope ends at
           PHASE-15;
        b. lift it partially, for example a single named enterprise customer
           under a bespoke contract, which avoids the catalog and subscription
           machinery while still requiring the isolation and billing gates;
        c. lift it fully, which means building sheets 43 through 48 and 53 and
           satisfying the four B2B P0 gates.
      Give a recommendation with reasoning. Do not make the decision.
   7. Record the owner's answer against OD-08 in docs/OPEN-DECISIONS.md with
      the date, the decider and the scope authorized. If the answer is to keep
      the deferral, that is a complete and successful outcome for this prompt.
   8. Add a guard test asserting no commercial feature has been built: no
      catalog, entitlement, subscription, branding, custom-domain or embed
      table, endpoint or service exists. This test protects against gradual,
      unauthorized scope creep, which is exactly the risk sheet 57 row 9 names.
   9. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - docs/commerce/SCOPE-ASSESSMENT.md covering all ten deltas with existing,
     remaining, security, effort and dependencies
   - the security and operational surface assessment
   - the prerequisite gate position
   - the list of owner-supplied commercial inputs
   - three decision options with consequences and a recommendation
   - the recorded decision against OD-08
   - tests/governance/no-commerce-scope-creep.* as a standing guard
   - docs/EXECUTION-LOG.md entry
   NO commercial feature code.

F. VERIFICATION
   - Paste the scope assessment's delta table.
   - Paste the guard test output confirming no commercial feature exists.
   - Paste the recorded OD-08 decision, or state that the owner has not yet
     answered and that the deferral therefore stands.
   - Acceptance criterion: a complete, honest assessment exists; no commercial
     code was written; the decision is recorded or explicitly pending.

G. COMPLETION CONTRACT
   Definition of Done: the assessment written, the guard test in place, the
   decision recorded or pending.
   Evidence to report: the delta table, the guard test, the decision state.
   Remaining blockers: the decision itself is the owner's. If the deferral
   stands, say so plainly and stop — do not proceed to P16-02.
   Next prompt: P16-02, ONLY if the owner's recorded decision authorizes it.
```

**المخرجات المتوقعة:** وثيقة تقييم نطاق، تقييم سطح أمني، قرار مُسجَّل، اختبار حارس ضد التوسع غير المصرح به.
**التحقق المطلوب:** لا كود تجاري مُضاف؛ القرار مُسجَّل أو مُعلَّق صريحاً.
**الاعتمادية التالية:** `P16-02` — فقط عند تفويض مُسجَّل.

---

---

### `P16-02` — تنفيذ التجارة متعددة المستأجرين (مشروط بالتفويض)

**Phase:** `PHASE-16` · **EN title:** Multi-tenant commerce implementation (conditional on authorization)

**المتطلبات السابقة:** `P16-01`

**المتطلبات المغطاة:** `REQ-DEF-01`, `REQ-DEF-02`, `REQ-DEF-03`, `REQ-DEF-04`, `REQ-AGT-10`, `REQ-AGT-11`

**ماذا سينفذ هذا الأمر؟** ينفّذ الاستحقاقات والكتالوج والعلامة البيضاء والفوترة
وعقود B2B — **فقط** إذا كان قرار المالك المُسجَّل يُفوّض ذلك.

**لماذا نحتاجه؟** لإكمال تغطية المصدر. الأوراق 43 إلى 48 و53 مواصفات حقيقية
بحالة `SPEC` و`DESIGN ONLY`، ولها بوابات إصدار `P0` خاصة بها في الورقة 54.

**ما المتطلبات السابقة؟** `P16-01` **مع** قرار مُسجَّل يُفوّض التنفيذ. بلا ذلك،
هذا الأمر لا يُنفَّذ.

**ما النتيجة المتوقعة؟** استحقاق مفروض وقت التشغيل، وعلامة بيضاء آمنة، وفوترة
مُطابَقة — أو لا شيء، إن لم يصدر التفويض.

**كيف نتحقق من نجاحه؟** تشغيل وكيل بلا استحقاق فعّال يُرفض؛ وعزل بين مؤسستين
مُثبت؛ ومطابقة فاتورة مع الاستهلاك.

```text
TASK P16-02 — Multi-tenant commerce implementation (conditional on authorization)

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P16-02
   Phase: PHASE-16
   Prerequisites: P16-01 complete AND a recorded owner decision against OD-08
                  in docs/OPEN-DECISIONS.md that authorizes implementation,
                  naming the authorized scope
   Requirements covered: REQ-AGT-10, REQ-AGT-11, REQ-DEF-01, REQ-DEF-02,
                         REQ-DEF-03, REQ-DEF-04

B. STOP CONDITION — CHECK THIS FIRST
   Read docs/OPEN-DECISIONS.md and find OD-08.
   - If OD-08 is unresolved, or records that the deferral stands, or does not
     exist: STOP. Do not implement anything. Report that PHASE-16 remains
     closed per sheet 68 row 8, and that the blueprint's execution scope ends
     at PHASE-15.
   - If OD-08 records an authorization, implement only the scope it names. A
     partial authorization (for example a single enterprise customer under a
     bespoke contract) does NOT authorize the catalog, the studio or
     subscription sales.
   Do not treat this prompt's existence as authorization. Do not infer
   authorization from the owner's enthusiasm, from a conversation, or from the
   presence of specifications in the source. Only the recorded OD-08 decision
   authorizes work here.

C. OBJECTIVE
   Implement the authorized subset of multi-tenant commerce: agent
   entitlement, the catalog, tenant agent configuration, white-label delivery,
   billing and the B2B API — each behind its own P0 release gate.

   Why this is necessary: sheets 43 through 48 and 53 specify this scope, and
   sheet 54 defines four B2B-specific P0 release blockers for it. If the owner
   authorizes commercialization, these are the requirements.

   SCOPE BOUNDARY: only what OD-08 authorizes. Everything else stays closed.

D. CONTEXT
   Required inputs:
     - docs/commerce/SCOPE-ASSESSMENT.md from P16-01
     - sheet 45 rows 2-10, the catalog fields with their enforcement and
       acceptance, including that an unlicensed agent cannot run and that
       revocation immediately rejects new requests
     - sheet 46 rows 2-9, the eight studio stages with their platform
       validation, API, security policy and output
     - sheet 47 rows 2-6, the five delivery modes with their guardrails: org
       routing verification; DNS TXT proof, TLS and CORS; CSP frame-ancestors
       and origin checks; scopes, webhooks and quotas; isolation and residency
       review
     - sheet 48 rows 2-7, the six SKUs with their units, entitlements,
       overages, controls, lifecycles and commercial caveats
     - sheet 53 rows 2-10, the nine B2B operations with their error cases,
       access control and SLO evidence
     - sheet 43 rows 2-9, the eight commerce capabilities with their
       acceptance tests
     - sheet 54 rows 3, 4, 5, 10 — the four B2B P0 gates

E. EXECUTION INSTRUCTIONS
   1. Implement entitlement as a runtime security control, not a billing
      record: every agent run performs an entitlement preflight, and an agent
      without an active entitlement is refused. Sheet 45 row 10 requires that
      revocation take effect on new requests immediately, and sheet 52 row 4's
      acceptance is that an unlicensed run is denied. Implement revocation as
      immediate, not eventually-consistent.
   2. Implement the catalog per sheet 45 with versioned immutable SKUs,
      capability schemas, bundles, dependency resolution that rejects an
      incomplete bundle, an approved-model pool enforced by the P04-02 registry,
      human gates, signed versioned customization, and per-tenant limits on
      concurrency, requests per minute, spend and tokens.
   3. Implement tenant agent configuration per sheet 46 with its critical
      security property from row 3: a tenant configuration cannot override the
      system prompt or the platform's protections. Tenant-supplied prompts,
      rules, tools and knowledge are untrusted input and are subject to the
      P05-03 trust labels and the P05-02 tool allowlist. Run the P11-04
      adversarial suite against tenant-supplied configuration specifically.
   4. Implement tenant knowledge upload per sheet 46 row 4 with licence check,
      malware scan and provenance, into a tenant RAG namespace, reusing P06-01
      and P06-02 unchanged — the rights gate applies to tenant-supplied sources
      exactly as it does to platform sources.
   5. Implement branding per sheet 46 row 5 and sheet 47: contrast and image
      size validation, domain ownership verification by DNS TXT, and safe HTML
      and CSS tokens only. Treat the branding payload as untrusted and render
      it through a strict allowlist; a tenant-supplied style must not be able to
      execute script or exfiltrate via CSS. Add an injection test suite.
   6. Implement the delivery modes the authorization covers, each with its
      guardrails: hosted with verified org routing; custom domain with DNS
      proof, TLS and CORS; embedded widget with CSP frame-ancestors, origin
      checks and short-lived signed tokens; API-only with scopes, webhooks and
      quotas; enterprise private with an isolation and residency review.
   7. Implement billing per sheet 48 on top of the P08-04 ledger: per-SKU
      units, included entitlements, overage charges, hard and soft budgets, and
      the lifecycle each SKU names. Enforce sheet 43 row 7's rule that no paid
      subscription is created automatically without a contract. Leave every
      price as owner-supplied configuration — the source states prices are to
      be set commercially, so ship no default price.
   8. Implement the nine B2B operations of sheet 53 with their exact error
      cases: 409 on a duplicate organization, 422 on an invalid or incompatible
      configuration, 403 on an unsigned contract or an out-of-scope token, 409
      on unmet dependencies or a domain conflict, 402 on quota and 403 on
      license for a run, 404 on a missing catalog entry.
   9. Implement the sales-assisted path per sheet 43 row 7 and sheet 52 row 3:
      lead to quote to contract with dual approval, and provisioning only after
      a signed contract.
  10. Satisfy the four B2B P0 gates with real evidence, into the P14-04 ledger:
        - G02 entitlement: three-agent and four-agent bundles, revocation and
          an expired contract;
        - G03 billing and metering: invoice reconciliation, caps and refunds;
        - G04 custom domain and SSO: ownership proof, OIDC and token rotation;
        - G09 white-label security: CSP, CORS, domain routing and brand
          isolation.
  11. Run the full cross-organization isolation suite, extending P11-04's
      cross-tenant category to two real organizations with separate brands,
      domains, knowledge namespaces and entitlements. Sheet 43 row 4's
      acceptance is a leak-prevention test between two organizations, and
      sheet 43 row 5's is that one organization's identity is never exposed to
      another.
  12. Remove or update the P16-01 guard test, which asserted no commercial
      feature exists. Replace it with a scope-conformance test asserting that
      only the authorized subset was built.
  13. Tests:
        a. an agent run with no active entitlement -> refused;
        b. revocation -> the next request is refused immediately;
        c. an incomplete bundle -> rejected on dependency resolution;
        d. a model outside the approved pool -> blocked;
        e. a tenant configuration attempting to override the system prompt or a
           protection -> refused; the adversarial suite against tenant
           configuration passes;
        f. tenant knowledge from an unlicensed source -> refused by the rights
           gate;
        g. branding injection attempts -> neutralized; no script execution and
           no CSS-based exfiltration;
        h. a custom domain without DNS proof -> not activated;
        i. an embedded widget from an unapproved origin -> refused by CSP and
           origin checks;
        j. a subscription creation attempt without a signed contract ->
           refused;
        k. all nine B2B operations return their documented error codes under
           real conditions;
        l. the two-organization isolation suite passes across database, object
           storage, queues, vector namespaces, caches, traces, brands and
           domains;
        m. invoice reconciliation against metered usage balances;
        n. the scope-conformance test confirms only the authorized subset
           exists.
  14. Append to docs/EXECUTION-LOG.md.

F. DELIVERABLES
   Only within the authorized scope:
   - runtime entitlement preflight with immediate revocation
   - the versioned catalog with dependency resolution and per-tenant limits
   - tenant agent configuration that cannot override protections
   - tenant knowledge upload through the unchanged rights gate
   - branding with strict allowlisting and an injection test suite
   - the authorized delivery modes with their guardrails
   - billing with owner-supplied prices and contract-gated provisioning
   - the nine B2B operations with their exact error cases
   - the sales-assisted provisioning path
   - evidence for the four B2B P0 gates in the ledger
   - the two-organization isolation suite
   - the scope-conformance test replacing the P16-01 guard
   - docs/EXECUTION-LOG.md entry

G. VERIFICATION
   - Paste the OD-08 authorization you acted on, with its named scope.
   - Paste the output of all fourteen test groups.
   - Paste the two-organization isolation results across all eight surfaces.
   - Paste the four B2B gate records with their evidence.
   - Paste the scope-conformance test confirming nothing beyond the
     authorization was built.
   - Acceptance criterion: no unlicensed run is possible, revocation is
     immediate, no tenant configuration can weaken a protection, two
     organizations are provably isolated, and only the authorized scope exists.

H. COMPLETION CONTRACT
   Definition of Done: the authorized subset implemented with its four P0 gates
   evidenced and cross-organization isolation proven.
   Evidence to report: the authorization, the test outputs, the isolation
   results, the gate records, the scope-conformance proof.
   Remaining blockers: prices, contract templates, trademark and IP terms and
   tax treatment are owner-supplied. Report any P0 gate still open — and note
   that adding external tenants while a platform P0 security gate is open is a
   decision the owner must make explicitly, not a gap to work around.
   Next prompt: none. This is the final prompt in the library. Return to
   PHASE-14's governance cycle for ongoing operation.
```

**المخرجات المتوقعة:** لا شيء — إلا إذا كان `OD-08` يُفوّض؛ وحينها النطاق المُفوَّض فقط.
**التحقق المطلوب:** التفويض مُسجَّل ومُقتبَس؛ عزل مؤسستين مُثبت على ثمانية أسطح؛ اختبار مطابقة النطاق ناجح.
**الاعتمادية التالية:** لا شيء — هذا آخر أمر في المكتبة.


---

## نهاية المكتبة

آخر أمر في المكتبة هو `P16-02`، وهو مشروط بتفويض مكتوب من المالك.
إن بقي تأجيل التجارة قائماً (وهو الوضع المسجَّل في المصدر، الورقة 68
الصف 8)، فإن نطاق التنفيذ ينتهي عند `PHASE-15`، ويستمر التشغيل عبر
دورة الحكومة في `PHASE-14`.

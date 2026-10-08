# API_AND_EVENT_CONTRACTS — Sketch Design

عقود الواجهات البرمجية والأحداث.

> **حالة هذه العقود: `DESIGNED`.**
> المرجع الشامل يصف سطح الواجهة بأنه _illustrative contracts_. لذلك ما يلي **مقترح تنفيذي مشتق**،
> وليس عقدًا مُصادقًا عليه. لا يجوز لأي أمر أن يعامله كعقد مُثبَّت قبل مصادقة مالك المنتج المسجّلة
> (قرار مفتوح `OD-V2-03`). ما هو **مُلزَم** من المصدر: أسماء النقاط التسع ومسؤولياتها. ما هو **مشتق**:
> أشكال الأجسام ورموز الأخطاء أدناه.

---

## 1. السطح الأدنى المُلزَم | Minimum mandated surface

| النقطة                            | المسؤولية (من المصدر، حرفيًا)                                  |
| --------------------------------- | -------------------------------------------------------------- |
| `POST /v1/projects`               | Create project and assign owner                                |
| `POST /v1/projects/{id}/evidence` | Signed-upload initiation; evidence metadata and consent        |
| `POST /v1/workflows`              | Start idempotent, policy-checked workflow                      |
| `GET /v1/workflows/{id}`          | Durable state and trace-linked progress                        |
| `GET /v1/workflows/{id}/events`   | Authenticated SSE/event feed; no fabricated updates            |
| `GET /v1/agents`                  | Visible permitted capabilities and versions                    |
| `POST /v1/admin/connectors`       | Admin-reviewed connector configuration; secret references only |
| `GET /v1/admin/observability`     | Aggregated metrics, scoped by role                             |
| `POST /v1/reviews/{id}/decision`  | Qualified reviewer sign-off and audit record                   |

## 2. قواعد عامة تسري على كل نقطة | Cross-cutting rules

- كل طلب مصادق عليه يحمل مُستفيدًا محلولًا: `{ user_id, tenant_id, organization_id, roles[], verification_state }`.
- كل طفرة حالة تُصرَّح وتُدقَّق في الخادم. التصريح لا يُستنتج من الواجهة.
- كل طفرة خارجية تحمل `Idempotency-Key`. تكرار المفتاح يُعيد النتيجة الأصلية ولا ينشئ سجلًا ثانيًا.
- كل استجابة تحمل `trace_id`.
- مورد لا يملك المستفيد حق قراءته يُرجع `404`، لا `403`، فلا يُسرَّب وجوده.
- لا حقل في أي استجابة قادر على حمل قيمة سرّ. هذا يُفرض بالمخطط لا بالمراجعة.

## 3. رموز الرفض المقصودة | Intentional refusal codes

هذه ليست أعطالًا. هي السلوك الصحيح عند نقص مُدخَل أو قرار، ويجب ألا تُستبدل بقيمة افتراضية.

| الرمز                             | متى يُرجَع                     | البديل الخاطئ الذي يُمنع     |
| --------------------------------- | ------------------------------ | ---------------------------- |
| `NO_ELIGIBLE_ROUTE`               | لا مرشح نماذج يحقق القيود      | إرخاء قيد لإنتاج إجابة       |
| `BUDGET_NOT_CONFIGURED`           | ميزانية لم تُضبَط قط           | اعتبارها غير محدودة          |
| `BUDGET_EXCEEDED`                 | تقدير التكلفة يخرق حدًا صارمًا | التنفيذ ثم الإبلاغ           |
| `RATE_CARD_INCOMPLETE`            | لا بند تسعير مطابق             | تسعير بصفر                   |
| `CONFIDENCE_NOT_ESTABLISHED`      | لا ثقة قياس مُسجَّلة           | رقم ثقة مُقدَّر              |
| `PLAN_NOT_ESTABLISHED`            | خطة المهام لم تُحدَّد          | نسبة مئوية محسوبة في المتصفح |
| `ATTRIBUTION_INCOMPLETE`          | نتيجة حرجة بلا اقتباس          | خفض تصنيفها إلى غير حرجة     |
| `SOURCE_RIGHTS_NOT_CLEARED`       | مصدر حقوقه غير مُخلّصة         | الإجابة من ذاكرة النموذج     |
| `TOOL_NOT_ALLOWED`                | أداة خارج قائمة الوكيل         | بناء الأداة ثم رفضها         |
| `REVIEW_BOUNDARY_VIOLATION`       | مراجع غير مؤهل لعائلة النتيجة  | مسار إقرار يتجاوز الحد       |
| `QUALIFICATION_NOT_VALID`         | مؤهل منتهٍ أو ملغى             | قبول التوقيع                 |
| `NO_QUALIFIED_REVIEWER_AVAILABLE` | لا مراجع مؤهل لعائلة           | التوجيه لمراجع غير مؤهل      |
| `RETRY_NOT_PERMITTED`             | مهمة غير عديمة التأثر بالتكرار | إعادة محاولة تُضاعف أثرًا    |
| `EVALUATION_NOT_RUN`              | إصدار بلا تشغيل تقييم          | ترقية بلا تقييم              |
| `THRESHOLD_NOT_SET`               | عتبة بلا أساس مُسجَّل          | عتبة افتراضية                |
| `REVIEW_NOT_PERFORMED`            | بند قانوني بلا مراجع مسمّى     | افتراض الامتثال              |

## 4. عقد بث الأحداث | Event feed contract

`GET /v1/workflows/{id}/events` — تدفّق أحداث مصادق عليه.

```
event: state_transition
id: <event_id>
data: {
  "event_id": "...", "workflow_id": "...", "task_id": "..." | null,
  "state": "queued|validating|running|waiting-for-input|human-review|completed|failed",
  "occurred_at": "<RFC3339>", "trace_id": "..."
}
```

- الحدث يُبثّ **بعد** تثبيت الحالة، فلا يرى العميل حالة غير مُلتزَمة.
- الاستئناف عبر `Last-Event-ID` بلا فجوة ولا تكرار.
- الحالات السبع حصرية. حالة غير معروفة تُعرض بوصفها غير معروفة ولا تُسقَط على أقرب حالة.
- لا يحمل التدفق نسبة مئوية ولا زمن إنجاز إلا ما اشتُقّ من `{ completed_tasks, total_planned_tasks }` الفعليين.

## 5. عقود داخلية حاكمة | Governing internal contracts

**استدعاء النموذج** — `invoke(task_descriptor, inputs, policy_context)`
حيث `task_descriptor = { task_type, sensitivity_class, residency_requirement, required_modalities[], language_requirements, risk_action_class, professional_consequence_class }`.

**استدعاء الأداة** — `invoke_tool(task_identity, tool_name, args)`: يفحص `tool_name` مقابل قائمة إصدار
الوكيل **قبل أي شيء آخر**، ويرفض بـ `TOOL_NOT_ALLOWED`.

**الاسترجاع** — `retrieve(query, policy_context) -> passages[]` حيث يحمل كل مقطع
`{ source_id, version, effective_date, jurisdiction, locator }` كاملة، وإلا لا يُرجَع للاقتباس.

**التوقيع** — `{ signature_id, document_digest_sha256, signer_user_id, qualification_ref, signed_at, algorithm, key_ref }`.
التحقق يُعيد حساب البصمة من البايتات المخزَّنة ولا يثق ببصمة محفوظة.

**حدث تدقيق** — `{ event_id, occurred_at, actor_type, actor_id, action, target_type, target_id, before_ref, after_ref, request_id, trace_id, outcome }`.
الجدول ملحق فقط، ومنع التعديل والحذف مفروض بصلاحيات قاعدة البيانات لا بعُرف التطبيق.

## 6. ما ليس في هذه الوثيقة | Explicit gaps

- **لا عقود فوترة أو اشتراكات.** مؤجَّلة بقرار معماري `ADR-V2-009`.
- **لا عقد ختم إلكتروني خارجي.** `P11` يبني الارتباط بالبصمة فقط، والكفاية القانونية `BLOCKED`.
- **لا مخطط OpenAPI مُصادَق عليه.** يُولَّد في `P04` ويُصادَق عليه قبل أن يُعامل كعقد مُثبَّت.

---

## 7. عقود كيانات الحوكمة التشغيلية | Operational governance entity contracts

> ## ⚠️ مصدرية هذا القسم | PROVENANCE OF THIS SECTION
>
> **`NEW USER DIRECTIVE / GOVERNANCE ADDITION`**
>
> كل ما في القسم 7 **توجيه مالك المستودع**، وليس متطلبًا مستخرجًا من
> `Sketch_Design_Ultimate_Master_Reference_2026.docx` ولا من
> `Sketch_Design_Model_Gateway_Observability_v11.md`.
>
> **لا يُنسب أي بند هنا إلى `SRC-01` أو `SRC-02`.** سجلّه في
> `execution/_registry/governance-additions.tsv`، منفصلًا عن
> `v2-requirements.tsv` الذي تحمل صفوفه مصدرية مشتقة من المصادر وحدها.
>
> حالة هذه العقود `DESIGNED`. **لا يوجد تنفيذ ولا قاعدة بيانات ولا اختبار تشغيلي** لأيٍّ منها.
> ما يُتحقَّق منه آليًا اليوم هو **اكتمال العقد نصًّا** عبر `_tools/check_governance_contracts.py`،
> وهذا ليس تحققًا من نظام عامل.

## 7.0 قواعد عامة على كل كيان | Rules binding every entity below

- كل كيان يحمل `tenant_id` غير قابل للإفراغ، ويُفرض نطاقه في طبقة البيانات لا في الكود وحده.
- كل الأوقات أوقات خادم بصيغة RFC3339، ولا تُقبل من العميل.
- `id` معرّف داخلي من نوع UUID، **ولا يُعرض في أي مسار عام** حيث يوجد معرّف عام بديل.
- كل طفرة تُدقَّق في `AuditEvent`، وكل طفرة خارجية تحمل `Idempotency-Key`.
- الحقل الغائب يُسمّى برمز رفض مقصود (القسم 3)، ولا يُستبدل بقيمة افتراضية.

## 7.1 `Request` — كيان الاستقبال المستقل

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | مفتاح داخلي |
| `tenant_id` | UUID | إلزامي، مفروض في طبقة البيانات |
| `submitted_by` | UUID | صاحب الطلب الفعلي |
| `request_type` | enum | نوع الطلب |
| `raw_summary` | text | نص الطلب كما وصل، **لا يُحوَّل إلى قرار** |
| `context_json` | json | الموقع/المدينة/القيود |
| `status` | enum | `received` · `triaged` · `converted` · `rejected` |
| `converted_project_id` | UUID \| null | **صفر أو مشروع واحد فقط** |
| `created_at` | timestamp | وقت الخادم |

**القيود المُلزَمة:**

- `UNIQUE (converted_project_id) WHERE converted_project_id IS NOT NULL` — **طلب واحد لا يُنتج مشروعين، ومشروع واحد لا ينتمي لطلبين.**
- `status = 'converted'` ⟺ `converted_project_id IS NOT NULL`. يُفرض بقيد تحقق، لا بعُرف تطبيقي.
- `Request` **ليس** `Project`. لا تُشتق حالة المشروع من حالة الطلب ولا العكس.

## 7.2 `Project` — المشروع ودورة حياته

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | مفتاح داخلي، **لا يُعرض في مسار عام** |
| `public_code` | text | **معرّف عام غير كاشف للـUUID** |
| `tenant_id` | UUID | إلزامي |
| `owner_id` | UUID | مالك المشروع |
| `source_request_id` | UUID | مرجع الطلب، فريد |
| `title` | text | اسم قابل للعرض |
| `summary` | text | لا يستبدل الأدلة |
| `context_json` | json | موقع/مدينة/نوع/قيود |
| `lifecycle` | enum | **مفردات مستقلة تمامًا عن حالة المهمة** |
| `blocker_code` | text \| null | إلزامي عند `BLOCKED` |
| `created_at`, `updated_at` | timestamp | وقت الخادم |
| `closed_at` | timestamp \| null | إلزامي عند `CLOSED` |

**`public_code` — القيود الكاملة:**

1. `UNIQUE (tenant_id, public_code)`.
2. **لا يُشتق من الـUUID** بأي تحويل عكوس: لا hex، ولا base32/base58/base64 للبايتات، ولا أي ترميز يستعيد الأصل.
3. **لا يُستخدم مفتاحًا داخليًا ولا مفتاحًا خارجيًا** في أي جدول. العلاقات تمر بـ`id` حصرًا.
4. مجال المحارف مُعلَن ومحدود، وطوله ثابت المدى، ولا يحمل دلالة ترتيبية تكشف حجم النشاط.

**`lifecycle` (مفردات المشروع — سبع قيم):**
`INTAKE` · `ACTIVE` · `PAUSED` · `BLOCKED` · `READY_FOR_REVIEW` · `DELIVERED` · `CLOSED`

**قواعد الانتقال:**

- `→ READY_FOR_REVIEW` ممنوع مع وجود مهمة حرجة غير مكتملة.
- `→ DELIVERED` ممنوع دون `ReviewDecision` صالح.
- `→ CLOSED` ممنوع دون `DeliveryManifest` أو سبب إغلاق مسجَّل.
- `BLOCKED` ليست فشلًا: تحمل `blocker_code` ومالكًا ووقت فتح.

> **فصل صريح:** مفردات `lifecycle` أعلاه **لا تتقاطع** مع حالات المهمة في 7.3.
> لا يُقرأ `Project.lifecycle` من `Task.status` ولا يُكتب أحدهما من الآخر.

## 7.3 `Task` — المهمة وحالتها وحجبها

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | — |
| `project_id` | UUID | إلزامي |
| `kind` | enum | `requirements` · `analysis` · `evidence` · `review` · `delivery` · `operational` |
| `title` | text | يصف ناتجًا أو فعلًا |
| `status` | enum | **الحالات السبع حصرًا** (أدناه) |
| `priority` | enum | `critical` · `high` · `normal` · `low` |
| `assignee_id` | UUID \| null | **إلزامي حين `kind = review`** |
| `depends_on` | UUID[] | مراجع مهام سابقة |
| `is_idempotent` | boolean | يُعلَن في التعريف؛ `false` يمنع إعادة المحاولة |
| `created_at`, `started_at`, `completed_at` | timestamp | أوقات خادم |

**`status` — سبع قيم، ولا ثامنة:**
`queued` · `validating` · `running` · `waiting-for-input` · `human-review` · `completed` · `failed`

> هذه هي القائمة التي يثبّتها `UR-009` من المصدر المعتمد. **لم تُعدَّل.**

**الحجب خاصية عمودية (orthogonal)، لا حالة:**

| الحقل | النوع | القيد |
| --- | --- | --- |
| `blocked` | boolean | مستقل تمامًا عن `status` |
| `block_code` | text \| null | إلزامي حين `blocked = true` |
| `block_reason` | text \| null | إلزامي حين `blocked = true` |
| `blocked_owner` | UUID \| null | إلزامي حين `blocked = true` |
| `blocked_at` | timestamp \| null | إلزامي حين `blocked = true` |
| `expected_resolution_at` | timestamp \| null | اختياري |
| `next_action` | text \| null | إلزامي حين `blocked = true` |

**قيود:**

- `blocked = true` ⟹ `block_code`، `block_reason`، `blocked_owner`، `blocked_at`، `next_action` كلها غير فارغة.
- **`BLOCKED` ليست قيمة مسموحة في `status`.** إضافتها تتطلب اعتماد مالك المنتج — انظر `RC-02`.
- مهمة محجوبة قد تكون في أي حالة من السبع. الحجب يصف عائقًا، لا موضعًا في المسار.

## 7.4 `Evidence` — الدليل

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | — |
| `project_id` / `task_id` | UUID | أحدهما على الأقل غير فارغ |
| `kind` | enum | `document` · `image` · `measurement` · `test_run` · `log` · `decision_support` · `export` |
| `source` | enum | `upload` · `generated` · `external_reference` |
| `version` | integer | إصدار الدليل، متزايد |
| `author_id` | UUID | منشئ الدليل أو هوية النظام |
| `storage_ref` | text | مرجع تخزين، **لا الملف نفسه داخل سجل القرار** |
| `content_sha256` | char(64) | **محسوبة من البايتات المخزَّنة في الخادم** |
| `metadata_json` | json | MIME، حجم، origin، consent، jurisdiction، الوحدات |
| `state` | enum | `UPLOADING` · `QUARANTINED` · `AVAILABLE` · `REJECTED` · `REVOKED` |
| `created_at` | timestamp | — |

**قيود:** لا يبلغ الدليل `AVAILABLE` قبل اجتياز الحجر **و** تطابق التجزئة. تغيير البايتات بعد التوقيع يُبطل كل `ReviewDecision` يستشهد به (7.5).

## 7.5 `ReviewDecision` — قرار المراجعة

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | — |
| `project_id` / `task_id` | UUID | نطاق القرار |
| `reviewer_id` | UUID | **مراجع بشري فعلي؛ لا هوية نظام** |
| `reviewer_accreditation_id` | UUID | مؤهل مطابق لعائلة القدرة، سارٍ وقت القرار |
| `decision` | enum | `APPROVE` · `REJECT` · `REQUEST_CHANGES` · `BLOCK` |
| `scope` | text | ما يغطيه القرار **وما لا يغطيه** |
| `evidence_refs` | UUID[] | **غير فارغ، وكل مرجع موجود وحالته `AVAILABLE`** |
| `document_digest_sha256` | char(64) | بصمة المخرج المُراجَع بعينه |
| `covered_finding_ids` | UUID[] | إضافة نتيجة بعد القرار تُبطل التغطية |
| `supersedes_id` | UUID \| null | القرار السابق إن وُجد |
| `audit_event_id` | UUID | مرجع سجل التدقيق |
| `created_at` | timestamp | — |

**قيود:** السجل ملحق فقط. لا موافقة ذاتية حيث تنطبق قاعدة الشخصين. مؤهل منتهٍ ⟹ `QUALIFICATION_NOT_VALID`.

## 7.6 `DeliveryManifest` — بيان التسليم

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | — |
| `project_id` | UUID | إلزامي |
| `version` | integer | متزايد لكل مشروع، `UNIQUE (project_id, version)` |
| `recipient_id` | UUID | **المستلم الفعلي** |
| `included_task_ids` | UUID[] | المهام الداخلة |
| `included_evidence_ids` | UUID[] | الأدلة الداخلة |
| `required_review_decision_ids` | UUID[] | **غير فارغ** |
| `included_file_refs` | json[] | `{storage_ref, filename, content_sha256, bytes}` لكل ملف |
| `manifest_digest_sha256` | char(64) | بصمة البيان نفسه |
| `state` | enum | `DRAFT` · `READY` · `SENT` · `ACKNOWLEDGED` · `REVOKED` |
| `created_at`, `sent_at`, `acknowledged_at` | timestamp | أوقات خادم |

**قيود الاكتمال المرجعي:** لا يبلغ البيان `READY` ما لم يكن المشروع والمستلم والمهام والأدلة وقرارات المراجعة والملفات والنسخة كلها حاضرة ومُحالة إلى سجلات موجودة. البيان بعد `SENT` **ثابت**؛ التصحيح نسخة جديدة. التراجع لا يحذف تدقيقًا ولا دليلًا.

## 7.7 `Accreditation` — الاعتماد المهني

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | — |
| `account_id` | UUID | صاحب المؤهل |
| `type` | enum | **`INTERIM` أو `OFFICIAL` فقط** |
| `specialty` | text | التخصص |
| `membership_ref` | text \| null | مرجع عضوية، لا وثيقة حساسة بلا ضرورة |
| `status` | enum | `PENDING` · `VERIFIED` · `REJECTED` · `EXPIRED` · `REVOKED` |
| `decision_ref` | UUID | قرار بشري موجود |
| `provider_ref` | text \| null | **إلزامي حين `type = OFFICIAL`** |
| `valid_from`, `expires_at` | timestamp | انتهاء صريح |
| `events` | append-only | `submit` · `approve` · `reject` · `revoke` · `expire` |

**القواعد الصارمة:**

1. `type = OFFICIAL` ⟹ `provider_ref` غير فارغ **و** يوجد قرار اعتماد مزوّد موثَّق.
2. **`INTERIM` لا يُعرض ولا يُصدَّر ولا يُطبع بوصفه `OFFICIAL`**، ولا بأي صياغة توحي بذلك. كل سطح عرض يحمل النوع صراحةً.
3. `status = PENDING` لا يُعامل معاملة `VERIFIED` في أي مسار.
4. **محظور صراحةً:** وصف صفحة دخول، أو CAPTCHA، أو بحث عام، بأنه «تحقق حكومي» أو «اعتماد رسمي» أو ما يرادفهما. لا يصير الاعتماد رسميًا إلا بـ`provider_ref` ومزوّد مُعتمَد.

## 7.8 `AuditEvent` — حدث التدقيق

| الحقل | النوع | القيد |
| --- | --- | --- |
| `event_id` | UUID | — |
| `occurred_at` | timestamp | وقت الخادم |
| `actor_type` | enum | `user` · `service` · `scoped_task_identity` |
| `actor_id` | UUID | — |
| `action` | text | — |
| `target_type`, `target_id` | text, UUID | — |
| `before_ref`, `after_ref` | text \| null | مراجع حالة، لا نسخ كاملة |
| `request_id`, `trace_id` | text | — |
| `outcome` | enum | `allow` · `deny` · `error` |

**قيود:** الجدول **ملحق فقط**؛ `UPDATE` و`DELETE` مسحوبتان من دور التطبيق بصلاحيات قاعدة البيانات. لا يحذفه تراجع ولا نسخة.

## 7.9 `UsageRecord` — سجل الاستهلاك

| الحقل | النوع | القيد |
| --- | --- | --- |
| `invocation_id` | UUID | — |
| `tenant_id`, `project_id`, `workflow_run_id` | UUID | الإسناد |
| `agent_version_id`, `model_candidate_id` | UUID | — |
| `input_tokens`, `output_tokens` | integer | — |
| `cost_sar` | numeric \| `RATE_CARD_INCOMPLETE` | **لا صفر عند غياب البند** |
| `cost_source` | text | مصدر السعر |
| `recorded_at` | timestamp | — |

**قيود:** ملحق فقط، ويُكتب حتى عند فشل الاستدعاء.

## 7.10 `OutboxEvent` — صندوق الصادر المعامِلي

| الحقل | النوع | القيد |
| --- | --- | --- |
| `id` | UUID | — |
| `aggregate_type` | text | نوع الكيان صاحب التغيير |
| `aggregate_id` | UUID | معرّفه |
| `event_type` | text | نوع الحدث |
| `payload` | json | الحمولة |
| `idempotency_key` | text | `UNIQUE` |
| `occurred_at` | timestamp | وقت التغيير |
| `published_at` | timestamp \| null | فارغ حتى أول نشر ناجح |
| `publish_attempts` | integer | يبدأ صفرًا ويتزايد |
| `last_error` | text \| null | آخر سبب فشل |
| `status` | enum | `PENDING` · `PUBLISHING` · `PUBLISHED` · `FAILED` · `DEAD_LETTER` |

**القواعد المُلزَمة:**

1. **الكتابة الذرّية:** تغيير النطاق و`OutboxEvent` المقابل يُكتبان **في المعاملة نفسها**. لا يُسمح بمعاملتين، ولا بنشر قبل التثبيت. فشل أيٍّ منهما يُرجِع الاثنين.
2. **النشر لاحق ومنفصل** عن المعاملة، ويقرأ الصفوف `PENDING`.
3. **قابل لإعادة المحاولة:** الفشل يزيد `publish_attempts` ويكتب `last_error` ويُبقي الصف قابلًا للالتقاط؛ تجاوز الحد ينقله إلى `DEAD_LETTER` مرئيًا للمشغّل.
4. **منع التكرار:** `idempotency_key` فريد، والمستهلك يتجاهل مفتاحًا رآه. التسليم مرة واحدة على الأقل، والأثر مرة واحدة بالضبط.
5. `status = PUBLISHED` ⟺ `published_at` غير فارغ.

## 7.11 التتبّع | Traceability

`P-GOV` ⟷ العقود 7.1–7.10 ⟷ `governance-additions.tsv` (`GOV-01`…`GOV-08`)
⟷ `RC-02` (حالات المهمة) ⟷ `GAP-07` (مصدر غير مُرفَق) ⟷ `OD-V2-12` (Manus API).

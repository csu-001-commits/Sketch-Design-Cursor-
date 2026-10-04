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

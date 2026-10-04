<!-- promptmeta
id: P10
file: P10_GOLDEN_WORKFLOW_VILLA.md
stage: 3 — Golden workflow
title_en: Villa review golden workflow, end to end
prereq: P09
requirements: UR-022,UR-011,UR-023,UR-009
status: DESIGNED
-->

# P10_GOLDEN_WORKFLOW_VILLA — Villa review golden workflow, end to end

**المسار الذهبي لمراجعة الفيلا من الطلب إلى التسليم**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 3 — Golden workflow |
| المتطلب السابق | P09 |
| المتطلبات المغطّاة | UR-022، UR-011، UR-023، UR-009 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ المسار الذهبي العشري لمراجعة فيلا سكنية كاملًا من الاستقبال والموافقة إلى تقرير مُصدَّر ومُسلَّم بعد مراجعة بشرية مؤهلة.

**لماذا نحتاجه؟**  
المرجع يجعل هذا المسار بوابة المرحلة الثالثة، ودليل خروجها أثر حقيقي قابل لإعادة الإنتاج باقتباسات. المسار الذهبي هو ما يثبت أن الطبقات السابقة تعمل معًا لا منفردة.

**ما المتطلبات السابقة؟**  
اكتمال P09 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
تشغيل واحد كامل ينتج تقريرًا مُصدَّرًا باقتباسات وأثرًا قابلًا لإعادة الإنتاج ومراجعة مهندس موثقة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا لم يُنتج تشغيلان متتاليان على نفس المدخلات أثرًا متكافئًا، أو إذا سُلّم تقرير دون مراجعة بشرية مسجّلة.

## EXECUTABLE PROMPT

```text
You are executing P10_GOLDEN_WORKFLOW_VILLA of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Compose the platform's first complete, end-to-end engineering workflow — villa review across all ten reference steps — producing a real artifact with citations and a reproducible trace.

2. DEPENDENCIES
P09 — this workflow exercises orchestration, gateway, agents, engines and knowledge together.

3. EXACT SCOPE
IN SCOPE:
- All ten steps: intake and consent; upload and integrity scan; drawing and context classification; evidence validation; discipline task planning; parallel deterministic checks and specialist agents; conflicting-finding reconciliation; source and confidence audit; qualified human review; versioned report and delivery.
- A reconciliation step that surfaces conflicting findings rather than selecting a winner automatically.
- A source and confidence audit step that fails the run when a critical finding lacks attribution.
- Report generation producing a versioned document with every finding linked to its evidence, agent execution and reviewer disposition.
- A fixture project with representative drawings, checked in, so the workflow is reproducible by anyone.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not issue any structural, permit or certification claim. The workflow produces a reviewed engineering report, not an approval.
- Do not auto-deliver. Delivery follows the recorded human review decision.
- Do not add disciplines beyond those the fixture and the registered agents actually cover; name the uncovered ones as gaps.

4. FILES AND MODULES AFFECTED
- workflows/villa-review/
- workflows/villa-review/steps/
- fixtures/villa-review/ — representative drawings and expected findings
- services/delivery/ — report assembly and versioning

5. REQUIRED CONTRACTS
- The workflow definition pins an exact agent version per step and an exact engine version per calculation.
- Reconciliation output: { finding_group_id, conflicting_findings[], reconciliation_state } where reconciliation_state is one of RESOLVED_BY_RULE, RESOLVED_BY_REVIEWER or UNRESOLVED. An UNRESOLVED group blocks delivery.
- The source and confidence audit returns ATTRIBUTION_INCOMPLETE naming each critical finding that lacks a citation, and the run moves to failed rather than to human-review.
- The delivered report carries { report_version, workflow_run_id, agent_versions[], engine_versions[], knowledge_source_versions[], reviewer_id, reviewed_at, finding_count }.
- Two runs over identical fixture inputs produce traces that are equivalent in structure, pinned versions, deterministic calculation values and finding identities. Free-text wording may differ; the structural equivalence is what is asserted.

6. IMPLEMENTATION INSTRUCTIONS
- Run discipline checks in parallel but reconcile serially, so a conflict cannot be hidden by ordering.
- Treat an unresolved conflict as a blocker, not a note. The reference requires reconciliation before delivery.
- Make the trace the primary artifact: every finding resolves to its evidence package, its agent execution, its model invocation and its reviewer disposition in a single query.
- Check the fixture into the repository with a declared expected-findings file, and assert against it. A fixture whose expectations drift silently is worthless.
- Never present a finding whose confidence is unknown as though it were established. Carry CONFIDENCE_NOT_ESTABLISHED through to the report.
- If the fixture cannot exercise a step because an upstream capability is incomplete, mark that step BLOCKED in the run record and say so in the report rather than skipping it quietly.

7. SECURITY REQUIREMENTS
- The fixture must contain no real customer data. Use synthetic or explicitly licensed drawings and record their provenance.
- The report is access-controlled to the project and tenant; a report URL is not a capability.
- Delivery requires the reviewer's recorded decision; a delivery without one is refused by the delivery service, not merely discouraged by the UI.
- Report versions are immutable; a correction produces a new version and the superseded version remains retrievable for audit.

8. AUTOMATED TESTS
- End-to-end: the full ten-step run over the fixture completes and produces a report.
- End-to-end: two runs over identical inputs produce structurally equivalent traces, asserted field by field over pinned versions, deterministic values and finding identities.
- Integration: an injected unresolved conflict blocks delivery.
- Integration: an injected critical finding without attribution fails the run at the audit step with the finding named.
- Integration: an attempt to deliver without a reviewer decision is refused by the delivery service.
- Integration: a retried failed step does not duplicate a finding or a billable record.
- Regression: the expected-findings fixture file is asserted against, and a drift fails the build.

9. ACCEPTANCE CRITERIA
- One complete run produces a versioned report whose every finding resolves to evidence, agent execution and reviewer disposition in a single trace query.
- Reproducibility is proven by two runs compared field by field.
- Delivery without human review is impossible at the service layer.
- Unresolved conflicts and missing attributions block, proven by injection.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The end-to-end run's trace export, with the trace identifier.
- The generated report file itself, with its citations.
- The two-run structural comparison output.
- The injection test outputs for unresolved conflict, missing attribution and missing reviewer decision.
- An explicit statement of which of the ten steps were fully exercised by the fixture and which were marked BLOCKED, with the reason for each.

11. ROLLBACK INSTRUCTIONS
Repin the workflow definition to the previous version. Reports already delivered are never retracted by a rollback; a correction is issued as a new report version with a stated reason, and the superseded version remains retrievable. Record the affected run identifiers.

12. DEFINITION OF DONE
- A real artifact exists, produced by a real run, with a trace that a third party can follow.
- The report explicitly names any step that was BLOCKED rather than implying full coverage.
- Reproducibility is asserted mechanically, not described.
- Status recorded as VERIFIED only once the run has been reproduced independently from the checked-in fixture by someone other than its author; otherwise TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


<!-- promptmeta
id: P19
file: P19_EVALUATION_AND_QUALITY_REGRESSION.md
stage: 6 — Launch readiness
title_en: Evaluation suites, quality regression detection and promotion gating
prereq: P18
requirements: UR-024,UR-031,UR-036
status: DESIGNED
-->

# P19_EVALUATION_AND_QUALITY_REGRESSION — Evaluation suites, quality regression detection and promotion gating

**مجموعات التقييم وكشف تراجع الجودة وبوابة الترقية**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 6 — Launch readiness |
| المتطلب السابق | P18 |
| المتطلبات المغطّاة | UR-024، UR-031، UR-036 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يبني مجموعات التقييم لكل وكيل، ويكشف تراجع الجودة عند تغيّر النموذج أو التلقين، ويربط الترقية بنتيجة التقييم.

**لماذا نحتاجه؟**  
المرجع يشترط ترقية عبر تقييم مرحلي واعتماد بشري، ويجعل نسبة نجاح التقييم وجودة الاقتباس ونسبة تجاوز المراجع مؤشرات رصد. بلا تقييم لا يمكن اكتشاف تراجع النموذج.

**ما المتطلبات السابقة؟**  
اكتمال P18 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
مجموعة تقييم لكل وكيل بمجموعة ذهبية، وكشف تراجع عند كل تغيير، وبوابة ترقية لا تُفتح بدون نتيجة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا رُقّي إصدار بنتيجة تقييم أسوأ من الأساس دون اعتماد صريح مسجّل، أو إذا اعتُمد عتبة غير محددة.

## EXECUTABLE PROMPT

```text
You are executing P19_EVALUATION_AND_QUALITY_REGRESSION of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Build the evaluation layer that makes quality drift detectable: per-agent suites with golden sets, regression detection on every model, prompt or agent change, and promotion gated on recorded results.

2. DEPENDENCIES
P18 — evaluation runs against the security-verified system and feeds the release gates.

3. EXACT SCOPE
IN SCOPE:
- A golden evaluation set per agent, with expected outputs or expected properties, reviewed by a qualified person where the domain requires it.
- Evaluation dimensions: task correctness, citation presence and accuracy, schema conformance, refusal appropriateness, latency and cost.
- Regression detection: a run compares against the recorded baseline and reports per-dimension deltas.
- Promotion gating: an agent version cannot be promoted without an evaluation run, and a regression beyond the declared tolerance requires an explicit recorded human override.
- Reviewer override rate tracked as a production quality signal and fed back into evaluation priorities.
- Model candidate benchmarking as the gate the Model Gateway's approval state depends on.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not set a pass threshold without an authorized basis. An unset threshold blocks promotion and never defaults to pass.
- Do not use production customer data in evaluation sets without an authorized, recorded basis.
- Do not report an evaluation score that was not produced by an executed run.

4. FILES AND MODULES AFFECTED
- evaluation/suites/
- evaluation/golden/
- evaluation/runner/
- evaluation/baselines/

5. REQUIRED CONTRACTS
- An evaluation run records { suite_id, agent_version_id, model_candidate_id, prompt_version_id, per_dimension_scores, baseline_ref, deltas, run_at, executed_by }.
- Promotion requires an evaluation run whose run_at is after the version's creation and whose deltas are within tolerance, or an override record naming the approver and the reason.
- A dimension with no declared threshold reports THRESHOLD_NOT_SET and blocks promotion.
- A model candidate's approval_state cannot move to APPROVED without a benchmark run record and a data-policy record.
- Golden set items carry provenance and, where the domain requires professional judgement, the identity of the qualified person who validated the expected output.

6. IMPLEMENTATION INSTRUCTIONS
- Make the evaluation run a prerequisite of promotion in the data model, so promotion without evaluation is impossible rather than discouraged.
- Compare against a recorded baseline, not against a remembered impression. Baselines are versioned artifacts.
- Report per-dimension deltas rather than a single composite score, because a composite hides a correctness regression behind a latency improvement.
- Never report a score for a run that did not execute. A missing run is reported as EVALUATION_NOT_RUN.
- Feed reviewer overrides back: a rising override rate on a family is the earliest honest signal that an agent is degrading.
- Where a golden expected output requires professional judgement, record who validated it. An unvalidated engineering expectation is not a ground truth.

7. SECURITY REQUIREMENTS
- Evaluation sets containing customer-derived content are access-controlled and their use is authorized and recorded.
- Evaluation runs are isolated from production data stores.
- Evaluation results are append-only; a rerun creates a new record rather than replacing one.
- Override approvals follow the two-person rule from P16.

8. AUTOMATED TESTS
- Unit: promotion is rejected when no evaluation run exists for the version.
- Unit: a dimension without a threshold reports THRESHOLD_NOT_SET and blocks.
- Unit: a regression beyond tolerance blocks promotion absent an override record.
- Integration: an override requires a distinct approver and is audited.
- Integration: changing the model candidate, the prompt version or the agent version each independently triggers a new evaluation requirement.
- Integration: a candidate without a benchmark record cannot reach APPROVED.
- Meta: a test asserts that no code path writes an evaluation score without an associated executed run record.

9. ACCEPTANCE CRITERIA
- Promotion without evaluation is impossible.
- Unset thresholds block rather than default.
- Every golden expected output requiring professional judgement names its validator.
- No score exists without an executed run, proven by the meta test.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The promotion-gating test output.
- A baseline file and a regression run showing per-dimension deltas.
- The golden set manifest listing each item's provenance and, where applicable, its professional validator.
- The meta test output proving no fabricated scores can be written.
- An explicit statement of which agents have evaluation suites and which do not, with the gap named.

11. ROLLBACK INSTRUCTIONS
Baselines are versioned and additive; a rollback repins the active baseline rather than deleting the newer one. Never delete an evaluation run record on rollback: the record of a failed run is exactly what a later investigation needs.

12. DEFINITION OF DONE
- Evaluation is a structural precondition of promotion.
- The absence of fabricated scores is proven by a meta test, not by policy.
- Agents without suites are named as gaps rather than assumed covered.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


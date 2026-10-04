<!-- promptmeta
id: P08
file: P08_DETERMINISTIC_ENGINEERING_TOOLS.md
stage: 2 — Model Gateway
title_en: Deterministic engineering engines and the calculation boundary
prereq: P07
requirements: UR-033,UR-021
status: DESIGNED
-->

# P08_DETERMINISTIC_ENGINEERING_TOOLS — Deterministic engineering engines and the calculation boundary

**المحركات الهندسية الحتمية وحدود الحساب**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 2 — Model Gateway |
| المتطلب السابق | P07 |
| المتطلبات المغطّاة | UR-033، UR-021 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يبني محركات الحساب الحتمية — الهندسة الرقمية، حصر الكميات، التحقق الأبعادي — ويفصلها فصلًا تامًا عن الاستدلال الاحتمالي.

**لماذا نحتاجه؟**  
المرجع يفرض أن تمر الرياضيات عبر محركات حتمية باختبارات وحدة وتفاوتات عددية، لا عبر نموذج لغوي. النموذج يستخرج، والحاسبة تحسب.

**ما المتطلبات السابقة؟**  
اكتمال P07 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
محركات حتمية قابلة لإعادة الإنتاج بالبت، بتفاوتات معلنة، ووحدات صريحة، وتفشل بوضوح عند نقص المدخلات.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا أنتج محرك نتيجة مختلفة لنفس المدخلات، أو إذا قُبل حساب بوحدات غير معلنة، أو إذا استُخدم نموذج لغوي كمصدر لرقم نهائي.

## EXECUTABLE PROMPT

```text
You are executing P08_DETERMINISTIC_ENGINEERING_TOOLS of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement the deterministic engineering engines and enforce the boundary that separates deterministic calculation from probabilistic reasoning, so that no final engineering number originates from a language model.

2. DEPENDENCIES
P07 — engines are registered as tools and run under the agent runtime's allowlist and sandbox.

3. EXACT SCOPE
IN SCOPE:
- Geometry and CAD measurement engine with declared numerical tolerances.
- Quantity take-off engine: a language model may extract line items and their attributes; only the engine computes quantities and applies rates.
- Unit handling: every quantity carries a unit; conversion is explicit and tested.
- A rate card interface with an explicit incomplete state.
- Dimensional validation: cross-checks between extracted and computed values, surfacing discrepancies as typed findings.
- Each engine declares determinism: same inputs, same outputs, bitwise, recorded by a reproducibility test.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not implement structural adequacy determination. The reference confines the platform to screening and calculation assistance under licensed professional validation.
- Do not populate a rate card with invented prices.
- Do not allow an engine to accept a value whose unit is unknown.

4. FILES AND MODULES AFFECTED
- services/engineering-tools/geometry/
- services/engineering-tools/qto/
- services/engineering-tools/units/
- services/engineering-tools/validation/

5. REQUIRED CONTRACTS
- Every engine function is pure with respect to its declared inputs: no clock, no randomness, no network, no ambient configuration.
- Quantity: { value, unit, method, tolerance, source_refs[] }. A quantity without a unit cannot be constructed.
- Pricing: price(quantity, rate_card_version) -> { amount_sar, rate_ref } or RATE_CARD_INCOMPLETE naming the missing item. It never returns zero for a missing rate.
- Extraction and calculation are separate calls with separate records: an extraction record names the model invocation; a calculation record names the engine version. A number may cite only a calculation record as its origin.
- Tolerances are declared per engine and recorded on every result. A result without a tolerance is invalid.

6. IMPLEMENTATION INSTRUCTIONS
- Forbid network and clock access inside engine code and prove it with a test that fails if either is reachable.
- Make unit-bearing types the only way to express a quantity, so a bare number cannot be passed by accident.
- Record the engine version on every calculation, so a later correction can identify affected results.
- Where extraction confidence is low, the engine still calculates from what it was given and the finding carries the extraction confidence separately. Never blend a confidence into a number.
- Fail loudly on missing rate card entries. RATE_CARD_INCOMPLETE is correct behavior given an incomplete rate card and must not be engineered away with a default.
- Cross-check extracted against computed values and emit a typed discrepancy finding rather than choosing a winner.

7. SECURITY REQUIREMENTS
- Engines are the highest-trust computation in the platform and therefore accept only validated, typed input; never raw document text.
- Engine code has no outbound network capability in the sandbox.
- Rate card changes are authorized and audited; a rate change is a financial control, not a configuration tweak.
- Discrepancy findings are never suppressed by configuration.

8. AUTOMATED TESTS
- Property: for every engine, the same inputs produce bitwise-identical outputs across repeated runs and across process restarts.
- Unit: constructing a quantity without a unit fails to compile or raises, depending on language.
- Unit: unit conversion round-trips within the declared tolerance, across a generated unit matrix.
- Unit: a missing rate yields RATE_CARD_INCOMPLETE and never 0.
- Unit: a result without a tolerance is rejected.
- Integration: an attempt to open a network socket from engine code fails the test.
- Integration: a discrepancy between extracted and computed values produces a typed finding and neither value is silently dropped.
- Golden: a fixed worked example with hand-verified expected values, checked into the repository with its derivation.

9. ACCEPTANCE CRITERIA
- Every engine is bitwise reproducible, proven across process restarts.
- No engine can reach the network or the clock.
- No final number in the system cites a model invocation as its origin, proven by a trace query over the finding records.
- Missing rates surface as RATE_CARD_INCOMPLETE.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The reproducibility test output across repeated runs and restarts.
- The network-isolation test output.
- A trace query over finding records showing that every numeric finding's origin is a calculation record.
- The golden worked example with its hand-derivation and the engine's matching output.

11. ROLLBACK INSTRUCTIONS
Engines are versioned and additive: a rollback repins the tool registration to the previous engine version. Results already computed are not recomputed by a rollback; instead record the engine version range affected so a corrective recomputation can be scheduled under authorization. Never silently overwrite a previously delivered calculation.

12. DEFINITION OF DONE
- Determinism is proven, not declared.
- The model-to-number boundary is proven by a trace query over real records.
- The golden example's derivation is checked in and independently reproducible.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


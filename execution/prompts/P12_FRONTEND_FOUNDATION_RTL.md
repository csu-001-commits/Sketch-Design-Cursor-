<!-- promptmeta
id: P12
file: P12_FRONTEND_FOUNDATION_RTL.md
stage: 4 — Frontend
title_en: Design system, Arabic-first RTL foundation and brand fidelity
prereq: P11
requirements: UR-001,UR-002,UR-003,UR-004,UR-005,UR-052
status: DESIGNED
-->

# P12_FRONTEND_FOUNDATION_RTL — Design system, Arabic-first RTL foundation and brand fidelity

**نظام التصميم وأساس RTL العربي أولًا والالتزام بالهوية**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 4 — Frontend |
| المتطلب السابق | P11 |
| المتطلبات المغطّاة | UR-001، UR-002، UR-003، UR-004، UR-005، UR-052 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يبني نظام التصميم ورموزه وأساس RTL العربي أولًا، ملتزمًا بالهوية المعتمدة والصور المرجعية المعتمدة الاتجاه.

**لماذا نحتاجه؟**  
المرجع يحدد لوحة ألوان ونبرة بصرية ومحظورات صريحة، ويشترط ألا تُستبدل الواجهة المعتمدة بلوحة عامة. والصور المرفقة اتجاه معتمد لا لقطات من منصة عاملة.

**ما المتطلبات السابقة؟**  
اكتمال P11 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
نظام تصميم برموز مطابقة، ودعم RTL كامل، ومكتبة مكونات تُقاس بصريًا مقابل الصور المعتمدة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا ظهرت أي قيمة لون خارج الرموز، أو إذا انكسر أي تخطيط في RTL، أو إذا خالف أي مكوّن قائمة المحظورات البصرية.

## EXECUTABLE PROMPT

```text
You are executing P12_FRONTEND_FOUNDATION_RTL of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Establish the design system, the Arabic-first RTL foundation and the brand constraints, so that every later screen is built from tokens that already match the approved visual direction.

2. DEPENDENCIES
P11 — the frontend consumes the APIs completed through P11; building it earlier would mean building against contracts that are still moving.

3. EXACT SCOPE
IN SCOPE:
- Design tokens for color, type scale, spacing, radius, elevation and motion, with the reference's color values recorded as the approved starting point and marked approximate as the reference marks them.
- RTL as the default direction, with logical properties throughout; LTR is the mirrored case, not the base.
- Arabic typography: a legible Arabic-first sans, validated numeral formatting, and line-height and letter-spacing tuned for Arabic rather than inherited from a Latin scale.
- A component library covering the primitives the approved screens use: navigation, cards, status chips, stepper, data table, file list, panel, modal, form controls.
- Accessibility baseline: contrast, focus visibility, keyboard operability, semantic structure, and screen reader labelling in Arabic.
- A visual regression harness capturing each component in both directions.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not ship the raster concept images as production assets. The reference requires the original vector artwork for the logo.
- Do not introduce the prohibited visual register: neon sci-fi, purple AI gradients, decorative bots, fabricated progress.
- Do not build page-level screens here. Those are P13.

4. FILES AND MODULES AFFECTED
- apps/web/ — application shell
- packages/design-tokens/
- packages/ui/ — component library
- packages/ui/__visual__/ — visual regression baselines

5. REQUIRED CONTRACTS
- Every color, spacing and type value in application code references a token. A raw hex, px or font-size literal in a component fails lint.
- Every layout uses logical properties (inline-start, inline-end) rather than physical left and right.
- Each component exposes an accessible name and role; a component without one fails the accessibility test.
- The logo asset is referenced from a single module so that replacing the raster concept with the production vector is a one-file change.
- No component renders a progress indicator that is not driven by server-reported completed and total counts.

6. IMPLEMENTATION INSTRUCTIONS
- Define tokens first and build components from them. A component that hardcodes a value will be duplicated and then diverge.
- Make RTL the default so that an untested component fails visibly in the common case rather than silently in the rare one.
- Record the reference's color values as the approved starting point, and mark them approximate in the token file's comments exactly as the reference marks them. Do not present an approximate token as a final brand value.
- Add a lint rule that fails on prohibited visual patterns where they are mechanically detectable: gradient declarations using the prohibited hue range, and any animated element bound to a non-server progress source.
- Validate Arabic numeral formatting explicitly, including mixed Arabic-Latin strings and unit suffixes.
- Capture visual baselines in both directions from the first component, not retroactively.

7. SECURITY REQUIREMENTS
- The frontend holds no provider key, no agent tool reference and no direct database access; it speaks only to the API gateway.
- Content security policy restricts script and style sources; inline script is disallowed.
- User-supplied text is rendered as text, never as markup, with an explicit test for injection through project and finding names.
- No authentication token is stored where script injection could read it if a safer option exists in the deployment target; record the chosen storage and its rationale.

8. AUTOMATED TESTS
- Lint: a raw color, spacing or font-size literal in a component fails the build.
- Lint: a physical left or right property in layout code fails the build.
- Unit: Arabic numeral formatting across a generated matrix of values, units and mixed-direction strings.
- Accessibility: automated checks for contrast, focus visibility, role and name on every component in the library, driven by enumerating the library rather than a hand-written list.
- Visual regression: every component captured in RTL and LTR, with a diff threshold that fails on layout breakage.
- Integration: user-supplied text containing markup renders as text in every component that displays user content.

9. ACCEPTANCE CRITERIA
- No raw design literal exists in component code, enforced by lint.
- Every component passes automated accessibility checks in both directions, with the library enumerated mechanically.
- Visual baselines exist for every component in both directions.
- The logo is referenced from a single swappable module, and its current asset is documented as a concept raster pending the production vector.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- Lint output showing the literal and physical-property rules active and passing.
- The accessibility run listing every enumerated component and its result.
- The visual regression baseline set, both directions.
- A written statement that the current logo asset is the approved-direction concept raster and that the production vector has not been supplied.

11. ROLLBACK INSTRUCTIONS
Frontend rollback is a deployment revert to the previous build artifact. Design token changes are the risk: a token rename cascades, so rename through a deprecation alias rather than a rename, and remove the alias only after a full visual regression pass. Record the build artifact identifier before and after.

12. DEFINITION OF DONE
- Tokens are the only source of design values, proven by lint.
- RTL is the default and both directions have visual baselines.
- The approximate nature of the reference's color tokens is recorded in the token file, not quietly dropped.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


<!-- promptmeta
id: P13
file: P13_FRONTEND_CUSTOMER_WORKSPACE.md
stage: 4 — Frontend
title_en: Landing, authentication and the customer workspace at approved fidelity
prereq: P12
requirements: UR-007,UR-008,UR-009,UR-010,UR-011,UR-052
status: DESIGNED
-->

# P13_FRONTEND_CUSTOMER_WORKSPACE — Landing, authentication and the customer workspace at approved fidelity

**الصفحة الرئيسية والدخول ومساحة عمل العميل بالدقة المعتمدة**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 4 — Frontend |
| المتطلب السابق | P12 |
| المتطلبات المغطّاة | UR-007، UR-008، UR-009، UR-010، UR-011، UR-052 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ الصفحة الرئيسية ومسار الدخول ومساحة عمل العميل مطابقةً للصور المعتمدة الاتجاه، مع حالات حقيقية من الخادم فقط.

**لماذا نحتاجه؟**  
المرجع يمنع استبدال التصميم المعتمد بلوحة عامة، ويمنع أي تقدم تمثيلي. والصور المعتمدة تحدد البنية المتوقعة: شريط وكلاء، بطاقات حالة، ملفات، عارض ثلاثي الأبعاد، مراجعة بشرية.

**ما المتطلبات السابقة؟**  
اكتمال P12 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
شاشات مطابقة بنيويًا للصور المعتمدة، وكل حالة فيها مشتقة من بث الأحداث، ومسار المؤسسات يقود إلى المبيعات لا إلى الشراء.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا ظهرت أي حالة أو نسبة لا تقابل حدثًا من الخادم، أو إذا أمكن للمؤسسات شراء مقاعد وكلاء.

## EXECUTABLE PROMPT

```text
You are executing P13_FRONTEND_CUSTOMER_WORKSPACE of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Build the customer-facing surfaces at the fidelity of the approved concept screens, with every displayed state derived from the server's event feed and no fabricated progress anywhere.

2. DEPENDENCIES
P12 — screens are composed from the token-based component library.

3. EXACT SCOPE
IN SCOPE:
- Public landing: value proposition, service discovery, transparent capability claims, FAQ, contact sales.
- Authentication: individual and engineer self-registration with verification; institutions routed to a Contact Sales lead form.
- Customer workspace matching the approved concept structure: project summary with current stage and expected date, the agent workflow stepper, per-agent status cards, files and drawings list, the interactive plan viewer region, recent agent results, and the human review panel.
- Live state from the authenticated SSE feed, with reconnection and resumption.
- Every finding card linking to its evidence, its agent execution and its reviewer disposition.
- Empty, loading, error and partial states for every data region.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not implement the 3D plan viewer's geometry pipeline. Render what the delivery service provides; if no model exists, render the empty state and say so.
- Do not implement institutional self-service purchase.
- Do not display any percentage, stage count or expected date that the API did not supply.

4. FILES AND MODULES AFFECTED
- apps/web/routes/ — landing, auth, workspace
- apps/web/features/workflow/ — stepper, agent cards, event subscription
- apps/web/features/evidence/
- apps/web/features/review/

5. REQUIRED CONTRACTS
- Every workflow visual element binds to a field the API returns. A component prop that has no API source fails review.
- When the API returns PLAN_NOT_ESTABLISHED, the stepper renders stage names without a percentage and without an expected date.
- The expected-date field renders only when the API supplies it; it is never computed client-side.
- The institutional path submits a lead and renders a confirmation. There is no purchase component in the codebase.
- Agent status chips render only the seven server states; an unknown state renders as unknown rather than being mapped to a nearby one.

6. IMPLEMENTATION INSTRUCTIONS
- Derive every status, stage and percentage from the event feed. If a value is wanted and the API does not provide it, the correct action is to add it to the API, not to compute it in the browser.
- Handle reconnection with Last-Event-ID so a dropped connection does not produce a gap the user reads as stalled progress.
- Render CONFIDENCE_NOT_ESTABLISHED explicitly rather than hiding the field, so a reviewer sees what is unknown.
- Build the approved structure region by region against the concept screens, and record any deliberate departure with its reason. Treat the screens as the structural target they are, and do not substitute a generic dashboard.
- Make the empty state of the plan viewer honest: no model yet, rather than a placeholder that reads as a rendering in progress.
- Every claim on the landing page must be traceable to a capability that exists. Mark planned capabilities as planned.

7. SECURITY REQUIREMENTS
- The SSE subscription is authenticated and scoped; a project the principal cannot read yields no events and no existence signal.
- No role-based UI hiding is treated as access control; every action is authorized server-side regardless of what the UI shows.
- File links are short-lived and scoped; a copied link does not grant durable access.
- Lead submission is rate-limited and bot-resistant without collecting more personal data than the lead requires.

8. AUTOMATED TESTS
- Component: the stepper renders no percentage when the API returns PLAN_NOT_ESTABLISHED.
- Component: an unknown workflow state renders as unknown and is never coerced to a known state.
- Integration: the event subscription resumes after a forced disconnect with no duplicated or missing stage transition.
- Integration: every finding card's evidence, execution and reviewer links resolve.
- Contract: a mechanical check that every workflow-related component prop maps to a field in the API schema, failing on any prop with no source.
- End-to-end: an institutional registration attempt reaches the lead form and no purchase route exists, proven by a route enumeration test.
- Visual regression: landing, auth and workspace at mobile, tablet and desktop widths in RTL.
- Accessibility: full-page automated checks on each route in Arabic.

9. ACCEPTANCE CRITERIA
- No displayed value lacks an API source, proven by the mechanical prop-to-schema check.
- The event feed resumes without gaps under forced disconnection.
- No purchase route exists for institutions.
- All three routes pass accessibility checks in Arabic at all three breakpoints.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The prop-to-schema check output listing every workflow component prop and its API field.
- A disconnection and resumption transcript.
- Visual regression captures for all three routes at all three breakpoints in RTL, placed side by side with the approved concept screens.
- The route enumeration output showing no purchase route.
- A written list of every deliberate departure from the approved concept screens, each with its reason.

11. ROLLBACK INSTRUCTIONS
Deployment revert to the previous build artifact. Because this prompt introduces the first customer-visible surfaces, pair the rollback with a check that the previous build is compatible with the current API version; never roll the frontend back across a breaking API change without also repinning the API.

12. DEFINITION OF DONE
- Every value on screen traces to the server, proven mechanically.
- Departures from the approved design are listed rather than absorbed silently.
- No fabricated progress exists in the built bundle.
- Status recorded as TESTED.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


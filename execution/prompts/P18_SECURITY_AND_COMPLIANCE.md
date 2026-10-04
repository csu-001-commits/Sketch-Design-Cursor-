<!-- promptmeta
id: P18
file: P18_SECURITY_AND_COMPLIANCE.md
stage: 6 — Launch readiness
title_en: Security verification, privacy obligations and the legal review gate
prereq: P17
requirements: UR-053,UR-055,UR-047,UR-028,UR-026
status: DESIGNED
-->

# P18_SECURITY_AND_COMPLIANCE — Security verification, privacy obligations and the legal review gate

**التحقق الأمني والتزامات الخصوصية وبوابة المراجعة القانونية**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 6 — Launch readiness |
| المتطلب السابق | P17 |
| المتطلبات المغطّاة | UR-053، UR-055، UR-047، UR-028، UR-026 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يجري التحقق الأمني الكامل، ويثبت غياب ثغرات P0 وغياب أي تجاوز بين المشاريع، ويسجّل بوابة المراجعة القانونية كحاجز صريح.

**لماذا نحتاجه؟**  
المرجع يجعل غياب ثغرة P0 وغياب تجاوز غير مصرّح به بين المشاريع بوابة إصدار، ويشترط مراجعة قانونية مؤهلة للخصوصية السعودية والالتزامات القطاعية والملكية الفكرية وتراخيص الأكواد.

**ما المتطلبات السابقة؟**  
اكتمال P17 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
تقرير تحقق أمني بأدلة، ونموذج تهديد موثق، وسجل التزامات خصوصية، وبوابة قانونية معلنة الحالة لا مفترضة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا أُعلن الامتثال دون مراجعة قانونية مسجّلة باسم مراجع مؤهل.

## EXECUTABLE PROMPT

```text
You are executing P18_SECURITY_AND_COMPLIANCE of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Verify the platform's security posture with evidence, document the privacy and data obligations, and record the legal review gate as an explicit, named blocker rather than an assumed clearance.

2. DEPENDENCIES
P17 — security verification runs against the fully instrumented system.

3. EXACT SCOPE
IN SCOPE:
- A documented threat model covering the agent runtime, the model gateway, the retrieval boundary, the capture path and the control plane.
- Automated security testing in CI: dependency vulnerability scanning, static analysis, secret scanning, and container or image scanning.
- An authenticated and unauthenticated penetration test scoped to the platform, conducted by someone other than the implementer.
- A cross-project and cross-tenant access verification sweep covering data, retrieval, logs, cached prompts, tool actions, files and billing.
- A data inventory: what personal data is collected, where it is stored, how long it is retained, who can access it and on what basis.
- A data processing record for every external provider that may receive customer data.
- The legal review gate: Saudi privacy obligations, sectoral obligations, intellectual property and code licensing, each with a named qualified reviewer and a recorded state.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not assert compliance with any regulation. Record the obligations, the controls and the review state; the determination belongs to qualified counsel.
- Do not ingest or process any source whose licensing state is unresolved.
- Do not conduct testing against third-party systems without authorization.

4. FILES AND MODULES AFFECTED
- security/threat-model.md
- security/data-inventory.md
- security/processing-records/
- security/pentest/
- compliance/review-gate.md

5. REQUIRED CONTRACTS
- The cross-boundary sweep enumerates all seven surfaces the reference names — data, RAG, logs, cached prompts, tool actions, files, billing — and asserts zero cross-tenant access on each. A surface not enumerated fails the sweep.
- Every finding carries a severity; a P0 finding blocks the release gate unconditionally.
- Each legal review item records { item, reviewer_name, reviewer_qualification, reviewed_at, determination, scope_limits }. An item with no reviewer is recorded as REVIEW_NOT_PERFORMED and blocks.
- A processing record exists for every provider endpoint that any approved candidate can reach.
- The threat model names, for each component, the trust boundary it sits on and the controls that defend it.

6. IMPLEMENTATION INSTRUCTIONS
- Enumerate the seven cross-boundary surfaces explicitly and test each. A sweep that covers only the database is the sweep that misses the cache.
- Have the penetration test performed by someone who did not build the system. Self-testing finds the bugs you already thought about.
- Record review states honestly. REVIEW_NOT_PERFORMED is the correct value until a named qualified person has reviewed, and it must block.
- Keep the data inventory derived from the schema where possible, so it cannot silently drift from what the system actually stores.
- Write processing records before a provider is approved, not after it is in use.
- Treat a P0 as a stop. There is no severity below which an unauthorized cross-project access is acceptable.

7. SECURITY REQUIREMENTS
- The penetration test scope and authorization are recorded in writing before testing begins.
- Findings are tracked to closure with a verification retest, not closed on assertion.
- Secrets discovered during testing are rotated immediately and the rotation is audited.
- Test artifacts containing findings are themselves access-controlled.
- No production customer data is used in any test.

8. AUTOMATED TESTS
- Automated: dependency, static analysis, secret and image scans run in CI and block on high severity.
- Sweep: the seven-surface cross-tenant verification, each surface enumerated and asserted independently.
- Integration: the adversarial injection corpus from P09 re-run against the integrated system.
- Integration: tool sandbox escape attempts across a generated attack matrix fail closed.
- Verification retest: every closed finding is retested and the retest result recorded.

9. ACCEPTANCE CRITERIA
- Zero open P0 findings.
- Zero cross-tenant access across all seven enumerated surfaces.
- Every legal review item carries either a named qualified reviewer with a determination, or REVIEW_NOT_PERFORMED with the gate blocking.
- Every reachable provider endpoint has a processing record.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The CI security scan outputs.
- The seven-surface sweep output, one assertion block per surface.
- The penetration test report with the tester's identity, the authorized scope and the retest results.
- The legal review gate record, stating plainly for each item whether a qualified review has occurred.
- An explicit written statement that the platform does not claim regulatory compliance and that any such determination belongs to qualified counsel.

11. ROLLBACK INSTRUCTIONS
Security findings do not roll back. If a deployment is rolled back, re-verify that the previous version does not reintroduce a closed finding; maintain the finding register across versions so a rollback cannot silently resurrect a fixed vulnerability.

12. DEFINITION OF DONE
- No P0 is open.
- The sweep covers all seven surfaces named in the reference.
- The legal gate reports its true state, and BLOCKED is recorded where review has not occurred.
- Status recorded as VERIFIED for the tested security controls; compliance determinations remain BLOCKED until a named qualified reviewer records one.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


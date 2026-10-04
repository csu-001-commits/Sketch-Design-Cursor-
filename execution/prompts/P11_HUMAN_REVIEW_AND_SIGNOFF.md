<!-- promptmeta
id: P11
file: P11_HUMAN_REVIEW_AND_SIGNOFF.md
stage: 3 — Golden workflow
title_en: Qualified human review, review boundaries and digest-bound sign-off
prereq: P10
requirements: UR-011,UR-021,UR-025
status: DESIGNED
-->

# P11_HUMAN_REVIEW_AND_SIGNOFF — Qualified human review, review boundaries and digest-bound sign-off

**المراجعة البشرية المؤهلة وحدود المراجعة والتوقيع المرتبط بالبصمة**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 3 — Golden workflow |
| المتطلب السابق | P10 |
| المتطلبات المغطّاة | UR-011، UR-021، UR-025 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ مساحة عمل المراجع المؤهل وقرار المراجعة وتوقيعًا مرتبطًا ببصمة SHA-256 للمستند الموقَّع.

**لماذا نحتاجه؟**  
المرجع يجعل المراجعة البشرية المؤهلة شرطًا لا يُتجاوَز في المهام الحساسة، ويربط المساءلة بشخص مؤهل. توقيع غير مرتبط بالمحتوى لا يثبت شيئًا.

**ما المتطلبات السابقة؟**  
اكتمال P10 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
قرار مراجعة مسجَّل لكل نتيجة حرجة، وتوقيع يفشل التحقق منه فور تغيُّر بايت واحد في المستند.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا قُبل توقيع على مستند تغيّر محتواه، أو إذا اعتُمدت نتيجة خارج حدود مراجعة عائلتها.

## EXECUTABLE PROMPT

```text
You are executing P11_HUMAN_REVIEW_AND_SIGNOFF of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement qualified human review as an enforced gate rather than a workflow courtesy, with each capability family's review boundary enforced and every sign-off cryptographically bound to the exact content signed.

2. DEPENDENCIES
P10 — review operates on the findings and reports the golden workflow produces.

3. EXACT SCOPE
IN SCOPE:
- A reviewer workspace listing assigned cases with the findings, their evidence, their citations and their confidence.
- ReviewDecision: approve, reject, request-changes, escalate, each with a mandatory rationale for anything other than approve-with-no-comment.
- Enforcement of each capability family's review boundary: a finding from the Structure family cannot be approved by a reviewer without the licensed qualification that family declares.
- Sign-off bound to the SHA-256 digest of the exact rendered document.
- Reviewer qualification records with expiry, so a lapsed qualification blocks sign-off.
- Override recording: when a reviewer contradicts an agent finding, the override is recorded and feeds the evaluation signal.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not implement a legally binding electronic seal integration without a recorded legal review. Build the digest binding; leave external seal integration as a declared gap.
- Do not allow the platform to approve on a reviewer's behalf under any timeout or escalation rule.
- Do not let a reviewer approve a finding outside their qualification by acknowledging a warning.

4. FILES AND MODULES AFFECTED
- services/review/
- services/review/qualification/
- services/review/signature/
- db/migrations/ — review_decision, reviewer_qualification, signature

5. REQUIRED CONTRACTS
- Signature: { signature_id, document_digest_sha256, signer_user_id, qualification_ref, signed_at, algorithm, key_ref }. Verification recomputes the digest from the stored document and fails on any mismatch.
- A ReviewDecision references the exact finding identifiers it covers. A decision cannot cover a finding added after the decision was made.
- Qualification: { user_id, family, authority, credential_ref, valid_from, valid_until, state }. An expired or revoked qualification blocks sign-off with QUALIFICATION_NOT_VALID.
- An approval of a finding whose family the reviewer is not qualified for is refused with REVIEW_BOUNDARY_VIOLATION. There is no acknowledgement path that permits it.
- No automatic approval exists. A review that is not performed leaves the workflow in human-review indefinitely, and that is the correct behavior.

6. IMPLEMENTATION INSTRUCTIONS
- Recompute the digest at verification time from stored bytes. Never trust a stored digest alone.
- Bind the decision to the finding set by identifier, so appending a finding invalidates coverage and requires a new decision.
- Check qualification validity at the moment of sign-off, not at assignment.
- Record overrides as first-class data; they are the honest quality signal and must not be smoothed away.
- Give the reviewer the evidence and the citation inline. A reviewer who must leave the workspace to verify a citation will not verify it.
- Where no qualified reviewer exists for a family, the workflow reports NO_QUALIFIED_REVIEWER_AVAILABLE and halts. It does not route to an unqualified reviewer.

7. SECURITY REQUIREMENTS
- Signing keys are held in the key management service; the application signs through it and never holds private key material.
- A reviewer cannot sign off on their own authored content where the process requires independence; enforce separation in policy.
- Review decisions are append-only; a changed mind produces a new decision referencing the prior one.
- Qualification records are modifiable only by an authorized administrator and every change is audited.
- Digest verification failures are security events, not display errors.

8. AUTOMATED TESTS
- Unit: signature verification fails when a single byte of the stored document changes.
- Unit: an expired qualification blocks sign-off, across a generated validity matrix including the boundary day.
- Unit: a decision's finding coverage is invalidated when a finding is appended.
- Integration: approval of an out-of-family finding is refused and audited, for every capability family.
- Integration: no code path produces an approval without a reviewer user identifier, proven by a search over the decision write path plus a test asserting rejection of a system-authored decision.
- Integration: a family with no valid qualified reviewer halts with NO_QUALIFIED_REVIEWER_AVAILABLE.
- Integration: a reviewer override is recorded and retrievable as an evaluation signal.

9. ACCEPTANCE CRITERIA
- A one-byte change invalidates the signature.
- Out-of-family approval is impossible for every family, with no acknowledgement bypass.
- No automatic or system-authored approval exists anywhere in the codebase.
- Expired qualifications block at the boundary day.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The byte-flip signature verification test output.
- The per-family boundary refusal test output.
- The qualification validity matrix output including boundary cases.
- A code search transcript showing no path writes an approval without a human user identifier.
- A written statement that external electronic seal integration is NOT implemented and remains a declared gap pending legal review.

11. ROLLBACK INSTRUCTIONS
Revert the service. Signatures already recorded remain valid and verifiable: a rollback must not change the digest algorithm or the stored document bytes. If an algorithm change is ever required, add a new algorithm alongside and re-sign under authorization; never reinterpret an old signature under a new algorithm.

12. DEFINITION OF DONE
- Signature binding is proven by a byte flip.
- Every capability family's boundary is individually tested.
- The absence of automatic approval is proven by search and by test.
- Status recorded as TESTED. Legal sufficiency of the signature is NOT claimed and remains BLOCKED pending the review the reference requires.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


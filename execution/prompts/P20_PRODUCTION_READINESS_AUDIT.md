<!-- promptmeta
id: P20
file: P20_PRODUCTION_READINESS_AUDIT.md
stage: 6 — Launch readiness
title_en: Independent production readiness audit against the release gates
prereq: P19
requirements: UR-049,UR-048,UR-051,UR-053,UR-054,UR-055
status: DESIGNED
-->

# P20_PRODUCTION_READINESS_AUDIT — Independent production readiness audit against the release gates

**التدقيق المستقل لجاهزية الإنتاج مقابل بوابات الإصدار**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 6 — Launch readiness |
| المتطلب السابق | P19 |
| المتطلبات المغطّاة | UR-049، UR-048، UR-051، UR-053، UR-054، UR-055 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يجري تدقيقًا مستقلًا لكل بوابة إصدار بالأدلة، ويصدر حكمًا صريحًا: جاهز أو محجوب، مع تسمية كل حاجز.

**لماذا نحتاجه؟**  
المرجع يشترط أن تتطلب كل بوابة إصدار دليلًا، ويمنع إعلان الجاهزية بلا دليل قابل لإعادة الإنتاج أو ادّعاء درجة كاملة بلا دليل تقييم صريح.

**ما المتطلبات السابقة؟**  
اكتمال P19 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
تقرير تدقيق يربط كل بوابة بدليلها أو بسبب غيابه، وحكم نهائي لا يحتمل التأويل.

**كيف نتحقق من نجاحه؟**  
يفشل التدقيق إذا سُجّلت بوابة كمجتازة دون رابط دليل، أو إذا أُعلنت الجاهزية مع وجود حاجز مفتوح.

## EXECUTABLE PROMPT

```text
You are executing P20_PRODUCTION_READINESS_AUDIT of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Audit every release gate against its evidence, by someone other than the implementer, and issue an unambiguous verdict that names every open blocker rather than averaging them away.

2. DEPENDENCIES
P19 — the audit consumes the evidence every prior prompt produced.

3. EXACT SCOPE
IN SCOPE:
- Each of the seven release gates audited independently: no P0 security vulnerability or unauthorized cross-project access; no unapproved model or provider receiving sensitive data; traceable engineering claims with qualified human approval where required; verified restore and rollback; sustained load with acceptable p95 latency, queue age and cost per completed case; accessibility, Arabic RTL and device behavior checked against approved images; Saudi privacy, sectoral obligations, IP and code licensing reviewed by qualified counsel.
- A traceability sweep confirming every requirement in both registries maps to at least one prompt and at least one acceptance test.
- A fabrication sweep: every readiness claim in every deliverable is checked against an executed artifact.
- A verdict: READY or BLOCKED, with every blocker named, owned and dated.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not grant a gate on the basis of a plan, an intention or a documented procedure. Only executed evidence passes a gate.
- Do not compute an overall score. A single blocker blocks regardless of how many gates passed.
- Do not perform this audit as the same person who implemented the work being audited.

4. FILES AND MODULES AFFECTED
- execution/audit/readiness-audit.md
- execution/audit/gate-evidence.tsv
- execution/audit/traceability-sweep.tsv

5. REQUIRED CONTRACTS
- gate-evidence.tsv columns: gate_id, gate_statement, required_evidence, evidence_ref, evidence_executed_at, auditor, verdict (PASS|FAIL|NOT_ASSESSED). A PASS with an empty evidence_ref is invalid and fails the audit's own linter.
- NOT_ASSESSED is a distinct and honest verdict. It is never merged into PASS.
- The overall verdict is BLOCKED if any gate is FAIL or NOT_ASSESSED. There is no weighted or partial READY.
- Every blocker carries an owner role and a date recorded, so it is actionable rather than decorative.
- The traceability sweep fails if any requirement maps to zero prompts or zero acceptance tests.

6. IMPLEMENTATION INSTRUCTIONS
- Follow each evidence reference to the actual artifact and confirm it was executed. A link to a document describing a test is not a test result.
- Record NOT_ASSESSED wherever the evidence was not produced. The reference's gates require evidence; absence of evidence is absence of a pass.
- Audit the language of every deliverable for unsupported readiness claims and list each one found, with its location.
- Do not compute a score. If asked for a score, report the gate table and state that a composite would obscure the blockers.
- Name every blocker with an owner and a date. An unowned blocker is a wish.
- Where this audit's own evidence is incomplete, say so in the audit itself rather than issuing a confident verdict on a thin basis.

7. SECURITY REQUIREMENTS
- The audit reads evidence; it changes no system state.
- Audit artifacts may reference sensitive findings and are access-controlled accordingly.
- A gate concerning security is not passed on the implementer's own assertion.

8. AUTOMATED TESTS
- Linter: a PASS row with an empty evidence_ref fails.
- Linter: the overall verdict is BLOCKED whenever any gate is FAIL or NOT_ASSESSED, asserted by a test over generated gate tables.
- Sweep: every requirement in both registries maps to at least one prompt and one acceptance test; unmapped requirements fail.
- Fabrication sweep: a scan over all deliverables flags unsupported readiness language for manual adjudication, and every flag is adjudicated and recorded.

9. ACCEPTANCE CRITERIA
- Every gate row carries either an executed evidence reference or a NOT_ASSESSED verdict.
- The overall verdict is mechanically derived and cannot be set by hand.
- The traceability sweep reports full coverage or names every gap.
- Every flagged readiness claim is adjudicated and recorded.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The completed gate-evidence table with every evidence reference resolvable.
- The traceability sweep output.
- The fabrication sweep output with each flag's adjudication.
- The audit's own linter run showing PASS.
- The named auditor and an explicit statement of their independence from the implementation.

11. ROLLBACK INSTRUCTIONS
This prompt changes no system state. A rollback is a revert of the audit document. An audit verdict is never retroactively amended: a changed conclusion is a new audit with a new date, and the superseded audit remains in the repository.

12. DEFINITION OF DONE
- The verdict is mechanically derived from the gate table.
- No gate is marked PASS without a resolvable, executed evidence reference.
- The auditor's independence is stated.
- Status recorded as VERIFIED for the audit itself. The platform's own status is whatever the gate table says, and READY is claimed only if every gate passes.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


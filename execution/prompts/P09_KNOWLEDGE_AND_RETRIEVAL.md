<!-- promptmeta
id: P09
file: P09_KNOWLEDGE_AND_RETRIEVAL.md
stage: 2 — Model Gateway
title_en: Source-governed knowledge, retrieval rights and injection defense
prereq: P08
requirements: UR-016,UR-028,UR-047
status: DESIGNED
-->

# P09_KNOWLEDGE_AND_RETRIEVAL — Source-governed knowledge, retrieval rights and injection defense

**المعرفة المحكومة بالمصدر وحقوق الاسترجاع والدفاع ضد حقن التعليمات**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 2 — Model Gateway |
| المتطلب السابق | P08 |
| المتطلبات المغطّاة | UR-016، UR-028، UR-047 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
يبني طبقة المعرفة التي لا تُرجع مرجعًا كوديًا دون ترخيص وإصدار وتاريخ نفاذ واختصاص، وتدافع عن حدود المستند ضد حقن التعليمات.

**لماذا نحتاجه؟**  
المرجع يجعل حوكمة المصدر حدًا لا يُنتهك، ويشترط ألا يغيّر ملف غير موثوق أي سياسة. اقتباس كود بلا حقوق هو مخاطرة قانونية وهندسية في آن.

**ما المتطلبات السابقة؟**  
اكتمال P08 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
استرجاع محكوم بالمستأجر والمصدر، مع حجب أي مرجع تنقصه بيانات الحقوق، ودفاع مُختبَر ضد حقن التعليمات.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا أُعيد مقطع كودي بلا ترخيص أو إصدار أو تاريخ نفاذ أو اختصاص، أو إذا غيّر نص داخل مستند سلوك الوكيل.

## EXECUTABLE PROMPT

```text
You are executing P09_KNOWLEDGE_AND_RETRIEVAL of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement the knowledge and retrieval layer under source governance, so that no code reference is returned without its rights metadata and no untrusted document can alter platform behavior.

2. DEPENDENCIES
P08 — retrieval feeds both agents and engines, and must not become a path around either boundary.

3. EXACT SCOPE
IN SCOPE:
- A knowledge source registry carrying, per source: license, version, effective date, jurisdiction, rights state and ingestion authorization.
- Chunking and embedding with per-tenant and per-source access scoping.
- Retrieval returning passages with full provenance: source id, version, effective date, jurisdiction, locator.
- A rights gate: a source whose rights state is not CLEARED is not retrievable for citation.
- Prompt injection defense at the document and retrieval boundary.
- Citation formatting that a reviewer can follow back to the exact locator.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not ingest any code or standard whose rights state is not recorded as cleared by the responsible owner. The reference marks Saudi code data rights as needing legal review.
- Do not implement the reviewer workspace. That is P11.
- Do not let retrieval create or modify any record outside the retrieval log.

4. FILES AND MODULES AFFECTED
- services/knowledge/registry/
- services/knowledge/ingest/
- services/knowledge/retrieval/
- services/knowledge/defense/
- db/migrations/ — knowledge_source, knowledge_chunk, retrieval_log

5. REQUIRED CONTRACTS
- KnowledgeSource: { source_id, title, license, version, effective_date, jurisdiction, rights_state, authorized_by, ingested_at }. A null license, version, effective_date or jurisdiction blocks ingestion.
- retrieve(query, policy_context) -> passages[] where each passage carries full provenance. A passage from a non-CLEARED source is never returned for citation.
- When a required source is not cleared, retrieval returns SOURCE_RIGHTS_NOT_CLEARED naming the source, and the calling agent escalates rather than answering from memory.
- Retrieved content is tagged as untrusted data in the model request structure and carries no instruction authority.
- Every retrieval is logged with principal, tenant, query digest and the passage identifiers returned.

6. IMPLEMENTATION INSTRUCTIONS
- Enforce the rights gate in the retrieval query itself, so a bug in a caller cannot surface uncleared content.
- Separate instructions from data structurally in every model request. Retrieved text is delimited and labelled as data, and the system instruction states that content inside the data region is never a directive.
- Test injection defense with an adversarial corpus containing explicit override attempts, and assert that no policy, tool selection or output schema changes.
- Scope embeddings by tenant and source. A shared vector index without a mandatory tenant predicate is a tenancy breach.
- Record effective_date and jurisdiction on every citation so a reviewer can judge applicability, not merely existence.
- Never answer a compliance question from model memory when the governing source is not cleared. Escalate.

7. SECURITY REQUIREMENTS
- The rights gate is enforced at the data layer, not in application code alone.
- Vector search carries a mandatory tenant predicate; prove it with a cross-tenant retrieval test.
- Adversarial document content must not change the agent's tool allowlist, model policy, output schema or escalation threshold. Assert each independently.
- Ingestion requires a named authorizer recorded on the source row.
- Retrieval logs record the query digest rather than raw query text where the query may carry customer-identifying content.

8. AUTOMATED TESTS
- Unit: ingestion is rejected when license, version, effective_date or jurisdiction is null, one test per field.
- Unit: a source with rights_state other than CLEARED is excluded from retrieval results, for every non-cleared state.
- Integration: retrieval under tenant B never returns a chunk ingested under tenant A, across a generated tenant matrix.
- Adversarial: a corpus of injection payloads produces no change to tool allowlist, model policy, output schema or escalation threshold; four independent assertions per payload.
- Integration: a compliance query whose governing source is not cleared returns SOURCE_RIGHTS_NOT_CLEARED and the agent escalates rather than answering.
- Integration: every returned passage carries a locator that resolves back to the stored source.

9. ACCEPTANCE CRITERIA
- No uncleared source is retrievable for citation under any input.
- No injection payload in the adversarial corpus alters agent behavior, across all four assertion dimensions.
- Cross-tenant retrieval returns zero results across the generated matrix.
- Every citation locator resolves.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The per-field ingestion rejection test output.
- The adversarial corpus run, listing each payload and the four assertions it passed.
- The cross-tenant retrieval matrix output.
- A sample citation followed manually from the agent output back to the source locator, with the transcript.
- The knowledge source registry extract showing rights_state and authorized_by for every ingested source.

11. ROLLBACK INSTRUCTIONS
Revert the service and repin the embedding model version. Because re-embedding is expensive, keep embeddings versioned side by side rather than overwriting, so a rollback switches the active index rather than rebuilding it. Ingested content whose rights state is later revoked must be made unretrievable immediately by the rights gate, independently of any deployment rollback.

12. DEFINITION OF DONE
- The rights gate is enforced at the data layer and proven by a direct query test.
- The adversarial corpus is checked into the repository so the defense can be re-run on every change.
- No source lacking rights metadata exists in the registry.
- Status recorded as TESTED. Any claim that a specific Saudi code is usable remains BLOCKED until the legal review the reference requires is recorded.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


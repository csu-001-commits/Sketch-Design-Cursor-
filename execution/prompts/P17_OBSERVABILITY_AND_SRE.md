<!-- promptmeta
id: P17
file: P17_OBSERVABILITY_AND_SRE.md
stage: 6 — Launch readiness
title_en: Observability, FinOps, incident response and verified restore
prereq: P16
requirements: UR-036,UR-044,UR-054,UR-027
status: DESIGNED
-->

# P17_OBSERVABILITY_AND_SRE — Observability, FinOps, incident response and verified restore

**الرصد وإدارة التكلفة والاستجابة للحوادث والاسترجاع المُتحقَّق منه**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 6 — Launch readiness |
| المتطلب السابق | P16 |
| المتطلبات المغطّاة | UR-036، UR-044، UR-054، UR-027 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ عائلات القياس السبع، ودفاتر التشغيل الخمسة، ويثبت الاسترجاع والتراجع بتجربة فعلية لا بوثيقة.

**لماذا نحتاجه؟**  
المرجع يشترط صراحة أن يكون الاسترجاع والتراجع مُتحقَّقًا منه لا موثقًا فقط، ويحدد سبع عائلات قياس وخمسة دفاتر تشغيل.

**ما المتطلبات السابقة؟**  
اكتمال P16 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
رصد شامل بالعائلات السبع، وتنبيهات مرتبطة بدفاتر تشغيل، وتجربة استرجاع موثقة بأرقام، واختبار حمل مستدام.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا غابت أي عائلة قياس، أو إذا لم تُجرَ تجربة استرجاع فعلية بنتيجة قابلة للمقارنة.

## EXECUTABLE PROMPT

```text
You are executing P17_OBSERVABILITY_AND_SRE of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Instrument the platform across all seven metric families, write and rehearse the five operational playbooks, and prove restore and rollback by execution rather than by documentation.

2. DEPENDENCIES
P16 — operators need the console to act on what observability surfaces.

3. EXACT SCOPE
IN SCOPE:
- The seven metric families: queue depth, age and wait p95; latency p50, p95, p99 and time to first token; requests per minute and tokens per second; 429, 5xx, timeout counts and fallback success rate; token and SAR cost by agent and project; evaluation pass rate, citation quality and reviewer override rate; GPU, CPU, RAM, database and storage utilisation.
- Distributed tracing from the edge request through the workflow, the agent, the tool and the model invocation.
- Alerting bound to runbooks: every alert names the playbook that answers it.
- The five playbooks: incident, maintenance, integration lifecycle, support privacy, SRE.
- A restore rehearsal with measured recovery time and verified data comparison.
- A sustained load test measuring p95 latency, queue age and cost per completed case.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not set an alert threshold without a stated basis; an unjustified threshold produces noise and then gets ignored.
- Do not log customer content or secrets into telemetry.
- Do not claim a recovery objective that has not been measured.

4. FILES AND MODULES AFFECTED
- packages/telemetry/
- ops/dashboards/
- ops/alerts/
- ops/playbooks/
- ops/load-test/

5. REQUIRED CONTRACTS
- Every metric carries tenant, project, agent version and model candidate dimensions where applicable, so cost and quality can be attributed.
- Every alert definition references a playbook path; an alert without one fails the configuration lint.
- A threshold carries a basis field: measured baseline, vendor SLO or explicit business decision with an approver. An unset threshold renders as THRESHOLD_NOT_SET and blocks the release gate rather than defaulting.
- The restore rehearsal records: backup identifier, restore start and end times, measured recovery time, and a row-count or checksum comparison against the source.
- Load test output records p95 latency, queue age and SAR cost per completed case at the sustained concurrency actually applied.

6. IMPLEMENTATION INSTRUCTIONS
- Propagate the trace identifier end to end, including into the model invocation record, so a cost spike can be traced to a workflow.
- Derive thresholds from measured baselines where possible and record the basis. A threshold with no basis is a guess that will be treated as a fact later.
- Scrub telemetry of customer content and secrets at the emission point, not at the ingestion point.
- Rehearse each playbook at least once and record what the rehearsal found. A playbook that has never been run is a draft.
- Perform the restore into an isolated environment and compare the restored data to the source quantitatively. 'Restore completed' without a comparison proves only that a command exited zero.
- Report the load test honestly: state the concurrency actually sustained, not the concurrency hoped for.

7. SECURITY REQUIREMENTS
- Telemetry contains no customer content, no secret and no raw provider response.
- Dashboard access follows the capability matrix; cost and security views are role-scoped.
- Backup artifacts are encrypted and access-controlled, and restore requires authorization.
- Trace data retention is bounded and stated.
- Alert channels do not carry sensitive detail; they carry a reference an authorized operator resolves.

8. AUTOMATED TESTS
- Configuration lint: every alert references an existing playbook file.
- Configuration lint: every threshold carries a basis; an unset threshold emits THRESHOLD_NOT_SET.
- Integration: a synthetic request produces a trace spanning edge, workflow, agent, tool and model invocation, asserted span by span.
- Integration: telemetry emitted during a run containing a planted sensitive string does not contain that string.
- Operational: a restore rehearsal in an isolated environment with a quantitative data comparison.
- Operational: a sustained load test at a declared concurrency, recording p95 latency, queue age and cost per completed case.
- Operational: each of the five playbooks rehearsed once with findings recorded.

9. ACCEPTANCE CRITERIA
- All seven metric families are present and dimensioned, verified by a metric inventory test.
- Every alert resolves to a playbook.
- The restore rehearsal produced a quantitative comparison, not merely a success message.
- The load test result states the concurrency actually sustained and the measured cost per case.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The metric inventory test output listing all seven families and their dimensions.
- The alert-to-playbook lint output.
- The restore rehearsal record with backup identifier, measured recovery time and the data comparison result.
- The load test report with the sustained concurrency, p95 latency, queue age and SAR cost per completed case.
- The five playbook rehearsal records with their findings.
- The scrubbing test output showing the planted string absent from telemetry.

11. ROLLBACK INSTRUCTIONS
Observability changes are additive and low risk, but alert threshold changes are not: record the previous threshold and its basis before changing it, so a rollback restores both the value and the justification. Dashboard and alert configuration lives in version control and rolls back with a revert.

12. DEFINITION OF DONE
- Restore is proven by measurement, satisfying the reference's requirement that it be verified and not merely documented.
- No threshold exists without a recorded basis, and unset thresholds block rather than default.
- Every playbook has been rehearsed at least once.
- Status recorded as VERIFIED for restore and load, since both are evidenced by executed rehearsals; TESTED elsewhere.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


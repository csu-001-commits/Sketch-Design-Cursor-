<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Produced by EXECUTION_BLUEPRINT/_tools/build.py from
     EXECUTION_BLUEPRINT/PHASES/*.md and EXECUTION_BLUEPRINT/_registry/*.tsv.
     Edit those sources and re-run the script. -->
# 04 — مصفوفة تتبع المتطلبات
> تربط هذه المصفوفة كل متطلب بمرجعه في المصدر، وبمرحلته، وبالأوامر التي
> تغطيه، وبضابط قبوله. المصفوفة **مُولَّدة** من `_registry/requirements.tsv`
> ومن كتل `meta` في ملفات المراحل، فلا يمكن أن تنحرف عنها.

## اصطلاح اللغة

محتوى الجدول بالإنجليزية لأنه معرّفات ومراجع قابلة للقراءة آلياً (`source_ref`, `req_id`, `phase`, `prompt_id`). الشرح العربي الكامل لكل نطاق موجود في `01-DEEP-ANALYSIS.md`.

## قراءة `source_ref`

الصيغة `<رقم الورقة>:<صف Excel>`. مثال: `02:r2` تعني الورقة
`02_قرارات_معمارية` الصف 2. أرقام الأوراق متطابقة بين ملف العمل v10
والتصدير v11.

## ملخص التغطية (تاريخ التوليد 2026-10-04)

| المقياس | القيمة |
|---|---|
| إجمالي المتطلبات | 192 |
| متطلبات مُغطاة بأمر واحد على الأقل | 192 |
| متطلبات غير مُغطاة | 0 |
| إجمالي الأوامر | 69 |
| إجمالي المراحل | 17 |

### التوزيع بحسب درجة الإثبات (`class`)

| class | العدد | المعنى |
|---|---|---|
| CONFIRMED | 189 | منصوص عليه في المصدر |
| UNKNOWN | 3 | لا يمكن إثباته من المصدر |

### التوزيع بحسب الأهمية (`criticality`)

| criticality | العدد |
|---|---|
| P0 | 155 |
| P1 | 26 |
| P2 | 2 |
| DEFERRED | 9 |

**لا يوجد متطلب غير مُغطى.** كل متطلب في السجل تغطيه أمر تنفيذي واحد على الأقل، أو هو مُعلَّم `DEFERRED` ومُغطى في `PHASE-16` خلف بوابة تفويض.

---

## المصفوفة

### PHASE-00 — الاكتشاف وجرد الواقع · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `57:r2` | `REQ-GOV-05` | CONFIRMED | UNVERIFIED | P0 | `P00-01` | runtime inventory + deploy SHA + test output |
| `68:r6` | `REQ-GOV-06` | CONFIRMED | SPEC | P0 | `P00-03` | provider agreement evidence per integration |
| `23:r2-r16` | `REQ-INT-01` | CONFIRMED | VERIFY/TEST/SANDBOX/REFERENCE | P0 | `P00-03`, `P08-04` | per-integration access evidence |
| `57:r5` | `REQ-INT-04` | CONFIRMED | UNVERIFIED | P0 | `P00-03`, `P13-02` | provider sandbox success |
| `67:r2` | `REQ-OPN-01` | UNKNOWN | NOT VERIFIED | P0 | `P00-01` | inventory result recorded as fact |
| `00:r12-r13` | `REQ-OPN-04` | CONFIRMED | conflict | P1 | `P00-04` | owner confirms authoritative version |
| `29:r2-r8;67:r2-r9` | `REQ-OPN-05` | CONFIRMED | conflict | P0 | `P00-04` | owner ratifies the reconciled sequence |
| `00:r17` | `REQ-OPN-06` | CONFIRMED | TEMPORARY | P2 | `P00-04` | official brand asset supplied |

### PHASE-01 — الأساسات: الهوية والعزل والسياسة والتدقيق · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r4` | `ADR-003` | CONFIRMED | APPROVED | P0 | `P00-04`, `P01-02` | negative cross-tenant test |
| `68:r3` | `REQ-GOV-01` | CONFIRMED | SPEC | P0 | `P01-01` | single-tenant launch with enforced tenant context |
| `27:r2` | `REQ-TEN-01` | CONFIRMED | DESIGNED | P0 | `P01-02` | AT-SEC-001 |
| `44:r2` | `REQ-TEN-02` | CONFIRMED | DESIGN ONLY | P1 | `P01-01` | API + DB tests |
| `44:r3` | `REQ-TEN-03` | CONFIRMED | DESIGN ONLY | P0 | `P01-02` | cross-tenant tests |
| `44:r4` | `REQ-TEN-04` | CONFIRMED | DESIGN ONLY | P2 | `P01-01` | UI/API tests |
| `44:r5` | `REQ-TEN-05` | CONFIRMED | DESIGN ONLY | P0 | `P01-03`, `P01-04` | auth tests |
| `44:r7` | `REQ-TEN-06` | CONFIRMED | DESIGN ONLY | P0 | `P01-02` | RLS tests |
| `03:r2-r11` | `REQ-TEN-07` | CONFIRMED | DESIGNED | P1 | `P01-03`, `P13-04` | per-surface boundary tests |
| `04:r2-r11` | `REQ-TEN-08` | CONFIRMED | DESIGNED | P0 | `P01-03`, `P01-05` | negative authorization tests per role |
| `27:r3` | `REQ-TEN-09` | CONFIRMED | DESIGNED | P0 | `P01-03` | access review + session tests |
| `27:r6` | `REQ-SEC-03` | CONFIRMED | DESIGNED | P0 | `P01-01`, `P10-04` | config review + restore test |
| `27:r7` | `REQ-SEC-04` | CONFIRMED | DESIGNED | P0 | `P01-05`, `P10-01` | tamper + retrieval test |
| `28:r2-r21` | `REQ-DAT-01` | CONFIRMED | DESIGNED | P0 | `P00-02`, `P01-01`, `P01-05`, `P11-03` | migration review + constraint tests |
| `39:r6` | `REQ-DAT-02` | CONFIRMED | proposed | P0 | `P01-01` | constraint test |
| `33:r7` | `REQ-API-03` | CONFIRMED | proposed | P0 | `P01-02`, `P03-04` | AT-SEC-001 |
| `23:r2` | `REQ-INT-03` | CONFIRMED | VERIFY | P0 | `P00-03`, `P01-03` | interim identity path documented |

### PHASE-02 — الأدلة والملفات وسلامة المخرجات · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `27:r5` | `REQ-SEC-02` | CONFIRMED | CRITICAL | P0 | `P02-01`, `P12-02` | AT-FILE-001 |
| `39:r9` | `REQ-DAT-05` | CONFIRMED | proposed | P0 | `P02-01`, `P02-02`, `P02-03` | constraint test |

### PHASE-03 — محرك مسارات العمل والعقود · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r2` | `ADR-001` | CONFIRMED | APPROVED | P0 | `P00-04`, `P03-01` | owner + schema + tests + pricing + approval |
| `39:r7` | `REQ-DAT-03` | CONFIRMED | proposed | P0 | `P03-02` | constraint test |
| `39:r13` | `REQ-DAT-09` | CONFIRMED | proposed | P0 | `P03-03` | outbox delivery audit |
| `39:r14` | `REQ-DAT-10` | CONFIRMED | proposed | P0 | `P03-03` | conflict test |
| `09:r2-r16` | `REQ-WF-01` | CONFIRMED | DESIGNED | P0 | `P03-02`, `P03-04`, `P03-05`, `P08-02` | AT-WF-001 |
| `15:r4` | `REQ-WF-02` | CONFIRMED | DESIGNED | P0 | `P03-01` | AT-WF-002 |
| `37:r7` | `REQ-WF-03` | CONFIRMED | Not verified | P0 | `P03-02` | restart during job + queue receipt |
| `37:r8` | `REQ-WF-04` | CONFIRMED | Not verified | P0 | `P03-03` | repeat-key test + retry trace |
| `07:r2-r9` | `REQ-WF-07` | CONFIRMED | PILOT TARGET/DEFINED/DESIGNED | P0 | `P00-02`, `P03-01` | template registry schema test |
| `05:r4` | `REQ-WF-09` | CONFIRMED | DESIGNED | P0 | `P03-02`, `P03-05` | stuck-run and recovery metrics |
| `05:r3` | `REQ-WF-10` | CONFIRMED | DESIGNED | P0 | `P03-01` | routing accuracy + misroute count |
| `26:r2-r20` | `REQ-API-01` | CONFIRMED | DESIGNED | P0 | `P02-01`, `P03-04`, `P07-06`, `P08-02` | contract tests per endpoint |
| `33:r6-r15` | `REQ-API-02` | CONFIRMED | proposed | P0 | `P03-04` | schema contract tests |
| `34:r3` | `REQ-API-04` | CONFIRMED | proposed | P0 | `P03-03` | envelope schema test |
| `34:r6-r13` | `REQ-API-05` | CONFIRMED | proposed | P0 | `P02-03`, `P03-03`, `P07-04`, `P07-06`, `P08-02`, `P12-02` | event replay + dedupe test |

### PHASE-04 — بوابة الذكاء والتوجيه والميزانية · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r3` | `ADR-002` | CONFIRMED | APPROVED | P0 | `P00-04`, `P04-01` | no keys in browser |
| `39:r12` | `REQ-DAT-08` | CONFIRMED | proposed | P0 | `P04-06` | exactly-once test |
| `74:r2` | `REQ-API-06` | CONFIRMED | NOT VERIFIED | P0 | `P04-01` | server-derived tenant test |
| `74:r3-r4` | `REQ-API-07` | CONFIRMED | NOT VERIFIED | P0 | `P04-01` | role-scope test + stream redaction test |
| `74:r8-r9` | `REQ-API-08` | CONFIRMED | NOT VERIFIED | P0 | `P04-01` | event replay + DLQ test |
| `70:r2` | `REQ-GW-01` | CONFIRMED | measure | P0 | `P04-01` | p95 gateway overhead measured against a stated target |
| `70:r3` | `REQ-GW-02` | CONFIRMED | NOT VERIFIED | P0 | `P01-04`, `P04-01` | policy decision log completeness |
| `70:r4` | `REQ-GW-03` | CONFIRMED | NOT VERIFIED | P0 | `P04-02` | no policy-violating route |
| `70:r5` | `REQ-GW-04` | CONFIRMED | NOT VERIFIED | P0 | `P04-03` | quality floor per task class |
| `70:r6` | `REQ-GW-05` | CONFIRMED | NOT VERIFIED | P0 | `P04-04` | chaos 429/5xx/timeout |
| `70:r7` | `REQ-GW-06` | CONFIRMED | NOT VERIFIED | P0 | `P04-04` | fallback tested under 429 and 5xx |
| `70:r8` | `REQ-GW-07` | CONFIRMED | NOT VERIFIED | P1 | `P04-05`, `P06-02` | token saving measurement |
| `70:r9` | `REQ-GW-08` | CONFIRMED | NOT VERIFIED | P1 | `P04-05` | cache isolation test + hit rate |
| `70:r10` | `REQ-GW-09` | CONFIRMED | NOT VERIFIED | P0 | `P04-06` | no unauthorized over-budget call |
| `70:r11` | `REQ-GW-10` | CONFIRMED | NOT VERIFIED | P0 | `P04-07` | eval pass-rate by task class |
| `70:r12` | `REQ-GW-11` | CONFIRMED | NOT VERIFIED | P0 | `P04-06`, `P10-01`, `P10-02` | billable usage completeness |
| `72:r2-r11` | `REQ-GW-13` | CONFIRMED | NOT VERIFIED | P0 | `P04-02`, `P14-02` | registry schema test |
| `71:r2-r9` | `REQ-GW-14` | CONFIRMED | NOT VERIFIED | P0 | `P04-03`, `P06-03` | per-class routing tests |
| `71:r9` | `REQ-GW-16` | CONFIRMED | NOT VERIFIED | P0 | `P04-03`, `P04-07` | fail-closed test |
| `77:r2` | `REQ-GW-17` | CONFIRMED | Adopt | P0 | `P04-03`, `P04-04` | two independent providers exercised |
| `51:r2-r9` | `REQ-GW-20` | CONFIRMED | SPEC | P0 | `P04-02` | per-control evidence |
| `05:r36` | `REQ-COM-10` | CONFIRMED | DESIGNED | P0 | `P04-06` | attribution + budget breach tests |

### PHASE-05 — تشغيل الوكلاء والسجل والإصدارات · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r6` | `ADR-005` | CONFIRMED | APPROVED | P0 | `P00-04`, `P05-04` | P3 requires specialist; R4 requires delegation |
| `27:r8` | `REQ-SEC-05` | CONFIRMED | DESIGNED | P0 | `P05-03` | adversarial tests |
| `39:r8` | `REQ-DAT-04` | CONFIRMED | proposed | P0 | `P05-01` | constraint test + redaction test |
| `36:r6-r15` | `REQ-AGT-01` | CONFIRMED | proposed | P0 | `P04-06`, `P05-01` | per-contract validation test |
| `36:r8` | `REQ-AGT-02` | CONFIRMED | proposed | P0 | `P05-01`, `P05-03` | context isolation test |
| `36:r7` | `REQ-AGT-03` | CONFIRMED | proposed | P0 | `P05-02`, `P05-03` | unregistered tool rejection test |
| `36:r11` | `REQ-AGT-04` | CONFIRMED | proposed | P0 | `P04-07`, `P05-01` | malformed-result rejection test |
| `36:r15` | `REQ-AGT-05` | CONFIRMED | proposed | P0 | `P05-01` | failure injection test |
| `62:r2-r6` | `REQ-AGT-06` | CONFIRMED | SPEC | P0 | `P05-02`, `P14-03` | rollback proof |
| `57:r4` | `REQ-AGT-07` | CONFIRMED | SPECIFIED | P0 | `P05-02` | rollback proof |
| `05:r2-r46` | `REQ-AGT-08` | CONFIRMED | DESIGNED | P0 | `P00-02`, `P05-02`, `P05-04`, `P09-01`, `P09-02` | capability registry completeness + per-capability stop-condition test |

### PHASE-06 — المعرفة وحقوق المصادر وRAG · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r10` | `ADR-009` | CONFIRMED | APPROVED | P0 | `P00-04`, `P06-01` | rights gate on every source |
| `24:r2-r11` | `REQ-KNW-01` | CONFIRMED | DESIGNED | P0 | `P06-02` | per-collection metadata + isolation test |
| `25:r2` | `REQ-KNW-02` | CONFIRMED | BLOCK until ALLOWED | P0 | `P06-01` | AT-RAG-001 |
| `25:r2-r7` | `REQ-KNW-03` | CONFIRMED | DESIGNED | P0 | `P06-01` | rights register completeness |
| `24:r5` | `REQ-KNW-04` | CONFIRMED | DESIGNED | P0 | `P04-05`, `P06-02` | RAG isolation test |
| `37:r13` | `REQ-KNW-05` | CONFIRMED | Not verified | P0 | `P04-07`, `P06-03` | RAG evaluation report |
| `05:r11` | `REQ-KNW-06` | CONFIRMED | DESIGNED | P0 | `P06-03`, `P09-02` | citation validity + recall |

### PHASE-07 — الملاحظات والمراجعة والأهلية والتسليم · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r5` | `ADR-004` | CONFIRMED | APPROVED | P0 | `P00-04`, `P07-01`, `P07-04` | no critical report without findings |
| `02:r7` | `ADR-006` | CONFIRMED | APPROVED | P0 | `P00-04`, `P02-02`, `P07-05` | lock before decision |
| `02:r11` | `ADR-010` | CONFIRMED | APPROVED | P0 | `P00-04`, `P07-02`, `P07-05` | eligibility snapshot + COI + MFA |
| `27:r15` | `REQ-SEC-13` | CONFIRMED | CRITICAL | P0 | `P07-05` | mutation + revocation test |
| `39:r10` | `REQ-DAT-06` | CONFIRMED | proposed | P0 | `P07-04` | constraint test |
| `09:r17-r21` | `REQ-WF-05` | CONFIRMED | DESIGNED | P0 | `P07-03`, `P07-04` | review state tests |
| `09:r23-r26` | `REQ-WF-06` | CONFIRMED | DESIGNED | P0 | `P02-02`, `P07-05` | AT-DEL-001 |
| `10:r2-r22` | `REQ-FND-01` | CONFIRMED | DESIGNED | P0 | `P07-01`, `P07-04` | AT-REV-001 |
| `10:r12` | `REQ-FND-02` | CONFIRMED | DESIGNED | P0 | `P02-03`, `P07-01` | schema test + sample |
| `10:r14` | `REQ-FND-03` | CONFIRMED | DESIGNED | P0 | `P07-01` | confidence semantics test |
| `11:r2-r16` | `REQ-REV-01` | CONFIRMED | DESIGNED | P0 | `P07-02` | registry completeness test |
| `12:r2-r9` | `REQ-REV-02` | CONFIRMED | DESIGNED | P0 | `P07-02` | AT-REV-002 |
| `13:r2-r11` | `REQ-REV-03` | CONFIRMED | DESIGNED | P0 | `P07-03` | AT-REV-002 |
| `13:r3` | `REQ-REV-04` | CONFIRMED | DESIGNED | P0 | `P07-03` | hard-filter test |
| `13:r5` | `REQ-REV-05` | CONFIRMED | DESIGNED | P0 | `P07-03` | self-review rejection test |
| `13:r6` | `REQ-REV-06` | CONFIRMED | DESIGNED | P1 | `P07-03` | ranking reproducibility test |
| `14:r2-r11` | `REQ-DEL-01` | CONFIRMED | DESIGNED | P0 | `P07-05` | delivery E2E test |
| `14:r10` | `REQ-DEL-03` | CONFIRMED | DESIGNED | P1 | `P07-06` | verification + revocation test |
| `14:r11` | `REQ-DEL-04` | CONFIRMED | DESIGNED | P0 | `P02-02`, `P07-06` | AT-DEL-001 |
| `05:r6` | `REQ-DEL-05` | CONFIRMED | DESIGNED | P0 | `P07-05` | manifest completeness test |
| `23:r3` | `REQ-INT-02` | CONFIRMED | PARTNERSHIP | P0 | `P00-03`, `P06-03`, `P07-02` | verification channel evidence |
| `35:r6` | `REQ-SVC-02` | CONFIRMED | proposed | P0 | `P05-04`, `P07-05`, `P09-02` | guardrail test |

### PHASE-08 — التسعير والدفع والفوترة · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r8` | `ADR-007` | CONFIRMED | APPROVED | P0 | `P00-04`, `P08-03` | replay and ordering test |
| `27:r14` | `REQ-SEC-12` | CONFIRMED | CRITICAL | P0 | `P08-03`, `P08-04` | sandbox + failure tests |
| `21:r8` | `REQ-SEC-15` | CONFIRMED | DESIGNED | P0 | `P08-03` | PCI scope statement + storage scan |
| `14:r8` | `REQ-DEL-02` | CONFIRMED | DESIGNED | P0 | `P07-06`, `P08-04` | release gate test |
| `18:r2-r13` | `REQ-COM-01` | CONFIRMED | DESIGNED | P0 | `P08-01` | AT-PRICE-001 |
| `19:r54` | `REQ-COM-02` | CONFIRMED | warning | P0 | `P08-01` | rate completeness precondition |
| `19:r39-r52` | `REQ-COM-03` | CONFIRMED | DESIGNED | P0 | `P08-01` | formula parity test |
| `15:r14` | `REQ-COM-04` | CONFIRMED | DESIGNED | P0 | `P08-01` | AT-PRICE-001 |
| `28:r16` | `REQ-COM-05` | CONFIRMED | DESIGNED | P0 | `P08-02` | quote lock test |
| `21:r7` | `REQ-COM-06` | CONFIRMED | DESIGNED | P0 | `P08-03` | AT-PAY-001 |
| `15:r9` | `REQ-COM-07` | CONFIRMED | DESIGNED | P0 | `P08-03` | AT-PAY-002 |
| `21:r2-r6` | `REQ-COM-08` | CONFIRMED | VERIFY | P0 | `P08-03` | provider sandbox evidence |
| `23:r8` | `REQ-COM-09` | CONFIRMED | ONBOARD | P1 | `P08-04` | sandbox invoice acceptance |
| `19:r5-r35` | `REQ-OPN-03` | UNKNOWN | 0 | P0 | `P00-04`, `P08-01` | rate card provided by owner |

### PHASE-09 — المسار الذهبي لمراجعة الفيلا · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `08:r2-r11` | `REQ-WF-08` | CONFIRMED | PILOT TARGET | P0 | `P09-01`, `P09-02`, `P09-03` | 42:G01 villa E2E |
| `35:r6-r11` | `REQ-SVC-01` | CONFIRMED | proposed | P1 | `P09-03`, `P15-01` | per-service acceptance |

### PHASE-10 — الرصد والموثوقية وFinOps · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `27:r16` | `REQ-SEC-14` | CONFIRMED | DESIGNED | P0 | `P10-04`, `P11-03` | DR drill |
| `57:r11` | `REQ-COM-11` | CONFIRMED | UNVERIFIED | P0 | `P08-04`, `P10-03` | reconciliation run |
| `73:r2-r10` | `REQ-OBS-01` | CONFIRMED | NOT VERIFIED | P0 | `P10-02` | alert drill per dashboard |
| `73:r10` | `REQ-OBS-02` | CONFIRMED | NOT VERIFIED | P0 | `P10-01` | trace linkage test |
| `75:r2-r8` | `REQ-OBS-03` | CONFIRMED | NOT VERIFIED | P0 | `P04-04`, `P10-03` | runbook drill |
| `30:r2-r12` | `REQ-OBS-05` | CONFIRMED | PENDING | P0 | `P03-05`, `P10-02` | KPI source binding test |

### PHASE-11 — الأمن والخصوصية وPDPL · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `57:r10` | `REQ-SEC-06` | CONFIRMED | UNVERIFIED | P0 | `P05-03`, `P11-04` | red-team suite |
| `27:r9` | `REQ-SEC-07` | CONFIRMED | DEFINED | P0 | `P11-01` | RoPA + notice |
| `27:r10` | `REQ-SEC-08` | CONFIRMED | DEFINED | P0 | `P11-02` | AT-PRIV-001 |
| `27:r11` | `REQ-SEC-09` | CONFIRMED | DEFINED | P0 | `P11-03` | deletion test |
| `27:r12` | `REQ-SEC-10` | CONFIRMED | CRITICAL | P0 | `P11-04` | tabletop exercise |
| `27:r13` | `REQ-SEC-11` | CONFIRMED | DESIGNED | P1 | `P11-01` | annual vendor review |
| `77:r5` | `REQ-GW-19` | CONFIRMED | Adopt | P0 | `P00-03`, `P04-02`, `P11-04` | residency assessment per provider |

### PHASE-12 — المسح والالتقاط · `P1`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `71:r7` | `REQ-GW-15` | CONFIRMED | NOT VERIFIED | P0 | `P04-03`, `P12-03` | measurement provenance test |
| `49:r2-r8` | `REQ-SCN-01` | CONFIRMED | SPEC | P1 | `P12-01`, `P12-02`, `P12-03` | device matrix test |
| `49:r4` | `REQ-SCN-02` | CONFIRMED | SPEC | P1 | `P12-01` | sampling + budget test |
| `50:r2-r9` | `REQ-SCN-03` | CONFIRMED | SPEC | P1 | `P12-02` | contract + event tests |
| `57:r6` | `REQ-SCN-04` | CONFIRMED | SPECIFIED | P0 | `P12-03` | field validation report |
| `54:r6` | `REQ-SCN-05` | CONFIRMED | UNVERIFIED | P0 | `P11-04`, `P12-01` | consent and deletion tests |
| `66:r2-r6` | `REQ-SCN-06` | CONFIRMED | SPEC | P1 | `P12-01` | processing constraint test |

### PHASE-13 — لوحة التحكم الإدارية والموصلات والدعم · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `68:r4` | `REQ-GOV-03` | CONFIRMED | SPEC | P0 | `P01-04`, `P13-01` | no direct browser agent calls |
| `27:r4` | `REQ-SEC-01` | CONFIRMED | DESIGNED | P0 | `P04-04`, `P13-02` | scanning + rotation drill |
| `65:r2-r9` | `REQ-API-09` | CONFIRMED | SPEC | P0 | `P13-01`, `P13-04` | admin contract tests |
| `70:r13` | `REQ-GW-12` | CONFIRMED | NOT VERIFIED | P0 | `P13-03` | change audit completeness |
| `61:r2-r8` | `REQ-OBS-04` | CONFIRMED | SPEC | P0 | `P10-03`, `P12-03`, `P13-04` | scenario drill |
| `58:r2-r17` | `REQ-ADM-01` | CONFIRMED | SPEC | P0 | `P13-03`, `P13-04` | admin negative authorization tests |
| `59:r2-r10` | `REQ-ADM-02` | CONFIRMED | SPEC | P0 | `P13-03` | matrix enforcement test |
| `57:r3` | `REQ-ADM-03` | CONFIRMED | SPECIFIED | P0 | `P13-01` | negative authorization tests |
| `60:r2-r7` | `REQ-ADM-04` | CONFIRMED | SPEC | P0 | `P13-02` | revocation test |
| `60:r4` | `REQ-ADM-05` | CONFIRMED | SPEC | P0 | `P13-02` | sandbox contract tests |
| `52:r2-r9` | `REQ-ADM-06` | CONFIRMED | SPEC | P0 | `P13-01` | per-area acceptance |
| `58:r14` | `REQ-ADM-07` | CONFIRMED | SPEC | P0 | `P13-03` | expiry test |

### PHASE-14 — التقييم والتعلم وبوابات الإصدار · `P0`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `02:r9` | `ADR-008` | CONFIRMED | APPROVED | P0 | `P00-04`, `P14-04` | evidence board |
| `68:r7` | `REQ-GOV-04` | CONFIRMED | SPEC | P0 | `P09-03`, `P14-04` | gate record completeness check |
| `15:r19` | `REQ-GOV-07` | CONFIRMED | DESIGNED | P0 | `P14-04` | status vocabulary enforcement |
| `32:r3` | `REQ-GOV-08` | CONFIRMED | APPROVED | P0 | `P14-04` | artifact scan for unevidenced READY |
| `77:r3` | `REQ-GW-18` | CONFIRMED | Adopt | P0 | `P14-02` | benchmark report |
| `24:r11` | `REQ-KNW-07` | CONFIRMED | DESIGNED | P0 | `P14-01` | leakage control test |
| `13:r11` | `REQ-REV-07` | CONFIRMED | DESIGNED | P1 | `P14-05` | policy test |
| `17:r2-r12` | `REQ-OBS-06` | CONFIRMED | DESIGNED | P0 | `P14-01`, `P14-03`, `P14-05` | metric computation test |
| `17:r17-r26` | `REQ-OBS-07` | CONFIRMED | DESIGNED | P1 | `P14-05` | cycle instrumentation |
| `16:r2-r14` | `REQ-EVL-01` | CONFIRMED | PENDING | P0 | `P00-02`, `P11-02`, `P14-04` | all thirteen executed with evidence |
| `15:r2-r17` | `REQ-EVL-02` | CONFIRMED | DESIGNED/DEFINED | P0 | `P00-02`, `P14-04` | per-control evidence link |
| `15:r12` | `REQ-EVL-03` | CONFIRMED | DESIGNED | P0 | `P14-03` | AT-EVAL-001 |
| `64:r2-r8` | `REQ-EVL-04` | CONFIRMED | NOT TESTED | P0 | `P14-01`, `P14-02` | per-dimension evaluation report |
| `37:r6-r15` | `REQ-EVL-05` | CONFIRMED | Not verified | P0 | `P02-03`, `P14-04`, `P14-05` | traceability completeness |
| `38:r6-r15` | `REQ-EVL-06` | CONFIRMED | Open | P0 | `P14-04` | all gates evidenced |
| `42:r5-r16` | `REQ-EVL-07` | CONFIRMED | NOT RUN | P0 | `P09-03`, `P14-04` | ledger populated with reproducible evidence |
| `54:r2-r13` | `REQ-EVL-08` | CONFIRMED | UNVERIFIED | P0 | `P10-04`, `P11-04`, `P14-04` | all P0 gates verified |
| `76:r2-r11` | `REQ-EVL-09` | CONFIRMED | NOT VERIFIED | P0 | `P14-04` | all ten gates evidenced |
| `40:r7-r14` | `REQ-EVL-10` | CONFIRMED | UNVERIFIED/BLOCKED | P0 | `P14-04` | cockpit recomputed from real evidence |
| `30:r14` | `REQ-OPN-02` | UNKNOWN | TBD | P0 | `P00-04`, `P14-03`, `P14-05` | baseline measurement before threshold setting |
| `57:r7` | `REQ-OPN-07` | CONFIRMED | UNVERIFIED | P0 | `P14-02` | golden-set evaluation report |

### PHASE-15 — التوسع في المسارات التخصصية · `P1`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `39:r11` | `REQ-DAT-07` | CONFIRMED | proposed | P1 | `P15-02` | constraint test |
| `06:r2-r9` | `REQ-AGT-09` | CONFIRMED | DESIGNED | P1 | `P05-04`, `P15-03` | per-capability acceptance |
| `22:r2-r30` | `REQ-INT-05` | CONFIRMED | mixed | P1 | `P15-02` | per-tool validation before adoption |
| `07:r3` | `REQ-EXP-01` | CONFIRMED | DEFINED | P1 | `P15-02` | AT-BIM-v1 defined and executed |
| `07:r4` | `REQ-EXP-02` | CONFIRMED | DEFINED | P1 | `P15-02` | AT-QTO-v1 defined and executed |
| `07:r6` | `REQ-EXP-03` | CONFIRMED | DEFINED | P1 | `P15-03` | AT-MEP-v1 defined and executed |
| `07:r7` | `REQ-EXP-04` | CONFIRMED | DEFINED | P1 | `P15-03` | AT-INFRA-v1 defined and executed |
| `07:r5` | `REQ-EXP-05` | CONFIRMED | DEFINED | P1 | `P15-03` | AT-SITE-v1 defined and executed |
| `20:r2-r6` | `REQ-EXP-06` | CONFIRMED | DESIGNED | P1 | `P15-01` | scenario pricing review |
| `29:r2-r8` | `REQ-EXP-07` | CONFIRMED | PLANNED | P1 | `P15-01`, `P15-03` | per-stage decision gate |

### PHASE-16 — التجارة المؤجلة (خارج نطاق الإطلاق) · `DEFERRED`

| source_ref | req_id | class | state (source) | crit | prompts | acceptance_ref |
|---|---|---|---|---|---|---|
| `68:r8` | `REQ-GOV-02` | CONFIRMED | DEFERRED | DEFERRED | `P16-01` | owner authorization required before any work |
| `45:r2-r10` | `REQ-AGT-10` | CONFIRMED | SPEC | DEFERRED | `P16-02` | entitlement tests |
| `46:r2-r9` | `REQ-AGT-11` | CONFIRMED | SPEC | DEFERRED | `P16-02` | stage validation tests |
| `43:r2-r9` | `REQ-DEF-01` | CONFIRMED | DESIGN ONLY | DEFERRED | `P16-02` | owner authorization + isolation tests |
| `47:r2-r6` | `REQ-DEF-02` | CONFIRMED | SPEC | DEFERRED | `P16-02` | domain and embed tests |
| `48:r2-r7` | `REQ-DEF-03` | CONFIRMED | SPEC | DEFERRED | `P16-02` | reconciliation tests |
| `53:r2-r10` | `REQ-DEF-04` | CONFIRMED | SPEC | DEFERRED | `P16-02` | contract tests |
| `55:r2-r11` | `REQ-DEF-05` | CONFIRMED | P0-in-B2B-scope | DEFERRED | `P16-01` | per-delta validation |
| `57:r9` | `REQ-DEF-06` | CONFIRMED | PLANNED | DEFERRED | `P16-01` | isolation test |

---

## العرض المعاكس: أمر ← متطلبات

| prompt_id | phase | prereq | requirements covered |
|---|---|---|---|
| `P00-01` | `PHASE-00` | — | `REQ-GOV-05`, `REQ-OPN-01` |
| `P00-02` | `PHASE-00` | `P00-01` | `REQ-WF-07`, `REQ-AGT-08`, `REQ-EVL-01`, `REQ-EVL-02`, `REQ-DAT-01` |
| `P00-03` | `PHASE-00` | `P00-01`, `P00-02` | `REQ-GOV-06`, `REQ-INT-01`, `REQ-INT-04`, `REQ-INT-02`, `REQ-INT-03`, `REQ-GW-19` |
| `P00-04` | `PHASE-00` | `P00-01`, `P00-02`, `P00-03` | `REQ-OPN-04`, `REQ-OPN-05`, `REQ-OPN-06`, `REQ-OPN-02`, `REQ-OPN-03`, `ADR-001`, `ADR-002`, `ADR-003`, `ADR-004`, `ADR-005`, `ADR-006`, `ADR-007`, `ADR-008`, `ADR-009`, `ADR-010` |
| `P01-01` | `PHASE-01` | `P00-04` | `REQ-DAT-01`, `REQ-DAT-02`, `REQ-SEC-03`, `REQ-GOV-01`, `REQ-TEN-02`, `REQ-TEN-04` |
| `P01-02` | `PHASE-01` | `P01-01` | `ADR-003`, `REQ-TEN-01`, `REQ-TEN-03`, `REQ-TEN-06`, `REQ-API-03` |
| `P01-03` | `PHASE-01` | `P01-02` | `REQ-TEN-05`, `REQ-TEN-07`, `REQ-TEN-08`, `REQ-TEN-09`, `REQ-INT-03` |
| `P01-04` | `PHASE-01` | `P01-03` | `REQ-GW-02`, `REQ-TEN-05`, `REQ-GOV-03` |
| `P01-05` | `PHASE-01` | `P01-04` | `REQ-SEC-04`, `REQ-DAT-01`, `REQ-TEN-08` |
| `P02-01` | `PHASE-02` | `P01-05` | `REQ-SEC-02`, `REQ-DAT-05`, `REQ-API-01` |
| `P02-02` | `PHASE-02` | `P02-01` | `ADR-006`, `REQ-DEL-04`, `REQ-DAT-05`, `REQ-WF-06` |
| `P02-03` | `PHASE-02` | `P02-02` | `REQ-FND-02`, `REQ-API-05`, `REQ-DAT-05`, `REQ-EVL-05` |
| `P03-01` | `PHASE-03` | `P02-03` | `ADR-001`, `REQ-WF-02`, `REQ-WF-07`, `REQ-WF-10` |
| `P03-02` | `PHASE-03` | `P03-01` | `REQ-WF-01`, `REQ-WF-03`, `REQ-WF-09`, `REQ-DAT-03` |
| `P03-03` | `PHASE-03` | `P03-02` | `REQ-WF-04`, `REQ-DAT-09`, `REQ-DAT-10`, `REQ-API-04`, `REQ-API-05` |
| `P03-04` | `PHASE-03` | `P03-03` | `REQ-API-01`, `REQ-API-02`, `REQ-API-03`, `REQ-WF-01` |
| `P03-05` | `PHASE-03` | `P03-04` | `REQ-WF-09`, `REQ-WF-01`, `REQ-OBS-05` |
| `P04-01` | `PHASE-04` | `P03-05` | `ADR-002`, `REQ-GW-01`, `REQ-GW-02`, `REQ-API-06`, `REQ-API-07`, `REQ-API-08` |
| `P04-02` | `PHASE-04` | `P04-01` | `REQ-GW-03`, `REQ-GW-13`, `REQ-GW-19`, `REQ-GW-20` |
| `P04-03` | `PHASE-04` | `P04-02` | `REQ-GW-04`, `REQ-GW-14`, `REQ-GW-15`, `REQ-GW-16`, `REQ-GW-17` |
| `P04-04` | `PHASE-04` | `P04-03` | `REQ-GW-05`, `REQ-GW-06`, `REQ-GW-17`, `REQ-SEC-01`, `REQ-OBS-03` |
| `P04-05` | `PHASE-04` | `P04-04` | `REQ-GW-07`, `REQ-GW-08`, `REQ-KNW-04` |
| `P04-06` | `PHASE-04` | `P04-05` | `REQ-GW-09`, `REQ-GW-11`, `REQ-DAT-08`, `REQ-COM-10`, `REQ-AGT-01` |
| `P04-07` | `PHASE-04` | `P04-06` | `REQ-GW-10`, `REQ-GW-16`, `REQ-AGT-04`, `REQ-KNW-05` |
| `P05-01` | `PHASE-05` | `P04-07` | `REQ-AGT-01`, `REQ-AGT-02`, `REQ-AGT-04`, `REQ-AGT-05`, `REQ-DAT-04` |
| `P05-02` | `PHASE-05` | `P05-01` | `REQ-AGT-03`, `REQ-AGT-06`, `REQ-AGT-07`, `REQ-AGT-08` |
| `P05-03` | `PHASE-05` | `P05-02` | `REQ-SEC-05`, `REQ-SEC-06`, `REQ-AGT-03`, `REQ-AGT-02` |
| `P05-04` | `PHASE-05` | `P05-03` | `ADR-005`, `REQ-AGT-08`, `REQ-AGT-09`, `REQ-SVC-02` |
| `P06-01` | `PHASE-06` | `P02-03` | `ADR-009`, `REQ-KNW-02`, `REQ-KNW-03` |
| `P06-02` | `PHASE-06` | `P06-01` | `REQ-KNW-01`, `REQ-KNW-04`, `REQ-GW-07` |
| `P06-03` | `PHASE-06` | `P06-02` | `REQ-KNW-05`, `REQ-KNW-06`, `REQ-GW-14`, `REQ-INT-02` |
| `P07-01` | `PHASE-07` | `P06-03` | `ADR-004`, `REQ-FND-01`, `REQ-FND-02`, `REQ-FND-03` |
| `P07-02` | `PHASE-07` | `P07-01` | `REQ-REV-01`, `REQ-REV-02`, `REQ-INT-02`, `ADR-010` |
| `P07-03` | `PHASE-07` | `P07-02` | `REQ-REV-03`, `REQ-REV-04`, `REQ-REV-05`, `REQ-REV-06`, `REQ-WF-05` |
| `P07-04` | `PHASE-07` | `P07-03` | `ADR-004`, `REQ-FND-01`, `REQ-DAT-06`, `REQ-WF-05`, `REQ-API-05` |
| `P07-05` | `PHASE-07` | `P07-04` | `ADR-006`, `ADR-010`, `REQ-DEL-01`, `REQ-DEL-05`, `REQ-SEC-13`, `REQ-SVC-02`, `REQ-WF-06` |
| `P07-06` | `PHASE-07` | `P07-05` | `REQ-DEL-02`, `REQ-DEL-03`, `REQ-DEL-04`, `REQ-API-01`, `REQ-API-05` |
| `P08-01` | `PHASE-08` | `P07-06` | `REQ-COM-01`, `REQ-COM-02`, `REQ-COM-03`, `REQ-COM-04`, `REQ-OPN-03` |
| `P08-02` | `PHASE-08` | `P08-01` | `REQ-COM-05`, `REQ-WF-01`, `REQ-API-01`, `REQ-API-05` |
| `P08-03` | `PHASE-08` | `P08-02` | `ADR-007`, `REQ-COM-06`, `REQ-COM-07`, `REQ-COM-08`, `REQ-SEC-12`, `REQ-SEC-15` |
| `P08-04` | `PHASE-08` | `P08-03` | `REQ-COM-09`, `REQ-COM-11`, `REQ-SEC-12`, `REQ-DEL-02`, `REQ-INT-01` |
| `P09-01` | `PHASE-09` | `P08-04` | `REQ-WF-08`, `REQ-AGT-08` |
| `P09-02` | `PHASE-09` | `P09-01` | `REQ-WF-08`, `REQ-AGT-08`, `REQ-KNW-06`, `REQ-SVC-02` |
| `P09-03` | `PHASE-09` | `P09-02` | `REQ-WF-08`, `REQ-EVL-07`, `REQ-SVC-01`, `REQ-GOV-04` |
| `P10-01` | `PHASE-10` | `P09-03` | `REQ-OBS-02`, `REQ-GW-11`, `REQ-SEC-04` |
| `P10-02` | `PHASE-10` | `P10-01` | `REQ-OBS-01`, `REQ-OBS-05`, `REQ-GW-11` |
| `P10-03` | `PHASE-10` | `P10-02` | `REQ-OBS-03`, `REQ-OBS-04`, `REQ-COM-11` |
| `P10-04` | `PHASE-10` | `P10-03` | `REQ-SEC-14`, `REQ-SEC-03`, `REQ-EVL-08` |
| `P11-01` | `PHASE-11` | `P10-04` | `REQ-SEC-07`, `REQ-SEC-11` |
| `P11-02` | `PHASE-11` | `P11-01` | `REQ-SEC-08`, `REQ-EVL-01` |
| `P11-03` | `PHASE-11` | `P11-02` | `REQ-SEC-09`, `REQ-DAT-01`, `REQ-SEC-14` |
| `P11-04` | `PHASE-11` | `P11-03` | `REQ-SEC-06`, `REQ-SEC-10`, `REQ-GW-19`, `REQ-SCN-05`, `REQ-EVL-08` |
| `P12-01` | `PHASE-12` | `P11-04` | `REQ-SCN-01`, `REQ-SCN-02`, `REQ-SCN-05`, `REQ-SCN-06` |
| `P12-02` | `PHASE-12` | `P12-01` | `REQ-SCN-03`, `REQ-SCN-01`, `REQ-SEC-02`, `REQ-API-05` |
| `P12-03` | `PHASE-12` | `P12-02` | `REQ-SCN-04`, `REQ-GW-15`, `REQ-SCN-01`, `REQ-OBS-04` |
| `P13-01` | `PHASE-13` | `P12-03` | `REQ-GOV-03`, `REQ-ADM-03`, `REQ-ADM-06`, `REQ-API-09` |
| `P13-02` | `PHASE-13` | `P13-01` | `REQ-ADM-04`, `REQ-ADM-05`, `REQ-SEC-01`, `REQ-INT-04` |
| `P13-03` | `PHASE-13` | `P13-02` | `REQ-ADM-01`, `REQ-ADM-02`, `REQ-ADM-07`, `REQ-GW-12` |
| `P13-04` | `PHASE-13` | `P13-03` | `REQ-OBS-04`, `REQ-ADM-01`, `REQ-API-09`, `REQ-TEN-07` |
| `P14-01` | `PHASE-14` | `P13-04` | `REQ-KNW-07`, `REQ-EVL-04`, `REQ-OBS-06` |
| `P14-02` | `PHASE-14` | `P14-01` | `REQ-EVL-04`, `REQ-GW-18`, `REQ-GW-13`, `REQ-OPN-07` |
| `P14-03` | `PHASE-14` | `P14-02` | `REQ-EVL-03`, `REQ-AGT-06`, `REQ-OBS-06`, `REQ-OPN-02` |
| `P14-04` | `PHASE-14` | `P14-03` | `ADR-008`, `REQ-GOV-04`, `REQ-GOV-07`, `REQ-GOV-08`, `REQ-EVL-01`, `REQ-EVL-02`, `REQ-EVL-05`, `REQ-EVL-06`, `REQ-EVL-07`, `REQ-EVL-08`, `REQ-EVL-09`, `REQ-EVL-10` |
| `P14-05` | `PHASE-14` | `P14-04` | `REQ-OBS-06`, `REQ-OBS-07`, `REQ-REV-07`, `REQ-EVL-05`, `REQ-OPN-02` |
| `P15-01` | `PHASE-15` | `P14-05` | `REQ-EXP-07`, `REQ-EXP-06`, `REQ-SVC-01` |
| `P15-02` | `PHASE-15` | `P15-01` | `REQ-EXP-01`, `REQ-EXP-02`, `REQ-DAT-07`, `REQ-INT-05` |
| `P15-03` | `PHASE-15` | `P15-02` | `REQ-EXP-03`, `REQ-EXP-04`, `REQ-EXP-05`, `REQ-AGT-09`, `REQ-EXP-07` |
| `P16-01` | `PHASE-16` | `P14-04` | `REQ-GOV-02`, `REQ-DEF-05`, `REQ-DEF-06` |
| `P16-02` | `PHASE-16` | `P16-01` | `REQ-DEF-01`, `REQ-DEF-02`, `REQ-DEF-03`, `REQ-DEF-04`, `REQ-AGT-10`, `REQ-AGT-11` |

---

## فهرس اختبارات القبول في المصدر (الورقة 16)

الاختبارات الثلاثة عشر `AT-*` هي ضوابط القبول المُسمّاة في المصدر. كل واحد منها يُنفَّذ في أمر محدد:

| test_id | الأمر الذي ينفّذه | المرحلة |
|---|---|---|
| `AT-SEC-001` | `P01-02` | `PHASE-01` |
| `AT-FILE-001` | `P02-01` | `PHASE-02` |
| `AT-WF-002` | `P03-01` | `PHASE-03` |
| `AT-WF-001` | `P03-02` | `PHASE-03` |
| `AT-RAG-001` | `P06-01` | `PHASE-06` |
| `AT-REV-001` | `P07-04` | `PHASE-07` |
| `AT-REV-002` | `P07-03` | `PHASE-07` |
| `AT-DEL-001` | `P07-05` | `PHASE-07` |
| `AT-PRICE-001` | `P08-01` | `PHASE-08` |
| `AT-PAY-001` | `P08-03` | `PHASE-08` |
| `AT-PAY-002` | `P08-03` | `PHASE-08` |
| `AT-PRIV-001` | `P11-02` | `PHASE-11` |
| `AT-EVAL-001` | `P14-03` | `PHASE-14` |

والاختبار المركّب `AT-VILLA-v1` (الورقة 07 الصف 2) يُعرَّف ويُنفَّذ في `P09-03`، وهو دليل البند `G01` في دفتر الأدلة.

---

## تحذير

تغطية المتطلب بأمر تنفيذي تعني أن **خطة** تنفيذه موجودة. ولا تعني أنه
مُنفَّذ أو مُختبَر. حالة التنفيذ الحقيقية تُقرأ من دفتر الأدلة الذي يبنيه
`P14-04`، وفقاً للقرار `ADR-008`.

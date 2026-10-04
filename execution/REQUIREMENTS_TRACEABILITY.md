<!-- coverage: total=247 covered=214 deferred=33 uncovered=0 -->

# REQUIREMENTS_TRACEABILITY — Sketch Design V2

مصفوفة التتبّع. **مُولَّدة آليًا** من السجلّين بـ `execution/_tools/gen_traceability.py`.
لا تُحرَّر يدويًا: التغطية تُحسَب ولا تُدَّعى.

## 1. الحصيلة | Totals

| | العدد |
| --- | --- |
| متطلبات من مصنف v11 (`EXECUTION_BLUEPRINT/_registry/requirements.tsv`) | 192 |
| متطلبات من المرجع الشامل 2026 (`execution/_registry/v2-requirements.tsv`) | 55 |
| **الإجمالي** | **247** |
| مغطّاة بأمر واحد على الأقل | 214 |
| **مؤجَّلة صراحةً** خارج نطاق هذه الحزمة | 33 |
| **غير مغطّاة** | 0 |

لا متطلب غير مغطّى وغير مؤجَّل. المؤجَّل **ليس مغطّى**، ويُعدّ منفصلًا بقصد.

## 2. التغطية لكل أمر | Coverage per prompt

| الأمر | عدد المتطلبات | المعرّفات |
| --- | --- | --- |
| `P00` | 12 | REQ-GOV-05، REQ-GOV-06، REQ-INT-01، REQ-INT-04، REQ-OPN-01، REQ-OPN-04، REQ-OPN-05، REQ-OPN-06، UR-029، UR-048، UR-050، UR-051 |
| `P01` | 18 | ADR-003، REQ-API-03، REQ-DAT-01، REQ-DAT-02، REQ-GOV-01، REQ-INT-03، REQ-SEC-03، REQ-SEC-04، REQ-TEN-01، REQ-TEN-02، REQ-TEN-03، REQ-TEN-04، REQ-TEN-05، REQ-TEN-06 … (+4) |
| `P02` | 23 | ADR-003، REQ-API-03، REQ-DAT-01، REQ-DAT-02، REQ-GOV-01، REQ-INT-03، REQ-SEC-03، REQ-SEC-04، REQ-TEN-01، REQ-TEN-02، REQ-TEN-03، REQ-TEN-04، REQ-TEN-05، REQ-TEN-06 … (+9) |
| `P03` | 4 | REQ-DAT-05، REQ-SEC-02، UR-018، UR-040 |
| `P04` | 20 | ADR-001، REQ-API-01، REQ-API-02، REQ-API-04، REQ-API-05، REQ-DAT-03، REQ-DAT-09، REQ-DAT-10، REQ-WF-01، REQ-WF-02، REQ-WF-03، REQ-WF-04، REQ-WF-07، REQ-WF-09 … (+6) |
| `P05` | 27 | ADR-002، REQ-API-06، REQ-API-07، REQ-API-08، REQ-COM-10، REQ-DAT-08، REQ-GW-01، REQ-GW-02، REQ-GW-03، REQ-GW-04، REQ-GW-05، REQ-GW-06، REQ-GW-07، REQ-GW-08 … (+13) |
| `P06` | 24 | ADR-002، REQ-API-06، REQ-API-07، REQ-API-08، REQ-COM-10، REQ-DAT-08، REQ-GW-01، REQ-GW-02، REQ-GW-03، REQ-GW-04، REQ-GW-05، REQ-GW-06، REQ-GW-07، REQ-GW-08 … (+10) |
| `P07` | 17 | ADR-005، REQ-AGT-01، REQ-AGT-02، REQ-AGT-03، REQ-AGT-04، REQ-AGT-05، REQ-AGT-06، REQ-AGT-07، REQ-AGT-08، REQ-DAT-04، REQ-SEC-05، UR-014، UR-020، UR-021 … (+3) |
| `P09` | 9 | ADR-009، REQ-KNW-01، REQ-KNW-02، REQ-KNW-03، REQ-KNW-04، REQ-KNW-05، REQ-KNW-06، UR-016، UR-028 |
| `P10` | 3 | REQ-SVC-01، REQ-WF-08، UR-022 |
| `P11` | 23 | ADR-004، ADR-006، ADR-010، REQ-DAT-06، REQ-DEL-01، REQ-DEL-03، REQ-DEL-04، REQ-DEL-05، REQ-FND-01، REQ-FND-02، REQ-FND-03، REQ-INT-02، REQ-REV-01، REQ-REV-02 … (+9) |
| `P12` | 6 | UR-001، UR-002، UR-003، UR-004، UR-005، UR-052 |
| `P13` | 1 | UR-007 |
| `P14` | 10 | REQ-GW-15، REQ-SCN-01، REQ-SCN-02، REQ-SCN-03، REQ-SCN-04، REQ-SCN-05، REQ-SCN-06، UR-038، UR-039، UR-041 |
| `P15` | 7 | REQ-GW-15، REQ-SCN-01، REQ-SCN-02، REQ-SCN-03، REQ-SCN-04، REQ-SCN-05، REQ-SCN-06 |
| `P16` | 16 | REQ-ADM-01، REQ-ADM-02، REQ-ADM-03، REQ-ADM-04، REQ-ADM-05، REQ-ADM-06، REQ-ADM-07، REQ-API-09، REQ-GOV-03، REQ-GW-12، REQ-OBS-04، REQ-SEC-01، UR-013، UR-037 … (+2) |
| `P17` | 9 | REQ-COM-11، REQ-OBS-01، REQ-OBS-02، REQ-OBS-03، REQ-OBS-05، REQ-SEC-14، UR-036، UR-044، UR-054 |
| `P18` | 9 | REQ-GW-19، REQ-SEC-06، REQ-SEC-07، REQ-SEC-08، REQ-SEC-09، REQ-SEC-10، REQ-SEC-11، UR-053، UR-055 |
| `P19` | 21 | ADR-008، REQ-EVL-01، REQ-EVL-02، REQ-EVL-03، REQ-EVL-04، REQ-EVL-05، REQ-EVL-06، REQ-EVL-07، REQ-EVL-08، REQ-EVL-09، REQ-EVL-10، REQ-GOV-04، REQ-GOV-07، REQ-GOV-08 … (+7) |
| `P20` | 1 | UR-049 |

## 3. المؤجَّل صراحةً | Deliberately deferred

هذه المتطلبات **ليست مغطّاة**، وعدم تغطيتها قرار لا سهو.

### commerce — 23 متطلبًا

مؤجَّل بقرار معتمد ADR-V2-009: الإطلاق لمشغّل واحد، والتجارة الذاتية خارج نطاق الإطلاق.

`ADR-007`، `REQ-AGT-10`، `REQ-AGT-11`، `REQ-COM-01`، `REQ-COM-02`، `REQ-COM-03`، `REQ-COM-04`، `REQ-COM-05`، `REQ-COM-06`، `REQ-COM-07`، `REQ-COM-08`، `REQ-COM-09`، `REQ-DEF-01`، `REQ-DEF-02`، `REQ-DEF-03`، `REQ-DEF-04`، `REQ-DEF-05`، `REQ-DEF-06`، `REQ-DEL-02`، `REQ-GOV-02`، `REQ-OPN-03`، `REQ-SEC-12`، `REQ-SEC-15`

### specialist — 10 متطلبًا

خارج نطاق هذه الحزمة: المسارات التخصصية تتوسع بعد إثبات المسار الذهبي في P10.

`REQ-AGT-09`، `REQ-DAT-07`، `REQ-EXP-01`، `REQ-EXP-02`، `REQ-EXP-03`، `REQ-EXP-04`، `REQ-EXP-05`، `REQ-EXP-06`، `REQ-EXP-07`، `REQ-INT-05`

## 4. تعارضات الاصطلاح بين المرجعين | Convention conflicts

المرجعان يتعايشان، وهذه نقاط اختلافهما الصريحة. **تحكم هذه الحزمة للتنفيذ الإنتاجي**،
ويبقى المرجع الأول مصدرًا للمتطلبات وجردها.

| الموضوع | `EXECUTION_BLUEPRINT` | هذه الحزمة | الحاكم |
| --- | --- | --- | --- |
| مفردات الحالة | كلمة المصدر الأصلية لكل بند | `DESIGNED/IMPLEMENTED/TESTED/VERIFIED/BLOCKED` | هذه الحزمة |
| تسمية الأوامر | `P00-01` داخل ملف مرحلة | `P00_DISCOVERY.md` ملف لكل أمر | هذه الحزمة |
| بنية الأمر | سبعة أقسام A–G | اثنا عشر عنصرًا، منها التراجع والأدلة | هذه الحزمة |
| الموقع | `EXECUTION_BLUEPRINT/PHASES/` | `execution/prompts/` | الاثنان، لغرضين |
| المكدس القديم | غير مذكور في مصنف v11 | **متقاعد صراحةً** (`ADR-V2-001`) | هذه الحزمة |
| التجارة | `PHASE-08` و`PHASE-16` بتفصيل | مؤجَّلة خارج النطاق | هذه الحزمة للإطلاق |

**ملاحظة على التقاعد.** قرار تقاعد AI Core والمكدس السابق **لا يوجد في مصنف v11**؛
مصدره الوحيد هو المرجع الشامل 2026. وهو معلومة جديدة تعلو على أي افتراض سابق،
لا تناقضًا بين مصدرين.

## 5. ما لا تثبته هذه المصفوفة | What this matrix does not prove

تثبت أن كل متطلب **مُسنَد إلى أمر**. لا تثبت أن الأمر نُفِّذ، ولا أن التنفيذ صحيح،
ولا أن المتطلب مُحقَّق. الإسناد نية؛ والدليل المُنفَّذ في `P20` هو ما يثبت التحقق.

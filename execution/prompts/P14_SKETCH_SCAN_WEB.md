<!-- promptmeta
id: P14
file: P14_SKETCH_SCAN_WEB.md
stage: 5 — Sketch Scan
title_en: Sketch Scan on mobile web: capture, consent, quality and measurement honesty
prereq: P13
requirements: UR-038,UR-039,UR-041,UR-040
status: DESIGNED
-->

# P14_SKETCH_SCAN_WEB — Sketch Scan on mobile web: capture, consent, quality and measurement honesty

**سكيتش سكان على الويب المحمول: الالتقاط والموافقة والجودة وصدق القياس**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 5 — Sketch Scan |
| المتطلب السابق | P13 |
| المتطلبات المغطّاة | UR-038، UR-039، UR-041، UR-040 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ سطح الالتقاط على الويب المحمول بضوابطه الثمانية، مع إعلان صريح أن الهندسة المستخرجة من الكاميرا دليل أولي لا قياس معتمد.

**لماذا نحتاجه؟**  
المرجع يحدد الويب المحمول أولًا، ويمنع الوعد بـ LiDAR عام في المتصفح، ويضع حدًا أمنيًا: لا ضمان إنشائي ولا امتثال تصاريح ولا أبعاد معتمدة من مخرج كاميرا حي.

**ما المتطلبات السابقة؟**  
اكتمال P13 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
التقاط صور وفيديو وتحليل حي اختياري، مع فحص قدرات الجهاز، وموافقة صريحة، ومؤشرات عدم يقين على كل قياس.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا عُرض قياس بلا عدم يقين، أو إذا استمر الالتقاط دون مؤشر مرئي، أو إذا ادّعت الواجهة قياسًا معتمدًا.

## EXECUTABLE PROMPT

```text
You are executing P14_SKETCH_SCAN_WEB of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Implement the mobile web capture surface with all eight controls the reference specifies, honest uncertainty on every measurement, and the safety boundary enforced in the product rather than stated in a footnote.

2. DEPENDENCIES
P13 — capture attaches to a project in the customer workspace.

3. EXACT SCOPE
IN SCOPE:
- Device and browser capability detection before offering any capture mode; an unsupported capability is not offered rather than offered and failing.
- Photo capture with metadata, blur and lighting quality checks, and explicit consent.
- Time-limited video recording with upload progress and resume.
- Opt-in live analysis over selected frames, showing provisional findings and the actual latency.
- Measurement display with estimated dimensions, uncertainty, unit system and calibration state.
- A versioned evidence list with delete, retake, timestamps and audit trail.
- Privacy: no background capture, visible camera and microphone indicators, stated retention and consent.
- Offline and poor-network handling: local draft with resumable, securely expiring transfer.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not claim or imply browser LiDAR. The companion handoff is P15.
- Do not present any camera-derived dimension as certified, permit-compliant or structurally assured.
- Do not capture location at a precision finer than the recorded policy permits.

4. FILES AND MODULES AFFECTED
- apps/web/features/scan/
- apps/web/features/scan/capability/
- apps/web/features/scan/quality/
- services/evidence/capture/ — server-side capture session handling

5. REQUIRED CONTRACTS
- Every measurement renders as { value, unit, uncertainty, method, calibration_state }. A measurement without uncertainty cannot be rendered; the component requires the field.
- calibration_state is one of CALIBRATED, UNCALIBRATED or CALIBRATION_UNKNOWN. UNCALIBRATED and CALIBRATION_UNKNOWN both display a prominent qualifier.
- Capability detection returns a capability set; the UI offers only modes present in that set and states plainly which modes the device does not support.
- A capture session carries its consent record before the first frame is retained. Consent is not a checkbox at the end.
- Quality checks produce quality_flags on the evidence record; a failed quality check does not block capture but is carried forward so that downstream findings inherit the flag.

6. IMPLEMENTATION INSTRUCTIONS
- Detect capability first and degrade honestly. An unsupported mode is named as unsupported with the reason, not silently absent.
- Make uncertainty a required prop so a measurement cannot be displayed without it. A type-level requirement outlasts a code review note.
- Show real latency on live analysis. A spinner that does not reflect actual processing time is fabricated progress.
- Carry quality flags into the evidence record so a later finding derived from a blurry capture inherits that context.
- Honour the platform's camera and microphone indicators and never retain frames outside an active, consented session.
- State the safety boundary in the capture flow itself, at the point of measurement, in Arabic: camera-derived geometry is preliminary evidence subject to field verification.
- Mirrors, glass, occlusion, lighting and device variation distort measurements. Where the quality check can detect these conditions, flag them specifically rather than lowering a generic confidence number.

7. SECURITY REQUIREMENTS
- Camera and microphone access is requested only on explicit user action and released when the session ends.
- Local drafts are encrypted at rest where the platform permits and expire on a defined schedule.
- Resumable upload tokens are short-lived, single-session and scoped to one evidence record.
- Retention and deletion of raw media follow the recorded policy; a deleted capture is removed from the read path and its deletion is audited.
- No capture occurs while the application is backgrounded.

8. AUTOMATED TESTS
- Unit: rendering a measurement without uncertainty fails at the type level and at runtime.
- Unit: each calibration_state renders its required qualifier, one test per state.
- Integration: a device profile lacking a capability never sees that mode offered, across a generated device-profile matrix.
- Integration: capture before consent is rejected server-side, not only hidden client-side.
- Integration: an interrupted upload resumes and produces exactly one evidence record.
- Integration: quality flags propagate from capture to the derived finding.
- Integration: backgrounding the application stops capture, verified on the supported device matrix.
- Content: an automated scan of the scan feature's user-facing strings fails on any string asserting certified, approved or permit-compliant measurement.

9. ACCEPTANCE CRITERIA
- No measurement can render without uncertainty, enforced by the type system.
- No unsupported mode is offered on any profile in the device matrix.
- Consent precedes retention, enforced server-side.
- No user-facing string claims certified or permit-compliant measurement, proven by the content scan.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The device-profile matrix test output.
- The content scan output over scan feature strings.
- An interrupted-upload transcript showing exactly one evidence record.
- A recorded walkthrough or screenshot set showing the uncertainty qualifier and the safety statement at the point of measurement.
- The named list of physical devices and browsers actually tested, and an explicit statement of which were not tested.

11. ROLLBACK INSTRUCTIONS
Deployment revert. Captures already uploaded are customer evidence and are never removed by a rollback. Local drafts created under the newer client may be unreadable by the previous client; on rollback, the previous client must surface an explicit message rather than discarding a draft silently.

12. DEFINITION OF DONE
- Uncertainty is structurally required, not conventionally included.
- The tested device list is stated, including what was not tested.
- The safety boundary appears at the point of measurement in the product.
- Status recorded as TESTED for the tested device set only. Devices not in that set are explicitly not claimed.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


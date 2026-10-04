<!-- promptmeta
id: P15
file: P15_SKETCH_SCAN_LIDAR_COMPANION.md
stage: 5 — Sketch Scan
title_en: Optional native LiDAR companion and authenticated project handoff
prereq: P14
requirements: UR-038,UR-040,UR-041
status: DESIGNED
-->

# P15_SKETCH_SCAN_LIDAR_COMPANION — Optional native LiDAR companion and authenticated project handoff

**التطبيق المرافق الاختياري لماسح LiDAR والتسليم المصادق عليه للمشروع**

| | |
| --- | --- |
| مرحلة خارطة الطريق | 5 — Sketch Scan |
| المتطلب السابق | P14 |
| المتطلبات المغطّاة | UR-038، UR-040، UR-041 |
| الحالة | DESIGNED |

## الشرح بالعربية

**ماذا ينفذ هذا الأمر؟**  
ينفذ التطبيق المرافق الاختياري لالتقاط LiDAR على أجهزة iOS المدعومة، وتسليم النتيجة إلى المشروع عبر مسار مصادق عليه.

**لماذا نحتاجه؟**  
المرجع يحدد إعادة بناء الغرف الاحترافية عبر واجهات أصلية على أجهزة مدعومة فقط، لا كوعد بـ LiDAR عام في المتصفح. المرافق اختياري ولا يجوز أن يصبح شرطًا للمسار الأساسي.

**ما المتطلبات السابقة؟**  
اكتمال P14 ببوابة خروجه كاملة.

**ما النتيجة المتوقعة؟**  
مسار التقاط أصلي اختياري، وفحص قدرة قبل العرض، وعودة مصادق عليها إلى المشروع، وهندسة بوحدات وثقة معلنة.

**كيف نتحقق من نجاحه؟**  
يفشل الأمر إذا انكسر المسار الأساسي بغياب المرافق، أو إذا قُبلت هندسة بلا وحدات أو بلا ثقة قياس.

## EXECUTABLE PROMPT

```text
You are executing P15_SKETCH_SCAN_LIDAR_COMPANION of the Sketch Design production implementation.
You are bound by execution/OPERATING_RULES.md. Read it before you begin.

1. OBJECTIVE
Deliver the optional native LiDAR companion as a genuinely optional path: capability-gated, authenticated on return, and never a precondition for the mobile web flow.

2. DEPENDENCIES
P14 — the companion hands off into the same evidence contract the web capture populates.

3. EXACT SCOPE
IN SCOPE:
- Capability check on supported iOS devices before the companion is offered at all.
- Native room capture using the platform's room reconstruction APIs.
- An authenticated handoff: the companion returns to the originating project with a scoped, expiring, single-use token.
- Geometry export into the Evidence Package contract with explicit coordinate units and measurement confidence.
- A clear statement, in the product, of which devices support this path and which do not.

OUT OF SCOPE — do not do these, and do not quietly widen into them:
- Do not make the companion required for any workflow. Every workflow must complete with web capture alone or with uploaded drawings.
- Do not publish to an app store in this prompt. Distribution requires a separate authorized release decision.
- Do not claim certified dimensions from LiDAR output; the safety boundary applies identically.

4. FILES AND MODULES AFFECTED
- apps/companion-ios/
- apps/companion-ios/capture/
- apps/companion-ios/handoff/
- services/evidence/handoff/ — token issuance and verification

5. REQUIRED CONTRACTS
- Handoff token: single-use, expiring, scoped to one project and one capture session, bound to the issuing principal. Reuse is rejected and audited.
- Exported geometry enters the system through the same EvidencePackage contract as web capture; there is no privileged ingestion path.
- measurement_confidence is populated from the capture API's own confidence output where available, and CONFIDENCE_NOT_ESTABLISHED where it is not. It is never estimated by the application.
- The companion declares device_capability on every capture so downstream consumers know the provenance.
- A workflow that has no companion capture proceeds normally; no step may require one.

6. IMPLEMENTATION INSTRUCTIONS
- Gate the companion behind a real capability check, not a device name list that will age badly.
- Treat the companion as a client with no more privilege than the web client. It authenticates the same way and is scoped the same way.
- Carry the native confidence output through rather than converting it to a friendlier number.
- Make the fallback path the primary path in testing: run the full workflow suite without the companion to prove it is optional.
- State device support honestly in the product, including the devices that are not supported.

7. SECURITY REQUIREMENTS
- Handoff tokens are single-use and expiring; a replayed token is rejected and audited as a security event.
- The companion stores no long-lived credential; it holds a scoped session that expires.
- Captured media is encrypted in transit and at rest on the device until uploaded, then removed from the device per the retention policy.
- The companion requests only the permissions it uses and states why at the point of request.
- Deep links into the companion are validated; an unvalidated deep link is an injection path.

8. AUTOMATED TESTS
- Unit: handoff token reuse is rejected and audited.
- Unit: an expired token is rejected at the boundary second.
- Integration: geometry without coordinate units is rejected by the evidence contract, identically to the web path.
- Integration: the full workflow suite passes with the companion absent, proving optionality.
- Integration: a deep link with a tampered project identifier is rejected.
- Device: capture on the named supported device set, with results recorded per device.

9. ACCEPTANCE CRITERIA
- Every workflow completes with the companion absent.
- Token reuse and expiry are rejected and audited.
- Companion geometry passes through the same contract and validation as web capture.
- Supported and unsupported devices are stated in the product.

10. REQUIRED EVIDENCE
Attach each item. An item you cannot attach is reported as not produced, never described as if it were.
- The full workflow suite output with the companion absent.
- The token reuse and expiry test outputs with the audit rows.
- Per-device capture results for every device in the named supported set.
- An explicit statement that the companion is NOT distributed and that distribution requires a separate authorized release decision.

11. ROLLBACK INSTRUCTIONS
The companion is a separate artifact: rolling it back means withdrawing the build from the distribution channel, which requires authorization. Because handoff is server-verified, a server-side rollback must keep verifying tokens issued by the companion version still in users' hands; never remove verification for a version that may still be installed.

12. DEFINITION OF DONE
- Optionality is proven by a full suite run without the companion.
- No privileged ingestion path exists for companion data.
- Distribution status is stated plainly and no release is claimed.
- Status recorded as TESTED for the named device set only.

STOP CONDITION
Stop and report rather than proceeding if: a dependency's exit gate is not met; a required
decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would
delete production data, deploy publicly, modify DNS, incur paid API usage, or make an
irreversible infrastructure change without explicit authorization.
Report the blocker, record the status as BLOCKED, and do not substitute an approximation.
```


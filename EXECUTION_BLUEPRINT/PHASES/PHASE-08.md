# PHASE-08 — التسعير والدفع والفوترة

<!-- phasemeta
id: PHASE-08
depends_on: [PHASE-03, PHASE-07]
criticality: P0
-->

## الغرض من المرحلة

`ADR-007` قرار معتمد: «لا يبدأ العمل من redirect؛ webhook موثق واستعلام خادمي
وidempotency»، وضابط قبوله «اختبار replay/order». هذه هي أكثر نقطة في المنصة
عرضة للخطأ المالي، ولذلك يفصل المصدر بين الحالات السبع للدفع ويشترط المطابقة.

## تحذير اقتصادي حاكم

الورقة 19 الصف 54 تحذير صريح: «كل معدلات التكلفة صفر باستثناء VAT. أدخل القيم
الفعلية من العقود قبل أي عرض تجاري». والورقة 01 الصف 11 تؤكد: «الأسعار والمعادلات
نموذج تخطيط قابل للتعديل وليست عرضاً تجارياً».

لذلك هذه المرحلة تبني **المحرك** ولا تُنتج **سعراً**. أي نظام يُصدر عرض سعر من
معدلات صفرية يُنتج رقماً بلا معنى، وقد يُنتج التزاماً تعاقدياً خاطئاً. محرك
التسعير يجب أن يرفض إصدار عرض عندما تكون المعدلات غائبة.

## شروط الدخول

- اكتمال `PHASE-03` و`PHASE-07`.
- إما بطاقة معدلات مُوقَّعة من المالك، أو تعليم البيئة صراحة كـ«غير تجارية».

## شروط الخروج

- نجاح `AT-PRICE-001` (نفس اللقطات = نفس العرض).
- نجاح `AT-PAY-001` (redirect بلا webhook لا يُفعّل شيئاً).
- نجاح `AT-PAY-002` (أحداث مكررة وخارج الترتيب تبقى idempotent).
- لا تخزين لأي `PAN` أو `CVV` في أي موضع.

## المتطلبات المغطاة في هذه المرحلة

`ADR-007`, `REQ-COM-01`..`REQ-COM-09`, `REQ-SEC-12`, `REQ-SEC-15`,
`REQ-DEL-02`, `REQ-OPN-03`

---

## الأوامر التنفيذية

### P08-01 — محرك التسعير ولقطات المعدلات

<!-- meta
id: P08-01
phase: PHASE-08
title_en: Pricing engine with rate snapshots and reproducibility
prereq: [P07-06]
requirements: [REQ-COM-01, REQ-COM-02, REQ-COM-03, REQ-COM-04, REQ-OPN-03]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ مكونات التسعير الاثني عشر في الورقة 18 وسلسلة
الحساب في الورقة 19، مع لقطات معدلات تجعل العرض قابلاً للإعادة بالضبط.

**لماذا نحتاجه؟** الورقة 15 الصف 14 (`CTRL-013`) دليله: «نفس اللقطات نفس العرض».
والورقة 18 تفصل بوضوح بين تكلفة الذكاء وتكلفة الأدوات وأجر المراجع وتكلفة PMO —
والورقة 18 الصف 9 صريحة: «لا يخف داخل AI» أي لا يُدمج أجر PMO في تكلفة الذكاء.

**ما المتطلبات السابقة؟** `P07-06`.

**ما النتيجة المتوقعة؟** محرك تسعير مُنفَّذ بمعادلاته، ولقطات معدلات، ورفض صريح
عند غياب معدل.

**كيف نتحقق من نجاحه؟** `AT-PRICE-001` ناجح؛ ومحرك يرفض إنتاج سعر عندما يكون
معدل مطلوب غائباً أو صفراً غير مقصود.

```text
TASK P08-01 — Pricing engine with rate snapshots and reproducibility

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-01
   Phase: PHASE-08 (Pricing, payment and billing)
   Prerequisites: P07-06
   Requirements covered: REQ-COM-01, REQ-COM-02, REQ-COM-03, REQ-COM-04,
                         REQ-OPN-03

B. OBJECTIVE
   Implement the twelve-component pricing engine and the quote computation
   chain with immutable rate snapshots, so a quote is exactly reproducible —
   and so the engine refuses to produce a commercial price when a required rate
   is absent.

   Why this is necessary: sheet 15 row 14 (CTRL-013) requires the evidence
   "same snapshots same quote". Sheet 18 separates AI inference, document AI,
   engineering tools, reviewer fee and PMO cost as distinct components, and
   row 9 states explicitly that PMO cost must not be hidden inside the AI cost.
   Sheet 19 row 54 warns that every rate is zero except VAT and that actual
   contract values must be entered before any commercial quotation.

   SCOPE BOUNDARY: the pricing engine, rate snapshots and the computation
   chain. The quote lifecycle is P08-02. Payment is P08-03. Do not set any
   commercial rate yourself.

C. CONTEXT
   Required inputs, sheet 18 rows 2-13, the twelve components as component /
   formula / source / control:
     Scope base / base fee / rate card version / not a market price
     Size / quantity times unit rate / scope / per-workflow driver
     Complexity / multiplier or line items / rules / explained to the client
     AI inference / million tokens times rate / provider contract / usually
       internal
     Document AI / usage times rate / tool contract / linked to the run
     Engineering tools / usage times rate / vendor contract / includes a
       minimum charge
     Reviewer / hourly, fixed or share / reviewer contract / second review is
       independent
     PMO / hours times rate or fixed / internal rate / never hidden inside AI
     Risk reserve / eligible cost times percentage / workflow policy /
       reconciled after pilot
     Payment fees / percentage plus fixed / PSP agreement / do not assume fees
     Target margin / gross-up denominator / commercial policy / approval below
       the floor
     VAT / price times VAT / ZATCA or advisor / 15 percent for the standard
       taxable case
   And the computation chain, sheet 19 rows 39-52, which must be reproduced
   exactly:
     size cost = area * area_rate + pages * page_rate + disciplines *
       discipline_fee
     ai cost = input_mtokens * input_rate + output_mtokens * output_rate
     tool cost = bim_hours * bim_rate + fixed_tool_cost
     direct reviewer fee = (HOURLY: r1_hours * r1_rate | FIXED:
       reviewer_fixed_fee | SHARE: 0) + r2_hours * r2_rate
     pmo cost = pmo_hours * pmo_rate
     direct cost = base_fee + size + ai + tool + reviewer + pmo
     reserve = direct_cost * risk_reserve_pct
     revenue share = (SHARE: reviewer_share_pct | else 0)
     price before VAT = IF(1 - psp_pct - target_margin - revenue_share <= 0,
       "CHECK INPUTS", (direct_cost + reserve + psp_fixed) /
       (1 - psp_pct - target_margin - revenue_share))
     final reviewer payout = (SHARE: price_before_vat * reviewer_share_pct |
       else direct_reviewer_fee)
     vat amount = price_before_vat * vat_rate
     total = price_before_vat + vat_amount
     expected profit = price_before_vat - (direct_cost + reserve +
       final_reviewer_payout + price_before_vat * psp_pct + psp_fixed)
     margin pct = IF(price_before_vat = 0, 0, expected_profit /
       price_before_vat)
   Source values: VAT is 0.15 for the standard taxable case (sheet 19 row 35,
   sheet 31 row 5); every other rate in the source is 0.

D. EXECUTION INSTRUCTIONS
   1. Implement each of the twelve components as a named, separately reported
      line item. The breakdown is a deliverable, not an internal detail —
      sheet 05 row 34 names the output as "quote, breakdown, sensitivity", and
      sheet 18 row 4 requires complexity to be explainable to the client.
   2. Implement the computation chain exactly as specified above, including the
      CHECK INPUTS guard: when 1 minus the PSP percentage minus the target
      margin minus the revenue share is less than or equal to zero, the engine
      returns a structured INVALID_PRICING_INPUTS error naming the offending
      inputs. It must never divide by a non-positive denominator and never
      return a negative or infinite price.
   3. Implement reviewer compensation as three mutually exclusive methods
      (HOURLY, FIXED, SHARE) with the source's exact asymmetry: under SHARE the
      direct fee contributes zero to direct cost, the share enters the gross-up
      denominator, and the final payout is computed from the pre-VAT price.
      Reproduce that behaviour and test all three methods.
   4. Keep the second reviewer's fee an independent line per sheet 18 row 8,
      and keep PMO cost its own line per row 9. Add a test asserting the
      breakdown contains distinct, non-zero-able PMO and AI lines so one cannot
      absorb the other.
   5. Implement rate snapshots: a quote captures, immutably, every rate it used
      with that rate's source, version, effective date and currency. Rates live
      in versioned rate cards — provider contract rates (from the model
      registry in P04-02), tool vendor rates, reviewer contract rates (from the
      restricted rate cards in P07-02), internal PMO rates, PSP fees and the
      VAT rate.
   6. Implement the absent-rate refusal, which is the most important behaviour
      in this prompt. Classify every rate as REQUIRED or OPTIONAL for a given
      workflow. If a REQUIRED rate has no value from a contract source, the
      engine returns RATE_CARD_INCOMPLETE listing every missing rate and
      refuses to produce a commercial quote. It may produce a clearly labelled
      PLANNING_ESTIMATE with zeros, which carries a machine-readable
      non_commercial flag and cannot be attached to a quote a client can
      accept. Sheet 19 row 54 and sheet 01 row 11 both demand this separation.
   7. Implement AI and tool cost from measured usage where available: the usage
      ledger from P04-06 provides actuals per run, so a quote can use an
      estimate before the run and the ledger can be compared to it afterwards.
      Record which inputs were estimated and which were measured.
   8. Implement VAT applicability rather than a hardcoded 15 percent: the rate
      and its applicability depend on the taxpayer and the supply (sheet 18
      row 13). Default to the source's standard taxable case value of 0.15,
      record the applicability determination and its basis, and allow a
      zero-rated or exempt determination with a recorded reason.
   9. Implement sensitivity output per sheet 05 row 34: show how the price moves
      with the main drivers, so the breakdown is reviewable.
  10. Implement reproducibility: pricing is a pure function of (inputs, rate
      snapshot, engine version). Record all three on every computation. The same
      triple must produce a byte-identical result.
  11. Tests — AT-PRICE-001 plus the engine suite:
        a. AT-PRICE-001: compute a quote, then recompute with the same inputs
           and the same rate snapshot -> byte-identical result, including every
           breakdown line;
        b. a REQUIRED rate missing -> RATE_CARD_INCOMPLETE listing it, no
           commercial quote produced;
        c. a PLANNING_ESTIMATE carries the non_commercial flag and cannot be
           attached to an acceptable quote;
        d. the CHECK INPUTS condition -> INVALID_PRICING_INPUTS, no division;
        e. all three reviewer methods produce the source's expected asymmetry;
           under SHARE the payout derives from the pre-VAT price;
        f. the breakdown contains distinct AI and PMO lines;
        g. a rate card version change -> a new quote differs, and the old
           quote's snapshot still reproduces the old price;
        h. measured usage from the ledger versus the estimate -> both recorded
           and comparable;
        i. a zero-rated VAT determination -> recorded with its reason, and the
           total reflects it;
        j. engine version change -> flagged on the computation record so an old
           quote is not silently recomputed under new logic.
  12. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the twelve components as separately reported line items
   - the exact computation chain with the CHECK INPUTS guard
   - the three reviewer compensation methods with correct asymmetry
   - immutable rate snapshots with source, version, effective date and currency
   - RATE_CARD_INCOMPLETE refusal and the PLANNING_ESTIMATE separation
   - estimate-versus-measured usage recording
   - VAT applicability determination with a recorded basis
   - sensitivity output
   - reproducibility over (inputs, snapshot, engine version)
   - tests/pricing/at-price-001.* plus cases b through j
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste AT-PRICE-001 output showing two identical computations line by line.
   - Paste the RATE_CARD_INCOMPLETE output listing the missing rates. Given the
     source, this is the expected default state — report how many REQUIRED
     rates are currently absent.
   - Paste the three reviewer-method computations with their inputs.
   - Acceptance criterion: identical inputs and snapshot always give an
     identical quote, and no commercial quote is producible while a required
     rate is missing.

G. COMPLETION CONTRACT
   Definition of Done: the engine reproduces the source's formulas exactly, is
   reproducible, and refuses commercial output on an incomplete rate card.
   Evidence to report: AT-PRICE-001 output, the missing-rate count, the ten
   test results.
   Remaining blockers: the entire rate card is an owner blocker (open decision
   OD-03). The honest completion state is that the engine works and no
   commercial quote can be issued. Do not fill in rates to make the engine
   appear complete.
   Next prompt: P08-02.
```

**المخرجات المتوقعة:** محرك بمكونات اثني عشر، لقطات معدلات، رفض عند نقص المعدلات.
**التحقق المطلوب:** `AT-PRICE-001` ناجح؛ لا عرض تجاري مع معدل مطلوب غائب.
**الاعتمادية التالية:** `P08-02`.

---

### P08-02 — دورة حياة عرض السعر والقفل عند القبول

<!-- meta
id: P08-02
phase: PHASE-08
title_en: Quote lifecycle and lock on acceptance
prereq: [P08-01]
requirements: [REQ-COM-05, REQ-WF-01, REQ-API-01, REQ-API-05]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ دورة حياة عرض السعر: إنشاء من لقطات، صلاحية،
قبول يقفل العرض، وانتقال `QUOTED` → `AWAITING_PAYMENT`.

**لماذا نحتاجه؟** الورقة 09 الصف 3 تحدد ضابط حالة `QUOTED`: «Freeze quote» عند
القبول. والورقة 28 الصف 16 تحدد كيان `Quote` بـ«inputs/rate snapshots/expiry»
وضابطه «locked on accept». وبدون قفل، يمكن أن يتغير السعر بعد قبول العميل.

**ما المتطلبات السابقة؟** `P08-01`.

**ما النتيجة المتوقعة؟** عروض بصلاحية وقفل، ونقاط نهاية مطابقة للورقة 26.

**كيف نتحقق من نجاحه؟** قبول عرض يقفله ولا يتأثر بتغيير بطاقة المعدلات بعده؛
وعرض منتهي الصلاحية يُرفض قبوله بـ410.

```text
TASK P08-02 — Quote lifecycle and lock on acceptance

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-02
   Phase: PHASE-08
   Prerequisites: P08-01
   Requirements covered: REQ-COM-05, REQ-WF-01, REQ-API-01, REQ-API-05

B. OBJECTIVE
   Implement the quote lifecycle — creation from immutable snapshots, a defined
   validity window, acceptance that freezes the quote, and the workflow
   transition into AWAITING_PAYMENT.

   Why this is necessary: sheet 09 row 3 names the control on the QUOTED state
   as "freeze quote" on acceptance. Sheet 28 row 16 defines Quote with inputs,
   rate snapshots and expiry, and its control as "locked on accept". Without
   the freeze, a rate card change after a client accepts would silently alter
   what they agreed to.

   SCOPE BOUNDARY: the quote entity, its lifecycle and its endpoints. Payment
   session creation is P08-03.

C. CONTEXT
   Required inputs:
     - sheet 26 row 5: POST /v1/quotes, scope quotes:write, control "pricing
       snapshot", emits quote.created, responses 201/422
     - sheet 26 row 6: POST /v1/quotes/{id}/accept, scope quotes:accept,
       control version or etag, emits quote.accepted, responses 200/409/410
     - sheet 09 rows 2-4: DRAFT plus submit_for_quote -> QUOTED (control
       validate schema); QUOTED plus accept_quote -> AWAITING_PAYMENT (control
       freeze quote); AWAITING_PAYMENT plus payment.verified ->
       PAYMENT_VERIFIED (control webhook plus fetch)
     - sheet 09 row 14: a time-bound entity expiring on timer.expired with a
       reopen policy — this covers quote expiry
     - the pricing engine and snapshots from P08-01

D. EXECUTION INSTRUCTIONS
   1. Implement the Quote entity with: the workflow and pinned template
      version, the priced inputs, the immutable rate snapshot reference, the
      computed breakdown, the validity window, the state, and the acceptance
      record.
   2. Implement quote states: DRAFT, ISSUED, ACCEPTED, EXPIRED, WITHDRAWN,
      SUPERSEDED. Only an ISSUED quote inside its validity window is
      acceptable.
   3. Enforce that a quote cannot be ISSUED from a PLANNING_ESTIMATE or while
      RATE_CARD_INCOMPLETE holds. This is the gate that prevents the source's
      zero rates from reaching a client as an offer.
   4. Implement the freeze on acceptance: acceptance copies the full computed
      result and the snapshot reference into an immutable accepted-quote record
      and makes the quote non-recomputable. Enforce immutability in storage.
      Add a test that changes the rate card after acceptance and asserts the
      accepted amount is unchanged.
   5. Implement expiry using the P03-05 timers, producing EXPIRED and returning
      410 on an acceptance attempt per the source's response codes, with the
      reopen policy recorded.
   6. Implement optimistic concurrency with a version or etag per sheet 26
      row 6, returning 409 on a stale acceptance attempt, so a client cannot
      accept a quote they have not actually seen.
   7. Implement supersession: issuing a revised quote marks the prior one
      SUPERSEDED with a link, so the client's history is intact and no quote is
      silently replaced.
   8. Wire the workflow transition: acceptance moves the run from QUOTED to
      AWAITING_PAYMENT, and emits quote.accepted through the outbox.
   9. Record the acceptance act with the accepting identity, timestamp, the
      exact amount and currency, and the terms version, so the commercial gate
      in P07-06 has a verifiable authorization trail.
  10. Tests:
        a. issuing a quote while a required rate is missing -> refused;
        b. accepting an ISSUED quote -> frozen; a subsequent rate card change
           does not alter the accepted amount;
        c. an attempt to modify an accepted quote -> refused at the storage
           level;
        d. accepting an expired quote -> 410;
        e. accepting with a stale etag -> 409;
        f. issuing a revision -> the prior quote is SUPERSEDED with a link, not
           deleted;
        g. acceptance drives the run to AWAITING_PAYMENT and emits
           quote.accepted exactly once;
        h. a quote built from a PLANNING_ESTIMATE cannot be issued or accepted.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the Quote entity with snapshot reference and validity window
   - the six-state lifecycle with issuance gating
   - storage-enforced freeze on acceptance
   - timer-driven expiry with 410 semantics
   - etag concurrency with 409 semantics
   - supersession with linkage
   - the workflow transition and quote.accepted emission
   - the acceptance authorization record
   - tests/pricing/quote-*.* covering cases a through h
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eight tests.
   - For case b, paste the accepted amount before and after the rate card
     change, showing no drift.
   - Paste the storage-level refusal from case c.
   - Acceptance criterion: an accepted quote is immutable and
   unaffected by any later rate change, and no incomplete-rate quote can be
   issued.

G. COMPLETION CONTRACT
   Definition of Done: the lifecycle implemented, freeze proven immutable,
   expiry and concurrency semantics correct, supersession preserving history.
   Evidence to report: the eight test outputs, the no-drift proof.
   Remaining blockers: no quote can actually be issued while OD-03 is
   unresolved. Confirm the gate holds rather than bypassing it for testing —
   use a test-only rate card fixture clearly marked as such and say so.
   Next prompt: P08-03.
```

**المخرجات المتوقعة:** كيان عرض بست حالات، قفل مفروض عند القبول، صلاحية ومهلة.
**التحقق المطلوب:** العرض المقبول لا يتأثر بتغيير المعدلات؛ لا إصدار عرض بمعدلات ناقصة.
**الاعتمادية التالية:** `P08-03`.

---

### P08-03 — الدفع بالأحداث: تفعيل بـwebhook فقط

<!-- meta
id: P08-03
phase: PHASE-08
title_en: Event-driven payment with webhook-only activation
prereq: [P08-02]
requirements: [ADR-007, REQ-COM-06, REQ-COM-07, REQ-COM-08, REQ-SEC-12, REQ-SEC-15]
-->

**ماذا سينفذ هذا الأمر؟** ينفّذ `ADR-007`: جلسة دفع مُستضافة، تفعيل من webhook
موثق فقط مع استعلام خادمي، وidempotency، وسبع حالات دفع.

**لماذا نحتاجه؟** `AT-PAY-001` (الورقة 16 الصف 8) يحدد السيناريو: «success
redirect بلا webhook ثم webhook صحيح» والمتوقع «لا تفعيل ثم تفعيل مرة واحدة».
و`AT-PAY-002` يختبر «duplicate وout-of-order events» والمتوقع «Idempotent ولا
رجوع خاطئ». والورقة 21 الصف 8 تمنع تخزين `PAN/CVV` مطلقاً.

**ما المتطلبات السابقة؟** `P08-02`.

**ما النتيجة المتوقعة؟** مسار دفع لا يُفعّل من redirect، ومعالجة أحداث idempotent،
وحدود PCI واضحة.

**كيف نتحقق من نجاحه؟** `AT-PAY-001` و`AT-PAY-002` ناجحان؛ ولا بيانات بطاقة في
أي مخزن أو سجل.

```text
TASK P08-03 — Event-driven payment with webhook-only activation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-03
   Phase: PHASE-08
   Prerequisites: P08-02
   Requirements covered: ADR-007, REQ-COM-06, REQ-COM-07, REQ-COM-08,
                         REQ-SEC-12, REQ-SEC-15

B. OBJECTIVE
   Implement payment as an event-driven flow: a hosted or tokenized checkout
   session, activation only from a signature-verified webhook corroborated by a
   server-side fetch, full idempotency, and the seven-state payment lifecycle —
   with no card data ever entering the platform.

   Why this is necessary: ADR-007 (sheet 02 row 8) is an APPROVED decision
   whose reason is preventing fake or duplicate activation and whose acceptance
   control is a replay and ordering test. AT-PAY-001 (sheet 16 row 8) requires
   that a success redirect without a webhook activates nothing. AT-PAY-002
   requires idempotency under duplicate and out-of-order events. Sheet 21 row 8
   forbids storing PAN or CVV and requires an explicit PCI scope.

   SCOPE BOUNDARY: checkout sessions, webhook ingestion, verification,
   idempotent state transitions and milestone activation. Invoicing and
   reconciliation are P08-04. Do not integrate a provider for which no sandbox
   credential already exists — build to the normalized interface and use a
   contract-conformant fake, clearly labelled.

C. CONTEXT
   Required inputs:
     - sheet 26 row 7: POST /v1/payments/sessions, scope payments:write,
       Idempotency-Key, emits payment.initiated, responses 201/422
     - sheet 26 row 8: POST /v1/webhooks/payments/{provider}, authorized by
       provider signature, keyed by event id, emits payment.*, responses
       200/400/401
     - sheet 21 row 7 (PAY-EVT): the seven states INITIATED, AUTHORIZED, PAID,
       FAILED, EXPIRED, REFUNDED, CHARGEBACK; integration "signed webhook plus
       fetch plus idempotency"; control "a redirect does not open the service";
       note "audit transitions"
     - sheet 21 row 8 (PAY-SEC): no PAN or CVV storage; vault, TLS, WAF,
       signature; define the PCI scope; least scope
     - sheet 21 rows 2-5: Moyasar (hosted or tokenized, verify provider and
       contract), Geidea (hosted checkout preferred, no PAN or CVV, 3DS,
       server-to-server), Tamara BNPL (eligibility is not a guarantee, test the
       states), bank transfer (virtual IBAN, reference, reconcile; a transfer
       image never opens a milestone)
     - sheet 09 rows 4-5 and row 22: AWAITING_PAYMENT plus payment.verified ->
       PAYMENT_VERIFIED with the control "webhook plus fetch"; PAYMENT_VERIFIED
       plus enqueue -> QUEUED with the control idempotency; Payment INITIATED
       plus a provider event -> AUTHORIZED, PAID, FAILED or EXPIRED with the
       control verify

D. EXECUTION INSTRUCTIONS
   1. Define a normalized payment provider interface covering: create hosted
      session, fetch authoritative payment status, verify webhook signature,
      refund, and map provider states to the seven canonical states.
   2. Implement session creation with a required Idempotency-Key, bound to the
      accepted quote, its exact amount and currency, and the milestone it
      funds. Return only the hosted redirect or tokenized handle — never
      anything that could carry card data into the platform.
   3. Implement the PCI boundary explicitly and provably: the platform receives
      no PAN, no CVV, no expiry and no track data on any path. Add a test that
      submits card-shaped data to every payment endpoint and asserts rejection,
      plus a storage and log scan asserting no card-shaped string is persisted
      anywhere. Document the resulting PCI scope statement as a deliverable.
   4. Implement the redirect handler as informational only. It may show the
      user a status page; it may not change any state, activate any milestone,
      or mark any payment verified. Make that structurally true: the redirect
      handler has no write access to payment state. This is the core of
      AT-PAY-001.
   5. Implement webhook ingestion with layered verification, in this order:
        a. verify the provider signature over the raw request body, using a
           constant-time comparison, before parsing;
        b. reject an unsigned or badly signed event with 401 and no state
           change;
        c. enforce a replay window and reject stale timestamps;
        d. dedupe by provider event id using the idempotency store from
           P03-03;
        e. perform an independent server-side fetch of the authoritative
           payment status from the provider, and trust the fetch over the
           webhook payload;
        f. verify that the fetched amount, currency and reference match the
           quote exactly — a mismatch suspends rather than activates, per
           sheet 05 row 35's stop conditions (signature, amount, duplicate,
           fraud).
   6. Implement ordering tolerance: events may arrive out of order. Implement a
      state machine with a monotonic provider-side sequence or timestamp so an
      older event cannot regress a newer state (for example a late AUTHORIZED
      must not overwrite PAID, and a late PAID must not overwrite REFUNDED).
      This is the "no wrong regression" clause of AT-PAY-002.
   7. Implement milestone activation exactly once: the transition to
      PAYMENT_VERIFIED and the resulting enqueue are idempotent, so repeated
      webhooks for the same payment activate one milestone. Track the duplicate
      activation KPI from sheet 30 row 11, whose target is zero.
   8. Implement refund and chargeback as first-class states with their
      consequences recorded, requiring the FINANCE role with dual approval per
      sheet 04 row 8, and never silently reversing a delivered milestone — the
      compensation path is recorded for human handling.
   9. Implement bank transfer handling per sheet 21 row 5: a virtual IBAN and
      reference with automated reconciliation. An uploaded transfer image is
      explicitly not evidence and cannot activate a milestone — add a test.
  10. Implement BNPL eligibility handling per sheet 21 row 4: eligibility is not
      a payment guarantee, so activation still requires the PAID state through
      the same verification path.
  11. Audit every payment state transition per sheet 21 row 7, into the
      append-only store.
  12. Tests — AT-PAY-001 and AT-PAY-002 plus the payment suite:
        a. AT-PAY-001: hit the success redirect with no webhook -> nothing
           activated, run still AWAITING_PAYMENT; then deliver a valid webhook
           -> activated exactly once. Paste both halves;
        b. AT-PAY-002: deliver the same webhook event three times -> one
           activation; deliver AUTHORIZED after PAID -> no regression; deliver
           PAID after REFUNDED -> no regression;
        c. an unsigned webhook -> 401, no state change;
        d. a tampered body with a valid-looking signature -> rejected;
        e. a stale timestamp outside the replay window -> rejected;
        f. a fetched amount that differs from the quote -> suspended, not
           activated, with the reason recorded;
        g. card-shaped data submitted to every payment endpoint -> rejected;
           the storage and log scan finds no card-shaped string;
        h. the redirect handler has no write path to payment state — assert
           architecturally;
        i. a transfer image upload -> does not activate a milestone;
        j. BNPL eligibility granted but not PAID -> no activation;
        k. a refund attempt with a single approver -> refused; with dual
           approval -> recorded, with the compensation path logged;
        l. every state transition appears in the audit store.
  13. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the normalized payment provider interface with at least one
     contract-conformant implementation
   - idempotent session creation bound to quote, amount, currency and milestone
   - the proven PCI boundary and a written PCI scope statement
   - a write-incapable redirect handler
   - six-layer webhook verification including an independent server-side fetch
   - order-tolerant state machine with regression prevention
   - exactly-once milestone activation with the duplicate-activation metric
   - refund and chargeback with dual approval and recorded compensation
   - bank transfer reconciliation with image evidence explicitly rejected
   - BNPL eligibility handling
   - full transition auditing
   - tests/payment/at-pay-001.*, at-pay-002.* plus cases c through l
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste both halves of AT-PAY-001 and all three parts of AT-PAY-002.
   - Paste the card-shaped data rejections and the storage and log scan output
     from case g.
   - Paste the architectural assertion from case h.
   - State which provider was exercised with a real sandbox credential and
     which with a fake.
   - Acceptance criterion: no redirect ever activates anything, duplicate and
     out-of-order events never cause a wrong state, and no card data exists
     anywhere in the platform.

G. COMPLETION CONTRACT
   Definition of Done: AT-PAY-001 and AT-PAY-002 green, PCI boundary proven,
   activation exactly once, no state regression.
   Evidence to report: both acceptance tests, the card-data scans, the
   architectural proof, the real-versus-fake provider statement.
   Remaining blockers: provider contracts and merchant accounts are owner
   blockers (sheet 23 and P00-03). Sheet 31 row 16 requires verifying the PSP
   against the SAMA licensed list — report whether that check was done and by
   whom.
   Next prompt: P08-04.
```

**المخرجات المتوقعة:** واجهة مزود مُطبَّعة، تحقق webhook بست طبقات، تفعيل مرة واحدة، حدود PCI مُثبتة.
**التحقق المطلوب:** `AT-PAY-001` و`AT-PAY-002` ناجحان؛ لا بيانات بطاقة في أي مخزن أو سجل.
**الاعتمادية التالية:** `P08-04`.

---

### P08-04 — الفوترة والمطابقة وZATCA

<!-- meta
id: P08-04
phase: PHASE-08
title_en: Invoicing, ZATCA e-invoicing and reconciliation
prereq: [P08-03]
requirements: [REQ-COM-09, REQ-COM-11, REQ-SEC-12, REQ-DEL-02, REQ-INT-01]
-->

**ماذا سينفذ هذا الأمر؟** يبني الفوترة والمطابقة المالية، وتهيئة ZATCA للفاتورة
الإلكترونية، ودفتر مدفوعات قابل للتسوية.

**لماذا نحتاجه؟** الورقة 38 الصف 10 (`G-05 Credits persistence`) حاجز إصدار
بمعيار «لا خصم سلبي أو مزدوج». والورقة 57 الصف 11 (`A10`) تحدد الأثر: «تسرّب
الهامش»، والتنفيذ المطلوب: «ledger idempotency ومطابقة يومية». والورقة 21 الصف 6
تنبّه أن ZATCA «ليست بوابة دفع».

**ما المتطلبات السابقة؟** `P08-03`.

**ما النتيجة المتوقعة؟** دفتر مالي مُطابَق، وفوترة متوافقة مع التهيئة المطلوبة،
وتقرير مطابقة يومي.

**كيف نتحقق من نجاحه؟** مطابقة يومية تكشف أي فرق بين الدفتر والمزود؛ ولا خصم
مزدوج أو سلبي ممكن.

```text
TASK P08-04 — Invoicing, ZATCA e-invoicing and reconciliation

Read EXECUTION_BLUEPRINT/_registry/AGENT-OPERATING-CONTRACT.md first and comply
with it for the whole task.

A. IDENTITY
   Prompt ID: P08-04
   Phase: PHASE-08
   Prerequisites: P08-03
   Requirements covered: REQ-COM-09, REQ-COM-11, REQ-SEC-12, REQ-DEL-02,
                         REQ-INT-01

B. OBJECTIVE
   Implement the financial ledger with daily reconciliation against provider
   records, invoice generation, and the ZATCA e-invoicing integration path —
   with no possibility of a negative or double debit.

   Why this is necessary: sheet 38 row 10 (G-05) is a release blocker whose
   pass criterion is "no negative or double debit" with required evidence of a
   ledger test. Sheet 57 row 11 (A10) names the impact as margin leakage and
   requires ledger idempotency plus daily reconciliation, evidenced by a
   reconciliation run. Sheet 21 row 6 cautions that ZATCA Fatoorah is an
   e-invoicing system, not a payment gateway.

   SCOPE BOUNDARY: the ledger, reconciliation, invoice generation and the ZATCA
   onboarding path. Do not submit a real invoice to ZATCA production. Use the
   official sandbox only if a credential already exists; otherwise build to the
   interface and report that it is unexercised.

C. CONTEXT
   Required inputs:
     - sheet 23 row 8 (KSA-07): ZATCA Fatoorah, XML and QR invoicing with an
       SDK; portal and official sandbox exist; the connection plan is EGS
       registration, certificates, secrets and tests; status ONBOARD
     - sheet 21 row 6 (INV-01): XML and QR, phase two where applicable;
       portal, SDK, validator and sandbox; not a payment gateway; tax advice
       required
     - sheet 31 row 5 (SRC-004): ZATCA standard VAT is 15 percent where
       applicable
     - sheet 05 row 35 (FIN-02): invoice and checkout, link the milestone after
       a verified webhook and reconciliation; no PAN or CVV and no manual
       adjustment
     - sheet 28 row 17: Payment entity with provider, event, state and amount;
       control idempotent
     - the usage ledger from P04-06 and the payment states from P08-03

D. EXECUTION INSTRUCTIONS
   1. Implement a double-entry or equivalent financial ledger where every
      posting is immutable and every correction is a new compensating entry.
      Deleting or editing a posting is impossible. This is what makes "no
      negative or double debit" provable rather than hoped for.
   2. Enforce posting idempotency on the provider event id and on the internal
      operation id, so a retried webhook or a retried job posts once. Reuse the
      P03-03 idempotency store.
   3. Implement balance invariants as database-level constraints or checked
      invariants: no balance may go negative where the account type forbids it,
      and the sum of entries per transaction must be zero in a double-entry
      model. Add a test attempting to create an unbalanced or
      negative-forbidden posting.
   4. Implement invoice generation from the accepted quote and the delivered
      milestones, with: the invoice number series, the issue date, the supplier
      and customer tax details, the line items from the pricing breakdown, the
      VAT determination and its basis from P08-01, and the total. The invoice
      is an artifact version with a digest, locked on issue (P02-02).
   5. Implement the ZATCA integration path to the point the source supports —
      EGS unit registration, certificate handling via the secrets vault, XML
      generation to the required schema, QR generation, and validation against
      the official validator or sandbox. Each step records whether it was
      actually exercised. Do not claim compliance; the source marks this
      ONBOARD and requires tax advice.
   6. Implement the no-manual-adjustment rule from sheet 05 row 35: there is no
      endpoint or admin action that edits a payment state or an invoice amount
      by hand. Corrections flow through credit notes and compensating entries,
      with FINANCE dual approval per sheet 04 row 8. Add a test asserting no
      manual-adjustment path exists, and recall that sheet 04 row 9 forbids
      SUPPORT_L2 from setting a payment status manually.
   7. Implement daily reconciliation with three legs:
        a. platform ledger versus provider settlement records;
        b. platform usage ledger (P04-06) versus provider usage or billing
           records, which is the margin-leakage control in A10;
        c. invoiced amounts versus accepted quote amounts versus received
           payments.
      Each run produces a dated report listing every discrepancy with its
      amount and suspected cause, and a discrepancy above a threshold raises an
      alert rather than being absorbed.
   8. Implement the unit-economics inputs for sheet 17 rows 10-11: cost per
      workflow and gross margin, computed from the ledger and the usage ledger,
      returning PENDING where a required rate is absent rather than a
      misleading number.
   9. Implement retention and records handling per the Payment and Delivery
      entity retention classes, with the legal-hold interaction from P02-02.
  10. Tests:
        a. a repeated webhook -> one posting;
        b. an unbalanced posting -> rejected;
        c. a posting that would drive a forbidden balance negative -> rejected;
        d. a double debit attempt -> rejected, satisfying G-05's criterion;
        e. no manual-adjustment endpoint exists -> assert architecturally;
        f. a correction flows as a compensating entry with dual approval;
        g. a reconciliation run with an injected provider discrepancy ->
           detected, reported with the amount, alerted;
        h. a reconciliation run with no discrepancy -> clean report, retained
           as the A10 evidence;
        i. an invoice is locked on issue and its digest verifies;
        j. the ZATCA XML validates against the schema (sandbox or validator) if
           a credential exists; otherwise the step reports NOT EXERCISED;
        k. cost per workflow and gross margin return PENDING when a required
           rate is absent.
  11. Append to docs/EXECUTION-LOG.md.

E. DELIVERABLES
   - the immutable financial ledger with compensating-entry corrections
   - event-id and operation-id posting idempotency
   - database-level balance invariants
   - invoice generation, locked with a digest
   - the ZATCA path with per-step exercised or not-exercised status
   - the architecturally enforced no-manual-adjustment rule
   - three-leg daily reconciliation with dated reports and alerting
   - unit-economics inputs with honest PENDING semantics
   - tests/finance/ledger-*.* covering cases a through k
   - docs/EXECUTION-LOG.md entry

F. VERIFICATION
   - Paste the output of all eleven tests.
   - Paste the double-debit rejection for case d — this is the G-05 evidence.
   - Paste both reconciliation reports from cases g and h; retain the clean run
     as the A10 evidence.
   - State explicitly which ZATCA steps were actually exercised and which were
     not.
   - Acceptance criterion: a double or negative debit is impossible, every
     discrepancy is detected and reported, and no manual adjustment path
     exists.

G. COMPLETION CONTRACT
   Definition of Done: ledger immutable and invariant-protected, reconciliation
   running and detecting injected discrepancies, invoices locked, ZATCA path
   built with honest exercise status.
   Evidence to report: the eleven test outputs, the G-05 and A10 evidence
   artifacts, the ZATCA exercise statement.
   Remaining blockers: ZATCA onboarding, tax advice and a merchant account are
   owner blockers. Report them. Do not describe the platform as ZATCA compliant.
   Next prompt: P09-01. PHASE-08 exit requires AT-PRICE-001, AT-PAY-001 and
   AT-PAY-002 green, the PCI scan clean, and a clean reconciliation run
   retained.
```

**المخرجات المتوقعة:** دفتر مالي ثابت، مطابقة ثلاثية يومية، فواتير مقفلة، مسار ZATCA.
**التحقق المطلوب:** لا خصم مزدوج أو سلبي؛ كل فرق مكتشَف ومُبلَّغ؛ لا مسار تعديل يدوي.
**الاعتمادية التالية:** `P09-01`.

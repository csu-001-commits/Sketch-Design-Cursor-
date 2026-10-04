# -*- coding: utf-8 -*-
"""Generate REQUIREMENTS_TRACEABILITY.md from both registries.

Coverage is computed, never asserted. A requirement with no mapping is reported
as uncovered, and a deliberately deferred requirement is reported as deferred
rather than being quietly counted as covered.
"""
import os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(ROOT)

V1 = os.path.join(REPO, "EXECUTION_BLUEPRINT", "_registry", "requirements.tsv")
V2 = os.path.join(ROOT, "_registry", "v2-requirements.tsv")
OUT = os.path.join(ROOT, "REQUIREMENTS_TRACEABILITY.md")

# EXECUTION_BLUEPRINT phase -> V2 prompt(s). DEFER means deliberately out of V2 scope.
PHASE_MAP = {
    "PHASE-00": ["P00"],
    "PHASE-01": ["P01", "P02"],
    "PHASE-02": ["P03"],
    "PHASE-03": ["P04"],
    "PHASE-04": ["P05", "P06"],
    "PHASE-05": ["P07"],
    "PHASE-06": ["P09"],
    "PHASE-07": ["P11"],
    "PHASE-08": ["DEFER:commerce"],
    "PHASE-09": ["P10"],
    "PHASE-10": ["P17"],
    "PHASE-11": ["P18"],
    "PHASE-12": ["P14", "P15"],
    "PHASE-13": ["P16"],
    "PHASE-14": ["P19"],
    "PHASE-15": ["DEFER:specialist"],
    "PHASE-16": ["DEFER:commerce"],
}

DEFER_REASON = {
    "commerce": "مؤجَّل بقرار معتمد ADR-V2-009: الإطلاق لمشغّل واحد، والتجارة الذاتية خارج نطاق الإطلاق.",
    "specialist": "خارج نطاق هذه الحزمة: المسارات التخصصية تتوسع بعد إثبات المسار الذهبي في P10.",
}


def read_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        header = None
        for line in fh:
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("\t")
            if header is None:
                header = parts
                continue
            if len(parts) != len(header):
                raise SystemExit("column mismatch in %s: %r" % (path, parts[:1]))
            rows.append(dict(zip(header, parts)))
    return rows


def main():
    v1 = read_tsv(V1)
    v2 = read_tsv(V2)

    unmapped_phase = sorted({r["phase"] for r in v1 if r["phase"] not in PHASE_MAP})
    if unmapped_phase:
        raise SystemExit("unmapped phases: %s" % unmapped_phase)

    cov = collections.defaultdict(list)   # prompt -> [req_id]
    deferred = collections.defaultdict(list)
    for r in v1:
        for t in PHASE_MAP[r["phase"]]:
            if t.startswith("DEFER:"):
                deferred[t.split(":", 1)[1]].append(r["req_id"])
            else:
                cov[t].append(r["req_id"])
    for r in v2:
        cov[r["prompt_ref"]].append(r["req_id"])

    total = len(v1) + len(v2)
    covered = sum(len(v) for v in cov.values())
    deferred_n = sum(len(v) for v in deferred.values())
    # a requirement may map to more than one prompt; count distinct
    distinct_cov = len({q for v in cov.values() for q in v})
    distinct_def = len({q for v in deferred.values() for q in v})
    uncovered = total - distinct_cov - distinct_def

    L = []
    L.append("<!-- coverage: total=%d covered=%d deferred=%d uncovered=%d -->"
             % (total, distinct_cov, distinct_def, uncovered))
    L.append("")
    L.append("# REQUIREMENTS_TRACEABILITY — Sketch Design V2")
    L.append("")
    L.append("مصفوفة التتبّع. **مُولَّدة آليًا** من السجلّين بـ `execution/_tools/gen_traceability.py`.")
    L.append("لا تُحرَّر يدويًا: التغطية تُحسَب ولا تُدَّعى.")
    L.append("")
    L.append("## 1. الحصيلة | Totals")
    L.append("")
    L.append("| | العدد |")
    L.append("| --- | --- |")
    L.append("| متطلبات من مصنف v11 (`EXECUTION_BLUEPRINT/_registry/requirements.tsv`) | %d |" % len(v1))
    L.append("| متطلبات من المرجع الشامل 2026 (`execution/_registry/v2-requirements.tsv`) | %d |" % len(v2))
    L.append("| **الإجمالي** | **%d** |" % total)
    L.append("| مغطّاة بأمر واحد على الأقل | %d |" % distinct_cov)
    L.append("| **مؤجَّلة صراحةً** خارج نطاق هذه الحزمة | %d |" % distinct_def)
    L.append("| **غير مغطّاة** | %d |" % uncovered)
    L.append("")
    if uncovered == 0:
        L.append("لا متطلب غير مغطّى وغير مؤجَّل. المؤجَّل **ليس مغطّى**، ويُعدّ منفصلًا بقصد.")
    else:
        L.append("**تحذير: %d متطلبًا بلا تغطية.** هذا عيب يجب إصلاحه قبل اعتماد الحزمة." % uncovered)
    L.append("")
    L.append("## 2. التغطية لكل أمر | Coverage per prompt")
    L.append("")
    L.append("| الأمر | عدد المتطلبات | المعرّفات |")
    L.append("| --- | --- | --- |")
    for p in sorted(cov):
        ids = sorted(set(cov[p]))
        shown = "، ".join(ids) if len(ids) <= 14 else "، ".join(ids[:14]) + " … (+%d)" % (len(ids) - 14)
        L.append("| `%s` | %d | %s |" % (p, len(ids), shown))
    L.append("")
    L.append("## 3. المؤجَّل صراحةً | Deliberately deferred")
    L.append("")
    L.append("هذه المتطلبات **ليست مغطّاة**، وعدم تغطيتها قرار لا سهو.")
    L.append("")
    for k in sorted(deferred):
        ids = sorted(set(deferred[k]))
        L.append("### %s — %d متطلبًا" % (k, len(ids)))
        L.append("")
        L.append(DEFER_REASON[k])
        L.append("")
        L.append("`" + "`، `".join(ids) + "`")
        L.append("")
    L.append("## 4. تعارضات الاصطلاح بين المرجعين | Convention conflicts")
    L.append("")
    L.append("المرجعان يتعايشان، وهذه نقاط اختلافهما الصريحة. **تحكم هذه الحزمة للتنفيذ الإنتاجي**،")
    L.append("ويبقى المرجع الأول مصدرًا للمتطلبات وجردها.")
    L.append("")
    L.append("| الموضوع | `EXECUTION_BLUEPRINT` | هذه الحزمة | الحاكم |")
    L.append("| --- | --- | --- | --- |")
    L.append("| مفردات الحالة | كلمة المصدر الأصلية لكل بند | `DESIGNED/IMPLEMENTED/TESTED/VERIFIED/BLOCKED` | هذه الحزمة |")
    L.append("| تسمية الأوامر | `P00-01` داخل ملف مرحلة | `P00_DISCOVERY.md` ملف لكل أمر | هذه الحزمة |")
    L.append("| بنية الأمر | سبعة أقسام A–G | اثنا عشر عنصرًا، منها التراجع والأدلة | هذه الحزمة |")
    L.append("| الموقع | `EXECUTION_BLUEPRINT/PHASES/` | `execution/prompts/` | الاثنان، لغرضين |")
    L.append("| المكدس القديم | غير مذكور في مصنف v11 | **متقاعد صراحةً** (`ADR-V2-001`) | هذه الحزمة |")
    L.append("| التجارة | `PHASE-08` و`PHASE-16` بتفصيل | مؤجَّلة خارج النطاق | هذه الحزمة للإطلاق |")
    L.append("")
    L.append("**ملاحظة على التقاعد.** قرار تقاعد AI Core والمكدس السابق **لا يوجد في مصنف v11**؛")
    L.append("مصدره الوحيد هو المرجع الشامل 2026. وهو معلومة جديدة تعلو على أي افتراض سابق،")
    L.append("لا تناقضًا بين مصدرين.")
    L.append("")
    L.append("## 5. ما لا تثبته هذه المصفوفة | What this matrix does not prove")
    L.append("")
    L.append("تثبت أن كل متطلب **مُسنَد إلى أمر**. لا تثبت أن الأمر نُفِّذ، ولا أن التنفيذ صحيح،")
    L.append("ولا أن المتطلب مُحقَّق. الإسناد نية؛ والدليل المُنفَّذ في `P20` هو ما يثبت التحقق.")
    L.append("")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("total=%d covered=%d deferred=%d uncovered=%d" % (total, distinct_cov, distinct_def, uncovered))
    print("wrote", OUT)


if __name__ == "__main__":
    main()

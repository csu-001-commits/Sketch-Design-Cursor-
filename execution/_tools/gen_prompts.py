# -*- coding: utf-8 -*-
"""Render the Sketch Design V2 execution prompt package.

Every prompt file carries an Arabic explanation for the reader and a single
English executable block holding the twelve mandatory elements. Identifiers,
contracts and commands stay in English by design; see
SKETCH_DESIGN_PRODUCTION_EXECUTION_MASTER_V2.md, section 11.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "prompts")

from prompts_a import PROMPTS_A
from prompts_b import PROMPTS_B
from prompts_c import PROMPTS_C

PROMPTS = PROMPTS_A + PROMPTS_B + PROMPTS_C

CONTRACT = "execution/OPERATING_RULES.md"

ELEMENTS = [
    "1. OBJECTIVE",
    "2. DEPENDENCIES",
    "3. EXACT SCOPE",
    "4. FILES AND MODULES AFFECTED",
    "5. REQUIRED CONTRACTS",
    "6. IMPLEMENTATION INSTRUCTIONS",
    "7. SECURITY REQUIREMENTS",
    "8. AUTOMATED TESTS",
    "9. ACCEPTANCE CRITERIA",
    "10. REQUIRED EVIDENCE",
    "11. ROLLBACK INSTRUCTIONS",
    "12. DEFINITION OF DONE",
]


def bullets(items, marker="-"):
    return "\n".join("%s %s" % (marker, i) for i in items)


def render(p):
    name = "%s_%s" % (p["id"], p["slug"])
    L = []
    L.append("<!-- promptmeta")
    L.append("id: %s" % p["id"])
    L.append("file: %s.md" % name)
    L.append("stage: %s" % p["stage"])
    L.append("title_en: %s" % p["title_en"])
    L.append("prereq: %s" % p["prereq"])
    L.append("requirements: %s" % p["reqs"])
    L.append("status: %s" % p.get("status", "DESIGNED"))
    L.append("-->")
    L.append("")
    L.append("# %s — %s" % (name, p["title_en"]))
    L.append("")
    L.append("**%s**" % p["title_ar"])
    L.append("")
    L.append("| | |")
    L.append("| --- | --- |")
    L.append("| مرحلة خارطة الطريق | %s |" % p["stage"])
    L.append("| المتطلب السابق | %s |" % (p["prereq"] if p["prereq"] != "-" else "لا يوجد"))
    L.append("| المتطلبات المغطّاة | %s |" % p["reqs"].replace(",", "، "))
    L.append("| الحالة | %s |" % p.get("status", "DESIGNED"))
    L.append("")
    ex = p.get("executed")
    if ex:
        L.append("## سجل التنفيذ | Execution record")
        L.append("")
        L.append("نُفِّذ هذا الأمر في `%s`." % ex["at"])
        L.append("")
        L.append("**المخرجات:**")
        L.append("")
        L.extend("- %s" % o for o in ex["outputs"])
        L.append("")
        L.append("**الأدلة المرفقة:**")
        L.append("")
        L.extend("- %s" % e for e in ex["evidence"])
        L.append("")
        L.append("**ما اكتُشف:**")
        L.append("")
        L.extend("- %s" % f for f in ex["findings"])
        L.append("")
    L.append("## الشرح بالعربية")
    L.append("")
    L.append("**ماذا ينفذ هذا الأمر؟**  \n%s" % p["ar_what"])
    L.append("")
    L.append("**لماذا نحتاجه؟**  \n%s" % p["ar_why"])
    L.append("")
    L.append("**ما المتطلبات السابقة؟**  \n%s" % (
        "لا يوجد. هذا أمر الدخول." if p["prereq"] == "-"
        else "اكتمال %s ببوابة خروجه كاملة." % p["prereq"]))
    L.append("")
    L.append("**ما النتيجة المتوقعة؟**  \n%s" % p["ar_result"])
    L.append("")
    L.append("**كيف نتحقق من نجاحه؟**  \n%s" % p["ar_verify"])
    L.append("")
    L.append("## EXECUTABLE PROMPT")
    L.append("")
    L.append("```text")
    L.append("You are executing %s of the Sketch Design production implementation." % name)
    L.append("You are bound by %s. Read it before you begin." % CONTRACT)
    L.append("")
    L.append(ELEMENTS[0])
    L.append(p["objective"])
    L.append("")
    L.append(ELEMENTS[1])
    L.append(p["deps"])
    L.append("")
    L.append(ELEMENTS[2])
    L.append("IN SCOPE:")
    L.append(bullets(p["scope_in"]))
    L.append("")
    L.append("OUT OF SCOPE — do not do these, and do not quietly widen into them:")
    L.append(bullets(p["scope_out"]))
    L.append("")
    L.append(ELEMENTS[3])
    L.append(bullets(p["files"]))
    L.append("")
    L.append(ELEMENTS[4])
    L.append(bullets(p["contracts"]))
    L.append("")
    L.append(ELEMENTS[5])
    L.append(bullets(p["impl"]))
    L.append("")
    L.append(ELEMENTS[6])
    L.append(bullets(p["security"]))
    L.append("")
    L.append(ELEMENTS[7])
    L.append(bullets(p["tests"]))
    L.append("")
    L.append(ELEMENTS[8])
    L.append(bullets(p["accept"]))
    L.append("")
    L.append(ELEMENTS[9])
    L.append("Attach each item. An item you cannot attach is reported as not produced, never described as if it were.")
    L.append(bullets(p["evidence"]))
    L.append("")
    L.append(ELEMENTS[10])
    L.append(p["rollback"])
    L.append("")
    L.append(ELEMENTS[11])
    L.append(bullets(p["dod"]))
    L.append("")
    L.append("STOP CONDITION")
    L.append("Stop and report rather than proceeding if: a dependency's exit gate is not met; a required")
    L.append("decision in execution/OPEN_DECISIONS.md is unresolved and blocks this prompt; an action would")
    L.append("delete production data, deploy publicly, modify DNS, incur paid API usage, or make an")
    L.append("irreversible infrastructure change without explicit authorization.")
    L.append("Report the blocker, record the status as BLOCKED, and do not substitute an approximation.")
    L.append("```")
    L.append("")
    return name, "\n".join(L) + "\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    seen = set()
    for p in PROMPTS:
        assert p["id"] not in seen, "duplicate prompt id %s" % p["id"]
        seen.add(p["id"])
        name, body = render(p)
        with open(os.path.join(OUT, name + ".md"), "w", encoding="utf-8") as fh:
            fh.write(body)
    index = ["# Sketch Design — Execution Prompt Package (V2)", "",
             "حزمة أوامر التنفيذ الإنتاجية. كل أمر يحمل اثني عشر عنصرًا إلزاميًا، ويُنفَّذ بالترتيب،",
             "ولا يبدأ أمر قبل اكتمال بوابة خروج سابقه.", "",
             "كل أمر مقيّد بـ `execution/OPERATING_RULES.md`.", "",
             "| Prompt | Roadmap stage | Prereq | Requirements | Status |",
             "| --- | --- | --- | --- | --- |"]
    for p in PROMPTS:
        name = "%s_%s" % (p["id"], p["slug"])
        index.append("| [%s](%s.md) | %s | %s | %s | %s |" % (
            name, name, p["stage"], p["prereq"], p["reqs"], p.get("status", "DESIGNED")))
    index.append("")
    done = [p for p in PROMPTS if p.get("status", "DESIGNED") != "DESIGNED"]
    index.append("## الحالات")
    index.append("")
    if done:
        n = len(done)
        count = {1: "أمر واحد", 2: "أمران"}.get(n, "%d أوامر" % n if n < 11 else "%d أمرًا" % n)
        index.append("نُفِّذ من هذه الحزمة %s: %s، وله سجل تنفيذ بأدلته داخل ملفه."
                     % (count, "، ".join("`%s`" % d["id"] for d in done)))
        index.append("")
    index.append("بقية الأوامر في حالة DESIGNED: مكتوبة ولم تُنفَّذ بعد.")
    index.append("لا تُرقّى حالة أي أمر إلى IMPLEMENTED أو TESTED أو VERIFIED إلا بدليل مُنفَّذ ومرفق،")
    index.append("وفق سلّم الحالات في `SKETCH_DESIGN_PRODUCTION_EXECUTION_MASTER_V2.md`.")
    index.append("")
    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(index))
    print("wrote %d prompts + README to %s" % (len(PROMPTS), OUT))


if __name__ == "__main__":
    main()

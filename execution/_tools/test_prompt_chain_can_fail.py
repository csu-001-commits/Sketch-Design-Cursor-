# -*- coding: utf-8 -*-
"""Prove validate_v2.check_chain can fail after the P-GOV relaxation.

check_chain used to assert that prompt ids were exactly P00..Pnn. P-GOV is a
registered insertion into that chain, so the rule was relaxed — and a relaxed
rule has to be shown still able to reject the mistakes it was guarding against.

Run: python3 execution/_tools/test_prompt_chain_can_fail.py
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def fresh():
    if "validate_v2" in sys.modules:
        del sys.modules["validate_v2"]
    return importlib.import_module("validate_v2")


def trial(name, gen, metas, order):
    v = fresh()
    v.generated_order = lambda: gen
    v.errors[:] = []
    v.check_chain(metas, order)
    caught = bool(v.errors)
    print("%-56s %s" % (name[:56],
                        ("CAUGHT  " + v.errors[0][:70]) if caught else "no error"))
    return caught


def M(pre):
    return {"prereq": pre}


GOOD_GEN = ["P00", "P01", "P02", "P03", "P-GOV", "P04"]
GOOD_METAS = {"P00": M("-"), "P01": M("P00"), "P02": M("P01"),
              "P03": M("P02"), "P-GOV": M("P03"), "P04": M("P03")}
GOOD_ORDER = ["P-GOV", "P00", "P01", "P02", "P03", "P04"]

CASES = [
    ("numeric sequence has a gap (P02 missing)",
     ["P00", "P01", "P03", "P-GOV"],
     {"P00": M("-"), "P01": M("P00"), "P03": M("P01"), "P-GOV": M("P03")}),
    ("unregistered non-numeric prompt id",
     ["P00", "P01", "P-XYZ"],
     {"P00": M("-"), "P01": M("P00"), "P-XYZ": M("P01")}),
    ("a prereq that runs later in the execution order",
     ["P00", "P01", "P-GOV"],
     {"P00": M("-"), "P01": M("P-GOV"), "P-GOV": M("P00")}),
    ("prompts/ holds a prompt the generator does not define",
     ["P00", "P01"],
     {"P00": M("-"), "P01": M("P00"), "P-GOV": M("P00")}),
    ("a second prompt claiming no prereq",
     ["P00", "P01"],
     {"P00": M("-"), "P01": M("-")}),
    ("a prereq that does not exist at all",
     ["P00", "P01"],
     {"P00": M("-"), "P01": M("P99")}),
]


def main():
    if trial("baseline — a valid chain containing P-GOV", GOOD_GEN, GOOD_METAS, GOOD_ORDER):
        print("\nbaseline must pass before injection means anything")
        return 1
    print("")
    missed = 0
    for name, gen, metas in CASES:
        if not trial(name, gen, metas, sorted(metas)):
            missed += 1
    print("")
    print("chain injections: %d  caught: %d  missed: %d"
          % (len(CASES), len(CASES) - missed, missed))
    return 1 if missed else 0


if __name__ == "__main__":
    sys.exit(main())

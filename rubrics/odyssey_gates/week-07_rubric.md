# Odyssey Gate — Week 7 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Parameterized function | A function definition exists with ≥1 parameter. |
| Real return | The function returns a value used by the caller (not `None`/print-only). |
| Called + behavior-preserving | Called from outside its own body at least once; world output matches pre-refactor behavior. |

**All three present → pass.** Fully mechanical — parameter presence, return
statement, and a call site are all detectable statically; "behavior
preserved" is checkable by diffing pre/post output if both are available,
otherwise a light human spot-check.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- A function that takes a parameter but ignores it (dead parameter) does
  not pass "parameterized function" in spirit — check the parameter is
  actually used in the function body, not just present in the signature.
- The World Bible one-line log entry (this week's assignment) is a
  required but not-separately-scored part of the submission — tracked
  across the semester and reviewed as a whole at Week 17's checkpoint
  (`rubrics/odyssey_gates/week-17_rubric.md`), not graded week-by-week
  here.
- Light Build (Part 2 above) is graded separately and holistically — not
  part of this gate's pass/fail criteria.

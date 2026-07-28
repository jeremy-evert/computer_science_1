# Odyssey Gate — Week 5 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Real loop | A `for` or `while` loop is present and iterates more than once in the demonstrated run. |
| Data- or sentinel-driven | Iteration count comes from real world data or a sentinel condition, not a hardcoded constant disconnected from world state. |
| State changes across iterations | An accumulator, running total, or other state actually changes iteration to iteration (not the same print repeated N times). |

**All three present → pass.** This is the clearest fully-mechanical gate so
far — all three criteria are detectable from a static/behavioral trace
without a judgment call, a strong first candidate for a real Marker
LOCAL-style check.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- A loop with a hardcoded `range(3)` that happens to match the current data
  size by coincidence does not pass "data- or sentinel-driven" — check that
  the bound is actually derived from state, not a lucky constant.
- The World Bible one-line log entry (this week's assignment) is a
  required but not-separately-scored part of the submission — tracked
  across the semester and reviewed as a whole at Week 17's checkpoint
  (`rubrics/odyssey_gates/week-17_rubric.md`), not graded week-by-week
  here.
- Light Build (Part 2 above) is graded separately and holistically — not
  part of this gate's pass/fail criteria.

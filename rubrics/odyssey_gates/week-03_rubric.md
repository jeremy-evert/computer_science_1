# Odyssey Gate — Week 3 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Conditional present | An `if` (with or without `else`) exists and is reachable in the submitted run. |
| Real condition | The condition references actual world state carried from Week 2, not a literal `True`/`False` or unrelated toy value. |
| Both paths shown | Submission demonstrates the world in both a true-condition and a false-condition state (two runs, or one run plus a clear code-level explanation of the other path). |

**All three present → pass.**

**Grading route:** mechanical-checkable for presence of an `if` and
non-literal condition; the "both paths shown" criterion needs a light human
or frontier-agent check (does the demonstrated state actually differ, not
just cosmetically).

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2's rubric (Strong/Solid/Minimal) — see
`rubrics/odyssey_gates/week-02_rubric.md` for the band descriptions;
applied here to "does the decision feel like it belongs to this world."

## Grading notes

- A condition that's technically present but never actually reachable
  (dead code) does not pass "Conditional present" — it must run in the
  demonstrated submission.
- The World Bible one-line log entry (this week's assignment) is a
  required but not-separately-scored part of the submission — tracked
  across the semester and reviewed as a whole at Week 17's checkpoint
  (`rubrics/odyssey_gates/week-17_rubric.md`), not graded week-by-week
  here.
- Light Build (Part 2 above) is graded separately and holistically — not
  part of this gate's pass/fail criteria.

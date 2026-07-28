# Odyssey Gate — Week 4 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| 3+ outcomes | `if`/`elif`/`else` chain or nested conditions reach at least 3 distinct outcomes from the same decision point. |
| Boundary handled | At least one edge/boundary case (the threshold itself, not just clearly-above/clearly-below) is deliberately handled, not accidentally correct. |
| Real behavior change | A stored value or execution path differs across outcomes — not just the printed sentence. |

**All three present → pass.**

**Grading route:** "3+ outcomes" and "real behavior change" are
mechanical-checkable (branch count, whether downstream state differs across
a traced run). "Boundary handled" needs a human/frontier-agent check — it's
a judgment call about whether the edge case was deliberate, not just
lucky.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- Do not require exactly 3 outcomes as a hard ceiling — more is fine; fewer
  than 3 does not pass.
- "The threshold itself" boundary case matters because it's the classic
  off-by-one/edge trap this lesson's own objectives name
  (`lessons/03-branching.md`: "Test boundary and invalid cases").
- The World Bible one-line log entry (this week's assignment) is a
  required but not-separately-scored part of the submission — tracked
  across the semester and reviewed as a whole at Week 17's checkpoint
  (`rubrics/odyssey_gates/week-17_rubric.md`), not graded week-by-week
  here.
- Light Build (Part 2 above) is graded separately and holistically — not
  part of this gate's pass/fail criteria.

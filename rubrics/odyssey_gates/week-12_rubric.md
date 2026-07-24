# Odyssey Gate — Week 12 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Real class | `__init__` sets ≥1 real instance attribute — not an empty pass-only class. |
| Real method | ≥1 method beyond `__init__` uses `self`'s state meaningfully. |
| Instantiated + used | An instance is created and its method called in the demonstrated run. |

**All three present → pass.** Fully mechanical.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- An empty class with only `pass` or attributes set but never read by any
  method does not pass — the point is behavior tied to state, not a data
  container renamed "class."

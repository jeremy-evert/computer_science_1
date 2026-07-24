# Odyssey Gate — Week 8 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Real string processing | At least one real string method/operation (search, slice, transform) is applied to input text — f-string display formatting alone does not count. |
| Result is used | The processed result feeds a decision or gets stored, not discarded immediately after computing. |
| Edge case handled | At least one validation/whitespace edge case is deliberately handled. |

**All three present → pass.**

**Grading route:** "real string processing" and "result is used" are
mechanical-checkable; "edge case handled" needs a light human/frontier-agent
judgment call (was it deliberate, matching this lesson's own "combine input
validation with text operations" objective — `lessons/06-strings.md`).

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- Genre latitude: Investigation Bureau and Starship Log naturally produce
  richer free text to parse than Small Business or Frontier Settlement —
  don't penalize a genre for having a thinner natural text source this
  week; judge processing quality relative to the text available, not
  absolute text volume.

# Odyssey Gate — Week 5: The first season passes

**Gate status:** active

**Concept:** loops and repetition (`lessons/04-loops.md`).
**Arc:** 1 — Foundations. **Instrument:** Quick Check (pass/fail) — see
`docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Add a loop that processes an **unknown or variable number** of events in
your world — sentinel-controlled (keeps going until some condition) or
range-driven from real world state (not a hardcoded `for i in range(3)`
with no connection to anything). Something repeated — harvests, patrols,
transactions, log entries, whatever fits your genre — happens more than
once because the loop says so, not because you wrote it out three times by
hand.

## Quick Check (pass/fail)

- [ ] A `for` or `while` loop is present and actually repeats (not a
      single-iteration loop standing in for an `if`).
- [ ] The number of iterations is driven by real data or a sentinel
      condition, not a hardcoded constant unrelated to world state.
- [ ] An accumulator or running total/state changes across iterations (the
      loop does more than print the same thing N times).

## Suggested practice problem (optional scaffolding)

The general problem: write a loop over a short list of 3–5 made-up events,
printing something for each one and keeping a running total or count as
you go.

- **Frontier Settlement:** loop over a list of harvest amounts (e.g.
  `[12, 9, 15, 11]`), summing into `total_food`.
- **Investigation Bureau:** loop over a list of witness statements,
  counting how many mention a keyword (e.g. `"saw"`).
- **Starship Log:** loop over a list of system-check results, counting how
  many came back `"fail"`.
- **Small Business:** loop over a list of daily sales figures, summing into
  `total_revenue`.

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

## World Bible

One line: what gate you passed, what broke.

## Looking ahead

Week 6 folds loops review directly into **Coding Odyssey Checkpoint 1**
(the "baby project" dry run) — see `assignments/A2-coding-odyssey-project.md`
and `planning/week-06.md`. No separate gate next week; the checkpoint is
the gate.

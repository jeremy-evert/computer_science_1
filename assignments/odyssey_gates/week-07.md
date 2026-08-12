# Odyssey Gate — Week 7: Someone else must be able to run this

**Gate status:** active

**Concept:** functions and decomposition (`lessons/05-functions.md`).
**Arc:** 2 — First Real Choices. **Instrument:** Quick Check (pass/fail) —
see `docs/curriculum/judgment_toolkit.md` §1. Full graded functions
instruction starts this week (Week 6 was preview-only, ungraded — see
`planning/week-06.md`).

## The gate (do this first)

Take one distinct action your world already does (something from Weeks
2-6 — the founding print, the decision, the loop) and pull it into its own
function with **at least one parameter and a return value**. Call it from
somewhere else in your code. This is your world's first refactor: the same
behavior as before, now named and reusable.

## Quick Check (pass/fail)

- [ ] A function is defined with at least one parameter (not a
      zero-argument function that just reads globals).
- [ ] The function returns a value (not just prints and returns `None`).
- [ ] The function is called at least once from outside its own
      definition, and the world's behavior is unchanged from before the
      refactor (same output, cleaner structure).

## Suggested practice problem (optional scaffolding)

The general problem: take a branching check you already wrote (Week 3 or
4) and turn it into a function that takes the value as a parameter and
*returns* the status label instead of printing it directly; call the
function and print the result yourself.

- **Frontier Settlement:** `def food_status(stock): ...` returns
  `"critical"`/`"low"`/`"stable"`.
- **Investigation Bureau:** `def case_temperature(hours_cold): ...` returns
  `"hot"`/`"cooling"`/`"cold"`.
- **Starship Log:** `def fuel_status(fuel_remaining): ...` returns
  `"critical"`/`"low"`/`"nominal"`.
- **Small Business:** `def cash_status(balance): ...` returns
  `"overdrawn"`/`"tight"`/`"healthy"`.

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

## World Bible

One line: what gate you passed, what broke — this is the first week where
"what broke" is likely to mean something real (refactors reveal bugs that
were hiding in copy-pasted code).

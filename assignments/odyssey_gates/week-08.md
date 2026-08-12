# Odyssey Gate — Week 8: The world starts reading its own mail

**Gate status:** active

**Concept:** strings and text processing (`lessons/06-strings.md`).
**Arc:** 2 — First Real Choices. **Instrument:** Quick Check (pass/fail) —
see `docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Parse or transform a piece of free-text input in your world — a log entry,
a witness statement, a customer message, a ship's log line — using **real
string operations** (indexing/slicing, search, or transform methods; not
just `print(f"...")` interpolation, which doesn't count as processing).

Genre note: this is the natural strong week for **Investigation Bureau**
(parsing witness statements) and a good fit for any genre's log/report
data.

## Quick Check (pass/fail)

- [ ] Input text is searched, sliced, or transformed using real string
      methods (`.split()`, `.find()`, slicing, `.strip()`, etc.) — not just
      formatted for display.
- [ ] The result of that processing is used for something (a decision, a
      stored value) — not processed and immediately discarded.
- [ ] At least one input-validation or whitespace/edge case from the
      lesson's own focus is handled on purpose.

## Suggested practice problem (optional scaffolding)

The general problem: write one short, made-up line of text relevant to
your world, then pull one specific piece of information out of it with
`.split()`, `.find()`, or slicing — not just print it back formatted.

- **Frontier Settlement:** `"Day 12: harvested 40 units of grain"` → split
  out the day number and the harvest amount.
- **Investigation Bureau:** `"The suspect left around 9pm near the
  docks"` → extract the time or the location.
- **Starship Log:** `"STATUS: fuel=62 hull=98"` → split out the fuel and
  hull values.
- **Small Business:** `"SKU-2291 x3 @ $4.50"` → parse out the quantity and
  the unit price.

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

## World Bible

One line: what gate you passed, what broke.

## Looking ahead

Week 9 (strings continued) is **Coding Odyssey Checkpoint 2** — your first
real project pass, not a dry run this time. See
`assignments/A2-coding-odyssey-project.md` and `planning/week-09.md`. No
separate gate; the checkpoint is the gate, graded with the full Build
rubric this time (`docs/curriculum/judgment_toolkit.md` §2).

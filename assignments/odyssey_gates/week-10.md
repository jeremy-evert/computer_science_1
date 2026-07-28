# Odyssey Gate — Week 10: The census

**Concept:** lists and dictionaries — lists first (`lessons/07-collections.md`).
**Arc:** 3 — Systems That Remember Themselves. **Instrument:** Quick Check
(pass/fail) — see `docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Your world's population/inventory/case-load/customer-base becomes
**enumerable**: track a growing collection of named entities in a list,
built up over more than one addition (not a list literal typed out once
and never modified).

## Quick Check (pass/fail)

- [ ] A list holds multiple distinct entities relevant to the world (not a
      list of unrelated scratch values).
- [ ] The list is built up via `.append()` (or equivalent) at least twice
      across the program's run, not hardcoded as a single literal.
- [ ] At least one operation traverses the list (a loop, `len()`-based
      report, or search) and reports something real about it.

## Suggested textbook problem (optional scaffolding)

The general problem: start an empty list, `.append()` at least two
entities to it one at a time (not a list literal typed out once), then
loop over it to report something real.

- **Frontier Settlement:** `colonists = []` → append names one at a time →
  loop to print the roster and a headcount.
- **Investigation Bureau:** `suspects = []` → append names → loop to print
  the suspect list.
- **Starship Log:** `crew = []` → append names → loop to print the crew
  manifest.
- **Small Business:** `customers = []` → append names → loop to print the
  customer list and a count.

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

## World Bible

One line: what gate you passed, what broke.

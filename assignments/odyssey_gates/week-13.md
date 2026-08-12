# Odyssey Gate — Week 13: The world becomes real things (Round 2)

**Gate status:** active

**Concept:** classes, objects, modules — Round 2 (`lessons/08-classes-and-modules.md`).
**Arc:** 3 — Systems That Remember Themselves. **Instrument:** Quick Check
(pass/fail) + **Decide/Compare #2 (capstone)** — see
`docs/curriculum/judgment_toolkit.md` §1/§3.

**Moved 2026-08-12:** Decide/Compare #2 (capstone) now lands here instead
of Week 16, since Week 16 is now the Farkle/ML fun week and substantial
Odyssey building culminates this week, not Week 16. See
`planning/week-16.md` and `planning/coding-odyssey-arc-map.md`.

## Decide/Compare #2 — capstone scale

A bigger version of Week 11's move, applied to the whole world instead of
one data structure. Pick one real design decision your world still has open
(not necessarily technical — could be a scope choice, a feature you're
cutting, a structure you're keeping despite knowing a "better" one exists)
and:

1. Commit to the choice, in writing, before comparing.
2. Compare against at least one real alternative, naming the actual
   trade-off for *this* world at *this* stage of the semester (not a
   textbook trade-off).
3. State why the comparison, not the alternative, is what changed your
   mind (or confirmed your original choice).

Log the choice and rationale in your World Bible — this feeds directly
into Week 14's Full Trail Debrief and the Week 17 final Judgment Log
review.

## The gate (do this first)

At least **two** of your world's classes must interact — a method call
between objects, not just standalone instances that never talk to each
other. If Week 12 only produced one class, this is where a second one
(or a second instance type) shows up and the two connect.

## Quick Check (pass/fail)

- [ ] At least 2 distinct classes exist (or a second meaningfully different
      instance role of the same class, if the genre only naturally
      supports one noun-type — flag this case for a human read rather than
      auto-failing).
- [ ] At least one method call crosses between two objects (object A's
      method calls or reads from object B, not two isolated silos).
- [ ] The interaction produces a real, demonstrable effect (a state change,
      a computed result) — not just proof the syntax runs.

## Suggested practice problem (optional scaffolding)

The general problem: add a second class (or a second, meaningfully
different role of the same class), and have one object's method call or
read from another object — not two classes that never talk to each other.

- **Frontier Settlement:** `Colonist` + `Settlement` — `Settlement.
  consume_food()` reads and updates a list of `Colonist` objects.
- **Investigation Bureau:** `Suspect` + `CaseFile` — `CaseFile.
  add_suspect(suspect)` reads a `Suspect` object's data.
- **Starship Log:** `CrewMember` + `Ship` — `Ship.report_status()` reads
  each `CrewMember` object.
- **Small Business:** `Customer` + `Store` — `Store.process_sale(customer)`
  updates a `Customer` object's balance.

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

This is the natural point to reflect on Weeks 12-13 as a whole — see
Checkpoint 3's **Full Trail Debrief** next week
(`docs/curriculum/judgment_toolkit.md` §4), which asks specifically what
broke in this OOP refactor and what you'd design differently starting
fresh. Start taking notes now, while it's fresh, for that Debrief.

## World Bible

One line: what gate you passed, what broke.

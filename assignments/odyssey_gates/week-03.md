# Odyssey Gate — Week 3: The world starts noticing things

**Concept:** types/formatting continued; branching introduced
(`lessons/02-variables-expressions-types.md`, `lessons/03-branching.md`).
**Arc:** 1 — Foundations. **Instrument:** Quick Check (pass/fail) — see
`docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Add **one `if` statement** to your world that changes what gets printed
based on some piece of world state (a number, a flag, a name — whatever you
already have from Week 2). This is your world's first real decision — small
on purpose. Full branching depth (elif chains, nested conditions) is next
week; this gate only asks for one working condition.

Examples, illustrative only:

- **Frontier Settlement:** if food stock is below a threshold, print a
  shortage warning instead of the normal status line.
- **Investigation Bureau:** if the case clock passes some number of hours,
  print "growing cold" instead of "active."
- **Starship Log:** if fuel is below a threshold, print a warning instead of
  the normal status.
- **Small Business:** if cash on hand is negative, print a different ledger
  line than the normal one.

## Quick Check (pass/fail)

- [ ] An `if` statement (with or without `else`) is present and reachable.
- [ ] The condition references real world state from Week 2, not a
      hardcoded `True`/`False`.
- [ ] Both branches (or the one branch + fallthrough) are demonstrated —
      show your world in a state where the condition is true, and a state
      where it isn't.

## Suggested textbook problem (optional scaffolding)

The general problem: pick one number or flag you already track, and write
one `if`/`else` that prints a different sentence depending on its value —
show both a true-condition run and a false-condition run.

- **Frontier Settlement:** `if food_stock < 20:` print a shortage warning;
  `else:` print "The settlement is stable."
- **Investigation Bureau:** `if hours_cold > 48:` print "The trail has gone
  cold."; `else:` print "The case is still active."
- **Starship Log:** `if fuel_remaining < 20:` print "Warning: fuel
  critical."; `else:` print "Fuel levels nominal."
- **Small Business:** `if opening_cash < 0:` print a negative-balance
  alert; `else:` print "Opening balance looks normal."

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

Keep extending your world's opening scene. See
`docs/curriculum/judgment_toolkit.md` §2.

## World Bible

One line: what gate you passed, what broke.

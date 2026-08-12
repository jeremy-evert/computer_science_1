# Odyssey Gate — Week 2: The world wakes up

**Gate status:** active

**Concept:** variables, expressions, types (`lessons/02-variables-expressions-types.md`).
**Arc:** 1 — Foundations. **Instrument:** Quick Check (pass/fail) — see
`docs/curriculum/judgment_toolkit.md` §1. Full map: `planning/coding-odyssey-arc-map.md`.

## Step 0 — Pick your genre (moved here 2026-07-24 from Week 1 Friday)

Before anything else this week: pick one of 4 bounded genres and keep it
all semester.

- **The Frontier Settlement** — manage colonists, resources, events.
- **The Investigation Bureau** — a detective case-file engine (strongest
  fit for the optional NLP/text-analysis side-quest — see
  `planning/coding-odyssey-arc-map.md`).
- **The Starship Log** — crew and exploration management.
- **The Small Business** — inventory, customers, transactions.

Write a one-paragraph **founding charter**: what is this world, who's in
it, what's at stake. This is the seed of your World Bible
(`assignments/A2-coding-odyssey-project.md`) and the first Judgment Log
checkpoint (`docs/curriculum/judgment_toolkit.md` §5) — not graded
pass/fail like the gate below, just needs to genuinely exist.

## The gate (do this first)

Write a short scene where your world states its own founding condition —
using **at least one variable** and **at least one arithmetic or comparison
expression** — and prints the result. That's it. This is a gate, not the
week's whole assignment: if you're writing more than a few lines of world
logic to pass it, you've overbuilt it.

Examples of "founding condition," by genre (pick whichever fits the genre
you chose above — these are illustrations, not requirements):

- **Frontier Settlement:** starting food stock, computed as rations ×
  colonist count, printed as "The settlement begins with N days of food."
- **Investigation Bureau:** a case clock — hours since the report was filed,
  computed and printed as "The trail is N hours cold."
- **Starship Log:** fuel remaining after the jump, computed from a starting
  reserve minus a jump cost, printed as a status line.
- **Small Business:** opening cash on hand after rent, computed and printed
  as a ledger's first line.

## Quick Check (pass/fail)

- [ ] A variable is assigned and reused (not just a literal printed directly).
- [ ] At least one arithmetic or comparison expression computes something
      from that variable.
- [ ] The result prints as part of a sentence about the world, not a bare
      number.

All three present → pass. Missing any → not yet; resubmit, this is a gate,
not a one-shot.

## Suggested practice problem (optional scaffolding)

If you'd rather start from concrete numbers than invent your own scenario,
plug these straight into the genre examples above — same shapes, filled in:

- **Frontier Settlement:** `rations_per_colonist = 2`, `colonist_count = 40`
  → `food_stock = rations_per_colonist * colonist_count` → "The settlement
  begins with 80 days of food."
- **Investigation Bureau:** `report_filed_hour = 14`, `current_hour = 20` →
  `hours_cold = current_hour - report_filed_hour` → "The trail is 6 hours
  cold."
- **Starship Log:** `fuel_reserve = 100`, `jump_cost = 37` →
  `fuel_remaining = fuel_reserve - jump_cost` → "63 units of fuel remain
  after the jump."
- **Small Business:** `cash_on_hand = 5000`, `rent = 1200` →
  `opening_cash = cash_on_hand - rent` → "Opening cash on hand: $3800."

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

Once the gate passes, keep building your world's opening scene for the rest
of the week using anything covered through Week 2. Add more state, more
detail, more of your founding charter coming alive in code. Graded
holistically, not against this gate's checklist — see
`docs/curriculum/judgment_toolkit.md` §2 (light Build).

## World Bible

Add one line to your World Bible: what gate you passed, and anything that
broke along the way. See `assignments/A2-coding-odyssey-project.md` and
`docs/curriculum/judgment_toolkit.md` §5.

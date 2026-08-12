# Odyssey Gate — Week 4: The world weighs its options

**Concept:** branching and decision-making, full depth
(`lessons/03-branching.md`). No Monday session this week (Labor Day) — the
lecture content moves to Wed/Fri active time or the podcast; this gate is
unaffected.
**Arc:** 1 — Foundations. **Instrument:** Quick Check (pass/fail) — see
`docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Deepen last week's single `if` into a real decision with **at least three
distinct outcomes** (an `if`/`elif`/`else` chain, or nested conditions) that
meaningfully changes your world's behavior — not just its printed text.
"Meaningfully changes behavior" means something downstream is actually
different (a different value gets stored, a different path gets taken),
not just a different sentence printed.

## Quick Check (pass/fail)

- [ ] At least 3 distinct outcomes are reachable from the same decision
      point (`if`/`elif`/`else` or equivalent nesting).
- [ ] At least one boundary or edge case is handled on purpose (not just
      the obvious middle case) — e.g., the threshold value itself, not just
      clearly-above and clearly-below.
- [ ] The decision changes real behavior downstream, not only output text.

## Suggested practice problem (optional scaffolding)

The general problem: take the same value from Week 3 and sort it into
three or more named bands (not just true/false), and deliberately test the
exact boundary value between two bands, not just the obvious middle cases.

- **Frontier Settlement:** `food_stock` → "critical" (< 5), "low" (5–14),
  "stable" (15+); test exactly `5` and exactly `15`.
- **Investigation Bureau:** `hours_cold` → "hot" (< 24), "cooling" (24–71),
  "cold" (72+); test exactly `24` and exactly `72`.
- **Starship Log:** `fuel_remaining` → "critical" (< 10), "low" (10–29),
  "nominal" (30+); test exactly `10` and exactly `30`.
- **Small Business:** `cash_on_hand` → "overdrawn" (< 0), "tight" (0–999),
  "healthy" (1000+); test exactly `0` and exactly `1000`.

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

## World Bible

One line: what gate you passed, what broke.

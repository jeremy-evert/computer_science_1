# Odyssey Gate — Week 11: The registry, and the first real trade-off

**Concept:** lists and dictionaries continued (`lessons/07-collections.md`).
**Arc:** 3 — Systems That Remember Themselves. **Instruments:** Quick Check
(pass/fail) **and** Decide/Compare #1 — see
`docs/curriculum/judgment_toolkit.md` §1 and §3.

## The gate (do this first)

Add a dictionary that looks up an entity from Week 10's list **by name or
ID** — lookup replaces linear search by hand.

## Quick Check (pass/fail)

- [ ] A dict is used to look up an entity by a key (name/ID), not a manual
      loop-and-compare search.
- [ ] The dict is populated from real world data (from the Week 10 list or
      equivalent), not a hardcoded literal.
- [ ] At least one lookup is demonstrated returning a real result.

## Decide/Compare #1 (separately graded — see `judgment_toolkit.md` §3)

Before you build the lookup above, **commit to your data-structure choice
first, in writing, then compare it against at least one real alternative.**
Example prompts:

- Why a `dict` here and not a `list` you search each time?
- Would a `set` fit better for anything else in your world right now (e.g.,
  tracking which entities have already been processed this "day")? Why or
  why not?

**What makes this pass:** the comparison names a real trade-off (lookup
speed vs. insertion order, memory, code complexity) specific to *your*
world's actual data — not a generic "dicts are faster" restatement. The
choice should visibly follow from the comparison, not precede it
cosmetically (don't write the code first and rationalize afterward).

## Then: open continuation (light Build, holistic)

## World Bible

One line: what gate you passed, what broke. Also log your Decide/Compare
choice and rationale here — it's part of your Judgment Log.

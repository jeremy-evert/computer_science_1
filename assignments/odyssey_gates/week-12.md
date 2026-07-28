# Odyssey Gate — Week 12: The world becomes real things (Round 1)

**Concept:** classes, objects, modules — Round 1 (`lessons/08-classes-and-modules.md`).
**Arc:** 3 — Systems That Remember Themselves. **Instrument:** Quick Check
(pass/fail) — see `docs/curriculum/judgment_toolkit.md` §1.

This is the start of the deliberate refactor: the major noun you've been
tracking as dict/list entries since Week 10-11 becomes a real class. Full
reckoning (multiple classes interacting) is Week 13; this gate only asks
for the first one.

## The gate (do this first)

Turn **at least one major noun** already tracked in your Week 10-11
collection into a class, with a constructor (`__init__`) that sets real
instance attributes, and at least one method beyond `__init__`.

## Quick Check (pass/fail)

- [ ] A class is defined with `__init__` setting ≥1 real instance
      attribute (not an empty shell class).
- [ ] At least one method beyond `__init__` exists and does something with
      `self`'s state (not a static/unrelated helper).
- [ ] At least one instance is created and its method called, replacing (or
      alongside, mid-refactor) the old dict/list-entry representation.

## Suggested textbook problem (optional scaffolding)

The general problem: turn one entity from your Week 10–11 dict/list into a
class with `__init__` setting at least one real attribute, plus one method
beyond `__init__` that does something with that attribute.

- **Frontier Settlement:** `class Colonist:` — `__init__(self, name,
  role)`; `def status(self):` returns a sentence using `self.role`.
- **Investigation Bureau:** `class Suspect:` — `__init__(self, name,
  alibi)`; `def summary(self):` returns a one-line case note.
- **Starship Log:** `class CrewMember:` — `__init__(self, name, role)`;
  `def report(self):` returns a status line.
- **Small Business:** `class Customer:` — `__init__(self, name,
  balance)`; `def account_status(self):` returns a label based on
  `self.balance`.

Do this version directly if it helps, then let it *be* your gate
submission — you don't need a second, different one.

## Then: open continuation (light Build, holistic)

## World Bible

One line: what gate you passed, what broke — refactors into classes tend to
surface real bugs from the dict/list version; that's expected, log it.

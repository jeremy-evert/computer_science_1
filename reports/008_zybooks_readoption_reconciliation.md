# Report 008 — CS1 ZyBooks re-adoption reconciliation (prompt 049)

## What was confirmed

Jeremy supplied CS1's exact current ZyBooks adoption directly (2026-08-11,
pasted verbatim from his instructor "About this material" page):

- **Product:** custom zyBook "COMSC 1033: Computer Science I," built from
  2 zyBook titles, zyLabs enabled.
- **ISBN:** 979-8-203-33060-4
- **URL:** `https://learn.zybooks.com/zybook/SWOSUCOMSC1033Fall2026`
  (identifier `SWOSUCOMSC1033Fall2026`)
- **Current release:** September 2025, intended for class use starting
  January 2026 — current as adopted for Fall 2026.
- **Full TOC:** 33 top-level chapters — a 16-chapter core teaching
  sequence (Introduction to Python → Searching and Sorting Algorithms),
  followed by 14 "Additional Labs" chapters paired to the core 16 (plus
  one extra, "One Large Program"), then Python for Data Science, Coding
  Practice Problems, and (new for this release) Artificial Intelligence.

`computer_science_1/course_metadata.yaml`'s `textbook` block is now
populated with this real data, matching the schema Architecture's
`EvertCOD(MIPS)Jul2021` entry uses.

## Reconciliation against existing Deitel-cited curriculum

Not deleted or rewritten, per prompt 049's rule. Compared existing
`planning/week-NN.md` chapter citations against the real adoption's TOC:

- **Core chapters 1, 2, 5, 6, 7, 8, 9 all match** the existing week
  citations' chapter numbers already in `planning/week-NN.md`.
- **One real mismatch found and surfaced, not silently fixed:**
  `planning/week-03.md` cites "chapter 3's branching concept," but in the
  real adoption Chapter 3 is "Types" and Branching is Chapter 4.
  `planning/week-04.md` already correctly cites "chapter 4['s] ...
  branching." Root cause: the internal lesson-file numbering
  (`lessons/02-variables-expressions-types.md`) bundles the real
  adoption's Ch 2 and Ch 3 into one lesson, so lesson numbers `03`
  onward sit one behind the real chapter numbers they describe. This is
  a one-line citation-text bug in `week-03.md`, not a content bug — left
  for Jeremy to confirm/fix per prompt 049's rule against rewriting
  existing planning content unilaterally.
- **Four core chapters have no existing week citation at all:**
  Exceptions (Ch 10), Files (Ch 12), Inheritance (Ch 13), Recursion
  (Ch 14). Two more (Plotting Ch 15, Searching/Sorting Ch 16) also have no
  citation and may be intentionally CS2-level rather than CS1 gaps.
- Full chapter-by-chapter table, the Week 3 mismatch writeup, and six
  open decision points for Jeremy are in
  `planning/zybooks-assignment-map.md`.

## What's still unknown / open for Jeremy

1. Whether to fix `week-03.md`'s citation (recommended: "chapter 3" →
   "chapter 4").
2. Whether Ch 10/12/13/14 get folded into the 16-week plan or are
   deliberately out of scope for CS1.
3. Whether Ch 15 (Plotting) / Ch 16 (Searching and Sorting) are in scope.
4. Whether Ch 33 (Artificial Intelligence, new to this release)
   supplements or overlaps CS1's existing `ai_fluency/ai_i/` Lens strand.
5. Whether Ch 32 (Coding Practice Problems) is the "chapter problem set"
   the odyssey-gate files already gesture at as not-yet-assigned.
6. Real point values / Pt 1-Pt 2 splits for eventual graded assignments —
   not assumed to carry the Fall 2025 archive's older-edition shape.

## What was NOT done (by design, per prompt 049's rules)

- No live ZyBooks, Canvas, or Savnac writes.
- No assignments created anywhere.
- No existing Deitel-cited `planning/week-NN.md`, `docs/syllabus.md`, or
  Coding Odyssey assignment content deleted or rewritten (including the
  Week 3 mismatch — flagged, not auto-fixed).

## Deliverables

- `computer_science_1/course_metadata.yaml` — `textbook` block populated
  with real, Jeremy-confirmed facts.
- `computer_science_1/planning/zybooks-assignment-map.md` — full TOC
  reconciliation table, the confirmed Week 3 mismatch, and a draft target
  assignment list for Ch 1–16.
- This report.

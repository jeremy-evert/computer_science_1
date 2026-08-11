# CS1 ZyBooks assignment map — Fall 2026 (draft, prompt 049)

Target list for the ZyBooks-graded-practice layer being added back on top
of the existing Deitel-cited Coding Odyssey curriculum, per Jeremy's
2026-08-11 ZyBooks-first call. Sourced from the real, current adoption
(`course_metadata.yaml` `textbook` block — `SWOSUCOMSC1033Fall2026`,
ISBN 979-8-203-33060-4, current release September 2025), **not** assumed
identical to the Fall 2025 Canvas archive shape
(`Ch 01`..`Ch 09 Pt 2`, ~100 pts each — see
`jeremy_task_tracking/reports/2026-08-11_zybooks_lti_real_integration_options.md`).
This is planning only — nothing here has been created in Canvas, Savnac,
or ZyBooks. Creation is gated on `prompts/050_savnac_public_https_edge.md`
and a ZyBooks LTI registration for Savnac's domain
(`prompts/051_savnac_zybooks_lti_registration_pilot.md`), or on doing this
directly against real SWOSU Canvas per Jeremy's stated sequencing.

## What changed vs. the Fall 2025 archive template

The Fall 2025 archive's `Ch 01`–`Ch 09 Pt 2` (9 chapters, some split into
Pt 1/Pt 2, ~100 pts each) mapped to an older "Programming in Python 3"
edition. The current adoption is a different, combined custom zyBook
("built from 2 zyBook titles") with **33** top-level chapters, of which
**16** are the core teaching sequence (Ch 1–16), plus 17 more chapters of
additional-labs/data-science/practice-problems/AI material (Ch 17–33).
The old 9-chapter split does not carry over cleanly — the real adoption
has roughly double the core teaching chapters. Treat the table below, not
the archive's 9-item list, as the current target.

## Core ZyBooks chapters (1–16) vs. CS1's existing lecture sequence

| ZyBooks Ch | ZyBooks title | Existing internal lesson | Existing week(s) citing it | Alignment |
|--|---|---|---|---|
| 1 | Introduction to Python | `lessons/01-*` (implied, L01 "Foundations") | Week 1 | Matches — no numeric citation conflict (Week 1 doesn't cite a chapter number) |
| 2 | Variables and Expressions | `lessons/02-variables-expressions-types.md` | Week 2 ("chapters 1–2's variables") | Matches |
| 3 | Types | `lessons/02-variables-expressions-types.md` (combined with Ch 2 above) | Week 2/3 (no explicit "chapter 3 = types" citation exists) | **Combined, not split** — see mismatch below |
| 4 | Branching | `lessons/03-branching.md` | Week 3 says **"chapter 3's branching concept"**; Week 4 says "chapter 4's ... branching" | **Mismatch — see below** |
| 5 | Loops | `lessons/04-loops.md` | Week 5 "chapter 5's loops", Week 6 "chapter 5's loops" | Matches (real Ch 5 = Loops) |
| 6 | Functions | `lessons/05-functions.md` | Week 6 "chapter 6 practice begins Week 7", Week 7 "chapter 6's functions" | Matches (real Ch 6 = Functions) |
| 7 | Strings | `lessons/06-strings.md` | Week 8 "chapter 7's string", Week 9 (strings continued) | Matches (real Ch 7 = Strings) |
| 8 | Lists and Dictionaries | `lessons/07-collections.md` | Week 10 "chapter 8's lists", Week 11 "chapter 8's dictionaries" | Matches (real Ch 8 = Lists and Dictionaries, combined — matches internal combining lists+dicts into one lesson too) |
| 9 | Classes | `lessons/08-classes-and-modules.md` | Week 12/13 "chapter 9 Round 1/2" classes | Matches for classes; internal lesson also bundles Modules (real Ch 11) into the same lesson file — not a numbering conflict since Week 12/13 only ever cite "chapter 9" |
| 10 | Exceptions | *(not explicitly cited anywhere in `planning/week-*.md`)* | — | Gap — no existing week names Exceptions/Ch 10 |
| 11 | Modules | `lessons/08-classes-and-modules.md` (bundled with Ch 9 above) | Week 12/13 (implicitly, via lesson file, not by chapter number) | No numeric citation exists to conflict — bundled at the lesson-file level only |
| 12 | Files | *(not explicitly cited)* | — | Gap |
| 13 | Inheritance | *(not explicitly cited)* | — | Gap |
| 14 | Recursion | *(not explicitly cited)* | — | Gap |
| 15 | Plotting | *(not explicitly cited)* | — | Gap — likely intentionally out of scope for CS1 (Plotting is often a CS2/data-science topic) |
| 16 | Searching and Sorting Algorithms | *(not explicitly cited)* | — | Gap — likely intentionally out of scope for CS1 (typically a CS2-level topic) |

## Confirmed mismatch: Week 3's "chapter 3" citation

`planning/week-03.md` (line 22) says the Week 3 Coding Odyssey gate should
"apply chapter 3's branching concept" — but in the real, current adoption,
**Chapter 3 is "Types," not "Branching."** Branching is **Chapter 4**.
`planning/week-04.md` (line 23) independently and correctly says
"chapter 4's full branching/decision-making depth," which is consistent
with the real TOC.

Root cause: the existing internal lesson numbering
(`lessons/02-variables-expressions-types.md`) combines the real
adoption's Ch 2 (Variables and Expressions) and Ch 3 (Types) into a single
lesson file, then resumes 1:1 with `lessons/03-branching.md`. That
lesson-file numbering was evidently built assuming a 2-chapter-shorter
TOC than the one actually adopted, so every internal lesson number from
`03` onward sits one behind the real ZyBooks chapter number it's meant to
correspond to (lesson `03` = real Ch 4, lesson `04` = real Ch 5, etc. —
confirmed consistent through `lessons/07-collections.md` = real Ch 8).

This is a **citation-text bug, not a curriculum-content bug**: the actual
teaching content in `lessons/03-branching.md` is branching, matching real
Ch 4, and `week-04.md`'s citation is already correct. Only `week-03.md`'s
prose ("chapter 3's branching concept") is wrong — it should say
**"chapter 4's branching concept"**, or better, stop citing a bare chapter
number where it can drift and instead cite the lesson file name (as most
other weeks already do) plus the confirmed real chapter number.

**Not fixed in this pass** — prompt 049's rules say do not rewrite
existing Deitel-cited planning content; this is flagged here for Jeremy's
call, not silently corrected. Recommended fix scope: one line in
`week-03.md`.

## Chapters 17–33: extra inventory, not mapped to any week

Chapters 17 (Additional Material), 18–30 (Additional Labs, chapter-paired
with 1–16... note 30 is "One Large Program," an extra capstone-labs
chapter with no single paired core chapter), 31 (Python for Data
Science), 32 (Coding Practice Problems), and 33 (Artificial Intelligence)
are real content in the adoption but are not assumed to map onto any
existing CS1 week. Two are worth flagging for Jeremy specifically:

- **Ch 33 (Artificial Intelligence)** — CS1 already has a full AI-fluency
  strand (`ai_fluency/ai_i/`, 16 Lenses, Monday Moments in
  `planning/block-map.md`). Whether Ch 33 supplements, duplicates, or is
  simply skipped relative to that existing strand is worth a direct call
  from Jeremy rather than assuming either way.
- **Ch 32 (Coding Practice Problems)** — could plausibly serve as the
  "chapter problem set" the weekly gate files (`assignments/odyssey_
  gates/week-NN.md`) already gesture at ("no separate chapter problem set
  is due" appears repeatedly, implying one was originally planned) — worth
  confirming with Jeremy whether this closes that gap.

## Draft target assignment list (core Ch 1–16 only, for now)

Following the Fall 2025 archive's proven *shape* (one graded ZyBooks
assignment per chapter, ~100 pts each) as a starting template only — not
a guarantee the point value or Pt 1/Pt 2 split still applies to this
adoption's chapter content or length:

| Assignment (draft) | ZyBooks Ch | Target week |
|---|--|--|
| Ch 01 — Introduction to Python | 1 | Week 1 |
| Ch 02 — Variables and Expressions | 2 | Week 2 |
| Ch 03 — Types | 3 | Week 3 |
| Ch 04 — Branching | 4 | Week 4 |
| Ch 05 — Loops | 5 | Week 5–6 |
| Ch 06 — Functions | 6 | Week 7 |
| Ch 07 — Strings | 7 | Week 8–9 |
| Ch 08 — Lists and Dictionaries | 8 | Week 10–11 |
| Ch 09 — Classes | 9 | Week 12–13 |
| Ch 10 — Exceptions | 10 | *unassigned — gap, see above* |
| Ch 11 — Modules | 11 | Week 12–13 (bundled with Classes lesson) |
| Ch 12 — Files | 12 | *unassigned — gap* |
| Ch 13 — Inheritance | 13 | *unassigned — gap* |
| Ch 14 — Recursion | 14 | *unassigned — gap* |
| Ch 15 — Plotting | 15 | *out of scope? confirm with Jeremy* |
| Ch 16 — Searching and Sorting Algorithms | 16 | *out of scope? confirm with Jeremy* |

Chapters 10, 12, 13, 14 are real core content with no assigned week in
the current 16-week plan — either the plan needs to make room for them,
or Jeremy should confirm they're intentionally deferred/out of scope for
a CS1 (vs. CS2) offering.

## Open items for Jeremy

1. Confirm/correct the `week-03.md` "chapter 3" → "chapter 4" citation
   fix described above.
2. Decide whether Ch 10 (Exceptions), 12 (Files), 13 (Inheritance), 14
   (Recursion) get folded into the existing 16-week plan, or stay
   deliberately out of scope for CS1 (some may be more natural at the CS2
   level).
3. Decide whether Ch 15 (Plotting) and Ch 16 (Searching and Sorting
   Algorithms) are in scope for CS1 at all.
4. Decide how/whether Ch 33 (Artificial Intelligence) relates to the
   existing `ai_fluency/ai_i/` Lens strand.
5. Decide whether Ch 32 (Coding Practice Problems) is the "chapter
   problem set" the odyssey-gate files already reference as not-yet-due.
6. Confirm point values / Pt 1-Pt 2 splitting once ready to build real
   assignments — not assumed to carry over from the Fall 2025 archive's
   older-edition shape.

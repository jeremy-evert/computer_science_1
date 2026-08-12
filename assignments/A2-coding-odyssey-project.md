# Coding Odyssey / Choose Your Own Adventure

## Purpose

One persistent, student-chosen project that runs the whole semester and
applies each week's concepts as they're taught. As of the 2026-07-24 pivot,
reconciled 2026-07-27, this is the spine of the course: every technical
week's textbook chapter gets applied here, inside the student's own world,
rather than through a separate standalone problem set. See the Design
history section at the bottom for why.

**This is the weekly coding practice assignment.** Each gate below also
fulfills `assignments/A1-weekly-coding-practice.md` for that week — they
are not two separate things to submit.

## Do

1. **Week 2:** pick one of the four genres below and write a one-paragraph
   founding charter — what the world is, who's in it, what's at stake. This
   starts your World Bible (below) and is your first Judgment Log
   checkpoint.
2. **Weeks with a gate (2–5, 7–8, 10–13):** pass that week's small Quick
   Check gate first, then keep extending your world for the rest of the
   week with anything covered so far. Each week's specific, small
   requirement is its own file: `assignments/odyssey_gates/week-NN.md`
   (rubric: `rubrics/odyssey_gates/week-NN_rubric.md`). If you'd rather
   start from a concrete example than invent your own scenario, each of
   these files also includes an optional **suggested textbook problem** —
   the same concept as a plain practice problem, with one version per
   genre.
3. **Checkpoints (Weeks 6, 9, 14):** submit a working version, explain
   in your own words what changed, and demonstrate it. Table below; full
   grading criteria in that week's own gate file.
4. **Week 17 (finals):** submit the final portfolio version — playable or
   usable, clear enough for someone else to try — with a final reflection.
5. Keep your World Bible current every week (below). It's graded evidence,
   not optional bookkeeping.

## The genre menu — pick once, Week 2, keep all semester

- **The Frontier Settlement** — manage colonists, resources, events.
- **The Investigation Bureau** — a detective case-file engine (strongest
  fit if you want to try the optional text-analysis side-quest at Week 15).
- **The Starship Log** — crew and exploration management.
- **The Small Business** — inventory, customers, transactions.

Bounded on purpose — four options, not open worldbuilding — so genre-based
peer grouping and grading stay tractable across roughly 30 different worlds.
Whichever you pick must be able to support, by the Week 13–17 capstone: a
collection of things, text data, a save/load state, **meaningful
classes/objects whose state and behavior contribute to the program,
including at least one meaningful interaction between objects** (not
inheritance/class hierarchies — see the C08 note below), and a numeric
feature.

**Reconciled 2026-08-12:** inheritance/class hierarchies are not CS1 core
and are not required for full credit. An earlier version of this
requirement said "at least one class hierarchy" — that was stale wording
that never matched the pinned C08 capability (meaningful class/object
modeling: state, behavior, methods, and interaction among objects).
Inheritance may still appear as optional enrichment/comparison where
already pedagogically useful (e.g. the Week 13 Decide/Compare discussion of
composition vs. inheritance), but it is never required.

## The four checkpoints

| Checkpoint | Week | What it is |
|---|---|---|
| 1 | 6 | "Baby project" dry run — small, complete, low-stakes, using only what's been taught through loops. Rehearses submit/explain/demonstrate before the real project ramps up; a few dozen lines is a completely acceptable baby project. |
| 2 | 9 | First real pass on the actual project — a real idea, meaningfully more code, closer to eventual scope. |
| 3 | 14 | Expanded pass, paired with GitHub/tools work and a mandatory Full Trail Debrief — see `assignments/odyssey_gates/week-14.md`. Substantial building already culminates the prior week (13), including capstone Decide/Compare #2 — this checkpoint is a receipt on that real code, not a new feature deadline. |

**Reconciled 2026-08-12: Checkpoint 4 is retired.** It previously sat at
Week 16 as a "final creative-project pass," but Week 16 is now the shared
Farkle/ML fun week and must not compete with a giant Odyssey deadline. The
capstone Decide/Compare (formerly paired with Checkpoint 4) moved to Week
13 alongside the real build culmination — see
`assignments/odyssey_gates/week-13.md`. The final Coding Odyssey portfolio
submission is still due Week 17 (finals week), but as evidence/receipt of
the finished journey alongside the Final Debrief and final reflection, not
another large technical performance — see `planning/week-17-finals.md` and
`assignments/A5-final-reflection.md`.

## Weekly gates

Starting Week 2, most weeks add a small pass/fail Quick Check tied to that
week's new concept — the smallest proof the concept was actually used, not
a full spec. If a gate takes more than a couple of sentences to state,
you've overbuilt it; that's true of the *assignment*, not just the code.
Full week-by-week map, including which weeks route through mechanical
checking versus a human/frontier-agent read: `planning/coding-odyssey-arc-map.md`.

## The World Bible

Keep a living document — your own miniature project roadmap:

- Your founding charter (from Week 2).
- Current state of the world.
- One line per week: what gate you passed, what broke.
- A running "known debt" list.

This is normal project record-keeping, not extra work layered on top of the
gates. It's reviewed as your **Judgment Log** at three points: Week 2 (the
charter exists), mid-semester (each Debrief draws on it), and Week 17 (the
whole log, reviewed as a record of judgment over the semester). See
`docs/curriculum/judgment_toolkit.md` §5.

## Decide/Compare moments

Twice a semester, commit to a real design choice in writing *before*
comparing it against a real alternative, then defend it — the choice should
visibly follow from the comparison, not precede it cosmetically:

- **Week 11** — a data-structure choice for something in your world.
- **Week 13** — a capstone-scale choice for the whole project (**moved
  2026-08-12** from Week 16, which is now the Farkle/ML fun week).

Full instrument definition: `docs/curriculum/judgment_toolkit.md` §3; each
week's specifics: that week's own gate file.

## Optional bonus practice (standalone problems)

Coding Odyssey remains the required, sufficient technical practice path —
you never need anything beyond the gates/checkpoints above to complete the
course. If you *want* extra reps, optional standalone programming problems
(instructor-owned, or selected CS50P problems that align with what's
already been taught, or other vetted open exercises) are available for
additive bonus/extra credit — see `assignments/A1-weekly-coding-practice.md`
for the policy. Skipping them never reduces your base grade.

## Grading

Each gate and checkpoint is graded from its own paired files —
`assignments/odyssey_gates/week-NN.md` and
`rubrics/odyssey_gates/week-NN_rubric.md` — using the five instruments
(Quick Check, Build, Decide/Compare, Debrief, Judgment Log) defined in full
in `docs/curriculum/judgment_toolkit.md`. Point values and the exact Canvas
weighting are not yet finalized — see that document's open items.

## Design history

Kept for provenance; none of this is needed to complete the assignment.

- Historically this project appears as CYOAG or Coding Odyssey 1–3 plus a
  final, graded on creativity, clarity, effort, playability, and
  presentation, with occasional bonus points for language/IDE/engine choice,
  sprites, or extra features.
- **2026-07-22:** added a fourth, earlier checkpoint (the Week 6 "baby
  project" dry run) ahead of the historical three-checkpoint pattern, so the
  first real project checkpoint (now Week 9) isn't also the first time a
  student handles submission mechanics. See
  `reports/007_coding_odyssey_baby_project_checkpoint.md`.
- **2026-07-24:** pivoted this project from an occasional checkpoint into
  the spine of the whole course — added the bounded genre menu, weekly
  gates, and the World Bible-as-Judgment-Log framing. Full rationale:
  `jeremy_task_tracking/DECISIONS.md`'s 2026-07-24 entry and
  `docs/curriculum/judgment_toolkit.md`. This is also the point where
  per-week gate assignments and rubrics (referenced above) were actually
  written — earlier drafts of this file said that work was "not yet done."
- **2026-07-27:** closed the gap the 2026-07-24 pivot left open —
  `assignments/A1-weekly-coding-practice.md`, `docs/course-ethos.md`,
  `docs/grading-model.md`, and most of `planning/week-NN.md` still described
  or linked a separate chapter-problem-set assignment running alongside
  the gates. Reconciled all of them: the weekly reinforcement assignment
  *is* the gate (or checkpoint), full stop, every technical week. The
  textbook stays part of the lecture and conversation; it no longer owns a
  separate weekly deliverable.

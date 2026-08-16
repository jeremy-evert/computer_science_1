# Week 16 — Farkle / Machine Learning fun week (Nov 30–Dec 4)

## Status
**GREEN — canonical shared Farkle + ML consumer validated on April.**

Full week — last full week of instruction before finals.

The Week 16 computational machine is now supplied by the provenance-pinned canonical repository `jeremy-evert/Farkle_and_Machine_Learning`. CS1 keeps its beginner-facing `farkle.cli`, lesson voice, evidence receipt, and classroom interpretation. The migration was validated on April against the same 32 regression tests and bounded CLI smokes used before the ownership change.

## Weekly Focus
**Reconciled 2026-08-12 (Jeremy's pinned decision):** Week 16 is no longer
the old generic final Odyssey creative-pass/show-and-tell/Checkpoint 4
week. It is the shared **Farkle / Machine Learning** applied, playful
capstone experience — it consumes the CS1 core (variables/state,
branching, loops/simulation, functions, collections, objects where useful,
testing/debugging, files/data where useful, Git habits, technical
judgment) rather than expanding the prerequisite core. Students explore
whether a computer can learn or improve a strategy for Farkle: what's the
state, what choices/actions exist, what counts as reward, what happens if
a machine plays many games, does its behavior change, how do its decisions
compare with ours, what evidence says one strategy is better. **No
reinforcement-learning mathematics is required and this is not a formal
ML unit.**

The old Coding Odyssey Checkpoint 4 and Decide/Compare #2 (capstone) are
**retired from this week** — the substantial Odyssey building already
culminated by the end of Week 13, and Decide/Compare #2 (capstone) moved
to Week 13 alongside that build (see `planning/week-13.md`,
`assignments/odyssey_gates/week-13.md`). Students are not asked to
complete a giant final Odyssey event and Farkle/ML at the same time.

**Built 2026-08-12 (prompt 055), hardened and shared-core migrated 2026-08-16:** the Farkle/ML lesson is a real, tested, runnable Week 16 package. Student lesson: `lessons/10-farkle-ml.md`. Instructor guide: `docs/curriculum/week-16-instructor-guide.md`. The stable student command surface remains `lessons/code/farkle/` through `python3 -m farkle.cli ...`; the canonical engine, strategies, transparent learner, and simulation code are synchronized under `lessons/code/farkle_ml/`. Evidence artifact: `assignments/W16-farkle-ml-experiment-receipt.md`. Full original build report: `reports/013_week16_farkle_ml_capstone.md`. Migration report: `sidecar/reports/101_cs1_shared_farkle_migration.md`.

The historical Spring 2026 Farkle/Q-learning assignment (`docs/reports/curriculum-history-synthesis.md`; the real Canvas snapshot at `archive/spring-2026/canvas-71244-snapshot-20260714-194807.json`) supplied the state/action/reward framing — (turn_points, dice_remaining) state, ROLL/BANK action — but the learning mechanism remains ruthlessly simple: a running-average dictionary, not formal Q-learning with a discount factor.

**Decision, 2026-07-22** (`reports/005_apply_pre_semester_decisions.md`, still standing): the professional-pathway artifact set does not land here — it's staged across the semester (Week 1 baseline, Week 14 update, Week 15 completion/submission).

## Monday — Nov 30 — Monday Moments
**AI I Lens 16: Reflect and Improve** — How has my thinking changed because of this course?

Technical tie-in: watching a machine's Farkle strategy change with repeated play is a concrete, playful instance of the same "does behavior change with feedback" question the lens asks about AI systems generally.

## Wednesday — Dec 2 — Wacky Wednesday
**Professional Minds Week 16** — Book: *Generative AI Design Patterns* — Question: What kind of professional do I want to become?

Farkle/ML applied session: state, actions, and reward for a simple game.

## Friday — Dec 4 — Fun Friday
**Professional Minds Week 16** — Book: *Semester Reflection* — Question: What kind of professional do I want to become?

Farkle/ML applied session continues; share-out of what changed as a strategy played more games. Optionally pair with a brief AI Fluency 1 reflection on how the student's thinking/verification habits changed over the course, if it strengthens rather than pads the final reflection (`assignments/A5-final-reflection.md`, which begins this week).

## Due this week
Farkle/ML applied session participation — no Coding Odyssey checkpoint or gate is due this week (retired; see above). Start of final reflection (`assignments/A5-final-reflection.md`). The professional-pathway artifact set (`assignments/A6-professional-pathway-artifacts.md`) is **not** due this week — it was submitted in Week 15.

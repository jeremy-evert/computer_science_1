# Report 013 — CS1 Week 16 Farkle / Machine Learning capstone

**Prompt:** `jeremy_task_tracking/prompts/055_cs1_week16_farkle_ml_capstone.md`
**Scope:** Fall 2026 COMSC 1033 (CS1) Week 16 only. CS1-only — no CS2,
Savnac, Canvas, or `machine_learning` repo changes.
**Date:** 2026-08-12.

## 0. What this report is answering

Prompt 055 asked for a real, tested, teachable Week 16 Farkle/ML
experience — not a design outline — plus reconciliation of stale
Week 16 checkpoint language in the grading model. Both are done. Details
below.

---

## 1. Historical material discovered and reused

- **Real Spring 2026 Canvas assignment**, found in
  `archive/spring-2026/canvas-71244-snapshot-20260714-194807.json`
  (search: `Farkle`): "Coding Odyssey 4 (0 points) — Farkle + Q-Learning
  (Get-It-Working Version)." State = `(turn_points, dice_remaining)`,
  action = ROLL or BANK, reward = `+turn_points` on bank, `-turn_points`
  (or a fixed penalty) on Farkle. This is the direct ancestor of this
  week's design — CS1's `ExperienceTable` keeps the same state and action
  shape almost verbatim, deliberately, because it was already
  well-matched to CS1 scope.
- **`docs/reports/curriculum-history-synthesis.md`** confirmed Spring
  2026 treated Farkle/Q-learning as a zero-point, "get it working"
  optional practice item, not a heavily graded capstone — consistent
  with this week staying light.
- **`jeremy_task_tracking/codex_prompts/shared_021_farkle_ml_week16_design_and_build.md`**
  — a prior, broader prompt that designed a shared CS1+CS2 Farkle/ML
  package to live in a `machine_learning` repo (decision trees,
  scikit-learn, visualization/storytelling, CS1+CS2 lanes). Checked: it
  was **never executed** — `machine_learning` contains no Farkle content
  (confirmed via `git log` and a repo-wide grep). Prompt 055 is CS1-only
  and explicitly says not to inherit complexity just because it exists;
  this build does not depend on or block that shared-package idea. Noted
  in the CS2 handoff (`docs/curriculum/cs2-farkle-ml-handoff.md`) as an
  open question for whoever picks up CS2's Week 16, rather than assumed.
- `reports/012_pre_savnac_source_reconciliation.md` (2026-08-12,
  same day) had already retired the old Checkpoint 4 / Decide-Compare #2
  from Week 16 and rewritten `planning/week-16.md`,
  `assignments/odyssey_gates/week-16.md`, and
  `rubrics/odyssey_gates/week-16_rubric.md` to describe Week 16 as the
  Farkle/ML fun week with no Odyssey gate — but explicitly flagged actual
  lesson content as a follow-up authoring task (report 012, item E.2).
  This report closes that follow-up.
- No scikit-learn, matplotlib, or numpy dependency was needed or used —
  Python's standard library only (`random`, `json`, `argparse`).
  Environment check: Python 3.9.21, `pytest` 8.4.2 and `numpy` 2.0.2
  already available in the environment, but neither numpy nor any
  third-party package is imported by any file in this build.

---

## 2. Final CS1 learning goals

By the end of Week 16, a student should be able to:

1. Explain Farkle's core risk/reward tension (bank vs. roll again) and
   have played it enough to have an opinion about strategy.
2. Name **state**, **action**, and **reward/outcome** in a decision they
   already understand, and recognize those words in real Python (a
   dictionary, a string, a running average).
3. Read and run a small, transparent "experience table" learner and
   explain in plain language why its printed preferences make sense
   (e.g., "cautious with few dice left, bold right after hot dice").
4. Compare a human-authored strategy to the learned strategy using
   evidence from thousands of simulated games — win rate, average score,
   Farkle rate — evaluated on fresh games the learner did not train on.
5. Answer the closing judgment questions: is "different" the same as
   "better," what evidence would be convincing, what does the machine
   still not account for.

No RL math, no neural networks, no gradient descent, no formal MDP
language, no inheritance-heavy design. See §8 and the CS2 handoff for
what was deliberately left out.

---

## 3. Exact Farkle rule variant chosen

Documented identically in `lessons/code/farkle/engine.py`'s module
docstring and `lessons/10-farkle-ml.md` §1 (word-for-word intent, not
copy-pasted, so each stands alone):

- Six dice. Single 1 = 100, single 5 = 50.
- Three of a kind: three 1s = 1000; three of value V = V × 100.
- Four/five/six of a kind: doubles the three-of-a-kind value per extra
  matching die (4-kind = 2×, 5-kind = 4×, 6-kind = 8×). One documented,
  simple, testable variant among several real-world house-rule options —
  chosen for a single unambiguous rule, not because it's the only valid
  one.
- **No straights, no three-pairs bonus** (deliberately excluded to keep
  `score_roll` small enough for a CS1 student to hand-trace).
- No scoring dice on a roll = Farkle: turn ends, turn score lost.
- Hot dice (all rolled dice scored) = reroll all six, keep turn score.
- Dice selection is automatic (engine always keeps every scoring die from
  a roll) — the only decision exposed to a strategy is ROLL vs. BANK,
  matching the historical assignment's state/action shape.
- Target score: **4000** (not the traditional 10,000), chosen so a
  simulation of thousands of games finishes in well under a second — a
  documented classroom simplification, not an error.
- No "final round" rule for the trailing player — the game ends the
  instant the target is reached. Documented simplification for easier
  hand-tracing.

---

## 4. Architecture, in plain language

`lessons/code/farkle/` — five small files, one responsibility each:

- **`engine.py`** — dice rolling with an injected `random.Random`
  (reproducibility), `score_roll()` (pure function, dice list in, points
  and dice-used out), `take_turn()` (the roll/bank loop, calls a
  strategy function every decision point, optionally records a
  human-readable trace).
- **`strategies.py`** — hand-written strategies as small functions:
  `bank_at(threshold)`, `cautious_near_target(...)`,
  `aggressive_when_behind(...)`, `always_bank_first_score`. Each has a
  one-line plain-English `.description` attribute students can print.
- **`learner.py`** — `ExperienceTable`: a dictionary keyed by
  `((turn_score_bucket, dice_remaining), action)` mapping to a running
  average of what happened. The whole update rule is one line
  (`average += (outcome - average) / count`) — a Monte-Carlo-style
  running average, not real Q-learning (no bootstrapping, no discount
  factor). Every decision made during a training turn is credited/blamed
  with that turn's single final result — a deliberate simplification
  over proper per-step reinforcement-learning credit assignment, named
  explicitly as such in the module docstring and in the CS2 handoff.
  `epsilon`-greedy exploration during training; greedy (`explore=False`)
  once trained. `save()`/`load()` round-trip to small JSON.
- **`simulate.py`** — `play_game()` (one two-player game to the target
  score), `run_many_games()` (aggregate win rate / avg score / Farkle
  rate / avg turns over N games from one seed), `format_comparison()`
  (readable text report).
- **`cli.py`** — the runnable entry point: `play`, `compare`, `train`,
  `learn-vs-baseline` subcommands, all seed-driven.

State is always a plain dictionary (`engine.build_state`), never a
custom class — dictionaries were chosen deliberately over a class/
dataclass so the "state" concept stays keyed to the collections unit
students already have, rather than introducing new class syntax to
describe it.

---

## 5. Files created / changed

**New (runnable code + tests):**
- `lessons/code/farkle/__init__.py`
- `lessons/code/farkle/engine.py`
- `lessons/code/farkle/strategies.py`
- `lessons/code/farkle/learner.py`
- `lessons/code/farkle/simulate.py`
- `lessons/code/farkle/cli.py`
- `lessons/code/farkle/sample_output/trained_table_seed1.json` (12 KB
  fixture — the exact table quoted in §7, generated by
  `train --seed 1 --turns 20000 --save ...`, kept as a fallback for the
  instructor guide's "learner behaves oddly" contingency)
- `tests/test_farkle_engine.py` (16 tests)
- `tests/test_farkle_learner.py` (11 tests)

**New (lesson/instructional content):**
- `lessons/10-farkle-ml.md` — student-facing lesson (rules, state/
  action/reward, experiment sequence, interpretation questions)
- `docs/curriculum/week-16-instructor-guide.md` — Wednesday/Friday
  classroom flow, likely confusions, fallback for a bad live demo seed
- `assignments/W16-farkle-ml-experiment-receipt.md` — the light evidence
  artifact
- `docs/curriculum/cs2-farkle-ml-handoff.md` — 10 numbered future-CS2
  extensions, explicitly not implemented here

**Changed (grading/source reconciliation, §6):**
- `docs/grading-model.md`
- `assignments/A2-coding-odyssey-project.md`
- `docs/curriculum/judgment_toolkit.md`
- `planning/coding-odyssey-arc-map.md`
- `planning/week-16.md` (pointed at the new content; the follow-up-task
  language from report 012 is now resolved)
- `assignments/odyssey_gates/week-16.md` (pointed at the new evidence
  artifact instead of "follow-up authoring task")

---

## 6. Grading-model reconciliation performed

Prompt 055 named one known seam: `docs/grading-model.md` still described
Week 16 as hosting Coding Odyssey Checkpoint 4 / a fourth Full Build
checkpoint, even though `reports/012` had already retired that event.
Grepping confirmed the drift was **wider than the one file named** — the
same stale "4 checkpoints including Week 16" pattern was present in three
more active-source files that all needed to agree with each other:

| File | What was stale | Fix |
|---|---|---|
| `docs/grading-model.md` (row) | "4 checkpoints (Wk 6/9/14/16)" | "3 checkpoints (Wk 6/9/14)" + inline reconciliation note |
| `docs/grading-model.md` (Axis 1 prose) | "checkpoint weeks (6, 9, 14, 16)" | "checkpoint weeks (6, 9, 14)" |
| `assignments/A2-coding-odyssey-project.md` | "Checkpoints (Weeks 6, 9, 14, 16)" | "Checkpoints (Weeks 6, 9, 14)" (the table two lines below this sentence already correctly listed only 3) |
| `docs/curriculum/judgment_toolkit.md` (instrument table) | "4 arc closes... Checkpoints 1-4" | "3 arc closes... Checkpoints 1-3" |
| `docs/curriculum/judgment_toolkit.md` (Build section) | "Checkpoints 2-4 and the Week 17 final" | "Checkpoints 2-3 and the Week 17 final" |
| `planning/coding-odyssey-arc-map.md` | "four Checkpoints (Wk 6/9/14/16)" in the arc-boundary rationale paragraph | "three Checkpoints (Wk 6/9/14)" + inline note |

All six were genuinely contradicted by other text in the *same files*
(e.g. `judgment_toolkit.md`'s own §4 already said "Checkpoint 4...is
retired" two sections below the stale table row) — this was not a new
design decision, just finishing a rename that report 012 started but
didn't sweep completely.

**No new numeric value was invented.** Per the prompt's explicit
constraint, this task did not touch the standing open items in
`docs/grading-model.md` (optional bonus-practice point value, A4 weight,
drop-lowest policy, submission-location mapping) — those remain exactly
as open as report 012 left them.

**Week 16's light evidence artifact and existing categories.** Added one
short paragraph to `docs/grading-model.md` (not a new table row)
documenting that `assignments/W16-farkle-ml-experiment-receipt.md` is
participation/reflection evidence of the same shape as the existing
weekly Wacky-Wednesday/Fun-Friday/attendance categories — Week 16 already
has both slots scheduled (`planning/week-16.md`) — so no new percentage
row was needed or added. If Jeremy later wants a distinct graded weight
specifically for this receipt, that is flagged as his decision, not made
here.

**Verification that no active source resurrects a retired Week 16
event:** grepped the whole repo (excluding `archive/`) for
`Wk 6/9/14/16`, `Weeks 6, 9, 14, 16`, `checkpoint weeks (6, 9, 14, 16)`,
`4 checkpoints`, `Checkpoints 1-4`, `Checkpoints 2-4`, `Odyssey Checkpoint
4`, and `Decide/Compare #2` after the fixes above. Every remaining hit is
an explicit self-described retirement/move notice (e.g. "Checkpoint 4 is
retired," "Decide/Compare #2...moved to Week 13") — none is an active
requirement. Two historical report files (`reports/007`, `reports/010`)
retain the old language unmodified, correctly, as point-in-time records.

---

## 7. Commands run and sample results

All commands run from `computer_science_1/lessons/code/` unless noted.

### Tests

```
$ PYTHONPATH=lessons/code python3 -m pytest tests/ -v
============================== 27 passed in 0.87s ==============================
```
16 engine tests (every documented scoring rule: single 1/5, three-of-a-
kind for 1s and other values, 4/5/6-of-a-kind doubling, Farkle detection,
mixed triple-plus-leftover-singles, reproducibility under a fixed seed,
never-negative turn results, trace recording, state-dict shape) + 11
learner/simulation tests (table starts empty and grows, training is
reproducible under a fixed seed, greedy action selection is deterministic,
the learner comes to prefer banking at very high turn scores with few
dice left, save/load round-trips exactly, `run_many_games` is
reproducible and its rates sum to 1.0).

### `git diff --check`
```
$ git diff --check
(no output — clean)
```

### Fixed-seed single-turn demo (reproducibility check: ran twice, byte-
identical output both times)
```
$ python3 -m farkle.cli play --seed 1 --strategy bank_at_300
Playing one turn with strategy 'bank_at_300' (Bank once turn score reaches 300, else roll.), seed=1
  rolled [2, 5, 1, 3, 1, 4] -> scores 250 points using 3 of the dice
  turn score now 250, 3 dice left -> strategy says ROLL
  rolled [4, 4, 6] -> scores 0 points using 0 of the dice
  FARKLE -- turn ends, 250 points lost
Turn result: 0 points banked
```

### Baseline-vs-baseline comparison, 5000 games
```
$ python3 -m farkle.cli compare --seed 1 --games 5000 --strategy-a bank_at_300 --strategy-b bank_at_800
5000 games, seed=1
  bank_at_300                  win rate 73.8%   avg score 3952   farkle rate 11.1%
  bank_at_800                  win rate 26.2%   avg score 2761   farkle rate 33.9%
  ties: 0.0%   avg turns/game: 18.4
```
This is a genuinely useful in-class surprise: the intuitive "aggressive
threshold should win more" prediction is wrong here — banking early at
300 wins nearly 3-to-1 because the 800 threshold triples the Farkle rate.

### Learned table, trained on 20,000 solo turns
```
$ python3 -m farkle.cli train --seed 1 --turns 20000 --show-table
Trained on 20000 solo turns (seed=1, epsilon=0.2).
The table has learned about 162 (situation, action) pairs.
```
Selected rows (full table in
`lessons/code/farkle/sample_output/trained_table_seed1.json`):

| turn score | dice left | roll avg (n) | bank avg (n) | prefers |
|---:|---:|---:|---:|---|
| 100 | 4 | 212 (1299) | 100 (190) | roll |
| 300 | 1 | -18 (17) | 300 (159) | bank |
| 500 | 6 | 812 (71) | 500 (9) | roll |
| 700 | 2 | -252 (28) | 700 (231) | bank |
| 1000 | 1 | -413 (50) | 1383 (523) | bank |

This is exactly the interpretable, "makes sense out loud" story Wednesday
wants: the table learns to be cautious with few dice remaining (roll
averages go negative — rolling with 1-2 dice left is genuinely risky) and
bold right after hot dice (`dice left = 6`, roll average consistently
beats bank).

### Learned vs. baseline, on fresh (unseen) games — 5 different seeds
```
$ python3 -m farkle.cli learn-vs-baseline --seed N --turns 20000 --games 3000 --baseline bank_at_300
```
| seed | learned win rate | baseline win rate | learned farkle rate | baseline farkle rate |
|---:|---:|---:|---:|---:|
| 1 | 58.5% | 41.5% | 4.6% | 10.5% |
| 2 | 56.5% | 43.5% | 4.8% | 10.3% |
| 3 | 56.3% | 43.7% | 4.7% | 10.5% |
| 4 | 56.8% | 43.2% | 4.8% | 10.3% |
| 5 | 57.3% | 42.7% | 4.8% | 10.5% |

**This evidence is generated, not universal.** It says: under our
scoring rules, our 4000-point target, and 20,000 training turns, this
particular learned table beat a fixed 300-point threshold in 5/5
independently-seeded evaluation batches, by a stable and non-trivial
margin, primarily by farkling less than half as often. It does not claim
the table is "optimal Farkle play" or generalize beyond this rule
variant — that framing (and what a more rigorous evaluation would look
like) is explicit in the lesson's §7 closing note and interpretation
questions.

### Determinism check
Ran `learn-vs-baseline --seed 1 --turns 20000 --games 5000 --baseline
bank_at_300` twice to separate files and diffed them — byte-identical.
Same for `play --seed 1`.

---

## 8. What was deliberately deferred to CS2

Full list with rationale: `docs/curriculum/cs2-farkle-ml-handoff.md`.
Summary: real per-step reinforcement-learning credit assignment (Bellman-
style updates, discount factor), richer state (total/opponent score,
dice-composition detail), a real dice-selection decision (not just
ROLL/BANK), stronger agent architectures (real tabular Q-learning,
decision trees, function approximation), algorithmic/convergence
analysis, modular software architecture (interfaces, config objects),
deeper testing (property-based, statistical confidence intervals),
performance work (vectorized/parallel simulation), real experiment
infrastructure (multi-run tracking, proper train/val/test splits), and
comparison against additional ML methods. Also flagged: the
`shared_021_farkle_ml_week16_design_and_build.md` prompt's `machine_learning`-repo
ownership idea was never executed and is an open question for CS2, not
an assumption this report makes.

---

## 9. Independent review performed

Dispatched a background review agent (fresh context, no prior exposure to
this build) to walk through the student lesson and every code file *as a
CS1 student who never studied ML would*, run the tests and CLI itself
(all four subcommands, several seeds), and specifically hunt for:
unfamiliar Python constructs, quietly-too-advanced ML framing (Bellman/
gamma/MDP/convergence/stats language), whether the human-strategy-first
framing is genuinely present, and any correctness concerns in the
scoring/learning logic.

**Result: no blocking correctness or scope violations.** Tests passed
(27/27), every CLI command's output matched the documented narrative, and
the ML content itself never leaked into RL math, discount factors, or
statistics vocabulary — confirmed clean by direct grep and read-through.
The play-first, human-strategy-first structure was confirmed genuinely
present, not just claimed.

**Findings that WERE acted on** (the actual gap: code readability, not
ML-concept scope):

1. **Should-fix — closures in `strategies.py`.** The original build used
   closures (`bank_at(threshold)` returning an inner function) so one
   generic factory could produce `bank_at_300`, `bank_at_500`, etc. This
   is a step beyond CS1's own curriculum (functions/return values are
   core CS1; a function that builds and returns *another* function is
   not taught anywhere in `lessons/01`-`09`). **Fixed:** rewrote
   `strategies.py` with flat, concrete functions
   (`bank_at_300`, `bank_at_500`, `bank_at_800`, `cautious_near_target`,
   `aggressive_when_behind`, `always_bank_first_score`) — no closures,
   no factories. This also happened to remove a separate nice-to-have
   finding (manually overwriting `.__name__` on returned functions) for
   free, since flat functions already have the right `__name__`.
2. **Should-fix — dict/set comprehensions.** `engine.score_roll()` built
   its per-face dice count with a dict comprehension, and
   `learner.ExperienceTable.table_rows()` used a set comprehension with
   tuple unpacking — comprehensions are not in CS1's taught vocabulary
   per the same curriculum check. **Fixed:** both rewritten as plain
   `for` loops.
3. **Should-fix — unexplained type hints throughout.** Every function
   signature used type hints (`list[int]`, `int | None`, forward-
   reference string return types) plus `from __future__ import
   annotations` in every file, none of it explained anywhere.
   **Fixed:** removed type hints and the `__future__` import from all
   five files — pure deletion, no behavior change (confirmed by the full
   test suite passing identically before and after).
4. **Should-fix — `@classmethod` on `ExperienceTable.load`.**
   Goes beyond "classes/objects, light" scope. **Fixed:** replaced with
   a plain module-level function, `learner.load_table(path)`. Updated
   the one test and the instructor guide's fallback snippet that
   referenced the old `ExperienceTable.load(...)` spelling.
5. **Should-fix — `epsilon`/exploration never explained to students.**
   The `--epsilon` flag and its real behavioral effect were documented
   in `learner.py`'s docstring (for a reader of the code) but never
   mentioned in the student-facing lesson at all — a student watching
   the table sometimes "try the worse-looking option" during training
   had no vocabulary for why. **Fixed:** added a short plain-language
   paragraph to `lessons/10-farkle-ml.md` §4 introducing exploration and
   the `--epsilon` flag, matching the code's own explanation.

**Findings left as-is** (flagged nice-to-have, judged not worth the
added complexity or loss of narrative flow to fix):
- `train --show-table` prints ~89-162 dense rows (depends on
  `--turns`/seed) — the lesson already mitigates this by directing
  attention to specific rows rather than asking students to read the
  whole table, so left as guided-not-unbounded.
- `cli.py`'s `argparse` machinery remains unread by design — the lesson
  explicitly tells students not to read this file closely, which the
  reviewer confirmed was the right scoping choice, not an oversight.

**Post-fix reverification:** full test suite re-run (27/27 pass,
identical to before the fixes), and every sample result in §7 above was
re-run after the fixes with the same seeds — every number is
byte-identical to what's quoted in §7, confirming the readability fixes
were behavior-preserving refactors, not new logic.

---

## 10. Remaining genuine open items

- The exact grading weight/mechanism for
  `assignments/W16-farkle-ml-experiment-receipt.md`, if Jeremy wants one
  distinct from the existing Wacky-Wednesday/Fun-Friday/attendance
  categories it currently rides on (§6) — flagged, not decided, per the
  prompt's explicit instruction not to invent a number.
- `docs/grading-model.md`'s other pre-existing open items (bonus-practice
  point value, A4 weight, drop-lowest policy, Canvas submission mapping)
  are untouched and remain open, as instructed.
- CS2's own Week 16 build is not started and not designed beyond the
  handoff note's menu (§8) — intentionally, per the prompt's stop point.

## 11. Is CS1 curriculum-complete for Savnac synthetic-student testing?

From this task's scope (Week 16 content + the grading-model stale-
checkpoint seam): **yes, this piece is closed.** Week 16 now has real,
tested, runnable lesson content where report 012 had flagged a gap, and
the grading model's checkpoint count is internally consistent across
every active file that states it. This report does not re-audit the rest
of the semester (Weeks 1-15, 17) for curriculum-completeness — that was
report 012's scope, not this one's — so this is a statement about Week
16 and the grading-model seam specifically, not a full-course
Savnac-readiness re-certification.

---

## Boundaries respected

No Savnac writes. No Canvas writes. No `machine_learning` repo writes
(read-only inspection of its git history only, to confirm shared_021 was
never executed). No CS2 repo writes. No new Coding Odyssey checkpoint,
gate, or Decide/Compare instrument added to Week 16. No numeric grading
value invented. No large generated dataset committed (largest new file is
a 12 KB JSON table fixture). No RL math, discount factor, Bellman
equation, neural network, or formal MDP framing introduced anywhere in
CS1-facing content.

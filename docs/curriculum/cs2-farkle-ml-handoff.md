# CS2 handoff — Farkle / Machine Learning, future extensions

**Purpose of this note.** Protect CS1's Week 16 from scope creep, and
give CS2 (or any later course) a clean starting point if it wants to make
this system smarter, cleaner, deeper, or more sophisticated. Nothing
below is implemented in CS1 and nothing below should leak into CS1's
lesson, code, or grading. This is a menu, not a plan.

**Where the CS1 version lives:** `lessons/code/farkle/` (engine,
strategies, learner, simulate, cli), `lessons/10-farkle-ml.md` (student
lesson), `docs/curriculum/week-16-instructor-guide.md` (instructor
guide), `reports/013_week16_farkle_ml_capstone.md` (build report with
sample results and full design rationale).

---

## What CS1 deliberately did NOT do (and why each is a real CS2 opportunity)

### 1. Real reinforcement learning credit assignment
CS1's `ExperienceTable` gives every decision in a turn the *same* credit
or blame — the turn's final result. Real reinforcement learning
(temporal-difference learning, Q-learning with a discount factor gamma,
SARSA, etc.) credits each decision separately based on its effect on
future decisions, using a Bellman-style update. This is the single
biggest "make it smarter" opportunity: swap the flat per-turn credit for
a proper step-by-step update rule, and discuss why/when that produces
different (often better) behavior than CS1's simplification.

### 2. Richer state representation
CS1's table only looks at `(turn_score bucket, dice_remaining)` — a
minimum viable state, chosen to keep the printed table small enough to
read start to finish. CS2 could add `total_score`, `opponent_score`,
distance to the target score, or dice-composition detail (e.g., how many
of the remaining dice are "high value" faces) as real state features, and
discuss the trade-off between a bigger, more expressive state and a
table that gets too sparse to learn well (the classic "curse of
dimensionality" problem, introduced informally, not with the formal
term).

### 3. A real dice-selection decision
CS1's engine auto-selects the maximum-scoring combination from every
roll — students only ever decide ROLL vs. BANK. A CS2 version could
expose "which scoring dice do I keep vs. set aside for a bigger risk"
as a real decision with its own action space, which is a genuinely
different (and harder) game-theoretic problem.

### 4. Better agent architecture
CS1 uses a hand-rolled dictionary with a running-average update. CS2
could introduce a real tabular Q-learning agent, a linear function
approximator, or (with strong scaffolding and explicit dependency/version
discipline) a small supervised model trained on simulated (state,
action, outcome) triples — decision trees are a natural first choice
because their learned rules are still inspectable, matching this
family's "transparency over sophistication" value even at higher
sophistication.

### 5. Algorithmic analysis
No Big-O, convergence, or sample-efficiency analysis is attempted in
CS1. CS2 could analyze how many training turns are needed before the
table's preferences stabilize, and discuss why (state-space size, reward
variance).

### 6. Modular redesign / software architecture
CS1's package is five small flat files, deliberately simple. A CS2 pass
could introduce a proper `Strategy` interface/abstract base class,
pluggable agent architectures, configuration objects instead of
positional CLI args, or a package layout meant to be imported by other
projects rather than run as a script.

### 7. Testing depth
CS1's tests are scoring/turn correctness plus learner smoke tests
(reproducibility, table growth, save/load round-trip). CS2 could add
property-based tests (e.g., "score is never negative for any dice
combination," using a tool like `hypothesis`), statistical tests on win
rates (confidence intervals instead of point estimates), or regression
tests that pin exact learned-table values across code changes.

### 8. Performance
CS1's simulator is plain Python, single-threaded, and fast enough
(20,000 training turns and 5,000 evaluation games both finish in well
under a second). If CS2 wants much larger experiments (millions of
games, bigger state spaces), profiling, vectorization (e.g. NumPy-based
batch dice rolling), or parallel simulation become real, teachable
performance topics that CS1 has no reason to touch.

### 9. Serialization / experiment infrastructure
CS1 saves a trained table as a single small JSON file
(`ExperienceTable.save`/`.load`). CS2 could build a real experiment
tracker: multiple runs with different hyperparameters (`epsilon`,
`bucket_size`, `--turns`), a results database instead of print statements,
or a proper train/validation/test split with more rigor than CS1's
"different seed for evaluation" approach.

### 10. Additional ML methods, for comparison
CS1 uses exactly one learning mechanism on purpose ("a tiny visible
learner beats an impressive black box"). CS2 could compare the
experience-table approach against a decision tree, k-nearest neighbors,
or a small random forest trained on the same simulated data, and discuss
why interpretability and predictive power sometimes trade off against
each other.

---

## What should stay true even at CS2 depth

- Keep the Farkle rule set consistent with CS1's documented variant
  (`lessons/10-farkle-ml.md` §1) unless there's a real pedagogical reason
  to change it — students may compare notes across courses.
- Keep at least one fully interpretable option available and demonstrated,
  even while adding more sophisticated methods for comparison. The
  "transparency over sophistication" value that shaped CS1's design is
  worth preserving as a contrast point, not discarding once it's no
  longer a hard constraint.
- Any new dependency (scikit-learn, NumPy for more than what CS1 already
  uses via the standard library, visualization libraries) should fail
  gracefully and be documented with version/license, matching the
  discipline already asked for in `jeremy_task_tracking/codex_prompts/shared_021_farkle_ml_week16_design_and_build.md`.

## Explicitly not CS1's job to decide

- Whether CS2 keeps the shared-package framing from
  `shared_021_farkle_ml_week16_design_and_build.md` (a `machine_learning`
  repo as canonical owner) or forks CS1's `lessons/code/farkle/` directly.
  That prompt was written before this CS1-only build and was not executed
  as of this handoff — `machine_learning` currently contains no Farkle
  code. Whoever picks up CS2's Week 16 should decide fresh, with current
  repo state in hand, rather than inheriting a stale assumption.
- Any CS2 grading weight, rubric, or checkpoint design for this material.

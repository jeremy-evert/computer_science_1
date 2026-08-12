# Coding Odyssey — arc and gate map (reconciled onto the real Fall 2026 schedule)

**Supersedes nothing — extends what's already decided.** This maps the
2026-07-24 Odyssey pivot (genre menu, weekly gates, five judgment
instruments — see `docs/curriculum/judgment_toolkit.md`) onto the *actual*
`planning/week-01.md`…`week-17-finals.md` topics and the already-wired
4-checkpoint structure (`assignments/A2-coding-odyssey-project.md`,
`reports/007`), not the generic zyBooks-chapter map the pivot was first
drafted against before this repo's real state was checked. Monday
Moments (AI Fluency lenses), Wacky Wednesday / Fun Friday (Professional
Minds), and every existing date/topic are **untouched** — this only adds a
gate layer to the Monday lecture / weekly-focus track and deepens the
existing Coding Odyssey checkpoints.

**Arc boundaries follow the real checkpoints, not an invented 2-3 week
rule.** The four Checkpoints (Wk 6/9/14/16) already carry Debrief-shaped
mechanics ("submit a working version, explain what changed, and demonstrate
it" — the existing A2 template). Reusing them as arc closes means no new
due dates get invented; the arc structure formalizes spacing this course
already has.

## Arc structure

| Arc | Weeks | Real weekly-focus topics | Closes at |
|---|---|---|---|
| 1 — Foundations | 1-6 | Success Foundations (no programming) → on-ramp/variables → types/branching-intro → branching → loops → loops consolidation | **Checkpoint 1** (Wk6, baby project — light Debrief) |
| 2 — First Real Choices | 7-9 | Functions/decomposition → strings → strings continued | **Checkpoint 2** (Wk9, first real Odyssey pass) |
| 3 — Systems That Remember Themselves | 10-14 | Lists/dicts → dicts/organized data → classes Round 1 → classes Round 2 (+ capstone Decide/Compare #2) → tools/GitHub/AI-aware coding | **Checkpoint 3** (Wk14, **Full Trail Debrief**, mandatory) |
| 4 — Thanksgiving / Farkle | 15-16 | Fully async, no new technical material → Farkle/ML applied fun week (no Odyssey gate) | No Odyssey checkpoint — building is already finished |
| 5 — Finals | 17 | Wrap-up | Final Debrief + Judgment Log checkpoint 3, full show-and-tell |

Arc 3 is deliberately the longest (5 weeks) — it's where this course's real
sequence puts both collections *and* both OOP rounds *and* the tools week,
so the Full Trail Debrief lands where the actual deliberate-refactor moment
is (Weeks 12-13, OOP), not at an artificially even 2-3 week mark.

**Reconciled 2026-08-12:** Checkpoint 4 (formerly Wk16, "final creative
pass") is retired — Week 16 is now the shared Farkle/ML fun week and must
not compete with a giant Odyssey deadline. Capstone Decide/Compare #2 moved
from Wk16 to Wk13, alongside the real build culmination. Arc 4 (formerly
"The Reckoning") is renamed to reflect what the weeks actually are:
Thanksgiving (fully async, no new technical material) and Farkle/ML
(applied fun week, no Odyssey gate) — not a project-completion buffer
leading into a final creative pass that no longer exists at Wk16.

## Week-by-week gate map

Each gate follows `judgment_toolkit.md`'s Quick Check shape: one concept,
pass/fail, ≤2-3 sentences to define. "Route" flags whether this gate is a
plausible Marker-mechanical check or needs a human/frontier-agent Quick
Check — a starting call, not final; confirm during authoring
(task 5/6 in `jeremy_task_tracking/TASKS.md`).

| Wk | Real focus (`planning/week-NN.md`) | Gate | Route |
|---|---|---|---|
| 1 | Foundations — universal week | *No gate, no genre pick.* Stays identical across all five courses. | — |
| 2 | Variables, expressions, types | **Step 0:** genre pick + founding charter (existence check, not scored). **Gate:** world must print at least one computed value using a variable and an expression (not a hardcoded string). | Mechanical |
| 3 | Types/formatting continued; branching intro | World must use one conditional to change its output based on state. | Mechanical |
| 4 | Branching and decision-making | World must include a decision with ≥2 branches that meaningfully changes behavior (deeper than Wk3's intro use). | Mechanical |
| 5 | Loops and repetition | World must run a loop processing an unknown/variable number of events (sentinel- or range-driven). | Mechanical |
| 6 | Loops consolidation | *Gate = Checkpoint 1 itself* (baby project/dry run) — no separate parallel gate. | Build (Checkpoint) |
| 7 | Functions and decomposition | At least one distinct world action from Weeks 2-6 is refactored into its own function with a parameter and a return value. | Mechanical |
| 8 | Strings and text processing | World must parse or format at least one piece of text data (a log line, a message, a report) using real string operations. | Mechanical |
| 9 | Strings continued | *Gate = Checkpoint 2 itself* (first real Odyssey pass). | Build (Checkpoint) |
| 10 | Lists and dictionaries | World must track a growing collection of named entities in a list. | Mechanical |
| 11 | Lists and dictionaries continued | World must use a dict to look up an entity by name/ID. **Also hosts Decide/Compare #1** (structure choice, defended — see `judgment_toolkit.md`). | Mechanical (gate) / human (Decide-Compare) |
| 12 | Classes/objects/modules — Round 1 | At least one major noun already tracked in the Wk10-11 collection becomes a class. | Human/frontier-agent |
| 13 | Classes/objects/modules — Round 2 | At least two of the world's classes interact (method call between objects, not just standalone). **Also hosts Decide/Compare #2** (capstone-scale, moved here 2026-08-12 from Wk16). Substantial Odyssey building culminates this week. | Human/frontier-agent |
| 14 | Tools/GitHub/pair programming/AI-aware coding | *Gate = Checkpoint 3 itself*, **Full Trail Debrief mandatory** (see `judgment_toolkit.md` §4) — a Git-backed receipt on Week 13's real code, not a new build sprint. Natural home for the LLM-API-call side-quest — this week is literally "AI-aware coding practice." | Build + Debrief (Checkpoint) |
| 15 | No new technical material — fully async (Thanksgiving) | *No mandatory gate* — matches the week's own already-decided light/async framing. Optional side-quest slot (see below). | — |
| 16 | Farkle / ML applied fun week (**not** Checkpoint 4 — retired 2026-08-12) | *No Odyssey gate.* Consumes the CS1 core (variables/state, branching, loops/simulation, functions, collections, objects, testing, files, Git, judgment) rather than expanding it. No RL math required. | — |
| 17 | Finals — wrap-up | Final Judgment Log checkpoint + Debrief, full show-and-tell (already scheduled); final Odyssey code/World Bible submitted as evidence/receipt, not a new technical performance. | Human |

## Genre menu — Week 2 Monday (moved 2026-07-24 from Week 1 Friday)

**Placement, reconsidered.** Originally paired with Week 1 Friday's
"dream job"/career-interest theme. Jeremy's call, 2026-07-24: keep Week 1
strictly universal across all five courses (no CS1-only exception, even as
a technically-separate module), and start the Odyssey's own content at
Week 2 — the first week that's unambiguously CS1-only anyway. Genre pick +
founding charter now open Week 2 Monday, immediately before that week's
gate (`assignments/odyssey_gates/week-02.md`). Reasoning also considered
and rejected: a separate Friday-Week-1 module (technically easy, but muddies
the "Week 1 = identical everywhere" line and adds load to an already-full
universal week).

**The menu (unchanged from the original design, still bounded at 4):**
Frontier Settlement, Investigation Bureau, Starship Log, Small Business —
each guaranteed to support collections, text data, save/load state,
meaningful classes/objects with at least one meaningful interaction
(**not** a required class hierarchy/inheritance — corrected 2026-08-12,
see `assignments/A2-coding-odyssey-project.md`), and a numeric feature by
the Wk13-17 capstone (moved from "Wk16-17" since Wk16 no longer hosts a
capstone Odyssey event). Genre content (full descriptions, ML-hook framing)
is drafted separately — see task 5/6.

## What didn't survive the merge from the original brainstorm, and why

- **A fresh Ch.2-15 zyBooks chapter map** — this course already has its own
  real, historically-derived sequence (`docs/curriculum/course-sequence.md`,
  `unit-map.md`), which doesn't match a generic zyBooks numbering
  week-for-week (e.g., real Wk9 is strings, not files/exceptions; real Wk11
  is collections, not recursion/Big-O). The gate map above follows the real
  sequence.
- **NLP (Ch.12) and external-dataset (Ch.13) side-quests** — no clean
  mandatory slot exists in the real schedule for either. Kept as **optional
  enrichment**, available at Week 15's buffer slot or after Week 8's strings
  work for text-heavy genres (Investigation Bureau, Starship Log) — matches
  the original design's own framing of these two as optional side-quests,
  not gates.
- **A separate Wk11 Big-O/algorithm gate** — replaced by the Decide/Compare
  placement above, which follows the real Wk10-11 collections content
  instead of an assumed recursion/Big-O week that doesn't exist here.

## Still open

- Point values for gates/Build/Decide-Compare/Debrief — not set (see
  `judgment_toolkit.md`'s open items).
- Genre content itself, per-week gate assignment text, and rubrics — next
  steps (`jeremy_task_tracking/TASKS.md` tasks 5-6).
- Whether the Wk15 optional side-quests get real authored content or stay a
  standing offer — not decided.

# Prompt 005 — Apply Report 002's Pre-Semester Decisions

## Context

`reports/002_pre_semester_readiness_and_literature_audit.md` surfaced six
items under "Decisions Jeremy Must Make" and explicitly did not apply any
changes to `planning/` — that was left for a follow-up prompt once Jeremy
weighed in. Jeremy has now weighed in (drafted with ChatGPT, pasted in
2026-07-22; not final, but concrete enough to apply). This prompt applies
those six answers to the actual planner and policy files.

## Task

### 1. Weeks 5–6 pacing

Keep the current overall sequence. Week 5 introduces loops. Week 6 is loop
review/practice/consolidation; functions may appear only as a brief,
ungraded preview. Full functions instruction (parameters, return values,
decomposition) still begins Week 7 as already planned. No other unit
compresses.

- Edit `planning/week-06.md`'s Weekly Focus and Due-this-week lines so
  functions read as preview-only, not new graded content.

### 2. Holiday policy — Thanksgiving

Keep the existing Monday-holiday, Friday-holiday, and finals-week defaults.
Treat Thanksgiving week (Week 15, Nov 23–27) as **fully asynchronous** —
Jeremy will be out of the country and unavailable for normal meetings, not
just the existing Wed+Fri "skip, don't make up" default. Monday
Moments/Professional Minds/AI-fluency material for that week is recorded in
advance and loaded into Canvas around Nov 1. If planned material exceeds
what's reasonable for an async week, cut the weakest Professional
Minds/AI-fluency content first — do not compress it, push it into Week 16,
or turn it into extra assignments.

- Edit `planning/week-15.md`'s Status and day sections to reflect a fully
  async week with a Nov-1 load-by date, not just "only Monday meets."
- Add a new status type — "fully asynchronous week (instructor travel)" —
  to `course_foundry/planning/course-development-flow.md` Steps 1 and 6, so
  this is a documented, reusable case rather than a CS1-only one-off.

### 3. Content-authoring cadence

Fall 2026 authoring is scoped to the three courses actually taught this
fall: Computer Science 1, Computer Science 2, Discrete Structures and
Critical Thinking. Software Engineering, Machine Learning, and AI Fluency
2–5 are deferred to spring. Order: finish remaining course-design decisions
per course → CS1 Week 2 as the first full pipeline test (handout + slides +
assignment + rubric + Course Forge pass, Canvas-ready) → once Week 2
passes, run the rest of CS1 → repeat for CS2 → repeat for Discrete
Structures → build one shared AI Fluency 1 for all three. Enrichment
(podcasts, short-form video, extra AI-fluency levels) is not a launch
requirement.

- Record this in `ROADMAP.md`'s scope/next-step framing. This is a
  workspace-wide sequencing decision (also governs `computer_science_2`,
  `discrete_structures_and_critical_thinking`, `ai_fluency`), not just a
  CS1 planning-file edit — recorded centrally in
  `jeremy_task_tracking/DECISIONS.md` as well.

### 4. AI I doc fidelity

The missing "AI I: Thinking with AI" document is no longer a blocker.
`ai_fluency` is the authoritative source going forward. Fall 2026 builds AI
Fluency 1 only, shared across the three fall courses with course-specific
examples. Future Monday Moments should stay faithful to the AI Fluency 1
fundamentals map and stated instructional principles, not to the missing
document.

- Update `ROADMAP.md` and any stale "AI I doc is a blocker" language in
  `START_HERE.md` / `prompts/README.md` to reflect that this is resolved by
  decision, not still open.
- Do not edit `ai_fluency`'s own docs in this pass — flag in the report
  that its existing AI II–V architecture material (reports 008–010) should
  be reconciled against this scope call later, not assumed to match it
  already.

### 5. Online section scope

`COMSC-1033-1414` is in scope for Fall 2026, sharing CS1's Canvas
structure. Face-to-face attendance stays simple. Online students get three
brief (2–5 min) graded-for-completion check-ins a week (Mon/Wed/Fri),
piggybacked on existing activities where possible. A rolling Mon/Wed/Fri
disengagement check flags 7+ days of no qualifying activity: auto-reminder
first, then a single concise instructor report for anyone still inactive.

- Record the scope decision and the system's intended shape in
  `ROADMAP.md` as a real, defined-but-not-started gap. **Do not build the
  check-in/disengagement system in this pass** — it's a distinct
  `course_foundry`/Harbor build, out of scope for a planning-file
  application pass.

### 6. Week 16 redistribution

Stage the professional-pathway portfolio across the semester instead of
dumping all seven artifacts in Week 16:

- Week 1 (`semester_kickoff_week`) establishes baseline artifacts —
  already largely covered by that repo's A01–A09 set.
- Mid-semester, briefly update dream-job research, skill-gap analysis,
  resume, and GitHub/LinkedIn evidence. Use Week 14 (already carries
  GitHub/tools content and Coding Odyssey checkpoint 2).
- Week 15 (Thanksgiving, now fully async per item 2) is the independent
  completion/polishing week for the full portfolio submission, loaded
  ~Nov 1 alongside that week's other async material.
- Week 16 keeps only Coding Odyssey checkpoint 3, full show-and-tell, and
  the final-reflection kickoff (optionally a brief AI Fluency 1 reflection
  tie-in). Remove the 7-artifact professional-pathway set from Week 16's
  due items.

Edit `planning/week-01.md`, `week-14.md`, `week-15.md`, `week-16.md`, and
`assignments/A6-professional-pathway-artifacts.md` accordingly.

## Requirements

- These answers are explicitly **not final** — apply them as a real,
  committed revision, but don't treat this pass as closing the door on
  further adjustment.
- Leave Report 002's lower-priority Week 9 checkpoint-timing question
  (move Coding Odyssey checkpoint 1 to Week 10 or not) unresolved — Jeremy's
  answers didn't address it; don't invent one.
- Write the completion report to `reports/005_apply_pre_semester_decisions.md`
  per the standard contract (summary, files changed, commands run,
  limitations, ready-for-review status).
- Do not touch `course_foundry/load_adapters.py` or
  `course_foundry/semester_kickoff_content_map.py` — both have unrelated
  in-progress uncommitted changes from another session; leave that dirty
  state alone.

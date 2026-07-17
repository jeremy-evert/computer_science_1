# Start Here — Computer Science 1

If you're picking this repo up cold (human or agent), read in this order.

## 0. Workspace context first

This repo lives under `/data/git`, which is **not** a monorepo — it's a
working drive of independent repositories. Before touching anything here,
read `/data/git/START_HERE.md` and `/data/git/AGENTS.md` (the workspace-wide
agent rules: git/push discipline, delegation policy, prompt/report contract,
safety rules). There is currently no repo-local `AGENTS.md` or `CLAUDE.md` in
`computer_science_1` itself, so the workspace rules are the ones that apply
here — if you add repo-specific rules later, put them in a local `AGENTS.md`
and note the override here.

## 1. The map

- [`README.md`](README.md) — repository map (what every directory is for)
  and the course's technical shape (six-part sequence from foundations
  through career connection).
- [`ROADMAP.md`](ROADMAP.md) — living record of what's done, what's a real
  gap, and the next concrete step. **This is the file to check for "what's
  left to do."** Update it as work lands.
- [`reports/001_planning_status.md`](reports/001_planning_status.md) — a
  point-in-time snapshot from 2026-07-14. Useful for history; `ROADMAP.md`
  is the current source of truth.
- [`reports/002_pre_semester_readiness_and_literature_audit.md`](reports/002_pre_semester_readiness_and_literature_audit.md)
  — the readiness/literature audit (complete; Jeremy's decisions still
  pending) — and
  [`reports/004_source_reconciliation_and_slurp_status.md`](reports/004_source_reconciliation_and_slurp_status.md)
  — the follow-up source reconciliation against the newly pulled
  `professional_minds` and `ai_fluency` repos (complete). Read both before
  touching `planning/`.

## 2. Special instructions for course development

- [`prompts/README.md`](prompts/README.md) — read this before drafting any
  new curriculum-development prompt. It lists required reading (this
  README, Monday Moments docs, the relevant weekly plan, the professional
  pathway artifacts doc, plus AI-content sources in `../ai_fluency/` and
  `../drive_raw_pull_2026-07-14/`).
- [`prompts/001_course_development_source_walk.md`](prompts/001_course_development_source_walk.md)
  and [`prompts/001_pre_semester_readiness_and_literature_audit.md`](prompts/001_pre_semester_readiness_and_literature_audit.md)
  — the actual development prompts. The second one is the active work item;
  see `ROADMAP.md` for its status.
- [`docs/philosophy/teaching-patterns.md`](docs/philosophy/teaching-patterns.md)
  and [`docs/curriculum/course-sequence.md`](docs/curriculum/course-sequence.md)
  — the pedagogical and historical grounding to read before changing course
  structure or pacing.

## 3. Agent rules

- Workspace-wide rules: `/data/git/AGENTS.md` (see §0 above) — this covers
  commit/push discipline (standing authorization to commit+push completed
  work), the mechanical-work delegation policy (Codex/golem, not Claude
  tokens, for grunt work), and the prompt→report contract.
- Prompt/report contract specifically: when you execute a prompt at
  `prompts/NNN_slug.md`, write its completion report to
  `reports/NNN_slug.md` before stopping (summary, commands run, test
  results, files changed, known limitations, ready-for-review status).
- No repo-local agent rules exist yet for `computer_science_1`. If a rule
  turns out to be specific to this repo (not the whole workspace), add it to
  a new `AGENTS.md` here rather than overloading the workspace one.

## 4. First step if you're starting fresh right now

Open [`ROADMAP.md`](ROADMAP.md) → "Next step". As of 2026-07-16 (later same
day) Reports 002 and 004 are both complete: the readiness/literature audit
ran, and the two previously-missing source documents were re-investigated
against the newly pulled `professional_minds` and `ai_fluency` repos
(`professional_minds.csv` found and fully verified against the planner; the
AI I: Thinking with AI document still not located). The next step is
**Jeremy's decision pass** on Report 002's "Decisions Jeremy Must Make"
section — not a report-writing task. After those decisions land, a
follow-up prompt applies approved changes to `planning/`, and Professional
Minds book-slurp production begins.

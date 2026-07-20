# Repo Map — where CS1's pieces live and when they matter

**This repo (`computer_science_1`) is the course repo for COMSC 1033 —
Computer Science 1**, Jeremy's 3-credit-hour, semester-long intro programming
class. Everything here exists to design COMSC 1033 and eventually push it to
Canvas. Git is the source of truth; Canvas is the checkpoint.

The repos below are siblings under `~/git/`. Each entry says what it is and
**when it becomes important** to the CS1 build (now → Aug 17 → in-semester).

## `swosu_cs_curriculum` — the cross-course layer

The broader course-development repo spanning the whole five-course portfolio
(CS1, CS2, Discrete Structures, Software Engineering, Machine Learning). It
holds shared templates, decisions, and per-course folders — including
`courses/cs1-python-fall-2026/` and `courses/fall-2026-template/`.

**When it matters:** *Later, and at the boundaries.* Day-to-day CS1 authoring
happens here in `computer_science_1`. `swosu_cs_curriculum` matters when a
CS1 pattern is worth promoting to something CS2/DSCT can reuse, or when a
portfolio-wide decision (naming, policy, template) needs one home.
⚠ **Open reconciliation item:** its `courses/cs1-python-fall-2026/` folder
overlaps this repo's charter. Decide which one Canvas-bound CS1 content lives
in (this repo, per Jeremy 2026-07-15) and leave a pointer in the other, so
two half-real CS1s don't diverge.

## `ai_fluency` — the Monday Moments spine

Shared scaffolding for the five-course AI sequence (AI I "Thinking with AI"
through AI V "Machine Learning and AI Systems"). Each level has its own
`monday_moments/` folder plus a shared template. CS1 carries **AI I** — the
sixteen "AI as tutor, not typist" lenses the weekly planner already anchors
every Monday to.

**When it matters:** *Now.* Writing the 16 Monday Moments entries is on the
critical path to Aug 17. Author them against the AI I lens list, and decide
whether the canonical copy lives in `ai_fluency/ai_i/monday_moments/` (shared
across sections/years) with this repo's `monday_moments/` holding the
CS1-scheduled instances — or the reverse. Don't write them twice.

## `professional_minds` — Wacky Wednesday / Fun Friday curriculum

The book-anchored professional-development strand folded into every class:
book notes (`books/`), lesson folders (`lessons/week01/`–`week16/`),
assignments, portfolio structure, and its own monday_moments. CS1's weekly
planner points at it twice a week — *How Learning Works*, *Teach Students
How to Learn*, etc.

**When it matters:** *Now — it's the biggest unfunded promise in the CS1
plan.* The `lessons/week01/`–`week16/` folders are still empty, and the CS1
planner commits to 32 sessions against them. Before Aug 17, either write the
15-minute lessons (at least Weeks 1–4) or officially run Wed/Fri as
discussion from the book + question already in each planning file.

## `curriculum_rag_supporter` — the curriculum-craft library

A local RAG stack (ChromaDB + Ollama; `ingest.py` / `query.py` / `app.py`)
over a library of curriculum-development books. This is the "get better at
curriculum design" tool — ask it pedagogy questions grounded in the
literature.

**When it matters:** *As a consultant, not a blocker.* Two named uses: (1)
`prompts/001_pre_semester_readiness_and_literature_audit.md` §4 in this repo
has seven pedagogy questions written for it and never run — worth one session
before the semester to sanity-check pacing and workload; (2) in-semester,
when a lesson or assessment isn't landing, query it before redesigning by
instinct. Requires ChromaDB + Ollama running locally.

## `drive_raw_pull_2026-07-14` — frozen Drive source material

A one-time local export (2026-07-14) of the Google Drive design documents:
the Professional Minds integrated plan (0.1.7), the AI I–III course docs,
teaching blueprint, course blueprints, CS curriculum philosophy, and
future-ideas notes. Source Drive links preserved in its README. It looks
important because it is — it's the intellectual source material behind the
Monday Moments / Professional Minds / AI-sequence design — but it is a
**read-only snapshot**, not a workspace.

**When it matters:** *As reference while authoring, then never edit it.* When
writing Monday Moments, consult `ai_i_thinking_with_ai.md`; when writing
Professional Minds lessons, consult `professional_minds_integrated_plan_0.1.7.md`;
when a design question about course philosophy comes up, check
`cs_curriculum_philosophy.md` and `teaching_blueprint.md` before re-deciding.
If a document there changes direction, that edit belongs in Drive or in the
owning repo — not in the pull.

## Also connected (not curriculum content)

- **`jeremy_task_tracking`** — the cross-project ledger (`TASKS.md`,
  `DECISIONS.md`, `RISKS.md`). Matters whenever priorities shift: the
  2026-07-15 content-first pivot should be recorded there.
- **`harbor`** — the Canvas API client. Matters at **push time**: when CS1
  content in this repo is ready to load into Canvas. Push order, safest
  first: **Savnac** (a whole separate private Canvas instance on Brandy,
  zero real-data risk by construction — see
  [`docs/savnac-canvas-access.md`](savnac-canvas-access.md)) → sandbox
  course 24298 on real SWOSU Canvas → never a real course first.
- **`course_foundry`** — course-agnostic checks (sync_check,
  completeness_check) and the verification harness. Matters **after** CS1
  content exists and is Canvas-deployed; explicitly parked until then per
  the content-first pivot.

## The order of operations, in one line

Write CS1 content here → consult `drive_raw_pull` + `curriculum_rag_supporter`
while writing → fill `ai_fluency` (Monday Moments) and `professional_minds`
(Wed/Fri lessons) as the shared strands → push to Canvas via `harbor` →
verify with `course_foundry` → promote reusable patterns up to
`swosu_cs_curriculum`.

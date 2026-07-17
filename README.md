# Computer Science 1

This is the course repo for **COMSC 1033 — Computer Science 1**, a 3-credit-hour, semester-long intro programming class. Course content is designed here and eventually pushed to Canvas: git is the source of truth, Canvas is the checkpoint.

**[docs/course-ethos.md](docs/course-ethos.md)** is the canonical statement of the course's weekly contract — what we ask of students and what we give them. When documents disagree, it wins.

This repo is one node in a small ecosystem of sibling repos (Monday Moments in `ai_fluency`, Wacky Wednesday / Fun Friday in `professional_minds`, the cross-course layer in `swosu_cs_curriculum`, and more). See **[docs/repo-map.md](docs/repo-map.md)** for what lives where and when each repo matters to the CS1 build.
This repository is the working curriculum for a foundational Python and computer science course. It combines current teaching materials, reusable assignment components, weekly planning, curriculum analysis, and historical Canvas exports. The course is still evolving; the archive is evidence for future revisions, not a rigid calendar to copy semester-for-semester.

## Start here

- [Course sequence](docs/curriculum/course-sequence.md) — the historical learning arc from foundations through projects and professional reflection.
- [Durable unit map](docs/curriculum/unit-map.md) — the current concept-level map.
- [Weekly plan](planning/) — Week 1 through Week 17/finals for the Fall 2026 offering.
- [Lessons](lessons/) — the nine-part instructional sequence.
- [Assignment library](assignments/) — reusable student-facing assignment drafts.
- [Templates](templates/) — starting points for assignments, rubrics, and syllabi.
- [Curriculum history synthesis](docs/reports/curriculum-history-synthesis.md) — what recurs across the archived offerings and what has changed.

## Repository map

| Directory | Purpose |
| --- | --- |
| [`archive/`](archive/) | Historical Canvas snapshots from spring 2021 through spring 2026, plus uploaded files and other source artifacts. There are 12 snapshots across 11 semester labels; spring 2021 has two course IDs. |
| [`assignments/`](assignments/) | Reusable assignments for weekly coding practice, pair programming, Coding Odyssey/Choose Your Own Adventure projects, show-and-tell, professional pathway artifacts, and final reflection. |
| [`docs/`](docs/) | Durable course documentation. [`curriculum/`](docs/curriculum/) contains the unit map and course sequence; [`philosophy/`](docs/philosophy/) records teaching patterns; [`reports/`](docs/reports/) contains evidence-based curriculum analysis. |
| [`lessons/`](lessons/) | Nine lesson guides covering printing/input, variables and types, branching, loops, functions, strings, collections, classes/modules, and projects/tools/reflection. |
| [`monday_moments/`](monday_moments/) | Short weekly AI-and-learning tips for beginning programmers, with a [writing guide](monday_moments/README.md) and [entry template](monday_moments/template.md). |
| [`planning/`](planning/) | Week-by-week course plans for the 17-week semester, including Monday Moments, Wacky Wednesday, Fun Friday, focus, and due items. |
| [`portfolio/`](portfolio/) | Reserved space for student or course portfolio artifacts; currently empty except for `.gitkeep`. |
| [`prompts/`](prompts/) | Prompt files that guide curriculum development and source walks, plus prompt-specific working guidance. |
| [`quizzes/`](quizzes/) | Reusable quiz drafts, currently including getting-to-know-you and chapter-exam formats. |
| [`reflections/`](reflections/) | Reserved space for reflection artifacts; currently empty except for `.gitkeep`. |
| [`reports/`](reports/) | Project and planning reports produced during course development. |
| [`templates/`](templates/) | Reusable assignment, rubric, and syllabus templates. |
| [`tests/`](tests/) | Reserved space for validation or automated checks; currently empty except for `.gitkeep`. |

## Course shape

The durable technical sequence is:

1. Foundations: program execution, printing, input, variables, expressions, types, and formatting.
2. Decisions and repetition: Boolean logic, branching, loops, sentinels, and ranges.
3. Abstraction and text: functions, parameters, return values, testing, and string operations.
4. Collections and objects: lists, dictionaries, classes, objects, modules, and exceptions.
5. Building and explaining: project iteration, demonstrations, GitHub, collaboration, and responsible AI use.
6. Career connection: degree planning, resumes, target-job research, skill-gap analysis, LinkedIn, and GitHub.

Practice and explanation are central: students repeatedly write working code, show or discuss it, revise projects, and reflect on what they learned. AI is framed as a tutor and debugging aid—not a substitute for understanding or typing the code.

## Working with the repository

Most files are Markdown and can be read directly in GitHub or any text editor. A typical curriculum-development workflow is:

1. Review the [course sequence](docs/curriculum/course-sequence.md) and [teaching patterns](docs/philosophy/teaching-patterns.md).
2. Use the relevant [lesson](lessons/) and [weekly plan](planning/) as the instructional spine.
3. Adapt materials from [assignments](assignments/), [quizzes](quizzes/), and [templates](templates/).
4. Consult [`archive/`](archive/) when checking historical precedent or deciding whether an activity is durable or experimental.
5. Record substantial analysis in [`docs/reports/`](docs/reports/) or [`reports/`](reports/), and keep development prompts in [`prompts/`](prompts/).

There is currently no application runtime, dependency manifest, or automated test suite. Validation is therefore primarily editorial: check links, dates, assignment references, and consistency between the weekly plans and the reusable materials.

## Status

This is an active, in-progress course repository. The current planning backbone and lesson sequence are present, while the portfolio, reflections, and tests directories are intentionally reserved for future artifacts.

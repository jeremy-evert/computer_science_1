# Report 002 — Computer Science 1 Repository Inventory and Gap Report

## Scope

This report reviews the contents of `computer_science_1` as they exist on
2026-07-14. It treats the current course folders as the deliverable under
construction and the semester archives as historical evidence, not as
ready-to-teach current content.

## Executive summary

The repository has a coherent instructional skeleton: a README, a historical
curriculum map, nine lesson outlines, seventeen weekly plans, six reusable
assignment briefs, two quiz types, three templates, Monday Moments guidance,
development prompts, and twelve semester-labeled Canvas archives. The main
shortfall is implementation depth. Most current materials are outlines or
templates; the weekly plans point to content that has not been authored, and
the repository contains no current syllabus, detailed assessment/rubric set,
student-facing weekly Monday Moments, Professional Minds lessons, portfolio
structure, reflection bank, or test/validation suite. It is suitable for
continued curriculum development, but not yet a complete course shell that an
instructor could teach from without substantial additional writing and
decision-making.

## What is present

### Course framing and curriculum design

- `README.md` identifies the repository as the home for foundational Computer
  Science 1 concepts, programming practice, and learning artifacts.
- `docs/curriculum/course-sequence.md` and `docs/curriculum/unit-map.md`
  synthesize the historical Python sequence and its project, tool, and career
  strands.
- `docs/philosophy/teaching-patterns.md` records recurring archive evidence:
  practice-first work, visible demonstrations, flexible effort-based grading,
  creative application, relational support, and AI verification/transparency.
- `docs/reports/curriculum-history-synthesis.md` provides a high-level review
  of the archived Canvas material and identifies historical inconsistencies.

### Current instructional planning

- `planning/week-01.md` through `planning/week-17-finals.md` provide a full
  Fall 2026 calendar sequence, including weekly focus, class-day anchors,
  project checkpoints, and due items.
- The technical arc covers foundations, variables/types, branching, loops,
  functions, strings, collections, classes/modules, and project/tool/reflection
  work through nine lesson files in `lessons/`.
- The plans explicitly connect technical topics to Monday Moments, Professional
  Minds, show-and-tell, and project work.

### Assignments, assessments, and reusable authoring tools

- Six assignment briefs cover weekly coding practice, Coding Odyssey, pair
  programming, show-and-tell reflection, professional pathway artifacts, and
  end-of-course reflection.
- `quizzes/chapter-exam.md` and `quizzes/getting-to-know-you.md` provide two
  reusable quiz types, including historical context about when each was used.
- `templates/assignment-template.md`, `templates/rubric-template.md`, and
  `templates/syllabus-template.md` establish reusable authoring patterns.
- `prompts/` contains a source-walk prompt, a pre-semester readiness/literature
  audit prompt, and prompt usage guidance.
- `monday_moments/README.md` and `monday_moments/template.md` define the
  intended two-minute, AI-as-tutor-not-typist format.

### Historical source material

- `archive/` contains twelve Canvas snapshot files spanning spring 2021 through
  spring 2026, plus selected uploaded files, syllabi, assignments, images, and
  an academic calendar.
- The archive is valuable evidence for recurring chapter topics, project
  checkpoints, pair programming, career artifacts, demonstrations, and changes
  in assessment practice. It is not a substitute for current student-facing
  materials.

## What is missing or incomplete

### High-priority teachability gaps

- **Current syllabus:** only a reusable syllabus template exists. There is no
  Fall 2026 syllabus with section identity, instructor/contact details,
  prerequisites, materials, grading, attendance, late-work, AI, accessibility,
  and institutional-policy language filled in.
- **Student-facing lesson content:** the nine lesson files are concise outlines
  with objectives, key content, and historical notes. They do not yet include
  examples, worked code, demonstrations, practice sequences, misconceptions,
  answer keys, or instructor notes.
- **Weekly Monday Moments:** there are no week-specific entries in
  `monday_moments/`; the planning files name sixteen AI lenses but do not supply
  the short lessons students would read or discuss.
- **Professional Minds content:** no Professional Minds lesson directory or
  fifteen-minute lesson files exist in this repository. Weekly plans name book
  pairings and questions, but the actual reading extracts, activities, timing,
  and facilitation notes are absent.
- **Assessment implementation:** assignment briefs describe patterns, but there
  are no current chapter problem sets, submission instructions tied to a real
  LMS location, answer/checking guidance, complete project checkpoint briefs,
  or finalized grading rubrics.
- **Course-level assessment alignment:** there is no single map connecting
  course outcomes to lessons, practice, projects, quizzes, demonstrations, and
  final evidence.

### Important supporting gaps

- `portfolio/` contains only `.gitkeep`; there is no portfolio specification,
  milestone checklist, evidence convention, or final packaging guidance.
- `reflections/` contains only `.gitkeep`; reflection prompts are embedded in
  assignment briefs rather than organized as a reusable reflection sequence.
- `tests/` contains only `.gitkeep`; there are no validation checks for lesson
  links, week coverage, due-item references, rubric completeness, or runnable
  example programs.
- `docs/planning/` contains only `.gitkeep`, while active plans live in
  `planning/`. The duplicate directory purpose is unresolved and may create
  navigation or future-maintenance confusion.
- There is no current repository-level contribution/authoring guide explaining
  naming, review, source citation, or how to promote a draft into teach-ready
  content.
- The README does not yet link users to the active planning, curriculum,
  assignment, archive, and report locations.

### Known content and governance questions

- The weekly plan assumes a specific Fall 2026 section and meeting pattern,
  but that identity is not represented in a completed syllabus.
- The plan includes an AI lens and two Professional Minds anchors in many
  weeks, but the workload and pacing have not yet been documented as approved
  instructor decisions.
- Historical evidence is synthesized well, but chapter ordering and the status
  of optional topics such as exceptions, file I/O, searching, sorting,
  recursion, Farkle, and Q-learning still need a current-course decision.
- The archive shows changing policies and grading language across semesters;
  one canonical current policy set has not been selected.

## Inventory at a glance

| Area | Present | Current condition |
|---|---:|---|
| Weekly planning | 17 files | Complete calendar scaffold; needs review and linked content |
| Lesson outlines | 9 files | Present; outline-level |
| Assignment briefs | 6 files | Present; reusable, not fully instantiated |
| Quiz types | 2 files | Present; historical/reusable options |
| Templates | 3 files | Present; not populated for Fall 2026 |
| Monday Moments | 0 entries | Guidance and template only |
| Professional Minds lessons | 0 entries | Referenced by plans, absent here |
| Portfolio artifacts | 0 | Directory scaffold only |
| Reflection collection | 0 standalone files | Prompts embedded in assignments |
| Automated tests | 0 | Directory scaffold only |
| Reports | 2 substantive reports | Planning status plus this inventory/gap report |
| Historical archive | 12 Canvas snapshots | Strong source evidence; not current course content |

## Recommended next work

1. Resolve the open Fall 2026 course decisions: section scope, technical
   pacing, holiday handling, AI-lens adaptation, and whether content is
   authored before the semester or incrementally.
2. Produce the current syllabus and a course-outcome/assessment alignment map.
3. Author week-specific Monday Moments and the Professional Minds lesson
   materials before relying on their planning references.
4. Expand each lesson outline with worked examples, guided practice,
   independent practice, common errors, and evidence of learning.
5. Turn the reusable assignment and rubric templates into final,
   student-facing briefs for each planned checkpoint and chapter.
6. Decide whether `docs/planning/` is retired or given a distinct purpose, then
   add a README navigation map and lightweight repository validation checks.
7. Keep archive-derived claims visibly separate from current requirements so
   historical possibilities do not silently become assigned work.

## Bottom line

What is present is a credible curriculum foundation and a useful historical
record. What is missing is the layer that makes the foundation operational:
approved current policies, student-facing content, concrete practice and
assessment materials, weekly engagement lessons, portfolio/reflection
artifacts, and validation. The next milestone should be “teach-ready for Week
1,” not more broad historical synthesis.

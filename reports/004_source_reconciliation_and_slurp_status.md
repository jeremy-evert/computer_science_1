# Report 004: Source Reconciliation and Slurp Status

## Executive Summary

Report 002 (2026-07-16) found that two planner-dependent source documents —
`professional_minds/professional_minds.csv` and the "AI I: Thinking with AI"
course document — could not be located anywhere under `/data/git`. Two new
repositories, `professional_minds` and `ai_fluency`, have since been pulled.
This task re-inspected both directly.

**One of the two missing-source findings is now stale; the other is
confirmed still accurate.**

- `professional_minds/professional_minds.csv` **is now present** (committed
  2026-07-14, commit `2f3bfad`) and is the authoritative Wednesday/Friday
  book-and-question source. Every one of the 16 instructional weeks in
  `computer_science_1/planning/` was compared line-by-line against this CSV:
  **all 16 weeks are an exact match** (theme, Wednesday book, Friday book,
  and essential question all agree, including the two holiday weeks where
  the planner correctly records a "book of record" without live delivery).
- The "AI I: Thinking with AI" course document is **still not located**.
  `ai_fluency` (the newly pulled repo) does not contain it — it contains
  only generic five-course scaffolding (a shared Monday Moments README and
  template per AI level, no week-by-week lens/big-question content). A
  prior Codex scaffolding report
  (`course_foundry/reports/codex/2026-07-14_ai_professional_minds_scaffolding.md`)
  claims a raw Drive export bundle was created at
  `/home/jevert/git/drive_raw_pull_2026-07-14/` containing an "AI I:
  Thinking with AI" markdown export and a "Professional Minds Integrated
  Plan" markdown export. **That directory does not exist on disk.**
  `/home/jevert/git` and `/data/git` are the same filesystem location
  (confirmed via `readlink -f` on both), so this is not a path-alias issue —
  the bundle the report describes was never actually persisted, or was
  removed, and `ai_fluency/prompts/001_ai_i_source_walk.md` still points at
  it by name. This is a disclosed discrepancy between a prior agent's report
  and current on-disk reality, not a new problem this task created.

Because the planner's professional-minds anchors are now fully
source-verified and exact, and the AI I document remains unlocated, the
practical state of Report 002's Section 2 blocker is: **half resolved, half
confirmed as a real, still-open gap** — not resolved, and not simply stale.

No new book slurp was created this pass. See "Slurps Created or Updated"
below for why.

## Source Repositories Inspected

- `/data/git/professional_minds` — branch `main`, clean, in sync with
  `origin/main` (`git status --short --branch` showed nothing pending
  before this task's edits).
- `/data/git/ai_fluency` — branch `main`, clean, in sync with `origin/main`.
- `/data/git/course_foundry/planning/course-development-flow.md` — re-read
  as the method doc naming both sources.
- `/data/git/course_foundry/reports/codex/2026-07-14_ai_professional_minds_scaffolding.md`
  — the prior report claiming the Drive raw-pull bundle's existence.

## Authoritative AI Fluency Sources

- **Confirmed missing:** a full "AI I: Thinking with AI" 16-week
  lens/big-question document. Not in `ai_fluency`, not in
  `computer_science_1`, not in `Jeremy_Corpus`, not anywhere under
  `/data/git` (repo-wide `grep -rli "thinking with ai"` returns only
  references to the document's *name*, in `course-development-flow.md`,
  `ai_fluency/prompts/001_ai_i_source_walk.md`,
  `course_foundry/reports/codex/2026-07-14_ai_professional_minds_scaffolding.md`,
  and `computer_science_1`'s own ROADMAP/prompts/reports — never the
  document itself).
- **What does exist:** `ai_fluency/ai_i/monday_moments/README.md` — a
  generic placeholder naming a "suggested progression" (define the problem,
  gather context, plan, decompose, prompt, critique, verify, revise, decide,
  measure, reflect) and `ai_fluency/prompts/001_ai_i_source_walk.md`, which
  names a fuller 16-item verb sequence (define the problem, gather context,
  plan, decompose, select tools, engineer prompts, retrieve sources, reason,
  generate, critique, verify, revise, decide, automate, measure, reflect).
  This is metadata/scaffolding — a list of stage names — not a document with
  per-week big questions, source citations, or lesson content.
- **Evidence this is authoritative (as far as it goes):** it is the only
  artifact under `/data/git` naming an AI I stage sequence independently of
  `computer_science_1/planning/` itself.
- **Conflict:** none — nothing else claims to be the AI I document.
- **Which version should control:** neither is a full replacement for the
  missing source. The `ai_fluency` stage-name list should be treated as a
  *weak corroborating fragment*, not a verified source. Report 002's
  "Blocked pending evidence" finding for AI I doc fidelity stands.

## Authoritative Professional Minds Sources

- **File:** `/data/git/professional_minds/professional_minds.csv`.
- **Type:** original structured source (Week, Theme, Wednesday Book, Friday
  Book, Essential Question — exactly the shape `course-development-flow.md`
  Step 4 describes), not a derived summary.
- **Evidence it is authoritative:** it is named directly by
  `course-development-flow.md` Step 4, lives at the exact path that doc
  specifies, is committed (not untracked/ephemeral, unlike the copy Report
  001 noted and lost), and its own repository (`professional_minds`) treats
  it as canonical (`indexes/books.md`, `ROADMAP.md`'s production pipeline
  all reference it).
- **Conflicts:** none found — no second CSV or competing table exists.
- **Controls future planning:** yes, without qualification.

## Slurp Inventory Before This Task

- `professional_minds/books/slurps/make_it_stick.md` — the only slurp that
  exists anywhere in the pipeline (Book Slurp → DNA Card → 15-Minute Lesson).
  No DNA card, no lesson, for any book.
- `professional_minds/templates/book_slurp.md` and
  `professional_minds/prompts/generators/create_book_slurp.md` are both
  present but **empty** (0 bytes) — the de facto slurp format is therefore
  whatever `make_it_stick.md` itself demonstrates (Source, Why This Source
  Matters, Core Claim, Key Concepts, Evidence Claims Summarized, Course
  Design Notes, Example Curriculum Moves, Use With Caution), not a
  documented template.

## Slurps Created or Updated

**None, this pass.** Reasoning:

- The two sources this task was chartered to locate are `professional_minds.csv`
  (a structured table, already directly usable — a slurp would only
  restate it) and the AI I document (still missing — there is nothing to
  slurp).
- No other new raw source text was discovered in `professional_minds` or
  `ai_fluency` beyond what Report 002 already knew about. The 15 other
  books named in `professional_minds.csv` all have source PDFs available in
  `curriculum_rag_supporter/books/`, but producing a non-fabricated slurp
  for each requires a real per-book reading pass (as `make_it_stick.md`'s
  own extraction note describes: PyMuPDF text extraction failed on some
  PDFs and required visual page review). That is a substantial, book-by-book
  production task explicitly out of this task's scope ("do not author all
  Professional Minds classroom lessons") and is already tracked as the
  known content gap in `ROADMAP.md` and `professional_minds/ROADMAP.md`'s
  production pipeline. Manufacturing quick slurps at this pass's depth would
  risk exactly the fabricated-citation problem this task was told to avoid.

## Provenance and Metadata Validation

- `professional_minds.csv`: no invented fields — read verbatim, 17 lines
  (header + 16 weeks), matches `course-development-flow.md`'s documented
  shape exactly.
- `make_it_stick.md` (pre-existing, unmodified): already names its exact
  source PDFs and includes an explicit "Use With Caution" section disclaiming
  precise statistics/page quotations/external citations not present in the
  repository artifact — this task did not alter it and found no reason to.
- No quotations, page numbers, or authorship claims were invented in this
  report. Where a source's location could not be confirmed (the AI I
  document), this report says so rather than guessing.

## CS1 Weekly Anchor Reconciliation

Professional Minds Wednesday/Friday anchors verified against
`professional_minds/professional_minds.csv` directly, line by line. Monday
Moments/AI I lens anchors could only be checked against the thin `ai_fluency`
stage-name fragment described above (no full source document exists).

| Week | Planned anchor | Authoritative source | Classification | Notes or correction |
| ---- | -------------- | -------------------- | -------------- | -------------------- |
| 1 | AI I Lens 1: Define the Problem | `ai_fluency` stage list (fragment only) | Source-supported adaptation | Stage name and order match the fragment; no full AI I doc exists to verify big-question wording. |
| 1 | Wed: *How Learning Works* / Fri: *Teach Students How to Learn*, Q: "How do successful professionals learn?" | `professional_minds.csv` row 1 | Exact match | — |
| 2 | AI I Lens 2: Gather Context | `ai_fluency` stage list | Source-supported adaptation | Same caveat as Week 1. |
| 2 | Wed: *Make It Stick* / Fri: *Mindset*, Q: "How does the brain improve?" | CSV row 2 | Exact match | — |
| 3 | AI I Lens 3: Plan the Work | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 3 | Wed: *Limitless Mind* / Fri: *Resilience Education*, Q: "How do we keep growing through challenges?" | CSV row 3 | Exact match | — |
| 4 | AI I Lens 4: Decompose the Task (folded into Wednesday per Monday-holiday policy) | `ai_fluency` stage list | Source-supported adaptation | Same caveat; holiday handling matches `course-development-flow.md` Step 6. |
| 4 | Wed: *Critical Thinking* / Fri: *Thinking, Fast and Slow*, Q: "How do we make better decisions?" | CSV row 4 | Exact match | — |
| 5 | AI I Lens 5: Select the Right Model | `ai_fluency` stage list ("select tools") | Source-supported adaptation | Same caveat; wording differs slightly ("Model" vs. "tools") but concept matches. |
| 5 | Wed: *The Art of Thinking Clearly* / Fri: *How Not to Be Wrong*, Q: "How do we avoid common thinking mistakes?" | CSV row 5 | Exact match | — |
| 6 | AI I Lens 6: Engineer the Prompt | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 6 | Wed: *Statistics Done Wrong* / Fri: *Understanding Statistics and Experimental Design*, Q: "How do we know something is true?" | CSV row 6 | Exact match | — |
| 7 | AI I Lens 7: Research and Retrieve (RAG) | `ai_fluency` stage list ("retrieve sources") | Source-supported adaptation | Same caveat. |
| 7 | Wed: *Understanding by Design* / Fri: *Rethinking Grading*, Q: "How do we design meaningful learning?" | CSV row 7 | Exact match | — |
| 8 | AI I Lens 8: Reason | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 8 | Wed: *The Pragmatic Programmer* / Fri: *Clean Code*, Q: "What does professional software craftsmanship look like?" | CSV row 8 | Exact match | — |
| 9 | AI I Lens 9: Generate | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 9 | Wed: *Refactoring* (delivered) / Fri: *Clean Architecture* (book of record, Fall Break skip) | CSV row 9 | Exact match | Holiday handling matches Step 6's Friday-holiday policy. |
| 10 | AI I Lens 10: Critique | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 10 | Wed: *Software Engineering* / Fri: *Agile Software Development*, Q: "How do teams build quality software?" | CSV row 10 | Exact match | — |
| 11 | AI I Lens 11: Verify | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 11 | Wed: *Software Project Management* / Fri: *Growing Object-Oriented Software, Guided by Tests*, Q: "How do projects become reliable products?" | CSV row 11 | Exact match | — |
| 12 | AI I Lens 12: Revise | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 12 | Wed: *Getting Things Done* / Fri: *Joy on Demand*, Q: "How do professionals sustain performance?" | CSV row 12 | Exact match | — |
| 13 | AI I Lens 13: Decide | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 13 | Wed: *97 Things Every Programmer Should Know* / Fri: *How to Win Friends and Influence People*, Q: "How do professionals work with others?" | CSV row 13 | Exact match | — |
| 14 | AI I Lens 14: Automate | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 14 | Wed: *Docs for Developers* / Fri: *Prompt Engineering for Generative AI*, Q: "How do we communicate with humans and AI?" | CSV row 14 | Exact match | Neither title was individually confirmed present in `curriculum_rag_supporter --list-books` by Report 002; both are present as source files in `curriculum_rag_supporter/books/` (the ePub and PDF respectively), confirmed by this task's directory listing. |
| 15 | AI I Lens 15: Measure | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 15 | Wed: *The LLM Engineer's Handbook* (book of record) / Fri: *AI Engineering* (book of record), Thanksgiving Wed+Fri skip | CSV row 15 | Exact match | Holiday handling matches Step 6; see Report 002 Query 7 for the open pedagogical (not fidelity) question about this double-skip. |
| 16 | AI I Lens 16: Reflect and Improve | `ai_fluency` stage list | Source-supported adaptation | Same caveat. |
| 16 | Wed: *Generative AI Design Patterns* / Fri: *Semester Reflection*, Q: "What kind of professional do I want to become?" | CSV row 16 | Exact match | — |
| 17 | No Monday Moments / Professional Minds content (finals) | `course-development-flow.md` Step 6 | Exact match | Policy-compliant, no CSV row expected for finals week. |

## Monday Moments Findings

All 16 lens names and their sequence order match, concept-for-concept, the
only located AI I fragment (`ai_fluency/prompts/001_ai_i_source_walk.md`'s
16-item verb list). No week is a mismatch or contradicts that fragment.
However, this fragment is a bare stage-name list with no big questions,
sourcing, or lesson content — it is not the "AI I: Thinking with AI" course
document `course-development-flow.md` Step 3 calls the source of truth. The
planner's per-week big questions and technical tie-ins were therefore
authored to be *consistent with* the stage names, not verified against a
richer source, because no richer source exists. Classification for every
Monday Moments row is "source-supported adaptation," not "exact match" —
reserving "exact match" for cases verifiable against a full original
document, which this is not.

## Professional Minds Findings

Full, unqualified success: all 16 weeks' Wednesday/Friday books and
essential questions are exact, verbatim matches to `professional_minds.csv`,
including both holiday weeks where the planner correctly records a
skipped session's "book of record" rather than inventing a live delivery.
Report 002's finding that this fidelity "could not be confirmed" is now
resolved — it can be confirmed, and it holds.

## Corrections to Report 002

A dated update note has been added near the top of Report 002 (see that
file) stating:

- `professional_minds/professional_minds.csv` is no longer missing — it
  was pulled 2026-07-14 (commit `2f3bfad`) and this report's reconciliation
  confirms all 16 weeks match it exactly.
- The AI I: Thinking with AI course document remains unlocated even after
  the `ai_fluency` pull — this part of Report 002's finding is **not**
  stale.
- ROADMAP.md's "six decisions" language has been corrected (see below) to
  match the larger number of topics actually named across ROADMAP.md and
  Report 002's own Decisions list.
- Report 002's own text is otherwise left as historical record, per this
  task's instruction not to erase what was accurate at the time.

## Remaining Source Gaps

1. The AI I: Thinking with AI full course document (16 weeks of lens + big
   question + supporting content) — still not located anywhere under
   `/data/git`. The `drive_raw_pull_2026-07-14` bundle a prior Codex report
   claims to have produced does not exist on disk.
2. 15 of 16 Professional Minds books have no slurp, DNA card, or lesson
   (only *Make It Stick* has a slurp). Source PDFs/ePub exist in
   `curriculum_rag_supporter/books/` for all 16 CSV titles, confirmed by
   this task's directory listing (title-by-title fuzzy match, not opened
   for content).
3. `professional_minds/templates/book_slurp.md` and
   `professional_minds/prompts/generators/create_book_slurp.md` are empty —
   there is no documented slurp template; the format currently exists only
   as a convention demonstrated by `make_it_stick.md`.

## Recommended Planner Changes

None newly identified by this task. This task made no changes to
`planning/*.md` per its scope limits; Report 002's existing recommendations
(Week 5–6 pacing, Week 9 checkpoint placement, Week 16 redistribution,
Thanksgiving makeup question) stand unchanged and are not superseded by
anything found here.

## Decisions Jeremy Must Make

Unchanged in substance from Report 002's six items (see that report's
"Decisions Jeremy Must Make" section), with one update: **Decision 4 (AI I
doc fidelity) remains genuinely blocked** — the document still needs to be
located, re-derived from source, or explicitly declared superseded by the
`ai_fluency` stage-name fragment (a real but much thinner substitute) before
fidelity can be assessed. This task did not resolve Decision 4; it confirmed
it is still open.

## Immediate Next Steps

1. Decide whether to keep searching for the original AI I: Thinking with AI
   document (e.g., re-run the Drive export that `course_foundry`'s codex
   report claims already happened once, since its output no longer exists
   on disk) or to formally adopt the `ai_fluency` stage-name fragment as the
   working substitute and note the reduced fidelity guarantee.
2. Begin the book-slurp production pass for the remaining 15
   `professional_minds.csv` titles, at whatever cadence Jeremy sets
   (Report 002 recommended a 2–3 week lead time ahead of each week taught).
   This is grunt/production work suited to Worker delegation per
   `AGENTS.md`, with Architect review before each slurp is trusted.
3. Once slurps exist, continue the Book Slurp → DNA Card → 15-Minute Lesson
   pipeline per `professional_minds/ROADMAP.md`.

## Commands Run

```bash
find /data/git/professional_minds -maxdepth 4 -type f | sort
find /data/git/ai_fluency -maxdepth 5 -type f | sort
git -C /data/git/professional_minds status --short --branch
git -C /data/git/professional_minds log --oneline -10
git -C /data/git/ai_fluency status --short --branch
git -C /data/git/ai_fluency log --oneline -10
grep -rli "thinking with ai" /data/git --include="*.md"
grep -rli "professional_minds_integrated_plan\|integrated plan" /data/git --include="*.md"
find /data/git/Jeremy_Corpus -maxdepth 6 -iname "*ai_i*" -o -iname "*thinking*ai*" -o -iname "*professional_minds*"
ls -la /home/jevert/git/ ; readlink -f /home/jevert/git ; readlink -f /data/git
find /data/git/curriculum_rag_supporter/books -maxdepth 1 -type f | sort
grep -rn "Define the Problem|Gather Context|Select the Right Model|Reflect and Improve" /data/git --include="*.md"
ls -la /data/git/computer_science_1/reports/
git -C /data/git/computer_science_1 status --short --branch
git -C /data/git/computer_science_1 log --oneline -5
```

## Files Changed

- `computer_science_1/reports/004_source_reconciliation_and_slurp_status.md`
  (this report, new).
- `computer_science_1/reports/002_pre_semester_readiness_and_literature_audit.md`
  — dated update note added near the top; no other text altered.
- `computer_science_1/ROADMAP.md` — updated to reflect the resolved CSV
  finding, the still-open AI I document gap, and the corrected decision
  count.
- `computer_science_1/START_HERE.md` — updated so it no longer points at
  Report 002 as the next unfinished task.

No files were changed in `professional_minds`, `ai_fluency`,
`course_foundry`, or `curriculum_rag_supporter` — all were read-only
inspections, per scope limits. No new slurps were created (see "Slurps
Created or Updated" above for why).

## Known Limitations

- This task did not create any new book slurps. 15 of 16 Professional Minds
  books remain un-slurped; this is a known, tracked gap, not something this
  report resolves.
- The "source-supported adaptation" classification for all 16 Monday
  Moments rows reflects the genuine absence of a full AI I source document,
  not a defect in the planner — the planner cannot be more verified than its
  source allows.
- This task did not re-attempt the Drive export the prior Codex scaffolding
  report claims to have produced. It only confirmed that export's claimed
  output does not currently exist on disk; it did not investigate Google
  Drive itself to determine whether the original source documents (an "AI
  I: Thinking with AI" Doc and a "Professional Minds Integrated Plan" Doc)
  still exist there. That would require Drive access this task did not use.
- Two titles (`Docs for Developers`, `Prompt Engineering for Generative
  AI`) were matched to source files in `curriculum_rag_supporter/books/` by
  filename only, not opened or content-verified, consistent with Report
  002's own disclosed scope limit on this point.
- The seven-query literature audit from Report 002 was not rerun, per this
  task's instructions; its findings stand unchanged.

## Ready-for-Review Status

Ready for Jeremy's review. This report makes no `planning/*.md` changes and
resolves one of Report 002's two missing-source findings (the CSV) while
confirming the other (the AI I document) is still genuinely open — it does
not make Decision 4 on Jeremy's behalf.

# Report 002: Pre-Semester Readiness and Literature Audit

## Executive Summary

The 17-week Fall 2026 planner (`planning/week-01.md` … `week-17-finals.md`) is
internally consistent, follows `course_foundry/planning/course-development-flow.md`'s
method correctly in most places, and broadly matches the historical pacing
described in `docs/curriculum/course-sequence.md`. It is not yet ready to
teach from without revision. Three of the four weeks ROADMAP.md flagged
(Weeks 5–6, Week 16) show real pacing or load risk; Week 9 and Weeks 12–13
are lower-risk than the prompt implied. Two source documents the planner
depends on — the AI I: Thinking with AI course doc and
`professional_minds/professional_minds.csv` — cannot currently be located on
disk, which blocks verifying Monday Moments' and Professional Minds'
fidelity to their stated sources. Monday Moments entries and Professional
Minds 15-minute lessons remain unwritten (confirmed on disk), consistent
with `ROADMAP.md`. The literature audit (Section 4) was **not blocked** —
`curriculum_rag_supporter`'s ChromaDB/Ollama stack was already running and
the corpus is ingested (29 books) — and all seven queries returned
retrieval-grounded answers, though two answers included content that reads
as the model's own synthesis rather than a direct source citation; those are
flagged explicitly below rather than presented as sourced findings.

**Overall verdict: Ready with revision.** See the Readiness Verdict section
for the per-area breakdown.

## Scope and Sources Reviewed

Read in full, per the task's required reading list: `/data/git/START_HERE.md`,
`/data/git/AGENTS.md`, `computer_science_1/START_HERE.md`, `README.md`,
`ROADMAP.md`, `reports/001_planning_status.md`,
`reports/003_canvas_capability_planning.md`,
`prompts/001_pre_semester_readiness_and_literature_audit.md`,
`course_foundry/planning/course-development-flow.md`,
`docs/philosophy/teaching-patterns.md`, `docs/curriculum/course-sequence.md`,
and all 17 files in `planning/`. Also inspected: all 9 files in `lessons/`,
all 6 files in `assignments/`, `monday_moments/` (README + template only),
`professional_minds/` (as a sibling repo — `lessons/week01/`…`week16/` and
`books/slurps/`), and `curriculum_rag_supporter/` (live query run). Report
001's own `002_...` slug never landed as a file — confirmed via `ls -la
reports/` before starting, which is why this report claims the 002 number
cleanly.

## Current Course Readiness

- The 17 week files and 9 lesson files exist and are internally consistent
  with each other and with `docs/curriculum/course-sequence.md`'s historical
  chapter order (print/input → variables/types → branching → loops →
  functions → strings → collections → classes Round 1/2 → tools/reflection).
- `course_foundry/planning/course-development-flow.md` (the method doc) is
  present and was used correctly for holiday-status labeling in every week
  file that has a non-"full week" status (Weeks 4, 9, 15, 17) — see Holiday
  and Shortened-Week Review below.
- Two sources the method doc names as inputs are **not currently present on
  disk anywhere under `/data/git`**:
  - The "AI I: Thinking with AI" course document (`course-development-flow.md`
    Step 3 calls it "the source of truth for Monday content"). A repo-wide
    `grep -rli "thinking with ai"` found only references to its name in
    `course-development-flow.md`, this prompt, and one `course_foundry`
    report — never the document itself.
  - `professional_minds/professional_minds.csv` (Step 4's input for
    Wednesday/Friday anchors). `find` across `/data/git` returns nothing;
    Report 001 previously noted an *untracked* copy existed briefly in
    `professional_minds/` and was never committed — it is gone now.
  - **Practical implication:** the Monday/Wednesday/Friday anchors already
    baked into `planning/week-01.md`…`week-16.md` cannot be re-verified
    against their stated sources. This doesn't mean they're wrong — the
    content reads as plausible and consistent — but it cannot be confirmed
    as source-faithful with the source docs missing. **Blocked pending
    evidence**, not a pass/fail finding.

## Week-by-Week Risk Review

Full read of all 17 week files (see planning/ in Scope above). Outside the
four explicitly flagged groups, no additional overload risks stood out —
Weeks 1–3, 7–8, 10–11, 14, and 17 each carry one technical unit (or explicit
review/finals status) plus the standard Monday/Wednesday/Friday anchors and
a single due item, matching the course's historical one-unit-per-week-ish
cadence from `docs/curriculum/course-sequence.md`.

## Flagged Weeks

### Weeks 5-6

**What students are expected to learn:** Week 5 — loops (`for`/`while`,
ranges, accumulators, sentinels, off-by-one/non-terminating diagnosis, per
`lessons/04-loops.md`). Week 6 — loops *continued*, plus functions
introduced (parameters, return values, decomposition, per
`lessons/05-functions.md`) in the same week.

**What students are expected to complete:** Week 5 — weekly coding practice,
chapter 5. Week 6 — weekly coding practice, "chapter 6 start."

**The specific overload or pacing risk:** Week 6 is not a clean "loops
week 2" — it stacks a brand-new concept (functions) onto an unfinished one
(loops still being consolidated) in the same week. This is the exact
combination the literature audit flagged as risky (see Literature Audit
Findings, Query 3): introducing a new conceptual/technical framework before
the prior skill is fluent increases extraneous cognitive load. `Chapter 6
start` as the Week 6 due item (versus `chapter 6` in Week 7) suggests the
planner's own author anticipated this and split the assignment — but the
lesson content itself (Weekly Focus) is still doubled up in one week.

**Recommended change:** Either (a) give loops a full two weeks and push
functions' introduction to start in Week 7 alongside its current
continuation, compressing something else instead (Section 3 of the prompt
already asks Jeremy to decide what would compress — collections, at 2 full
weeks for one chapter, is the most plausible candidate), or (b) keep the
current split but make Week 6's Weekly Focus explicitly "functions
introduction only" with loops treated as review/practice, not new content.

**Requires Jeremy's decision:** Yes — this is exactly Section 3, Decision 1
("pacing risk tolerance... is that the right trade, or should something
else compress instead").

### Week 9

**What students are expected to learn:** Strings continued (no new lesson
content beyond `lessons/06-strings.md`, which was already introduced Week
8).

**What students are expected to complete:** Coding Odyssey checkpoint 1
(`assignments/coding-odyssey-project.md` — a staged creative project:
submit a working version, explain changes, demonstrate it).

**The specific overload or pacing risk:** Week 9 is a Friday-holiday week
(Fall Break begins Wed 10pm; only Monday and Wednesday meet). Per
`course-development-flow.md` Step 5, project checkpoints belong in
shortened weeks rather than new technical material — and that principle is
followed here (no new lesson content is introduced). However, this is also
the *first* Coding Odyssey checkpoint, landing in a week with one fewer
class meeting than normal. First checkpoints of a staged project typically
carry more overhead (deciding project scope, first-time submission
mechanics) than later ones. This is a real but modest risk, lower than
Weeks 5–6 or 16.

**Recommended change:** Consider moving Coding Odyssey checkpoint 1 to Week
10 (a full week immediately following), leaving Week 9 as pure
consolidation/practice on strings, consistent with the shortened-week
principle in Step 5 but without adding a first-time project deadline to a
short week.

**Requires Jeremy's decision:** Yes, but lower-priority than Weeks 5–6 or
16 — this is a milder version of the same risk category.

### Weeks 12-13

**What students are expected to learn:** Week 12 — classes/objects/modules
Round 1 (constructor, `self`, one method). Week 13 — classes/objects/modules
Round 2 (composition vs. inheritance, multi-class/module design).

**What students are expected to complete:** Week 12 — weekly coding
practice, chapter 9 Round 1. Week 13 — weekly coding practice, chapter 9
Round 2, plus a pair-programming session.

**The specific overload or pacing risk:** Lower than the prompt's framing
suggested. `docs/curriculum/course-sequence.md` explicitly documents that
classes are "commonly split into Round 1 and Round 2" historically — this
is the one unit in the whole planner with the clearest, named historical
precedent for a two-week, two-round treatment. Unlike Weeks 5–6, each week
here has one clear focus (no second new concept stacked in). The only
mild addition is Week 13's pair-programming session layered onto Round 2,
but pair programming is a delivery mode, not new conceptual material.

**Recommended change:** None needed — this pairing is well-supported by
documented historical practice.

**Requires Jeremy's decision:** No — this is a clear editorial confirmation,
not an open risk. Flagging it as resolved so it doesn't linger as an open
question.

### Week 16

**What students are expected to learn:** No new technical material —
Coding Odyssey checkpoint 3 (final creative-project pass) and the full
professional-pathway artifact set.

**What students are expected to complete:** Coding Odyssey checkpoint 3
(working, demoable, playable project + reflection, per
`assignments/coding-odyssey-project.md`) **and** the entire
`assignments/professional-pathway-artifacts.md` set in the same week:
unofficial transcript, advisor/degree check, semester-by-semester degree
plan, resume, dream-job/role research, skill-gap analysis, GitHub and
LinkedIn profile work, plus a full show-and-tell of the Coding Odyssey and
the kickoff of `assignments/final-reflection.md`.

**The specific overload or pacing risk:** This is the clearest overload
case in the planner. Week 16 is nominally a "full week," so it received no
shortened-week accommodation, but it is stacking a major staged-project
final checkpoint, a seven-artifact professional-pathway set, a full
show-and-tell, and the start of the final reflection — all in the single
week directly before finals, when students are also under load from other
courses. Week 15 immediately prior is explicitly a "light week —
consolidation... no new technical material" with "no new assignment due;
independent work time only," which is real slack sitting unused one week
before the crunch.

**Recommended change:** Move some of the professional-pathway artifacts
(the parts least tied to a specific in-class moment — transcript, degree
check, degree plan, resume) into Week 15's already-open independent-work
time, leaving Week 16 for the Coding Odyssey final push, show-and-tell, and
the artifacts most naturally tied to the end of the semester (dream-job
research, skill-gap analysis, LinkedIn/GitHub, final reflection kickoff).

**Requires Jeremy's decision:** Yes — redistributing due items across
weeks is a real scheduling change, and Section 3 doesn't explicitly ask this
question, so it's a new one this audit surfaces rather than one already on
Jeremy's list.

## Holiday and Shortened-Week Review

Compared each non-"full week" status against `course-development-flow.md`
Step 6's three defaults.

| Week | Current plan | Policy | Adjustment recommended |
|---|---|---|---|
| 4 (Sep 7–11, Labor Day) | Monday holiday; AI I Lens 4 folded into a brief intro ahead of Wednesday's Professional Minds conversation, per the week file's own note. | "Monday holiday — fold a brief version of that week's Monday-Moments lens intro into Wednesday." | None — followed correctly. |
| 9 (Oct 12–16, Fall Break) | Friday holiday; Friday's Professional Minds row (book: *Clean Architecture*) is recorded but not delivered; Fun Friday/show-and-tell skipped, not made up. | "Friday holiday — Fun Friday / show-and-tell is skipped that week, not made up. The week's Friday book/question stay recorded for continuity." | None — followed correctly. |
| 15 (Nov 23–27, Thanksgiving) | Wed+Fri holiday; both books recorded as "book of record" but not delivered; no Professional Minds content that week. | "Wed+Fri holiday — Professional Minds is skipped entirely that week. Its row in the CSV stays assigned to the week number for record-keeping." | None as literally written — but see the Literature Audit finding for Query 7 below, which raises a substantive (not just compliance) question about whether "skip, don't make up" is the right call for Thanksgiving week specifically, since it drops *two* Professional Minds sessions at once, not one. |
| 17 (Dec 7–11, finals) | No new Monday Moments or Professional Minds content. | "finals week — no Monday-Moments or Professional Minds content." | None — followed correctly. |

All four shortened/finals weeks are policy-compliant as literally written.
The one substantive question — whether skipping Professional Minds entirely
for a double session (Thanksgiving) carries a real pedagogical cost worth a
partial makeup — is a literature-informed question, not a compliance gap;
see Literature Audit Findings, Query 7.

## Alignment Across Plans, Lessons, and Assignments

- Every `planning/week-NN.md` "Weekly Focus" line correctly cites the
  matching file in `lessons/` (verified by cross-reading all 17 week files
  against all 9 lesson files).
- Every "Due this week" item that names an assignment correctly points at an
  existing file in `assignments/` or `quizzes/`.
- `docs/philosophy/teaching-patterns.md`'s documented tone (effort-based,
  demonstrative grading; two-week late windows; informal/relational
  instructor tone; AI as a tool requiring understanding, not a substitute)
  is not contradicted anywhere in the 17 week files — none of them specify a
  stricter grading posture or a harder deadline policy than what the archive
  shows. This is a confirmation, not a gap.
- One structural note: `docs/planning/` still exists as an empty
  (`.gitkeep`-only) directory, separate from `planning/`. This is already
  Section 2's explicit open task ("Decide whether `docs/planning/`... should
  be merged into `planning/` or kept as a distinct home for something
  else") and remains unresolved — no new information surfaced here beyond
  confirming the directory is still empty.

## Missing Content Review

### Monday Moments

**What currently exists:** `monday_moments/README.md` (931 bytes, writing
guide) and `monday_moments/template.md` (405 bytes, entry template). No
week-by-week entry files exist.

**What is planned:** Each week file's Monday section names an AI I lens and
a technical tie-in, implying 16 week-by-week Monday Moments entries
(`week-01.md`…`week-16.md`, following the existing template) are expected
eventually.

**What is missing:** All 16 entries.

**Recommendation:** See Content-Authoring Recommendation below.

### Professional Minds

**What currently exists:** `professional_minds/lessons/week01/`…`week16/`
directories, each containing only `.gitkeep` — confirmed by direct
directory listing, zero content files in any of the 16. `professional_minds/
books/slurps/make_it_stick.md` is the only book-pipeline artifact that
exists anywhere (Book Slurp → DNA Card → 15-Minute Lesson pipeline
described in the ROADMAP). No DNA cards and no 15-minute lessons exist for
any book, including Make It Stick.

**What is planned:** Two Professional Minds sessions per week (Wacky
Wednesday, Fun Friday) for 16 weeks = up to 32 book/lesson pairings named in
the week files (fewer where holidays reduce delivery), each needing a
15-minute lesson built through the production pipeline.

**What is missing:** All 15-minute lessons for all 16 books/weeks (Make It
Stick has only the first pipeline stage — a slurp — done; nothing further).

**Do not treat this as "one book done, fifteen to go" — it's "zero books
have a deliverable lesson,"** since a slurp alone isn't classroom content.

## Content-Authoring Recommendation

Given the confirmed on-disk state (zero Monday Moments entries, zero
Professional Minds 15-minute lessons, one partial pipeline artifact) and
the Aug 17, 2026 start date, a strict "complete everything before the
semester" plan means authoring 16 Monday Moments entries and running the
full three-stage Professional Minds pipeline (Slurp → DNA Card → Lesson)
for 16 books twice over (32 book-lesson pairs, since Wednesday and Friday
each use a different book) between now and Aug 17 — a large volume of new
authored content in a short window, and exactly the kind of grunt/production
work `AGENTS.md` says should go to a delegated Worker rather than be
hand-authored end to end.

**Recommendation:** maintain a fixed lead-time buffer rather than either
extreme (front-load everything, or build strictly just-in-time). A
2–3-week lead time (author/produce each week's Monday Moments entry and
both Professional Minds lessons no later than 2–3 weeks before that week is
taught) gives a real buffer against falling behind mid-semester — the
failure mode Section 3, Decision 3 explicitly calls out as worse than
starting slightly under-prepared — while not requiring all 16+32 pieces
finished before day one. Given the Codex/golem delegation policy already
standing in this workspace, the mechanical parts of the Professional Minds
pipeline (running Slurp/DNA Card generation once a book is chosen) are a
good candidate for Worker dispatch, with the Architect (Jeremy or an agent
under his direction) reviewing each 15-minute lesson before it's used in
class.

**This is a recommendation, not a decision made on Jeremy's behalf** —
Section 3, Decision 3 names content-authoring cadence as explicitly his
call.

## Literature Audit Method

Ran per the prompt's exact instructions against
`/home/jevert/git/curriculum_rag_supporter` (same path as
`/data/git/curriculum_rag_supporter`, confirmed identical inode listing).

```bash
cd /home/jevert/git/curriculum_rag_supporter
source .venv/bin/activate
python query.py --list-books
```

The corpus was **already ingested and ChromaDB/Ollama were already
running** — no diagnostics or troubleshooting were needed. `--list-books`
returned 29 books including all titles named in the prompt (How Learning
Works, Make It Stick, Mindset, Understanding by Design, Teach Students How
to Learn, and others), plus zyBooks/Deitel-equivalent material as "Intro to
Python for CS & Data Science" (932 chunks) and "Programming in Python 3" (4
chunks — very thin). Note: *Limitless Mind*, *Resilience Education*,
*Critical Thinking*, *Thinking Fast and Slow*, and several other titles
named in the week files are present; a few week-file book titles (e.g.
*The LLM Engineer's Handbook*, *AI Engineering* — present; *Docs for
Developers*, *Prompt Engineering for Generative AI* — not confirmed in the
`--list-books` output) were not individually cross-checked against the
full 29-title list beyond what's shown above; that cross-check was out of
scope for the seven required queries.

Each of the seven required queries was run verbatim with
`python query.py --top-k 5 "<question>"`.

## Literature Audit Findings

### Query 1 — Spaced retrieval practice length/frequency

**Question:** What does the research say about the right length and
frequency for spaced retrieval practice in an introductory programming
course?

**Sources returned:** Unnamed excerpt attributed to Rawson and Kintsch
(2005), cited as pp. 168–169 of a source the tool did not name explicitly
in this run (context indicates *How Learning Works* or *Make It Stick*,
consistent with the corpus list, but the tool's own citation line only
reads "Excerpt 5, pp. 168–169" without a book title).

**Findings:** Spaced practice (vs. massed practice) improves retention,
especially on delayed tests; spacing should be "significant" (the
retrieved example cites roughly a week). No hard number for session length.

**Conflicting/mixed evidence:** None surfaced against itself; the answer
is consistent but the citation is incomplete (excerpt-numbered, not
book-titled).

**Strength of evidence:** Moderate — grounded in a named study
(Rawson & Kintsch 2005) but the source book title wasn't captured in this
run's output.

**Practical implication:** Supports the current design's basic shape (a
weekly Monday Moments + twice-weekly Professional Minds cadence is
"spaced," not massed) but doesn't validate the *specific* once/twice-weekly
frequency as optimal versus some other spacing.

**Recommended course response:** Supports current design; no change
indicated.

### Query 2 — Understanding by Design backward sequencing vs. branching/loops order

**Question:** What does Understanding by Design say about sequencing a
course backward from desired outcomes, and does introducing branching
before loops (or loops before functions) match that principle?

**Sources returned:** Wiggins & McTighe, *Understanding by Design*, pp.
232–233; *Discrete Mathematics*, p. 31 (conditional statements); a further
excerpt on LLM planning (not clearly sourced to a named book in this
output).

**Findings:** Backward design starts from outcomes, then assessments, then
activities — it does not itself prescribe unit-to-unit sequencing like
"branching before loops." The corpus does not answer the specific ordering
question.

**Conflicting/mixed evidence:** None — the corpus is simply silent on the
specific ordering question asked.

**Strength of evidence:** Weak/inconclusive for the actual question asked.
The retrieval surfaced real backward-design principles but could not
connect them to the branching-vs-loops ordering.

**Practical implication:** No literature-grounded verdict on whether
branching-before-loops is correct; this remains an internal-consistency
question, not one this corpus can answer.

**Recommended course response:** Inconclusive from this corpus — do not
change sequencing on this basis.

### Query 3 — Cognitive load of new framework + new technical material together

**Question:** What do How Learning Works and Make It Stick say about
cognitive load when introducing a new conceptual framework (like the AI I
lens sequence) alongside new technical material in the same class session?

**Sources returned:** *How Learning Works*, pp. 145–146 and pp. 144–145
(citing Clarke et al. 2005 on spreadsheet-skills-plus-new-math-concepts
overload); *Understanding by Design*, pp. 228–229 (metacognitive prompts).
**Make It Stick was not directly quoted in this run** — the tool's own
answer explicitly says its Make It Stick-attributed points are "implied"
and reflect the book's known themes rather than a retrieved excerpt.

**Findings:** Combining a new technical skill and a new conceptual
framework in one session risks overloading working memory (grounded in
Clarke et al. 2005, retrieved from *How Learning Works*). Recommends
building fluency in one before layering the other.

**Conflicting/mixed evidence:** None on the *How Learning Works* portion;
the Make It Stick portion is not actually evidence — it's the tool
inferring likely content rather than quoting a retrieved chunk, and is
flagged here rather than reported as a sourced finding.

**Strength of evidence:** Moderate for the *How Learning Works* half only;
the Make It Stick half should be treated as unsupported by this run and
excluded from any decision.

**Practical implication:** Directly relevant to Weeks 1, 5, and especially
6 (loops continuing + functions introduced same week) — this is the
strongest literature support in the whole audit for the Week 6 concern
raised above.

**Recommended course response:** Suggests a change — see Week 5–6
recommendation above.

### Query 4 — Ideal length/structure of a 10-15 minute mid-lecture insert

**Question:** What does the literature say about the ideal length and
structure of a short (10-15 minute) mid-lecture insert for sustaining
attention and retention?

**Sources returned:** Unnamed excerpt, pp. 64–65 (study-cycle structure:
goal → active task → break → review) and pp. 72–73 (paraphrasing/
elaborative rehearsal) — book titles not captured in this run's citation
line.

**Findings:** The retrieved material describes a 10–15 minute *break*
inside a longer (50–60 minute) study session, not a 10–15 minute
*instructional insert* embedded in a lecture. The retrieval is topically
adjacent (same 10–15 minute duration, same attention/retention concern)
but is answering a related-but-different question than the one asked.

**Conflicting/mixed evidence:** The retrieved framing (break/recovery) and
the actual Professional Minds format (an active book-discussion segment)
are not the same thing, though the tool's synthesis blurs them together
without flagging the mismatch itself.

**Strength of evidence:** Weak — mismatched retrieval; treat as
inconclusive rather than as support either way.

**Practical implication:** No firm literature grounding either for or
against the current 10–15 minute Wacky Wednesday / Fun Friday format.

**Recommended course response:** Inconclusive from this corpus.

### Query 5 — Growth-mindset framing timing (Week 3 placement)

**Question:** What do Mindset and Limitless Mind say about introducing
growth-mindset framing early versus late in a course, and does Week 3's
placement (right before a Labor-Day-shortened week) fit that guidance?

**Sources returned:** *Limitless Mind*, pp. 77–78, pp. 99–101, pp. 75–76
(Carol Dweck's revised thinking on effort-praise and "false growth
mindset"), pp. 129–130 (early-success opportunities and pre-assessment).

**Findings:** The literature favors introducing growth-mindset framing
early and consistently, with early success opportunities to build efficacy.

**Conflicting/mixed evidence:** None on the substance; the retrieved answer
did not specifically address timing relative to a holiday-shortened week,
so the "fit" verdict is the tool's own extrapolation, not a direct
citation.

**Strength of evidence:** Moderate for "introduce early" generally; weak
for the specific Week 3-before-Labor-Day placement question, which the
corpus doesn't address directly.

**Practical implication:** Week 3's placement (early, Week 3 of 16) is
broadly consistent with "introduce early," but the corpus offers no
specific guidance about proximity to a holiday.

**Recommended course response:** Supports current design in general
placement (early); no specific change indicated regarding the Labor Day
adjacency.

### Query 6 — New syntax/concept load per week for true beginners

**Question:** What does the introductory-programming pedagogy literature
(zyBooks/Deitel or equivalent) say about how much new syntax/concept load
is reasonable in a single week for a true beginner?

**Sources returned:** Deitel, *Intro to Python for Computer Science and
Data Science*, pp. 44–46 (immediate-feedback interactive mode, Self-Check
Exercises); Henney, *97 Things Every Programmer Should Know*, pp. 114–116
(true fluency in a language "takes months of use, even if part-time");
*Software Project Management*, pp. 141–142.

**Findings:** The retrieved excerpts support small, iterative, immediately-
tested chunks of new material and caution that real fluency takes sustained
time, not a single week. **No source excerpt specifies a numeric hour
count.** The tool's answer includes a specific figure — "no more than
10–15 hours of direct instruction and hands-on practice" — that is **not
attributable to any cited excerpt**; it is the model's own estimate. This
number is flagged here explicitly and should not be treated as a literature
finding.

**Conflicting/mixed evidence:** None in the actual excerpts; the fabricated-
looking numeric estimate is the only issue, and it is excluded from the
finding below.

**Strength of evidence:** Moderate for the qualitative claim (small
iterative chunks, sustained practice over "months"); the numeric claim
should be disregarded as unsourced.

**Practical implication:** Supports the general principle behind Weeks
5–6's concern (stacking loops + functions in one week works against
"small, iterative, tested chunks") without adding a specific hour-based
threshold to enforce it by.

**Recommended course response:** Supports the qualitative concern already
raised for Weeks 5–6; do not adopt the "10–15 hours" figure as a
literature-backed number.

### Query 7 — Pedagogical cost of skipping vs. rescheduling a spaced-practice/reflection session on a holiday

**Question:** What does the literature say about the pedagogical cost of
skipping a spaced-practice or reflection session entirely (versus
rescheduling it) when a holiday falls midweek?

**Sources returned:** Excerpt pp. 64–65 (intense study sessions,
neuronal-connection framing); pp. 81–82 (consistency of practice, even
brief); *Understanding by Design*-attributed excerpt pp. 329–330 ("gourmet"
curriculum development framing); pp. 23–24 (attention vs. distraction); pp.
183–184 ("positive learning gains achieved in one burst may not be well
retained if not interspaced," recommending additional practice
opportunities later in the semester to compensate for a disrupted period).

**Findings:** The corpus does not address the exact scenario (a
holiday-driven full skip) directly, but multiple excerpts converge on the
same implication: disrupting an established spaced-practice routine
carries a real retention cost, and the literature (p. 183–184 excerpt
specifically) recommends *compensating* with additional later practice
rather than simply absorbing the loss.

**Conflicting/mixed evidence:** None between excerpts; all point the same
direction.

**Strength of evidence:** Moderate — several independent excerpts converge,
though none addresses the holiday-skip scenario by name.

**Practical implication:** This is the one query result that most directly
questions a specific policy default: the course-development-flow.md Step 6
"skip, don't make up" rule for Wed+Fri holidays (Thanksgiving, Week 15 in
this planner) drops *two* Professional Minds sessions in the same week with
no compensating practice, which is the exact pattern the retrieved
literature flags as costly.

**Recommended course response:** Suggests a change — specifically,
consider a lightweight makeup or consolidation touchpoint for the
Thanksgiving week's two skipped Professional Minds sessions (not
necessarily full sessions — even a short catch-up reference in Week 16
would address the "compensate later" recommendation). This is a policy
change to `course-development-flow.md`, which this prompt explicitly
prohibits editing directly — it is reported here as a recommendation for
Jeremy, not applied.

## Evidence-to-Course Decision Matrix

| Finding | Evidence source | Verdict | Action |
|---|---|---|---|
| Loops+functions stacked in Week 6 | Query 3 (moderate) + Query 6 (moderate, qualitative only) | Suggests a change | Jeremy's decision (Section 3, Decision 1) |
| Week 9 checkpoint 1 in a shortened week | Repository evidence (course-development-flow.md Step 5) | Editorial risk, policy-compliant but tight | Jeremy's decision (lower priority) |
| Weeks 12–13 classes Round 1/2 | Repository evidence (course-sequence.md historical precedent) | Supports current design | No action needed |
| Week 16 project + 7-artifact professional pathway stacked pre-finals | Repository evidence (assignment files + week file) | Clear overload risk | Jeremy's decision (new question, not in Section 3) |
| Holiday policy compliance (Weeks 4, 9, 17) | Repository evidence (course-development-flow.md Step 6) | Policy followed correctly | No action needed |
| Thanksgiving double-skip (Week 15) | Query 7 (moderate) | Suggests a change | Jeremy's decision |
| AI I course doc and professional_minds.csv missing from disk | Repository search (grep/find, negative result) | Blocked pending evidence | Cannot verify Monday/Wed/Fri content fidelity until located |
| Monday Moments entries | Repository evidence (directory listing) | Confirmed missing (0 of 16) | Content-authoring recommendation above |
| Professional Minds 15-minute lessons | Repository evidence (directory listing) | Confirmed missing (0 of 16, 1 partial slurp) | Content-authoring recommendation above |
| Spaced retrieval cadence (Query 1) | Moderate | Supports current design | No action needed |
| Backward-design ordering (Query 2) | Weak/inconclusive | Inconclusive | No action needed |
| 10–15 min insert format (Query 4) | Weak/mismatched | Inconclusive | No action needed |
| Growth-mindset Week 3 timing (Query 5) | Moderate (general), weak (specific) | Supports current design | No action needed |

## Decisions Jeremy Must Make

Carried forward from the prompt's Section 3, plus one new item this audit
surfaced:

1. **Pacing risk tolerance** — what compresses if loops/functions get
   separated in Weeks 5–6 (prompt's Decision 1; this audit's literature
   findings weakly support making a change here).
2. **Holiday policy** — confirm or revise the three defaults, specifically
   whether Thanksgiving's double-skip should get a compensating touchpoint
   (prompt's Decision 2, sharpened by this audit's Query 7 finding).
3. **Content-authoring order** — front-load, lead-time buffer, or
   just-in-time for Monday Moments and Professional Minds (prompt's
   Decision 3; this report recommends a 2–3 week lead-time buffer, but the
   call is Jeremy's).
4. **AI I doc fidelity** — cannot currently even be evaluated; the source
   document isn't located (prompt's Decision 4, now blocked on locating the
   file, not just deciding fidelity).
5. **Section scope** — online section `COMSC-1033-1414` in scope now or
   later (prompt's Decision 5, unchanged by this audit).
6. **New: Week 16 redistribution** — whether to move some professional-
   pathway artifacts into Week 15's open independent-work time, as
   recommended above.

## Recommended Revisions

Concrete and specific, per the prompt's requirement — none applied to
`planning/*.md` or `course_foundry/planning/*.md`, per the prompt's explicit
prohibition:

1. Week 6: either split functions' introduction out of the loops-continued
   week, or explicitly relabel Week 6's loops content as review/practice
   only.
2. Week 9: consider moving Coding Odyssey checkpoint 1 to Week 10.
3. Week 15/16: move transcript/degree-check/degree-plan/resume artifacts
   from Week 16 into Week 15's currently-unused independent-work time.
4. `course-development-flow.md` Step 6: consider a compensating touchpoint
   for Thanksgiving week's double Professional Minds skip (a policy change,
   flagged for Jeremy, not applied here).
5. Locate or re-derive the AI I: Thinking with AI course document and
   `professional_minds/professional_minds.csv` (or their replacements) so
   the existing Monday/Wednesday/Friday anchors in `planning/` can be
   source-verified.

## Readiness Verdict

| Area | Verdict |
|---|---|
| Overall planner structure and internal consistency | Ready |
| Weeks 5–6 pacing | Ready with revision — requires Jeremy's decision |
| Week 9 pacing | Ready with revision — lower priority |
| Weeks 12–13 pacing | Ready |
| Week 16 pacing | Not ready as currently sequenced — requires Jeremy's decision |
| Holiday policy compliance | Ready |
| Holiday policy substance (Thanksgiving) | Ready with revision — requires Jeremy's decision |
| Source-document fidelity (AI I doc, Professional Minds CSV) | Blocked pending evidence |
| Monday Moments content | Not ready — 0 of 16 entries exist |
| Professional Minds content | Not ready — 0 of 16 lessons exist (1 partial slurp) |
| Literature audit | Complete (not blocked) |

**Overall: Ready with revision.** The planner is a sound skeleton but
should not be taught from as-is until Jeremy resolves the Decisions list
above and the two content gaps (Monday Moments, Professional Minds) get a
committed authoring cadence.

## Immediate Next Steps

1. Jeremy reviews this report's Decisions list and the Week 6 / Week 16
   recommendations specifically.
2. Locate or re-derive the AI I course doc and `professional_minds.csv` (or
   confirm they were intentionally superseded by something else already in
   `planning/`).
3. Once Section 3 decisions land, a follow-up prompt applies any approved
   changes to `planning/` (explicitly out of scope for this report per the
   prompt's requirements).
4. Start Professional Minds/Monday Moments content authoring at the
   recommended 2–3-week lead time, per the Content-Authoring Recommendation
   above — Week 1 content should be ready well before Aug 17, 2026.
5. Per Report 003's sequencing recommendation, hold off on Canvas
   population until 1–4 above are further along.

## Commands Run

```bash
ls -la reports/
cd /home/jevert/git/curriculum_rag_supporter
source .venv/bin/activate
python query.py --list-books
python query.py --top-k 5 "What does the research say about the right length and frequency for spaced retrieval practice in an introductory programming course?"
python query.py --top-k 5 "What does Understanding by Design say about sequencing a course backward from desired outcomes, and does introducing branching before loops (or loops before functions) match that principle?"
python query.py --top-k 5 "What do How Learning Works and Make It Stick say about cognitive load when introducing a new conceptual framework (like the AI I lens sequence) alongside new technical material in the same class session?"
python query.py --top-k 5 "What does the literature say about the ideal length and structure of a short (10-15 minute) mid-lecture insert for sustaining attention and retention?"
python query.py --top-k 5 "What do Mindset and Limitless Mind say about introducing growth-mindset framing early versus late in a course, and does Week 3's placement (right before a Labor-Day-shortened week) fit that guidance?"
python query.py --top-k 5 "What does the introductory-programming pedagogy literature (zyBooks/Deitel or equivalent) say about how much new syntax/concept load is reasonable in a single week for a true beginner?"
python query.py --top-k 5 "What does the literature say about the pedagogical cost of skipping a spaced-practice or reflection session entirely (versus rescheduling it) when a holiday falls midweek?"
find /data/git -iname "*professional_minds*.csv"
grep -rli "thinking with ai" /data/git --include="*.md"
git status --short --branch
git log --oneline -5
```

## Files Changed

- `reports/002_pre_semester_readiness_and_literature_audit.md` — this
  report (new).
- `ROADMAP.md` — status update and stale-text removal (see next commit;
  edited immediately after this report per the task's ROADMAP cleanup
  step).

No files under `planning/`, `course_foundry/planning/`, `lessons/`,
`assignments/`, `monday_moments/`, `professional_minds/`, or any other
report were modified, per the prompt's and task's explicit scope limits.

## Known Limitations

- The literature audit's citations, as returned by `query.py`, are
  frequently excerpt-numbered ("Excerpt 5, pp. 168–169") without a captured
  book title in the same line. Where the source book was inferable from
  context (matching page ranges/authors named in the answer text) it is
  named above; where it was not clearly inferable, this report says so
  rather than guessing.
- Two of the seven query results (Query 3's Make It Stick attribution,
  Query 6's "10–15 hours" figure) contain content that is the retrieval
  tool's own synthesis rather than a directly retrieved, sourced claim.
  Both are explicitly flagged in their respective sections and excluded
  from the findings actually relied on.
- This report did not independently verify every book title named in
  `planning/week-01.md`…`week-16.md` against `--list-books`'s full output
  beyond a spot check — a handful of Professional Minds titles (e.g. *Docs
  for Developers*, *Prompt Engineering for Generative AI*) were not
  individually confirmed present or absent in the corpus, since that
  wasn't one of the seven required queries.
- The AI I course document and `professional_minds/professional_minds.csv`
  could not be located, so their content-fidelity questions (Section 2's
  first bullet, Section 3 Decision 4) remain genuinely unresolved rather
  than answered — this is reported as a blocker, not silently skipped.
- No changes were made to `planning/*.md`, `course_foundry/planning/*.md`,
  `lessons/`, `assignments/`, `monday_moments/`, or `professional_minds/`,
  per the prompt's and task's explicit prohibition — all findings above are
  recommendations for a follow-up prompt, not applied changes.

## Ready-for-Review Status

Ready for Jeremy's review. This report makes no planning-file changes and
no autonomous decisions on the six items listed in "Decisions Jeremy Must
Make" — it surfaces evidence and recommendations only, consistent with the
prompt's requirement not to make major instructional decisions on his
behalf.

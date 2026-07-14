# Prompt 001 — Pre-Semester Readiness and Literature Audit

## Context

`planning/week-01.md` … `week-17-finals.md` and `course_foundry/planning/course-development-flow.md`
now exist, assembled from four sources: the SWOSU Fall 2026 academic
calendar, `docs/curriculum/unit-map.md`, the AI I: Thinking with AI course
doc, and `professional_minds/professional_minds.csv`. Coursework begins
**Monday, Aug 17, 2026** for `COMSC-1033-1415`.

The planner is a first assembly pass, not a reviewed final. Before it's
trustworthy enough to teach from, three things need to happen: (1) Jeremy
reviews and corrects the pacing/holiday calls a person, not an agent, should
make; (2) a handful of concrete pre-semester tasks get done; (3) the design
gets checked against the actual pedagogy literature already ingested in
`curriculum_rag_supporter`, not just against internal consistency.

## Task

Work through the four sections below in order. Sections 1–3 are read/decide
work for Jeremy. Section 4 is a literature audit an agent can run directly
against `curriculum_rag_supporter` and should produce a written report.

---

## 1. Worth looking at now

- **Read `planning/week-01.md` through `week-17-finals.md` end to end.**
  They were assembled quickly from source docs and have not been proofread
  against actual classroom pacing. In particular:
  - Weeks 5–6 compress "loops" across two weeks and weeks 12–13 compress
    "classes/modules Round 1/2" — confirm two weeks is the right amount of
    time for each, given SWOSU CS I's historical pacing.
  - Week 9 (Fall Break) and Week 16 (last full week) both carry a Coding
    Odyssey checkpoint *and* a full technical/Professional-Minds load —
    confirm that's not overloading a short or a finals-adjacent week.
- **Read the holiday-adjustment policy** in
  `course_foundry/planning/course-development-flow.md` Step 6. It encodes
  three defaults (fold a lost Monday into Wednesday; skip a lost Friday
  without makeup; skip Professional Minds entirely when both Wed and Fri are
  lost, as in Thanksgiving week). These were reasonable defaults chosen
  without your sign-off — confirm or override them.
- **Read `docs/philosophy/teaching-patterns.md`** alongside the new planner.
  It documents that the 2021–2026 archive shows effort-based, demonstrative
  grading with two-week late windows and relational, informal instructor
  tone — confirm the new planner's Due-this-week items and Professional
  Minds cadence don't accidentally introduce a stricter, less relational
  posture than what's historically worked in this course.

## 2. Between now and Aug 17 — task list

- [ ] Approve or revise the week-by-week technical pacing (Section 1).
- [ ] Approve or revise the holiday-adjustment policy (Section 1).
- [ ] Confirm AI I: Thinking with AI content is usable as-is for Monday
      Moments, or flag which weeks need CS-I-specific rewrites (the AI I doc
      is written generically for "students from many majors," not
      CS-I-specific).
- [ ] Decide whether Monday Moments entries (`monday_moments/week-01.md` …)
      get authored before day one or built incrementally week-by-week during
      the semester. If before day one, that's ~16 short lesson entries to
      write using the existing `monday_moments/template.md`.
- [ ] Decide the same question for the Professional Minds 15-minute lessons
      (`professional_minds/lessons/week01/` … `week16/`) — those folders
      exist but are currently empty (`.gitkeep` only). Someone needs to run
      `professional_minds`'s production pipeline (Book Slurp → DNA Card →
      15-Minute Lesson) for each of the 16 books before its week, or accept
      building them just-in-time.
  - As of this writing only `books/slurps/make_it_stick.md` exists in that
    pipeline — Week 2's Wednesday book. The other 15 books/weeks have no
    slurp, DNA card, or lesson yet.
- [ ] Confirm the Fall 2026 section identity: `COMSC-1033-1415`, MWF
      10:00–10:50 AM, Gen. Thomas P. Stafford Center 125 (per the faculty
      portal screenshot in `archive/`) — the planner assumes this section,
      not the parallel online section `COMSC-1033-1414`.
  - If the online section also needs a planner, that's a distinct exercise:
    MWF anchors don't map cleanly onto an asynchronous format, and
    `course_foundry/planning/course-development-flow.md` Step 1 would need
    an "online/async" status alongside full/holiday/finals.
- [ ] Decide whether `docs/planning/` (currently just `.gitkeep`, separate
      from the new `planning/`) should be merged into `planning/` or kept as
      a distinct home for something else, so the repo doesn't end up with
      two same-purpose planning directories.

## 3. User decisions needed

These are calls only Jeremy can make — flagging them explicitly rather than
letting a default stand unexamined:

1. **Pacing risk tolerance.** The 9 durable technical units were spread
   across 16 weeks by compressing some (loops, classes) into shared weeks.
   Is that the right trade, or should something else compress instead
   (e.g., merge collections' two weeks into one, freeing a week for slower
   loops/classes pacing)?
2. **Holiday policy.** Confirm or change the three defaults in Section 1 —
   these directly affect how much Professional Minds content ships this
   term versus gets silently skipped.
3. **Content-authoring order.** Whether Monday Moments and Professional
   Minds lesson content gets front-loaded before the semester or produced
   just-in-time week to week. This is a real cadence commitment, not just a
   scheduling nicety — falling behind mid-semester is a different failure
   mode than starting under-prepared.
4. **AI I doc fidelity.** Whether to use the AI I course doc's lenses and
   labs verbatim, or adapt them more tightly to CS I's actual weekly Python
   topic (the current planner already proposes a one-line "technical tie-in"
   per week, but the labs themselves are still generic).
5. **Section scope.** Whether this planning effort should also cover the
   online section (`COMSC-1033-1414`) now, or stay MWF-traditional-only
   until that's explicitly requested.

## 4. Literature audit — best-practices check via `curriculum_rag_supporter`

`/home/jevert/git/curriculum_rag_supporter` has the actual books ingested
(Make It Stick, How Learning Works, Teach Students How to Learn, Mindset,
Understanding by Design, and the rest of the Professional Minds reading
list, plus zyBooks' *Programming in Python 3* and Deitel's *Intro to
Python*). This section is not opinion about pedagogy — it's a literal
retrieval-grounded check of specific design choices already made in
`planning/`.

**How to run it:**

```bash
cd /home/jevert/git/curriculum_rag_supporter
source .venv/bin/activate   # or: python3 -m venv .venv && pip install -r requirements.txt
scripts/start_chroma.sh     # or: docker compose up -d
python query.py --list-books   # confirm the corpus is actually ingested first
python query.py --top-k 5 "<question>"
```

If the corpus isn't ingested yet (`--list-books` comes back empty), that's
itself a pre-semester blocker to report, not something to route around —
don't fall back to answering from general knowledge instead of the actual
corpus, since the point of this audit is grounding claims in the specific
books Jeremy has already curated.

**Run each of these queries and record the answer plus source citations:**

1. `What does the research say about the right length and frequency for spaced retrieval practice in an introductory programming course?` — checked against the planner's once-per-week Monday Moments + twice-weekly Professional Minds cadence.
2. `What does Understanding by Design say about sequencing a course backward from desired outcomes, and does introducing branching before loops (or loops before functions) match that principle?` — checked against the CS I technical sequence.
3. `What do How Learning Works and Make It Stick say about cognitive load when introducing a new conceptual framework (like the AI I lens sequence) alongside new technical material in the same class session?` — checked against the "Monday = technical topic + AI lens" pairing.
4. `What does the literature say about the ideal length and structure of a short (10-15 minute) mid-lecture insert for sustaining attention and retention?` — checked against Professional Minds' 10-15 minute Wacky Wednesday / Fun Friday format.
5. `What do Mindset and Limitless Mind say about introducing growth-mindset framing early versus late in a course, and does Week 3's placement (right before a Labor-Day-shortened week) fit that guidance?`
6. `What does the introductory-programming pedagogy literature (zyBooks/Deitel or equivalent) say about how much new syntax/concept load is reasonable in a single week for a true beginner?` — checked against weeks that introduce a brand-new technical concept and a brand-new AI lens and a brand-new Professional Minds book pair simultaneously (e.g., Week 1, Week 5).
7. `What does the literature say about the pedagogical cost of skipping a spaced-practice or reflection session entirely (versus rescheduling it) when a holiday falls midweek?` — checked directly against the "skip, don't make up" holiday policy in `course_foundry/planning/course-development-flow.md` Step 6.

**Report the audit** in a new file,
`reports/001_pre_semester_readiness_and_literature_audit_report.md`, using
this shape:

```markdown
# Report 001 — Pre-Semester Readiness and Literature Audit

## Summary
<one paragraph>

## Section 1/2/3 status
<what was reviewed, what decisions are still open>

## Literature audit results
<one subsection per query above: question asked, corpus answer with source
citations, and a one-line verdict — "supports the current design",
"suggests a change", or "inconclusive from this corpus">

## Recommended changes to planning/
<concrete, specific — e.g. "Week N should move X" — not general advice>

## Still open
<anything Section 3's user decisions didn't resolve>
```

## Requirements

- Do not modify `planning/*.md` or `course_foundry/planning/*.md` as part of
  running this prompt — this is an audit and decision-surfacing pass, not an
  implementation pass. Propose changes in the report; apply them in a
  follow-up prompt once Jeremy has weighed in on Section 3.
- Cite the actual book/source for every literature-audit claim. If
  `curriculum_rag_supporter` returns nothing relevant for a query, say so
  in the report rather than filling the gap with unsourced general
  knowledge.
- If ChromaDB or Ollama aren't running locally, report that as a blocker
  with the exact command that failed — don't silently skip Section 4.

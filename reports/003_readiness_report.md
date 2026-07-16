# Report 003 — Pre-Semester Readiness Report (Honest Assessment)

**Date:** 2026-07-15 · **Days until Week 1 (Aug 17):** 33
**Author's note:** Written after independently reading the repo contents, not
by summarizing reports 001/002 — though I checked both and agree with most of
their findings. Where my view differs, I say so.

## Verdict

**Yellow.** The repo is structurally ready and content-light. The planning
layer is genuinely done — 17 date-checked weekly files, a coherent technical
arc, a thoughtful AI-engagement stance — and the new working syllabus draft
(`docs/syllabus.md`) closed the biggest gap report 002 flagged. But almost
nothing in this repo is something a *student* could be handed yet, and the
two-per-week Professional Minds anchors point at lesson folders that are
still empty in the sibling repo. With 33 days left, this is recoverable, but
the recovery path is "make Weeks 1–4 teach-ready," not "deepen everything
uniformly."

## What we have (and what it's actually worth)

| Layer | State | My read |
|---|---|---|
| Weekly planning (17 files) | Complete, date-reviewed | The real asset. Each week has focus, AI lens, book anchors, due items. Trustworthy skeleton. |
| Working syllabus (`docs/syllabus.md`) | New since report 002; thorough draft | Strong draft, honest about its own gaps — ~15 explicit TODOs, all blocked on *decisions/external inputs*, not writing. |
| Lesson outlines (9 files, 137 lines total) | Thin — objectives + one-line content + historical notes | Report 002 calls this a high-priority gap. **I partly disagree**: after 12 semesters teaching this course, the instructor doesn't need scripted lessons. These are adequate instructor skeletons. The gap is student-facing material, not instructor notes. |
| Assignment briefs (6) | Reusable patterns, written in historical/descriptive voice | Not yet handable to students — they describe what assignments *used to be* ("Historical grading pattern...") rather than telling a student what to do this fall. Conversion is mostly a voice/tense rewrite, a small job. |
| Monday Moments | README + template only; 0 of 16 entries | The framing ("AI as tutor, not typist") is the best-articulated pedagogy in the repo. Each entry is a 2-minute read — all 16 could be drafted in one focused session. |
| Quizzes (2), templates (3), prompts (3) | Present, reusable | Fine as-is. |
| Archive (12 Canvas snapshots + files) | Rich provenance | Excellent evidence base. Its job is done; it should not absorb more effort. |
| `portfolio/`, `reflections/`, `tests/`, `docs/planning/` | Empty scaffolds | Empty directories cost nothing, but `docs/planning/` vs `planning/` is a naming trap — retire one. |

## What we're missing — ranked by risk to Aug 17

1. **Professional Minds content (highest risk).** The planner commits to two
   book-anchored sessions *every week* — 32 slots — and the lesson folders in
   `../professional_minds/lessons/week01–16/` are empty. This is the largest
   promised-but-unwritten surface in the whole plan. Mitigation exists: each
   planning file already carries the book + discussion question, so a session
   can run as facilitated discussion from the question alone. **Decision
   needed:** write the 15-minute lessons, or officially downgrade Wed/Fri to
   question-driven discussion for fall and write lessons as-you-go.
2. **Syllabus finalization inputs.** Every TODO in `docs/syllabus.md` is
   waiting on a human or an external source: Faculty Commons template, section
   confirmation, ZyBooks status, grading-weight approval, attendance-policy
   language. No amount of repo work resolves these; they need calendar time
   with the right people/systems. Start now — external dependencies are the
   ones that slip.
3. **Zero runnable code.** This is a programming course and the repository
   contains no Python at all — no worked examples, no starter files, no
   solution references, nothing in `tests/`. Even a handful of Week 1–4
   example programs would let the lesson outlines punch above their weight.
4. **Monday Moments entries.** 0 of 16. Small, fully specified, blocked on
   nothing. Cheapest gap on this list to close completely.
5. **Student-facing assignment instantiation.** The six briefs plus the quiz
   files need converting into "here is what you submit in Week N" language
   with real Canvas locations. Depends partly on item 2.
6. **Repo hygiene.** Four files are untracked, including report 002 and the
   syllabus draft — the two most important recent artifacts are not in
   version control. Also: no README navigation links, and the
   `docs/planning/`-vs-`planning/` duplication.

## My own thoughts (the part you asked for)

- **The meta-to-content ratio is inverted.** Reports, prompts, templates, and
  synthesis documents currently outnumber and outweigh the material a student
  would ever touch. That was the right shape for the archaeology phase, and
  that phase produced real value — but it's done. The next commit that
  matters is one a student could read. I'd treat "no more reports until
  Week 1 is teach-ready" as a working rule (this one included).
- **Don't chase uniform depth.** Seventeen equally-developed weeks by Aug 17
  is neither achievable nor necessary. Weeks 1–4 teach-ready plus the
  finalized syllabus covers the actual exposure window; the course has always
  been built partly in flight, and the planning files make in-flight building
  safe now.
- **The plan is ambitious per-week — decide that on purpose.** Monday AI
  lens + Wednesday and Friday book sessions + technical content + project
  checkpoints is a lot of parallel strands for an intro course. The archive
  shows earlier offerings ran lighter. If fall runs the full stack, fine —
  but it should be a chosen commitment, not a default inherited from the
  planner, because every strand is a weekly content debt.
- **The pedagogy is the repo's quiet strength.** The effort-based grading
  ladder, the AI-as-tutor stance, and evidence-over-claims expectations are
  coherent and consistent across documents. That coherence is worth
  protecting as content gets written fast in the next month.

## Suggested order of work (33 days)

1. This week: commit the untracked files; send the Faculty Commons / section
   / ZyBooks queries (item 2 is the long-lead item).
2. Next: draft all 16 Monday Moments in one pass; make the Professional Minds
   decision (write vs. discussion-mode).
3. Then: make Weeks 1–4 fully teach-ready — student-facing assignment briefs,
   getting-to-know-you quiz finalized, a few runnable example programs.
4. Ongoing through the semester: Weeks 5+ content, staying ~3 weeks ahead.

## Bottom line

We have a well-planned course and a well-documented history. We do not yet
have a course a student can enroll in. The distance between those two is
about one focused month of *writing student-facing material* plus a handful
of external confirmations — which is exactly the month available. The risk
isn't the size of the gap; it's spending the month on more synthesis instead
of on Week 1.

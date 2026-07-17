# Roadmap

This file tracks the ongoing, big-picture state of `computer_science_1` —
what's built, what's open, and what the next concrete step is. Update it as
work lands; don't let it drift into a stale planning doc nobody reads.

This is a new file (created 2026-07-16) — there was no roadmap before this,
only a point-in-time snapshot in `reports/001_planning_status.md`. Treat that
report as history, and this file as the living version going forward.

## Where the course stands (2026-07-16)

- The 17-week Fall 2026 plan (`planning/week-01.md` … `week-17-finals.md`)
  and the nine-lesson technical sequence (`lessons/`) exist and are
  internally consistent.
- The course starts **Monday, Aug 17, 2026** (`COMSC-1033-1415`).

## Real gaps (not just "unreviewed")

1. **Pre-semester readiness decisions are still not made.**
   `reports/002_pre_semester_readiness_and_literature_audit.md` (completed
   2026-07-16) ran the full readiness review and literature audit from
   `prompts/001_pre_semester_readiness_and_literature_audit.md` Sections
   1–4. Sections 1–3 still need Jeremy's read/decide pass — the report's
   "Decisions Jeremy Must Make" section lists **six items**: (1) Weeks 5–6
   pacing/compression, (2) holiday policy — specifically the Thanksgiving
   double-skip, (3) content-authoring cadence, (4) AI I doc fidelity, (5)
   section scope (`COMSC-1033-1414`), and (6) Week 16 redistribution. This
   is more topics than a single "six decisions" label can carry cleanly
   (Week 9's checkpoint placement is a real but explicitly lower-priority
   seventh item folded into the same section, not a formal seventh
   decision) — see Report 002's own text for the full nuance rather than
   treating the count as a flat list.
2. **Literature-grounded audit is done.** Section 4 ran successfully
   against `curriculum_rag_supporter` (corpus already ingested, 29 books;
   no blockers) and all seven queries executed — but evidence quality
   varied query to query (moderate for four, weak/inconclusive for two,
   and two answers included content flagged as the model's own synthesis
   rather than a direct citation). See Report 002's Literature Audit
   Findings section for the per-query strength-of-evidence breakdown; do
   not describe this audit as uniformly "strongly literature-grounded."
3. **Professional Minds lesson content doesn't exist.** Confirmed again in
   Report 002 and re-confirmed in
   `reports/004_source_reconciliation_and_slurp_status.md`: all 16
   `professional_minds/lessons/week01/`…`week16/` folders are still
   `.gitkeep`-only; only one book (*Make It Stick*) has even a first-stage
   slurp, no DNA card or lesson for any book.
4. **Monday Moments entries don't exist.** Confirmed again in Report 002:
   `monday_moments/` still has only `README.md` and `template.md` — 0 of
   16 week entries written.
5. **Source-availability gap: partially resolved, partially still open.**
   Report 002 could not locate either the "AI I: Thinking with AI" course
   doc or `professional_minds/professional_minds.csv` anywhere under
   `/data/git`. Both `professional_minds` and `ai_fluency` were
   subsequently pulled as full repositories and reconciled in Report 004
   (2026-07-16, later same day):
   - `professional_minds.csv` **is now found** (committed 2026-07-14) and
     every one of the 16 weeks in `planning/` matches it exactly — this
     half of the gap is resolved.
   - The AI I: Thinking with AI document **is still not located**, even in
     the newly pulled `ai_fluency` repo (which has only generic
     five-course scaffolding, not the actual 16-week lens document). A
     prior Codex report claimed a Drive raw-pull bundle containing this
     document was created at `drive_raw_pull_2026-07-14/`; that path does
     not exist on disk. This half of the gap remains open and is now more
     specific: it is not "unknown where to look," it is "the document was
     reportedly exported once and the export no longer exists."

## Next step

Jeremy reads `reports/002_pre_semester_readiness_and_literature_audit.md`
and `reports/004_source_reconciliation_and_slurp_status.md`, then works
through Report 002's "Decisions Jeremy Must Make" section (six items,
including the Week 6 and Week 16 pacing risks, the Thanksgiving holiday
policy, and the now-sharpened AI I doc question — locate/re-export it, or
formally adopt `ai_fluency`'s thinner stage-name fragment as the working
substitute). Once those land, a follow-up prompt applies any approved
changes to `planning/` — neither Report 002 nor Report 004 made changes
there.

After the decisions land, the next production step is the Professional
Minds book-slurp pass (15 of 16 books still need a slurp; source PDFs/ePub
for all 16 are already present in `curriculum_rag_supporter/books/`), at
whatever lead-time cadence Jeremy sets.

## After that

Once readiness decisions are made: start filling Professional Minds lesson
content and Monday Moments entries, at the lead-time cadence Jeremy
chooses (Report 002 recommends 2–3 weeks ahead of each week taught, not
full front-loading or strict just-in-time). Canvas population
(`reports/003_canvas_capability_planning.md`) stays sequenced after this,
per that report's own recommendation.

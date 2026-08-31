# CS1 Aug. 31 lecture distillation — Phase 4/5 evidence

Date: 2026-08-31
Course: Computer Science I, Canvas course `74029`
Semantic week: **Week 3 — Growth** (`Aug. 31–Sep. 4`)

## Source and privacy boundary

The protected MP4 was transcribed locally on April with `whisper-ctranslate2 0.5.7`, `medium.en`, English, CPU `int8` after the GPU cuBLAS path failed. The protected transcript remains outside Git:

- Protected transcript: `/home/jevert/lecture_pipeline/protected_raw/2026-08-31/cs1/Fall 2026 Computer Science I (COMSC-1033-1415)-20260831_095929-Meeting Recording.vtt`
- Transcript SHA-256: `2fcfa55c6aee70cfc472a2a68d7830b7503feb55baee25621c564cd757d749b4`
- Protected MP4 SHA-256: `27da85dd0c502352d6707d8adc8e2a31452ad2c0c8c2f8f075df60edcc3e9e86`

The digest and student notes omit student names, chat, incidental audio, and identifying classroom details. The transcript and instructor digest were deliberately published as **unpublished** Canvas module items.

## Durable source artifacts

- `sidecar/lecture_notes/2026-08-31_cs1_lecture_digest.md`
- `presentations/beamer/week03_aug31_lecture_distillation/week03_aug31_lecture_distillation.tex`
- `presentations/beamer/week03_aug31_lecture_distillation/week03_aug31_lecture_distillation.pdf`
- `lessons/2026-08-31_monday_lecture_notes.md`

The deck compiles in two passes with `pdflatex`, produces 12 pages, and has no overfull/error diagnostics. Its title and path now use Week 3 semantics; no assignment source was renamed or moved.

## Canvas mutation

Read-only preflight found exactly one target: module `218505`, `Week 3: Growth`, published, position 1. Existing items were preserved in order. Six items were added at the bottom, with no assignment/module/page/file outside this additive bundle changed:

| Position | Canvas item | ID | Type | Published |
|---:|---|---:|---|---|
| 23 | Aug. 31 Lecture Recording (Optional Archive) | 1531412 | ExternalUrl | yes |
| 24 | Aug. 31 Companion Resource (Optional) | 1531413 | ExternalUrl | yes |
| 25 | Aug. 31 Lecture Distillation — Slides (PDF) | 1531414 | File; file 6578849 | yes |
| 26 | Aug. 31 Lecture Notes — Files, Terminals, and Python | 1531415 | Page | yes |
| 27 | Aug. 31 Lecture Transcript (Instructor Review) | 1531416 | File; file 6578850 | no |
| 28 | Aug. 31 Instructor Lecture Digest (Private) | 1531417 | Page | no |

The two ExternalUrl items point to the two owner-approved SharePoint resources. Their URLs are intentionally not repeated in Git evidence.

Independent readback confirmed:

- module `218505` is still `Week 3: Growth`, position 1, published;
- existing Week 3 items remain the prefix, unchanged in order;
- all six new items have the requested type, title, order, link/file/page identity, and published state;
- Week 2 module `218504` was not targeted and retains its existing item order and contents;
- no assignment was moved, renamed, re-dated, deleted, or recreated;
- existing Week 2 assignment state remains present: `Bonus Practice (Week 02)` assignment `912371` has 1 submitted submission and `week-02` assignment `912372` has 10 submitted submissions; neither was touched;
- the separate `qwen3:8b` Local AI gate report remains unchanged and open.

Final module order readback:

- Week 2 (`218504`, position 7): `01-foundations-print-input`; `02-variables-expressions-types`; `Monday Moment — week_02_gather_context`; `Monday Moment Activity — week_02_gather_context`; `Monday Moment Rubric — week_02_gather_context`; `week 02 wed retrieval practice`; `Slides — Week 02 Wednesday (PDF)`; `week 02 wed reading assignment`; `week 02 wed reading rubric`; `week 02 wed slides assignment`; `week 02 wed slides rubric`; `week 02 fri mindset at work`; `Slides — Week 02 Friday (PDF)`; `week 02 fri reading assignment`; `week 02 fri reading rubric`; `week 02 fri slides assignment`; `week 02 fri slides rubric`; `Bonus Practice (Week 02)`; `Slides — Week 02 Monday (PDF)`; `Slides — Week 02 Monday PM (PDF)`; `week-02`; `week-02_rubric`; `Attendance & Participation`; `Course Evaluation`; `The Judgment-Building Toolkit`.
- Week 3 (`218505`, position 1): existing prefix `03-branching`; `Bonus Practice (Week 03)`; `week-03`; `week-03_rubric`; then the six additive items in positions 23–28 listed above. No existing item was reordered.

## Repeatable pipeline recommendation

Use Teams/OneDrive as the automatic recording inbox, April as the protected ingest/transcription/distillation host, GitHub as the durable de-identified course source, and Canvas as the student front door. The smallest Wednesday/Friday seam is a protected-folder watcher that identifies the new MP4, records its hash, runs the approved local transcription command, and opens a reviewable digest/deck/notes bundle. Keep transcript and instructor digest unpublished by default; publish only reviewed student notes/deck and stable owner-approved archive links. The existing authenticated read-only Microsoft path on April is sufficient for future acquisition; do not add new credentials.

## Scope protections

No Week 2 Start Here page was created. No Week 2/Week 3 assignments, due dates, rubrics, submissions, grades, comments, enrollments, or unrelated modules were changed. The Local AI `qwen3:8b` production gate remains truthful and unresolved.

# CS1 Sept. 2 lecture distillation — evidence

Date: 2026-09-02
Course: Computer Science I, Canvas course `74029`
Module: `218505`, `Week 3: Growth` (position 1)

## Source and privacy boundary

The protected MP4 was transcribed locally on April with `whisper-ctranslate2 0.5.7`, `medium.en`, English, CPU `int8`. The recording is 23:55 long — a shorter session than the Aug. 31 lecture.

- Protected MP4: `/home/jevert/lecture_pipeline/protected_raw/2026-09-02/cs1/Fall 2026 Computer Science I (COMSC-1033-1415)-20260902_095623-Meeting Recording.mp4`
- Protected MP4 SHA-256: `5c2503cdfc4fda01fd77dd56b4acda96082f42fc86f54184c588f51dad4f5425`
- Fresh transcript: same directory, `.vtt`
- Transcript SHA-256: `42a8afaa9812baf7abb505e4551bfceaf1d365738eae86e4d9f0b327ad214509`

The video was staged from the instructor's Downloads on maise, hash-verified on arrival at April's protected ingest tree, and the maise copy was deleted after verification. The digest and student notes omit student names, chat, and identifying classroom details.

## Durable source artifacts

- `sidecar/lecture_notes/2026-09-02_cs1_lecture_digest.md`
- `lessons/2026-09-02_wednesday_lecture_notes.md`
- `presentations/beamer/week03_sep02_lecture_distillation/week03_sep02_lecture_distillation.tex`
- `presentations/beamer/week03_sep02_lecture_distillation/week03_sep02_lecture_distillation.pdf`
- `presentations/beamer/week03_sep02_lecture_distillation/img/` (four de-identified frames)
- this report

The deck reuses the existing `presentations/beamer/theme/preamble.tex`. It compiles to 16 pages with `latexmk -pdf -interaction=nonstopmode -halt-on-error`; the only remaining diagnostics are cosmetic ~10pt overfull-vbox notices from the four full-bleed screenshot frames, the same class of warning the Aug. 31 deck also carried.

## Screenshot evidence and crop proof

Four frames were extracted with `ffmpeg -ss <time> -frames:v 1 -q:v 3` at 1920x1080. Each was cropped to `1560x1080+0+0` (the same fixed crop used for the Aug. 31 CS1 deck), removing the right-edge Teams roster/avatar strip. Each was then masked with a black `drawbox` at `0,1040` sized `180x40` to cover the bottom-left "Evert, Jeremy" screen-share self-label. All four cropped+masked frames were visually inspected; none retain roster avatars, chat, faces, or name text.

| File | Approx. source time | Slide evidence |
|---|---:|---|
| `img/1024_gpt_generated.jpg` | 00:10:24 | Copilot/ChatGPT-generated `frontier_settlement.py` draft |
| `img/1744_paste_warning.jpg` | 00:17:44 | PowerShell multi-line-paste confirmation dialog |
| `img/1815_run_output.jpg` | 00:18:15 | Running the script; settlement report output |
| `img/2045_notepad_view.jpg` | 00:20:45 | Same file opened in Notepad, `if`/`elif`/`else` block |

## Canvas mutation

Read-only preflight against module `218505` found the same 9-item state left by the Aug. 31 run (positions 1–28, with position 27 — the Aug. 31 transcript file item — not returned by the items listing, consistent with its locked/unpublished state; unchanged from before). Five items were additively appended at positions 29–33:

| Position | Canvas item | ID | Type | Published |
|---:|---|---:|---|---|
| 29 | Sept. 2 Lecture Recording (Optional Archive) | 1532287 | ExternalUrl | yes |
| 30 | Sept. 2 Lecture Distillation — Slides (PDF) | 1532288 | File; file 6582711 | yes |
| 31 | Sept. 2 Lecture Notes — Reading and Running AI-Generated Code | 1532289 | Page | yes |
| 32 | Sept. 2 Instructor Lecture Digest | 1532290 | Page | no |
| 33 | Sept. 2 Lecture Transcript (Instructor Review) | 1532291 | File; file 6582712 | no |

The ExternalUrl item posts the exact owner-supplied SharePoint stream URL; it was created unpublished by the module-items API default and explicitly re-published via a follow-up `PUT`, then independently re-read to confirm `published: true` and the exact URL string.

Independent readback confirmed:

- module `218505` is still `Week 3: Growth`, position 1, published;
- positions 1–28 (the pre-existing item prefix, including the Aug. 31 additive block) are byte-for-byte unchanged in id, type, title, and published state;
- all five new items have the requested type, title, order, link/file/page identity, and published state;
- no assignment was moved, renamed, re-dated, deleted, or recreated;
- no other module was touched.

## Preservation and repeatable pipeline

This is the second run of the Wednesday/Friday seam described in the Aug. 31 report: protected ingest on April, local Whisper transcription, de-identified digest/notes/deck, additive-only Canvas write with preflight and readback. The transcript and instructor digest remain unpublished by design; only the recording link, slides, and student notes page are published.

## Scope protections

No existing page, assignment, rubric, submission, grade, enrollment, or unrelated module was changed. Only course `74029`, module `218505`, and the five listed new items were touched.

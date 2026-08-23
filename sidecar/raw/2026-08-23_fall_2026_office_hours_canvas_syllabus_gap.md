# Fall 2026 office-hours / Canvas syllabus evidence gap

Date: 2026-08-23
Status: OPEN EVIDENCE GAP, NOT A COURSE-TIME GAP

## What the repository already knows

The durable course metadata identifies the Fall 2026 traditional section as `COMSC-1033-1415`, meeting M/W/F 10:00-10:50 AM in Stafford Center 125. `docs/syllabus.md` repeats those Self-Service-confirmed facts and identifies the instructor office as Stafford 320.

The online section `COMSC-1033-1414` has already been cross-listed into the production Canvas course for 1415 (`74029`), so the two sections share one Canvas classroom.

The curriculum-wide canonical office-hours source is:

`jeremy-evert/swosu_cs_curriculum/shared/operations/office_hours/README.md`

Current canonical Fall 2026 office hours there are M/W/F 9:00-10:00 AM and 11:00 AM-noon; T/Th 10:00 AM-noon.

## Gap found

`docs/syllabus.md` still says `Office hours: TODO: publish current schedule and appointment instructions`.

The repository does not currently contain a source-backed snapshot/read-back of the Fall 2026 production Canvas **Syllabus** surface showing what students actually see after office-hours publication. Production Canvas credentials are intentionally not assumed or requested for this audit.

## Evidence needed to close the gap

Obtain the current student-facing Syllabus content from production Canvas course `74029` manually, without creating or restoring an API credential. A copied HTML/text export, PDF/print-to-PDF, or clear screenshot set is sufficient. If the Syllabus page is blank or only contains a link, record that exact state rather than filling it from memory.

Then reconcile the Canvas surface and `docs/syllabus.md` against the canonical office-hours source. Do not invent a second office-hours schedule in this repository.

## Not needed from the owner

No class meeting time, classroom, office room, phone number, or office-hours schedule needs to be re-supplied from memory. Those facts already have durable sources.
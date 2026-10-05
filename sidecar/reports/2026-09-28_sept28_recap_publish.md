# CS1 2026-09-28 class recording & recap — publish, and a real blocker

Anna, run `ba8e0940aa62beb521c67300930cb724`, on April.

## What happened

The 9/28 recording hold (see `2026-09-28_HOLD_recording_do_not_publish.md`)
was lifted by Jeremy same-day: he trimmed the recording himself and gave
the real SharePoint link directly to use as the recording source (not
Susie's earlier staged/protected copy of the raw untrimmed file, which
still holds the private conversation and was never meant to be published).

Published, matching the 9/23 precedent (`sept-23-class-recording-and-recap`)
exactly: page `Sept. 28 Class — Recording & Recap`
(`sept-28-class-recording-and-recap`, page id `457087`), live in course
74029, module 218509 ("Week 7: Design"), position 22 (after the existing
`05-functions`/`Bonus Practice`/`week-07`/`week-07_rubric` items). Target
lock verified live before writing. Live:
`https://swosu.instructure.com/courses/74029/pages/sept-28-class-recording-and-recap`

## Real blocker: could not write the recap text

`curl -sIL` on the SharePoint link returns `401 Unauthorized` (confirmed,
raw headers show `x-msdavext_error: ... Access denied. Before opening
files in this location, you must first browse to the web site and select
the option to login automatically.`) — this link requires Jeremy's own
SWOSU SSO session to actually stream/download, which is exactly why
`video_mechanics/scripts/windows_onedrive_signin.ps1` exists as a
separate interactive-login step in the normal pipeline. April has no
such session and no rclone/onedrive client configured, so there's no way
to fetch the video content from here to transcribe it.

I deliberately did **not** fall back to Susie's raw untrimmed Teams
recording's transcript (if one exists) to write the recap — that
recording contains the same private conversation Jeremy is holding back,
so using its transcript, even paraphrased, would defeat the point of the
hold. Fabricating recap content from the lesson plan (`planning/
week-07.md`) instead of what was actually said would also be dishonest
relative to the 9/23 precedent's standard (a real recap of what
happened, not a plan restated).

**The page is live with the recording link and an honest "Recap coming
soon" placeholder** rather than either fabricated or privacy-violating
content. Recap text needs one of:

1. Jeremy dictates a short recap (2-3 sentences, matching the 9/23
   shape: what we covered / key ideas / looking ahead) — fastest path.
2. Someone runs the transcription step from a host where Jeremy (or
   another authorized account) is actually signed into SharePoint/
   OneDrive (the normal `windows_onedrive_signin.ps1` + `transcribe_
   lecture.py` pipeline), against the trimmed file specifically, not the
   raw one.

## Evidence

`/tmp/cs1_0928_recap_publish.json` (page + module item + final module
readback, not committed -- ephemeral API response, no student data).

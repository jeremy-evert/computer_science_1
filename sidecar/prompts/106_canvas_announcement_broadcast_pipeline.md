# Prompt 106 — Build a safe multi-course Canvas announcement broadcast pipeline

**Status:** READY
**Owner:** Foreman dispatch to Codex/Golem
**Origin:** `jeremy-evert/computer_science_1`
**Primary worksite:** `jeremy-evert/course_foundry`
**Canvas boundary:** `jeremy-evert/harbor`
**Mode:** design + implementation + mocked tests only; **no live Canvas writes in this unit**

## Why this exists

Week 1 surfaced a recurring instructor-operations problem: Jeremy may need to send one clear announcement to Computer Science I and, when appropriate, to several or all of his current course shells without manually opening each Canvas course and pasting the same message.

The repository already has the correct production plumbing. `course_foundry/course_foundry/production_deploy.py` provides a production-host guard, explicit course targeting, dry-run/push separation, and a live-confirmation pattern. Harbor is already the single Canvas API boundary for Course Foundry. Do not create a side-channel script that talks directly to Canvas and bypasses those controls.

Harbor's current capability catalog explicitly says that Canvas Announcements are API-available but are **not exposed** through Harbor. That is the missing seam to fill.

The desired end state is simple for the instructor:

1. write one announcement in a Markdown source file;
2. select a named, reviewed target set of Canvas courses;
3. preview exactly what will be sent and exactly where it will go;
4. explicitly confirm a live push;
5. get a per-course receipt proving what happened;
6. safely re-run the command without spraying duplicate announcements everywhere.

This should become shared infrastructure for Jeremy's courses, not a CS1-only one-off.

## Mission

Build a small, safe, reusable announcement-broadcast capability using the existing architecture:

- **Harbor** owns typed Canvas transport for announcements.
- **Course Foundry** owns rendering, target selection, production safety gates, orchestration, idempotency, verification, and receipts.
- **Course repositories** such as `computer_science_1` own announcement source content and, if useful, thin convenience wrappers/configuration only. They must not own raw Canvas HTTP logic.

The MVP must support one announcement body sent to one or more explicitly reviewed current-term course shells in a single invocation.

## Investigation first

Before changing code:

1. Read:
   - `harbor/docs/canvas-capability-catalog.md`
   - `harbor/harbor/client.py`
   - `harbor/harbor/api.py`
   - Harbor course-allowlist tests and list-endpoint tests
   - `course_foundry/course_foundry/production_deploy.py`
   - `course_foundry/course_foundry/savnac_deploy.py`
   - the production-host marker/gate in `imprint`
   - the relevant Course Foundry tests around production deploys and receipts.
2. Check the **current official Instructure Canvas API documentation** for Announcements / Discussion Topics. Do not guess endpoint names, payload fields, delayed-post behavior, or update semantics from memory.
3. Inventory whether Harbor already has generic transport that can be reused cleanly. Add only the smallest dedicated announcement surface necessary.
4. Confirm how cross-listed sections are represented in production so that the broadcaster targets a Canvas **course shell once**, not every section record independently.
5. Confirm current repository conventions for Markdown-to-Canvas HTML rendering before adding a new renderer.

Document any material architectural discovery in the final handoff. Do not broaden the task into general Canvas messaging.

## Architecture requirements

### A. Harbor: expose the Canvas capability, nothing more

Add typed, tested Harbor operations for the minimum announcement lifecycle the broadcaster needs. The exact public function names should follow Harbor's existing conventions, but the surface should cover at least:

- list/read announcements for a single allowlisted course;
- create an announcement for a single allowlisted course;
- update an existing announcement only if update semantics are needed for the idempotency design.

Requirements:

- Reuse Harbor's authenticated request layer.
- Every course-scoped call must pass through the existing course allowlist protection.
- Harbor remains instance-agnostic. No `swosu.instructure.com`, Fall 2026, CS1, Jeremy, or course IDs belong in Harbor.
- Do not expose student enrollments, grades, submissions, private messages, or PII as part of this work.
- Add mocked tests covering request method/path/payload, course allowlist refusal, expected response parsing, and representative Canvas errors.

### B. Course Foundry: build the guarded broadcaster

Create a focused production announcement command/module in Course Foundry. Choose names that fit current conventions; `announcement_broadcast.py` is a reasonable default if no stronger convention exists.

It must reuse the same safety philosophy as `production_deploy.py`:

- production host must match the existing `PRODUCTION_HOST_MARKER`;
- preview/dry-run is the default safe posture;
- a live write requires an explicit command plus an unmistakable confirmation flag such as `--confirm-live`;
- the Canvas client must be allowlisted to **only the exact course IDs in the reviewed target set for that invocation**;
- no mutation is permitted outside those selected course IDs.

Do **not** simply add an `--all` switch that dynamically posts to every course Canvas happens to return. That is too easy to misuse.

### C. Reviewed target manifests

Support explicit, reviewable named target sets. Fit the storage format to existing project conventions rather than forcing YAML if the repository already has a better pattern.

A target entry should contain enough information to catch stale or mistaken IDs, for example:

- logical key;
- Canvas course ID;
- expected course name/course code;
- expected term;
- optional human note.

Provide a **read-only discovery** command or helper that can enumerate Jeremy's current instructor course shells and print or generate a *candidate* manifest. Discovery never implies authorization to post.

Before a push, validate at minimum:

- each Canvas course ID is reachable;
- the live name/code matches the reviewed expectation closely enough to detect an ID mix-up;
- the course belongs to the intended current term;
- the course is not a concluded/historical shell unless the manifest explicitly allows it;
- duplicate Canvas course IDs collapse to one destination so cross-listed sections do not receive duplicate announcements.

Named groups such as `cs1` and `fall-2026-current` are welcome **only after their exact members are reviewed and committed/configured**. A live push must never convert a broad dynamic search directly into recipients.

### D. Announcement source format

Use a human-editable Markdown source file. A simple front matter shape is acceptable, for example:

```markdown
---
title: "Week 1 Reset: Your Semester, Your Degree, Your Career"
id: "2026-08-18-week-1-reset"
---

Hello friends,

...
```

Minimum metadata:

- human-visible title;
- stable announcement ID/slug used for idempotency.

Render Markdown to Canvas-safe HTML using existing shared rendering machinery where possible. Preserve ordinary headings, emphasis, lists, and links. Do not invent a separate HTML dialect if Course Foundry already has one.

Scheduling, attachments, audience segmentation, per-course templating, and course-specific substitutions are **future work**, not MVP requirements.

## Idempotency: reruns must be boring

A broadcaster that duplicates the same announcement every time it is retried is not done.

Use a stable machine marker that survives body edits, plus a source hash. One acceptable design is conceptually equivalent to:

```html
<!-- course-foundry-announcement-id:2026-08-18-week-1-reset -->
<!-- course-foundry-source-sha256:... -->
```

The exact marker format may differ if Canvas sanitization or the official API behavior makes another mechanism stronger.

Required behavior:

- if no existing matching stable ID exists in a target course, plan `CREATE`;
- if the stable ID exists and the source hash matches, plan `UNCHANGED` and do nothing;
- if the stable ID exists but content differs, **do not silently edit it**. Default to a clear refusal or `CHANGED` state and require an explicit update flag such as `--update-existing` before mutation;
- if multiple live announcements somehow carry the same stable marker, refuse that course and report the ambiguity rather than guessing.

This behavior must make a partially failed multi-course push safely resumable.

## Preview UX

Before any live write, print a compact but unmistakable plan including:

- Canvas host;
- announcement source path;
- title;
- stable announcement ID;
- source hash;
- each target course ID and expected/live course name;
- action per course: `CREATE`, `UNCHANGED`, `CHANGED`, `REFUSE`, etc.;
- total destination count;
- explicit statement that no write occurred in preview mode.

A reasonable CLI shape, adjusted to project conventions, would look like:

```bash
python3 -m course_foundry.announcement_broadcast preview \
  --targets fall-2026-current \
  --message /path/to/announcement.md

python3 -m course_foundry.announcement_broadcast push \
  --targets fall-2026-current \
  --message /path/to/announcement.md \
  --confirm-live
```

The exact command is less important than the safety properties.

## Live push behavior

When a later human/Foreman explicitly performs a live push:

1. validate host and reviewed targets again immediately before writing;
2. publish sequentially or with deliberately conservative concurrency;
3. record a result after each course so a mid-run failure does not erase evidence;
4. read the created/updated announcement back from Canvas and verify title + stable ID/source hash when the API permits;
5. print one line per destination with success/failure, Canvas course ID/name, announcement ID, and URL when available;
6. return non-zero on any partial failure;
7. make the run safely resumable through the idempotency rules above.

Do not attempt distributed rollback by deleting successful announcements merely because a later destination failed. Preserve the successful writes, report the partial failure, and make retry safe.

## Receipts and audit trail

Write a non-secret receipt under the existing Course Foundry run/evidence convention. It should contain at least:

- timestamp;
- git commit/source revision if available;
- command mode (`preview` or `push`);
- Canvas host marker, not the token;
- announcement title, stable ID, and source hash;
- reviewed target-set name;
- per-course course ID/name, planned action, result, and returned announcement ID/URL when available;
- aggregate success/failure counts.

Never record API tokens, authorization headers, student lists, submissions, grades, or other student data.

## Scope guardrails

This capability is **announcement-only**.

It must not modify:

- assignments or due dates;
- modules/module items;
- grades/submissions;
- enrollments/sections/cross-listing;
- course publication state;
- course settings;
- inbox/conversation messages;
- existing announcements unless the user explicitly invokes the supported update path.

Do not make an announcement automatically because a Git file changed. There must always be a human-invoked preview and explicit live push.

## Tests

All implementation work in this unit is mocked/offline. **Do not send a live announcement while building this feature.**

At minimum test:

### Harbor

- create/list/update request shape against mocked Canvas transport;
- course allowlist enforcement;
- error propagation/normalization;
- no accidental unscoped endpoint use.

### Course Foundry

- preview performs zero write calls;
- production host guard rejects Savnac/wrong/empty hosts for the production broadcaster;
- push without explicit live confirmation refuses before any write;
- selected target IDs become the exact Canvas client allowlist;
- stale name/term mismatch refuses the destination;
- duplicate/cross-listed target IDs collapse to one destination;
- first run plans/creates once per unique target;
- exact rerun becomes `UNCHANGED` and writes nothing;
- changed source refuses without explicit update permission;
- changed source updates only when that permission is explicit;
- duplicate stable IDs in one course refuse safely;
- one-course failure yields a non-zero overall result while preserving receipts for earlier successes;
- rerunning after partial failure only acts on destinations still needing work;
- receipt output contains no token/authorization data.

Run the focused tests and the relevant full suites for Harbor and Course Foundry. Report exact commands and results.

## Documentation

Add concise operator documentation that answers:

1. How do I discover candidate current courses?
2. How do I review/create a target set?
3. How do I author an announcement?
4. How do I preview it?
5. How do I push it?
6. How do I safely change and re-publish an existing announcement?
7. Where is the receipt?
8. What happens after a partial failure?

Include one harmless mocked/example message in tests/docs. Do not publish the Week 1 announcement as part of implementation.

## Authority

This prompt explicitly authorizes the worker to make the smallest necessary, tested changes in:

- `jeremy-evert/harbor` for the typed Canvas announcement transport;
- `jeremy-evert/course_foundry` for safe multi-course orchestration, rendering integration, targeting, receipts, and tests;
- `jeremy-evert/computer_science_1` only if a thin wrapper/config/example is genuinely useful after the shared capability exists.

Prefer isolated branches/worktrees for every mutating repository. Respect each repository's `AGENTS.md` and existing safety conventions. Do not touch an unrelated dirty main checkout or a directory used by a live service.

## Forbidden

- Live Canvas writes during this implementation unit.
- A new direct `requests`/`httpx` Canvas client in Computer Science I or Course Foundry that bypasses Harbor.
- Weakening `production_deploy.py`, Savnac guards, host markers, or course allowlists.
- A magical dynamic `--all` live recipient mode.
- Posting to historical/concluded courses merely because discovery found them.
- Student-data reads that are unnecessary to determine instructor-owned course shells.
- Any grade, assignment, enrollment, module, cross-listing, or course-setting mutation.
- Secrets in source, config, logs, fixtures, or receipts.
- `git add -A`/`git add .` in a mixed worktree; stage only intended files.

## Acceptance criteria

This prompt is complete when the implementation can demonstrate, entirely with mocks/tests in this unit, that:

1. Harbor has a tested, allowlist-respecting announcement API surface.
2. Course Foundry can discover candidate courses read-only and operate only on a reviewed target manifest.
3. One Markdown announcement can be previewed against multiple unique course shells with zero writes.
4. A live push path exists but is double-gated by the production host check and explicit confirmation.
5. A successful push would create exactly one announcement per unique selected course shell.
6. Exact reruns are idempotent.
7. Changed content cannot silently overwrite the previously published announcement.
8. Partial failure is visible, non-zero, receipted, and safely resumable.
9. Cross-listed/duplicate section references cannot produce duplicate announcements in one Canvas shell.
10. The full change respects Harbor as the only Canvas transport boundary and preserves all existing deployment safety gates.

## Foreman live validation after implementation

**Not part of the worker's implementation unit.** After review and merge, Foreman should separately:

1. perform read-only discovery against production;
2. create/review the exact Fall 2026 target manifest;
3. preview a harmless test announcement against a deliberately chosen sandbox/test course if one exists;
4. inspect the complete preview and receipt;
5. only then consider a narrowly scoped live write;
6. after one-course proof, expand deliberately to the reviewed multi-course target set.

The goal is not merely "send announcements faster." The goal is to make broad instructor communication **fast enough to use and hard to misuse**.

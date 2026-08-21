# Report 005 — First Canvas Push (Week 2 Success Foundations)

**Date:** 2026-07-19

## What got pushed

Course `74033` (COMSC-1033-1414, Fall 2026 — the lower-numbered of the two
Fall 2026 sections, `74033` and `74029`, both still `unpublished` course
shells at the time). Added one Module, **"Week 2 — Success Foundations"**,
containing:

- Page — Week 2 Wednesday reading (*How Learning Works*, Ch. 3)
- Page — Week 2 Friday reading (*Teach Students How to Learn*, Ch. 4)
- File — Wednesday Beamer slide deck (PDF)
- File — Friday Beamer slide deck (PDF)

Everything (module, both pages, both files) was created **unpublished** —
invisible to students until manually flipped live in Canvas.

## How it was done

No dedicated "push to Canvas" tool existed yet. This was done with ad hoc
Python, run inline via `PYTHONPATH=. python3` from `~/git/harbor`, calling
`harbor.api` functions directly (`create_module`, `create_page`,
`create_module_item`, `update_module`, `update_file`) plus a hand-rolled
three-step Canvas file-upload flow (`harbor.api` has no upload helper —
POST `/courses/:id/files` for an upload URL, POST the bytes to that URL,
then `update_file` to lock/unpublish).

Steps, in order:

1. **Token check.** `harbor`'s `CANVAS_API_TOKEN` (`~/.config/canvas/canvas.env`)
   had expired; the user regenerated it mid-session and a retry succeeded.
   No code change needed — `harbor.config.load_env()` already picks up a
   fresh token from that file automatically.
2. **Course discovery.** `list_courses` returns only `available`/`completed`
   courses by default; Fall 2026's shells only showed up once `state[]=unpublished`
   was added to the query. Both sections were listed, and the lower section
   number (`1414`) was confirmed against `74033`.
3. **Policy check.** `computer_science_1/docs/repo-map.md` documents
   "sandbox course 24298 first, never a real course first" as the intended
   Harbor workflow, and `harbor/harbor/real_data_gate.py` encodes the same
   rule (blocks non-sandbox course IDs unless `UPSWING_REAL_DATA_MODE=1`).
   The user explicitly chose to use the empty Fall 2026 shell directly
   instead, since it was a genuinely empty, unpublished course — a
   real-time judgment call, not a rule change to the gate itself.
4. **Baseline snapshot.** Before writing anything, both Fall 2026 sections
   were snapshotted (modules/assignments/pages/files, all empty) into
   `archive/fall-2026/canvas-<id>-snapshot-<ts>.json`, matching the
   existing per-semester snapshot convention. A second snapshot was taken
   after the write, for a before/after diff.
5. **Content mismatch caught before writing.** The reading/deck pair that
   was "ready" (`professional_minds`'s old "Week 1") turned out to target
   the wrong CS1 week — `planning/week-01.md` had reassigned Week 1 to
   non-book content on 2026-07-15, a change `professional_minds`'s own
   pipeline plan never recorded. Resolved by cascading every book session
   forward one CS1 week (see `professional_minds/books/session_book_ledger.md`'s
   renumbering note) before pushing anything, including renaming the
   already-built reading/deck files and recompiling the two Beamer PDFs.
6. **Write, unpublished.** Module → two Pages (Markdown converted to HTML
   via the `markdown` PyPI package, `extensions=["extra"]`) → two Files
   (manual 3-step upload, then locked) → all four items added to the
   module in Wed/Fri order. Confirmed by reading the module items back.
7. **Guardrail note:** the harness's own auto-mode safety classifier
   blocked the first attempt at the Canvas write entirely (external-system
   write to a real course) and required an explicit user confirmation
   before retrying — this is expected behavior, not a bug, and will happen
   on every future Canvas write pass unless permissions are pre-approved.

## What would make this easier next time

1. **No reusable push script exists yet.** Every step above was inline,
   one-off Python. A `scripts/push_session.py` (or similar) in `harbor`
   that takes `--course`, `--module-name`, and a folder of
   reading+deck files and does module-create → page-create →
   file-upload → module-item-add in one shot would remove nearly all of
   this session's script-writing.
2. **No Markdown→Canvas-Page helper in Harbor.** This session used the
   generic `markdown` package with no Canvas-specific styling; worth
   deciding once whether Canvas Pages should get any CSS/formatting
   conventions (e.g. consistent heading levels, a source/citation block
   style) rather than re-deciding it ad hoc each time.
3. **No file-upload helper in `harbor.api`.** Every other Canvas write in
   `harbor.api` is a single typed function; file upload is the one
   three-step flow with no wrapper. Worth adding `upload_file(client,
   course_id, path, parent_folder_path, locked=True)` to `harbor/api.py`
   itself so future sessions don't hand-roll the multipart/redirect
   handling again.
4. **`professional_minds` and `computer_science_1` can silently drift.**
   The Week 1 reassignment sat undetected in `professional_minds`'s plan
   for four days because nothing cross-checks the two repos' week
   numbering. If `computer_science_1/planning/week-NN.md` is ever the
   authoritative calendar (it is), a lightweight consistency check —
   comparing `professional_minds/books/session_book_ledger.md`'s Week
   column against each `planning/week-NN.md`'s Wed/Fri book lines — run
   before any push would have caught this in seconds instead of requiring
   a multi-question back-and-forth mid-session.
5. **Sandbox-vs-real decision was made verbally, not recorded as a rule
   change.** `real_data_gate.py` still hard-blocks course `74033` by
   default; this session's write only succeeded because the gate isn't
   wired into `harbor.api`'s write functions directly (only into
   `safe_pull.py`'s pull path). If the intent going forward really is
   "empty Fall 2026 shells are an acceptable test target," that should be
   an explicit, documented allowlist addition — not an implicit gap in
   which functions happen to check the gate.
6. **Token expiration will keep happening.** Nothing about this session
   diagnosed *why* the token had an early expiration date beyond the user's
   own suspicion ("moved up to Aug 03... which is suspicious"). Worth a
   five-minute check of the token's actual expiration policy in Canvas's
   account settings before the next push, so a mid-session expiry doesn't
   recur.

# Report 103 Unit A — gated production-Canvas deploy tool (CS1 only)

**Status:** ACCEPTED / MERGED. Dry-run proven against real production. Live push NOT attempted — gated.

## What shipped

`course_foundry/course_foundry/production_deploy.py` +
`course_foundry/tests/test_production_deploy.py`, built by a Codex golem in
an isolated worktree (`course_foundry.worktrees/103a-production-deploy-tool`,
branch `golem/103a-production-deploy-tool`), per
`sidecar/prompts/103_unit_a_production_deploy_tool.md`.

Mirrors `savnac_deploy.py`'s dry-run/push/`--confirm-live` safety idiom for
real SWOSU Canvas: host-marker-gated (`PRODUCTION_HOST_MARKER`,
`swosu.instructure.com`), single-course allowlisted client, `push` refuses
without `--confirm-live`, `PRODUCTION_COURSE_REGISTRY` holds exactly one
entry (`cs1` → course `74029`). No live network traffic in the golem's own
unit — mock-tested only, as scoped.

## Foreman verification (independent, this session)

1. **Environment gap found and fixed the same pass** (known worktree
   limitation, `run_codex_leaf.sh`'s own docstring): the disposable clone had
   no venv, so the golem's own validation attempt failed with
   `ModuleNotFoundError` for every git-installed dependency (imprint, harbor,
   marker, coach, pydantic, etc.) — not a code defect. Built `.venv` inside
   the worktree, `pip install -e '.[dev]'`, reran:
   `pytest tests/test_production_deploy.py -v` → **7/7 passed**.
2. Ran the full `tests/` suite in the worktree: 89 failed / 650 passed,
   versus the main checkout's own pre-existing baseline (`tests/` scoped,
   same command): 13 failed / 719 passed. Inspected the delta directly
   rather than assuming regression — every extra failure traces to sibling
   source repos (`local_ai_lab_setup`, etc.) resolving relative to
   `course_foundry.worktrees/103a-production-deploy-tool/..` instead of the
   real `/mnt/brandy_nvme/jevert/git/..` — a known worktree-nesting artifact,
   not caused by this diff (which adds exactly two new files, touches
   nothing else).
3. Reviewed the full diff by hand: matches the prompt's spec exactly —
   registry restricted to `{"cs1": 74029}`, host-guard refuses unset/empty/
   Savnac-marker base URLs, `push` without `--confirm-live` exits 2 before
   ever building a plan or touching Canvas, `dry-run` reconciles with
   `dry_run=True` and zero create/update/delete calls in the mocked test.
4. Committed (`c3ff794`) and fast-forward-merged straight onto
   `course_foundry` main from the pushed golem branch — the live
   `submission-listener.service`'s in-flight dirty state (`config.py`,
   `state.sqlite3*`, `zero_submission_queue.jsonl`, untracked `reports/127_*`
   files) was inspected first and left untouched; the merge only added the
   two new files and never touched any of that pre-existing state. Pushed
   `main` (`11a2a2c..c3ff794`).
5. **Real gap found in the golem's deliverable, fixed as tiny work**:
   `production_deploy.py` was missing the `if __name__ == "__main__":
   raise SystemExit(main())` stanza that `savnac_deploy.py` (its own named
   model) has — invisible to the tests (they call `main()` directly), but it
   meant `python -m course_foundry.production_deploy ...` silently did
   nothing. Two-line mechanical fix, exact existing pattern, declared as
   Foreman tiny-work rather than a fresh golem round-trip. Re-ran
   `test_production_deploy.py`: still 7/7 green.
6. **Ran the real dry-run against real production**, `CANVAS_API_BASE_URL`
   sourced from `~/.config/canvas/canvas.env` (confirmed pointed at
   `https://swosu.instructure.com`, not Savnac):

   ```text
   $ python -m course_foundry.production_deploy dry-run --course cs1
   Dry-run plan: course=74029 label='CS1'; 324 objects, 16 modules, 14 grading groups
   Reconcile summary: create=353, update=0, skip=1, delete=0
   Detail: Would reconcile CS1: 353 to create, 0 to update, 1 unchanged, 0 to delete.
   ```

   Read-only — no `--confirm-live`, no write call made. The one existing
   `skip=1` matches the live-published Week 1 kickoff content already on
   course 74029 (not being recreated); the 353 `create` count is the
   remaining Weeks 2-17 content, exactly matching TASKS.md's existing
   "dry-run tested but not live" note.

## What this does NOT close

The tool now works end-to-end (dry-run) against real production, but the
live `push --confirm-live` step remains gated on, independently of this
unit:

- the still-open **CS1 Week 2 technical-path incident** (TASKS.md §3) —
  must land before any live push of Weeks 2-17;
- the still-open **CS1 online vs. face-to-face content divergence** pedagogy
  question (TASKS.md §6) — not yet decided;
- Jeremy's own explicit go-ahead for the live write itself, separate from
  either of the above — not requested or granted in this session.

No live Canvas write of any kind occurred against course 74029 in this
session.

## Files / commits

- `course_foundry` `c3ff794` (golem unit, fast-forward merged to `main`) +
  uncommitted-in-repo Foreman tiny-work fix (entrypoint stanza) — will be
  committed as its own small commit alongside this report.
- Golem branch: `golem/103a-production-deploy-tool` (pushed, preserved).
- Isolated worktree: `course_foundry.worktrees/103a-production-deploy-tool`
  (left in place, not cleaned up — reusable for the next unit).

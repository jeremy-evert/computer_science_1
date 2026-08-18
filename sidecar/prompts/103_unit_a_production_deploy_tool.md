# Prompt 103 Unit A — Build the gated production-Canvas deploy tool (CS1 only, mock-tested only)

**Status:** READY
**Owner:** assigned Golem (Codex), reviewed/accepted by Foreman
**Worksite:** `jeremy-evert/course_foundry`, via an **isolated disposable clone** at
`/mnt/brandy_nvme/jevert/git/course_foundry.worktrees/103a-production-deploy-tool`
(cross-repo from `computer_science_1`'s Prompt 103, explicitly authorized by
that prompt's "Shared Course Foundry/Harbor repairs are allowed when they
are necessary to complete CS1 correctly and are covered by tests")
**Worker branch:** `golem/103a-production-deploy-tool`
**Mode:** Work (mutating, isolated clone only), isolated branch, **no live credentials, no network calls of any kind — mock-tested only**

**Critical: do not touch `/mnt/brandy_nvme/jevert/git/course_foundry` (the
main checkout, without `.worktrees` in its path).** A real, live
`submission-listener.service` (systemd, 23h+ uptime, polling every 60s) runs
against that exact directory right now — it has its own uncommitted,
in-flight state (`submission_listener/config.py`, `runs/submission_listener/
state.sqlite3*`). This dispatch is pointed at a disposable local clone
specifically so this unit's `git checkout -b` and file writes never touch
that live directory. Confirm you are operating inside the `.worktrees/
103a-production-deploy-tool` path before any write — if `pwd` doesn't show
that path, stop immediately.

`imprint/imprint/config.py`'s `PRODUCTION_HOST_MARKER` constant is already
landed (Foreman tiny-work, commit `7745fe1`) — this unit only needs to
import it, not add it. Do not re-add or edit anything in `imprint`.

## Why this matters

`computer_science_1`'s Prompt 103 requires reconciling real production Canvas
course `74029`. Foreman investigated first (read-only, no mutation) and
found:

1. `course_foundry/course_foundry/savnac_deploy.py` is deliberately,
   correctly hard-gated to Savnac only — it calls
   `require_host_marker(base_url, SAVNAC_HOST_MARKER, ...)`, which raises
   `WrongCanvasHostError` on any non-Savnac `CANVAS_API_BASE_URL`. **Do not
   weaken, remove, or bypass this guard.** It is exactly correct as-is.
2. `imprint/imprint/config.py`'s `require_host_marker` function is already
   written generically ("Callers pass their own expected host (e.g.
   `SAVNAC_HOST_MARKER`, or a real production host once one exists)") — it
   was built anticipating exactly this need.
3. `cs1_savnac_desired_course(course_repo_path, course_id=1)` in
   `course_foundry/course_foundry/cs1_desired_course.py` already takes
   `course_id` as a plain parameter — it is not Savnac-specific in
   implementation, only in its (legacy) name.
4. The real production Canvas host is `swosu.instructure.com` (this is a
   public university domain name, not a secret — safe to hardcode as a
   comparison marker the same way `SAVNAC_HOST_MARKER` is).
5. The real, locked production target for CS1 is course id `74029` (per
   `computer_science_1/sidecar/reports/102_cs1_online_launch_recon_and_target_lock.md`
   and `102A_cs1_online_cross_list_into_1415.md`, both GREEN).

This unit builds a new, narrowly-scoped, explicitly-labeled production
deploy tool mirroring `savnac_deploy.py`'s existing dry-run/push/
`--confirm-live` safety idiom exactly, restricted **today** to CS1 only —
do not add Architecture/DSCT/CS2 to the production registry in this unit,
even though `savnac_deploy.py`'s `COURSE_REGISTRY` has entries for them.
Those courses each need their own target-lock evidence (their own
Prompt-102 equivalent) before they belong in a production registry; adding
them speculatively here would be exactly the kind of scope-creep this
tightly-gated tool exists to prevent.

**This unit produces no live Canvas traffic whatsoever.** Every test uses a
mocked `CanvasClient`/HTTP layer. Foreman will independently review the full
diff, then separately and personally run the tool's `dry-run` mode against
real production on host (the one step that needs the real token) before any
live write is even considered — that is a later, separate, foreman-direct
step, not part of this unit.

## Task

0. Run `pwd` and confirm it shows the `.worktrees/103a-production-deploy-tool`
   path, not the bare `course_foundry` path. Then run `git status --short`.
   Ignore untracked files under wherever `run_codex_leaf.sh`'s own raw
   receipt lands — anything else modified/untracked means stop and report
   instead of proceeding. Then run
   `git checkout -b golem/103a-production-deploy-tool`.

1. Create `course_foundry/course_foundry/production_deploy.py`, structured
   as closely as possible to `savnac_deploy.py` (reuse its `SourcePaths`,
   `DeploymentError`, `_build_cs1`, `_git_head` equivalents by importing
   them from `savnac_deploy` rather than duplicating logic, where that's
   clean to do — duplicate only what genuinely must differ):

   - `PRODUCTION_COURSE_REGISTRY: dict[str, CourseSpec] = {"cs1": CourseSpec(course_id=74029, builder=_build_cs1)}`
     — exactly one entry, CS1 only.
   - `build_plan(course, paths=None, *, course_id=None)` — same shape as
     `savnac_deploy.build_plan`, but resolving against
     `PRODUCTION_COURSE_REGISTRY`.
   - `_production_client(course_id)` — same shape as `_savnac_client`, but:
     - guards with `require_host_marker(base_url, PRODUCTION_HOST_MARKER, tool_name="production deployer")`
       instead of `SAVNAC_HOST_MARKER`;
     - still restricts the resulting `CanvasClient` to exactly the one
       `course_id` via `CanvasConfig(config.api_base_url, config.api_token, frozenset({course_id}))`
       — this single-course allowlist restriction is not optional, it is
       the main structural safety property of this tool.
   - `main(argv=None)` — same `dry-run` / `push` subcommand shape as
     `savnac_deploy.main`, with `push` still requiring `--confirm-live`.
     Only `--course cs1` is valid today (reject anything else with a clear
     `DeploymentError`, do not silently ignore).
   - A short module docstring stating plainly: this is the production
     (real SWOSU Canvas) counterpart to `savnac_deploy.py`; the Savnac
     version's guard must never be weakened as an alternative to writing
     this file; today it supports CS1 (course `74029`) only, by design —
     adding another course here requires that course's own target-lock
     evidence first.

2. Write tests in `course_foundry/tests/test_production_deploy.py`
   (mirroring `tests/test_savnac_deploy.py`'s mocking approach — no real
   network calls anywhere in the test suite) covering at minimum:

   - `_production_client`/the guard refuses when `CANVAS_API_BASE_URL` is
     unset, empty, or contains the Savnac marker instead of
     `swosu.instructure.com` (raises `WrongCanvasHostError`).
   - `main(["push", "--course", "cs1"])` (without `--confirm-live`) exits
     nonzero and performs no write.
   - `main(["dry-run", "--course", "cs1"])` builds a plan and calls the
     reconcile path with `dry_run=True`, and the test asserts (via the
     mock) that no create/update/delete Canvas API call was actually
     attempted.
   - `PRODUCTION_COURSE_REGISTRY` contains exactly the one `"cs1": 74029`
     entry — a test that fails loudly if someone adds another course later
     without updating this test deliberately.
   - `build_plan("architecture")` (or any course not in the registry)
     raises `DeploymentError` — proves the registry restriction is
     enforced, not just documented.

## Authority

- Create `course_foundry/course_foundry/production_deploy.py`.
- Create `course_foundry/tests/test_production_deploy.py`.
- Operate only inside the isolated clone at
  `course_foundry.worktrees/103a-production-deploy-tool` — never the bare
  `course_foundry` path.

## Forbidden

- Any file or directory outside the isolated clone, especially
  `/mnt/brandy_nvme/jevert/git/course_foundry` itself (the live-service
  directory).
- Any change to `imprint/` (already landed) or to
  `course_foundry/course_foundry/savnac_deploy.py` or its existing guard
  behavior.
- Any real network call, live or mocked-as-live, against any Canvas
  instance, real or Savnac, anywhere in this unit's code or tests.
- Adding Architecture, DSCT, or CS2 to `PRODUCTION_COURSE_REGISTRY`.
- Touching `computer_science_1`, `harbor`, or any other repo.
- `git add -A`/`git add .` — stage only the two files named above.

## Validation (acceptance test)

```bash
python3 -m pytest course_foundry/tests/test_production_deploy.py -v
```

All new tests must pass. Also run the full existing suite to confirm no
regression:

```bash
python3 -m pytest -q
```

Paste both outputs in full.

## Evidence destination

Do not write a report file — answer in your final chat message only: files
changed, both pytest outputs in full, and branch/commit pushed.

## Done when

- `course_foundry/course_foundry/production_deploy.py` and
  `course_foundry/tests/test_production_deploy.py` created exactly as
  specified, inside the isolated clone only;
- new tests pass, full suite has zero regressions;
- committed to `golem/103a-production-deploy-tool` and pushed. If `git
  commit` fails with "Author identity unknown" (a known container plumbing
  gap), leave the change staged on the branch and say so explicitly —
  Foreman will complete the commit after independent review.

## On blocker

Stop and report the exact blocker in your final message. Do not guess, do
not broaden scope, do not attempt any real network call to work around a
test difficulty.

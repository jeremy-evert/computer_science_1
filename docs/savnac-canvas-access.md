# Pushing to Savnac Canvas from a Claude session on Brandy

Savnac is a private lab Canvas instance — a separate VM (`savnac`) on a
machine called Brandy, not SWOSU's real Canvas and not even the `harbor`
sandbox course (24298) inside it. It's a whole separate Canvas install with
no real student data possible, ever. It's the safest possible rung to push
against, ahead of 24298, ahead of anything real — see `docs/repo-map.md`'s
`harbor` entry for the existing "24298 first, never a real course first"
policy this extends.

This repo (`computer_science_1`) has no Canvas or Harbor code of its own,
and shouldn't grow any: `harbor` is what talks to Canvas, `course_foundry`
is what calls `harbor` and points it at a course repo's `course_repo_path`.
This doc is about how *that pipeline*, run from a Claude Code session on
Brandy, reaches Savnac specifically.

## The three-repo shape

- `harbor` (`~/git/harbor` on Brandy) — the actual Canvas API client.
  `harbor/config.py` reads `CANVAS_API_BASE_URL` / `CANVAS_API_TOKEN` from
  the environment; nothing about which Canvas instance it's talking to is
  hardcoded anywhere in it. See `harbor/docs/savnac.md` for the full
  detail behind this section.
- `course_foundry` (`~/git/course_foundry`) — the orchestrator. Its
  `n001_select_course_and_repo` node uses a per-`course_id` adapter
  registry (`load_adapters.py`); an adapter takes `course_repo_path` as a
  call-time argument and does the actual push via `harbor`. As of
  2026-07-20 no adapter is registered yet for this repo's course id(s) —
  that's the next real piece of work, not yet built.
- `computer_science_1` (this repo) — pure content. No Python, no Canvas
  awareness. An adapter reads whatever it needs from here via
  `course_repo_path`; this repo never calls `harbor` or `course_foundry`
  itself.

## Why Brandy specifically

Savnac's Canvas (`http://192.168.122.172:3000`) is only reachable directly,
with no SSH tunnel, from Brandy — `savnac` is a VM on Brandy's own libvirt
NAT network. A Claude session (or any script) running elsewhere would need
an active tunnel first. Running the push from Brandy avoids that step
entirely.

## Pointing Harbor at Savnac (from Brandy)

Savnac's credentials live at `~/.config/canvas/savnac.env` on Brandy —
never loaded automatically (unlike the real SWOSU credentials at
`~/.config/canvas/canvas.env`, which Harbor's `load_env()` falls back to
by default). Source it explicitly before running anything Harbor-related:

```bash
set -a; source ~/.config/canvas/savnac.env; set +a
cd ~/git/harbor
PYTHONPATH=. python3 scripts/list_modules.py --course 1
```

Course id `1` is Savnac's test course, "Computer Science I (Savnac test)"
(`COMSC-1033-SAVNAC`), created 2026-07-20. It is unpublished, so it won't
appear via Harbor's `list_courses()` (that filters to `available`/
`completed` state) — use `GET /api/v1/accounts/1/courses` to see it
regardless of state. This id is Savnac-specific and must never become a
hardcoded constant in this repo or in whatever adapter eventually gets
written for it, same as 24298 or a real course id — it's only valid
because it pairs with Savnac's `CANVAS_API_BASE_URL`.

## Viewing the result: the Faith tunnel "magic"

Pushing from Brandy doesn't need a tunnel, but *looking at the result in a
browser* does — Firefox runs on Faith, not Brandy. From a terminal on
Faith:

```bash
ssh -L 3002:192.168.122.172:3000 jevert@10.2.0.48
```

Then open `http://localhost:3002/login/canvas`. Notes that cost real time
to work out once already (full detail in the `Savnac` repo's
`requirements/REQ-001/runbook.md`):

- `3002` is arbitrary — pick any free local port on Faith. It does not
  need to match Savnac's `3000`.
- `10.2.0.48` is Brandy's management-network address, reachable from Faith
  via mgmt's WireGuard routing. Brandy's own `wg0` (`10.8.0.2`) is a
  stale, unrelated network — don't use it.
- Login: `admin@savnac.local`, password in
  `~/.canvas-savnac-admin-credentials` on Brandy (mode 600, not in any
  repo). The Canvas API token Harbor uses is in the same file.

## What's not done yet

No load adapter exists for this course in `course_foundry` yet, so nothing
currently pushes `computer_science_1`'s actual content (lessons, planning,
assignments) into Savnac automatically — the steps above only prove the
connection and confirm a course shell exists. Building that adapter is
real content-mapping work, tracked as the next step, not started here.

#!/usr/bin/env bash
set -euo pipefail

CS1_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
FOREMAN_INTERFACE_DIR="${FOREMAN_INTERFACE_DIR:-$CS1_ROOT/../foreman_interface}"
COURSE_FOUNDRY_DIR="${COURSE_FOUNDRY_DIR:-$CS1_ROOT/../course_foundry}"
JOB_PROMPT="$CS1_ROOT/sidecar/jobs/103_104_cs1_production_closeout.md"
CANVAS_ENV="${CANVAS_ENV:-$HOME/.config/canvas/canvas.env}"

fail() {
  echo "FLO LAUNCH STOP: $*" >&2
  exit 1
}

require_repo() {
  local path="$1" label="$2"
  [[ -d "$path" ]] || fail "$label directory not found: $path"
  git -C "$path" rev-parse --is-inside-work-tree >/dev/null 2>&1 \
    || fail "$label is not a Git worktree: $path"
  git -C "$path" remote get-url origin >/dev/null 2>&1 \
    || fail "$label has no origin remote: $path"
}

command -v git >/dev/null 2>&1 || fail "git is not available on PATH."
command -v claude >/dev/null 2>&1 || fail "claude is not available on PATH."

require_repo "$CS1_ROOT" "computer_science_1"
require_repo "$FOREMAN_INTERFACE_DIR" "foreman_interface"
require_repo "$COURSE_FOUNDRY_DIR" "course_foundry"

for required in \
  "$JOB_PROMPT" \
  "$CS1_ROOT/sidecar/prompts/103_cs1_online_full_production_imprint.md" \
  "$CS1_ROOT/sidecar/prompts/104_cs1_online_student_view_launch_closeout.md" \
  "$FOREMAN_INTERFACE_DIR/FOREMAN.md" \
  "$FOREMAN_INTERFACE_DIR/contracts/owner_foreman.md" \
  "$FOREMAN_INTERFACE_DIR/contracts/foreman_worker.md" \
  "$FOREMAN_INTERFACE_DIR/spells/dispatch.md" \
  "$FOREMAN_INTERFACE_DIR/spells/golem.md"
do
  [[ -r "$required" ]] || fail "required file is missing or unreadable: $required"
done

[[ -r "$CANVAS_ENV" ]] || fail "production Canvas environment file is missing or unreadable: $CANVAS_ENV"
[[ -x "$COURSE_FOUNDRY_DIR/.venv/bin/python3" ]] \
  || fail "Course Foundry virtualenv Python is missing: $COURSE_FOUNDRY_DIR/.venv/bin/python3"

# Refuse obviously interrupted Git operations. Ordinary dirty state is left for
# Flo to inspect/protect because Course Foundry may legitimately have live
# process artifacts in its shared checkout.
for repo in "$CS1_ROOT" "$COURSE_FOUNDRY_DIR"; do
  git_dir="$(git -C "$repo" rev-parse --git-dir)"
  case "$git_dir" in
    /*) ;;
    *) git_dir="$repo/$git_dir" ;;
  esac
  [[ ! -e "$git_dir/MERGE_HEAD" ]] || fail "unfinished merge in $repo"
  [[ ! -d "$git_dir/rebase-merge" && ! -d "$git_dir/rebase-apply" ]] \
    || fail "unfinished rebase in $repo"
done

cd "$CS1_ROOT"

export CS1_FLO_ROOT="$CS1_ROOT"
export CS1_FLO_JOB="$JOB_PROMPT"
export CS1_FLO_FOREMAN_INTERFACE="$FOREMAN_INTERFACE_DIR"
export CS1_FLO_COURSE_FOUNDRY="$COURSE_FOUNDRY_DIR"
export CS1_FLO_CANVAS_ENV="$CANVAS_ENV"

STARTUP_PROMPT=$(cat <<EOF
You are Flo, the fresh Claude Sonnet Foreman for exactly one Computer Science 1 production-closeout job.

This is a NEW shift. Do not resume, continue, or inherit an older conversation. Do not select work from JTT.

WORKING DIRECTORY:
$CS1_ROOT

CANONICAL FOREMAN CONTRACTS — READ THESE FIRST:
1. $FOREMAN_INTERFACE_DIR/contracts/owner_foreman.md
2. $FOREMAN_INTERFACE_DIR/FOREMAN.md
3. $FOREMAN_INTERFACE_DIR/contracts/foreman_worker.md

WHEN YOU DISPATCH BOUNDED WANDAS/WORKERS, ALSO READ:
4. $FOREMAN_INTERFACE_DIR/spells/dispatch.md
5. $FOREMAN_INTERFACE_DIR/spells/golem.md

YOUR ONE JOB:
$JOB_PROMPT

Read the job prompt in full and execute it autonomously.

Important launch semantics:
- The human intentionally launched this script to authorize only the bounded production content/configuration writes to Canvas course 74029 described in the job prompt, after its fresh topology gate passes.
- This launch does NOT authorize cross-list changes, another production course, destructive unexplained cleanup, or unrelated repository work.
- computer_science_1 is the owning worksite. Course Foundry is allowed only when CS1 proves a shared implementation repair is necessary.
- Do not modify JTT. Do not take Piper/Architecture/DSCT/CS2 work.
- You may dispatch bounded Wandas/workers yourself under the canonical Foreman/Worker contract. Jeremy is not your message bus.
- Leave the reports and receipts exactly where the job prompt requires.
- Do not write Chaz's Owner after-action report. Chaz evaluates your evidence after you return.
- Keep moving until the job's DONE condition or a real human gate is reached.

Begin now.
EOF
)

CLAUDE_ARGS=(--model sonnet)
if claude --help 2>&1 | grep -q -- '--effort'; then
  CLAUDE_ARGS+=(--effort medium)
fi

echo ">>> Launching fresh Flo for CS1 production closeout"
echo ">>> Job: $JOB_PROMPT"
echo ">>> Worksite: $CS1_ROOT"

# No --continue/--resume flag is used: each invocation starts a fresh Claude
# Code conversation, matching the established foreman_interface launcher
# pattern while keeping this job scoped to CS1.
exec claude "${CLAUDE_ARGS[@]}" "$STARTUP_PROMPT"

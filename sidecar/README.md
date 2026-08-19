# Launch Flo for the CS1 production closeout

From the `computer_science_1` repository root, run:

```bash
./sidecar/launch_flo.sh
```

That one command starts a **fresh Claude Sonnet Flo** with exactly one job: finish the production proof/reconcile for Prompt 103 and, only if 103 is `DEPLOYED`, continue immediately through the Prompt 104 student-path closeout.

Flo reads the canonical contracts from the sibling `foreman_interface` checkout, reads `sidecar/jobs/103_104_cs1_production_closeout.md`, and may dispatch bounded Wandas/workers itself. Jeremy does not need to copy prompts, compose a Claude command, relay worker messages, or choose execution steps.

## Before it launches

The script fails loudly if any required runtime piece is missing:

- sibling Git checkouts for `foreman_interface` and `course_foundry`;
- `claude` and `git` on `PATH`;
- `course_foundry/.venv/bin/python3`;
- readable production Canvas environment file at `~/.config/canvas/canvas.env` (override with `CANVAS_ENV=...`);
- canonical 103/104 prompts and Foreman contracts.

It does **not** auto-pull or silently mutate `foreman_interface`. Flo safely synchronizes CS1 and Course Foundry as part of the bounded job and must preserve unexplained dirty/shared state.

Launching the script is explicit authority for only the bounded Prompt 103/104 production content/configuration work on Canvas course `74029`, and only after Flo freshly proves the two-section cross-list topology. It is not authority to change the cross-list itself or touch another production course.

## Where the evidence lands

Flo writes:

- Prompt 103 report: `sidecar/reports/103_cs1_online_full_production_imprint.md`
- Prompt 104 report, only after 103 is `DEPLOYED`: `sidecar/reports/104_cs1_online_student_view_launch_closeout.md`
- Flo handoff: `sidecar/reports/103_104_flo_foreman_completion.md`
- Raw/structured receipts: `sidecar/runs/103_104_flo_closeout/<UTC_TIMESTAMP>/`

After Flo returns, **Chaz** independently reviews that evidence and writes the Owner after-action report at:

`sidecar/reports/103_104_chaz_owner_after_action.md`

That Owner report answers: what Flo attempted, what actually changed, what production evidence proves, whether 103 is `DEPLOYED`, whether 104 passed, remaining yellows, anything Jeremy genuinely must decide, and whether the CS1 job is closed.

Flo must not write or self-accept that Owner report.

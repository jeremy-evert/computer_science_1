# Prompt 110 — CS1 Week 2 Local AI production gate audit

Date: 2026-08-31
Run: `1e0f7082696bd2135180863e010ec540`

## Verdict

`HUMAN_GATE — owner must complete a successful approved qwen3:8b Windows inference and bounded Aider exercise on the current package, then record the durable receipt.`

No CS1 or Commons production write was made by this run.

## Current source truth

- CS1 `main`: `2a007412cf56590ce778a89e07ee0e452dad8b52`.
- Current CS1 Week 2 source contains the coherent Local AI `00`–`09` road,
  three zero-point exit-ticket sources, and the accepted Monday→Wednesday→Friday
  teaching arc.
- Local AI source `main`: `764ad6e0bfd7cbeac5a9b6050494fe520cab0266`.
- Commons `main`: `13300e9` and its August 31 navigation report is present.

## Windows gate evidence evaluated

The durable `local_ai_lab_setup/Jeremy_run_1_dump` receipt from 2026-08-26
shows a non-admin Windows 11 run with Python 3.11.6, Git 2.45.2, Ollama
0.33.0, and Aider 0.86.2. The exact accepted `qwen3:8b` was downloaded but
direct inference failed with an Ollama CUDA/PTX unsupported-toolchain error.

A second receipt later that morning proves successful local inference only for
`qwen3:1.7b`. That is useful repair evidence, but it is not acceptance of the
CS1 contract, which remains explicitly pinned to `qwen3:8b`. The later durable
2026-08-28 recovery report also says the CS1 chain remains at the owner Windows
dry-run gate. The recent local-AI commits add validation/provisioning runners;
they do not add a successful `qwen3:8b` acceptance receipt or change the
accepted CS1 model policy.

Therefore the evidence resolves the old gate only partially: it proves the
Windows path, non-admin behavior, tool installation, and a fallback inference,
but not the required exact-model inference or complete current-package Aider
exercise.

## Canvas truth used for the decision

The same-day Commons navigation receipt records `Aider_Days` module `219031`
item `1531238` titled `CS1 Week 2 Local AI`, currently pointing at the shared
Commons Week 2 module `218816`, published. It also records that CS1 course
`74029` had no dedicated Week 2 Local AI module at that readback; its
`Week 2: Learning Science` module `218504` contained 17 Learning Science
items. No production object was mutated here.

## Exact human action required

On the owner Windows path, run the current `local_ai_lab_setup` package and
resolve or explicitly accept the exact-model runtime issue so that `qwen3:8b`
itself completes the bounded loopback inference. Then run the package's
bounded Aider exercise, inspect the diff, run its independent tests, and commit
the sanitized acceptance receipt. If `qwen3:8b` cannot be made to work, the
owner must explicitly decide whether the CS1 accepted model policy may change;
that is a separate academic/source decision and is not inferred from the
`qwen3:1.7b` fallback.

Until that one action and receipt exist, deploying CS1 and repointing the
Commons door would publish a production promise the accepted source gate does
not support.

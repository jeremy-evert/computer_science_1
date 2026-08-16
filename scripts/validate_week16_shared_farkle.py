#!/usr/bin/env python3
"""Validate CS1 Week 16 as a consumer of the canonical shared Farkle core.

This validator intentionally reuses the same regression tests and bounded CLI
smokes that were run before migration on April. It installs nothing and writes
one timestamped receipt under sidecar/runs/.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "lessons" / "code"
FACADE = CODE / "farkle"
SHARED = CODE / "farkle_ml"
MANIFEST = SHARED / "_SHARED_PROVENANCE.json"
RUNS = ROOT / "sidecar" / "runs"
EXPECTED_REPOSITORY = "jeremy-evert/Farkle_and_Machine_Learning"
EXPECTED_SOURCE_PATH = "src/farkle_ml"
DUPLICATE_MODULES = ("engine.py", "learner.py", "simulate.py", "strategies.py")


def run(command: list[str], env: dict[str, str]) -> tuple[int, str]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return completed.returncode, completed.stdout


def fenced(text: str) -> str:
    return "```text\n" + text.rstrip() + "\n```"


def main() -> int:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    RUNS.mkdir(parents=True, exist_ok=True)
    receipt = RUNS / f"cs1_farkle_shared_validation_{timestamp}.md"

    checks: list[tuple[str, bool, str]] = []

    if not MANIFEST.exists():
        checks.append(("shared provenance manifest", False, f"missing {MANIFEST.relative_to(ROOT)}"))
        manifest = {}
    else:
        try:
            manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
            provenance_ok = (
                manifest.get("shared_repository") == EXPECTED_REPOSITORY
                and manifest.get("source_path") == EXPECTED_SOURCE_PATH
                and bool(manifest.get("shared_commit"))
                and bool(manifest.get("files"))
            )
            checks.append(
                (
                    "shared provenance manifest",
                    provenance_ok,
                    (
                        f"repository={manifest.get('shared_repository')}; "
                        f"source={manifest.get('source_path')}; "
                        f"source commit={manifest.get('shared_commit')}"
                    ),
                )
            )
        except (OSError, json.JSONDecodeError) as exc:
            manifest = {}
            checks.append(("shared provenance manifest", False, str(exc)))

    duplicate_paths = [FACADE / name for name in DUPLICATE_MODULES if (FACADE / name).exists()]
    checks.append(
        (
            "no duplicated computational modules in CS1 facade",
            not duplicate_paths,
            "none" if not duplicate_paths else ", ".join(str(path.relative_to(ROOT)) for path in duplicate_paths),
        )
    )

    sys.path.insert(0, str(CODE))
    try:
        import farkle  # noqa: PLC0415
        import farkle_ml  # noqa: PLC0415

        aliases_ok = all(
            getattr(farkle, name) is getattr(farkle_ml, name)
            for name in ("engine", "learner", "simulate", "strategies")
        )
        checks.append(
            (
                "CS1 facade resolves canonical modules",
                aliases_ok,
                "engine/learner/simulate/strategies are canonical module objects",
            )
        )
    except Exception as exc:  # validation boundary: preserve import failure in receipt
        checks.append(("CS1 facade resolves canonical modules", False, repr(exc)))

    env = os.environ.copy()
    prior_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = str(CODE) + (os.pathsep + prior_pythonpath if prior_pythonpath else "")

    commands = [
        (
            "regression tests",
            [
                sys.executable,
                "-m",
                "pytest",
                "tests/test_farkle_engine.py",
                "tests/test_farkle_learner.py",
                "-v",
            ],
        ),
        (
            "threshold comparison smoke",
            [
                sys.executable,
                "-m",
                "farkle.cli",
                "compare",
                "--games",
                "50",
                "--seed",
                "17",
                "--strategy-a",
                "bank_at_300",
                "--strategy-b",
                "bank_at_425",
            ],
        ),
        (
            "learner comparison smoke",
            [
                sys.executable,
                "-m",
                "farkle.cli",
                "learn-vs-baseline",
                "--turns",
                "500",
                "--games",
                "50",
                "--seed",
                "17",
                "--baseline",
                "bank_at_425",
            ],
        ),
    ]

    command_results: list[tuple[str, list[str], int, str]] = []
    for label, command in commands:
        code, output = run(command, env)
        command_results.append((label, command, code, output))
        checks.append((label, code == 0, f"exit={code}"))

    overall_green = all(passed for _label, passed, _detail in checks)

    lines = [
        "# CS1 Week 16 shared Farkle validation receipt",
        "",
        f"- UTC: {timestamp}",
        f"- status: **{'GREEN' if overall_green else 'RED'}**",
        f"- Python: {sys.version.split()[0]}",
        f"- shared repository: `{manifest.get('shared_repository', 'UNKNOWN')}`",
        f"- shared source commit: `{manifest.get('shared_commit', 'UNKNOWN')}`",
        f"- shared repo head at sync: `{manifest.get('shared_repo_head', 'UNKNOWN')}`",
        "",
        "## Contract checks",
        "",
    ]

    for label, passed, detail in checks:
        lines.append(f"- {'GREEN' if passed else 'RED'} — {label}: {detail}")

    lines.extend(
        [
            "",
            "## Migration interpretation",
            "",
            "This receipt compares the migrated CS1 path against the same regression",
            "suite and bounded CLI behaviors used for the pre-migration April baseline.",
            "The CS1 lesson/CLI remain course-owned; the computational modules are",
            "provided by the provenance-pinned canonical shared package.",
        ]
    )

    for label, command, code, output in command_results:
        lines.extend(
            [
                "",
                f"## {label}",
                "",
                f"Command: `{' '.join(command)}`",
                f"Exit: `{code}`",
                "",
                fenced(output),
            ]
        )

    receipt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(receipt)
    print(f"CS1 shared Farkle validation: {'GREEN' if overall_green else 'RED'}")
    return 0 if overall_green else 1


if __name__ == "__main__":
    raise SystemExit(main())

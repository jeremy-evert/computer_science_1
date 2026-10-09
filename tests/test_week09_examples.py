"""Verify that Week 9 examples are runnable and have stable output."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).parents[1]
LESSON_SOURCES = (
    REPO_ROOT / "lessons/09-objects-you-use-classes-you-write.md",
    REPO_ROOT / "lessons/09-worked-example.md",
)

FENCE_RE = re.compile(r"```([^\r\n]*)\r?\n(.*?)```", re.DOTALL)
EXPECTED_OUTPUT_RE = re.compile(
    r"\s*<!--\s*expected-output\s*\r?\n(.*?)\r?\n\s*-->",
    re.DOTALL,
)


def _fenced_examples(source: Path) -> list[tuple[str, str]]:
    text = source.read_text(encoding="utf-8")
    examples: list[tuple[str, str]] = []

    for fence in FENCE_RE.finditer(text):
        language = fence.group(1).strip().lower()
        assert language in {"python", "python3"}, (
            f"{source} has a non-Python fenced block: {language!r}"
        )

        marker = EXPECTED_OUTPUT_RE.match(text, fence.end())
        assert marker is not None, (
            f"{source} block beginning {fence.group(2).splitlines()[0]!r} "
            "has no expected-output marker"
        )
        expected = marker.group(1).replace("\r\n", "\n") + "\n"
        examples.append((fence.group(2), expected))

    assert examples, f"{source} has no fenced examples"
    return examples


@pytest.mark.parametrize("source", LESSON_SOURCES)
def test_lesson_fences_are_standalone_and_exact(source: Path) -> None:
    for code, expected in _fenced_examples(source):
        result = subprocess.run(
            [sys.executable, "-c", code],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        assert result.stderr == ""
        assert result.stdout == expected


@pytest.mark.parametrize(
    ("program", "expected"),
    (
        (
            REPO_ROOT / "lessons/code/week09/objects_in_use.py",
            """OBJECTS IN USE
Signal Received
'  signal received  '
['water', 'maps', 'radio']
1
""",
        ),
        (
            REPO_ROOT / "lessons/code/week09/first_custom_class.py",
            """Scout
80
Scout has 80% battery.
""",
        ),
        (
            REPO_ROOT / "lessons/code/week09/worked_example.py",
            """North
3
North: 5
5
""",
        ),
    ),
)
def test_companion_programs_have_deterministic_output(
    program: Path, expected: str
) -> None:
    result = subprocess.run(
        [sys.executable, str(program)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert result.stdout == expected

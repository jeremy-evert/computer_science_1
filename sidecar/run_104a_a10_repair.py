#!/usr/bin/env python3
"""
Prompt 104A owner-run diagnostic/repair for the single CS1 A10 grading defect.

Default mode is READ-ONLY. It proves the source policy and the production
guardrails, then reports whether A10 needs repair.

Only --apply permits a write, and that write is exactly one Canvas Assignment
PUT changing only assignment_group_id for the uniquely identified A10
assignment in production course 74029.

This script intentionally does not invoke Course Foundry's Week 1 kickoff
adapter. That adapter is Savnac-only by design and its production guard must
not be weakened for this repair.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

COURSE_ID = 74029
COURSE_CODE_PREFIX = "COMSC-1033-1415"
NATIVE_SECTION_ID = 76384
MERGED_SECTION_ID = 76388
HISTORICAL_SOURCE_COURSE_ID = 74033
PRODUCTION_SCHEME = "https"
PRODUCTION_HOST = "swosu.instructure.com"
DEFAULT_GROUP_NAME = "Assignments"
KICKOFF_GROUP_NAME = "Semester kickoff week"
DEFAULT_GROUP_WEIGHT = 0.0
KICKOFF_GROUP_WEIGHT = 5.0

EXPECTED_DROP_LOWEST_GROUPS = {
    "Monday Moment quiz",
    "Wacky Wednesday reflection",
    "Fun Friday reflection",
    "Paired-programming report",
    "Friday feedback report",
    "Show-and-Tell reflection",
    "Weekly reinforcement assignment",
}

A10_SOURCE_REL = Path("assignments") / "A10_success_foundations_reflection.md"
A10_REQUIRED_SOURCE_PHRASES = (
    "this assignment is optional bonus work, not required.",
    "canvas's default, 0%-weighted assignment group",
)


class StopRepair(RuntimeError):
    """Raised when any guardrail differs from the proven CS1 production shape."""


@dataclass(frozen=True)
class GroupSnapshot:
    id: int
    name: str
    group_weight: float
    rules: dict[str, Any]


@dataclass(frozen=True)
class A10Snapshot:
    id: int
    name: str
    assignment_group_id: int
    points_possible: float
    grading_type: str
    submission_types: tuple[str, ...]
    omit_from_final_grade: bool
    due_at: str | None
    published: bool


def _repo_paths() -> tuple[Path, Path, Path]:
    cs1_root = Path(__file__).resolve().parents[1]
    git_parent = cs1_root.parent
    harbor_root = git_parent / "harbor"
    kickoff_root = git_parent / "semester_kickoff_week"
    return cs1_root, harbor_root, kickoff_root


def _bootstrap_harbor(harbor_root: Path) -> None:
    if not (harbor_root / "harbor" / "config.py").is_file():
        raise StopRepair(
            f"Expected sibling Harbor checkout at {harbor_root}; "
            "refusing to invent another API path."
        )
    sys.path.insert(0, str(harbor_root))


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def _prove_source_policy(kickoff_root: Path) -> dict[str, Any]:
    path = kickoff_root / A10_SOURCE_REL
    if not path.is_file():
        raise StopRepair(f"Authoritative A10 source is missing: {path}")

    text = path.read_text(encoding="utf-8")
    normalized = _normalize_text(text)
    missing = [phrase for phrase in A10_REQUIRED_SOURCE_PHRASES if phrase not in normalized]
    if missing:
        raise StopRepair(
            "Authoritative A10 source no longer proves the expected optional/0%-group policy. "
            f"Missing normalized phrase(s): {missing}"
        )
    if not text.lstrip().startswith("# A10 (Optional / Bonus)"):
        raise StopRepair("A10 source heading no longer declares Optional / Bonus.")

    return {
        "path": str(path),
        "policy": "optional bonus; 10 real points; default 0%-weighted Assignments group",
    }


def _build_client():
    from harbor.client import CanvasClient
    from harbor.config import CanvasConfig, load_env, read_canvas_config

    load_env()
    base = read_canvas_config(enforce_course_allowlist=False)
    parsed = urlsplit(base.api_base_url)

    if parsed.scheme != PRODUCTION_SCHEME or parsed.netloc != PRODUCTION_HOST:
        raise StopRepair(
            "Refusing non-production Canvas target. "
            f"Expected {PRODUCTION_SCHEME}://{PRODUCTION_HOST}, got {base.api_base_url!r}."
        )

    locked = CanvasConfig(
        api_base_url=base.api_base_url,
        api_token=base.api_token,
        allowed_course_ids=frozenset({COURSE_ID}),
    )
    return CanvasClient(locked)


def _get_sections(client) -> list[dict[str, Any]]:
    from harbor.api import _check_status

    path = f"/api/v1/courses/{COURSE_ID}/sections?per_page=100"
    response = client.get(path)
    _check_status(response)
    if response.links.get("next", {}).get("url"):
        raise StopRepair("Section listing unexpectedly paginated beyond 100 rows.")
    rows = response.json()
    if not isinstance(rows, list):
        raise StopRepair("Canvas sections endpoint returned a non-list payload.")
    return rows


def _prove_topology(client) -> dict[str, Any]:
    from harbor.api import get_course

    _, course = get_course(client, COURSE_ID)
    if int(course.get("id", -1)) != COURSE_ID:
        raise StopRepair(f"Canvas returned unexpected course id: {course.get('id')!r}")

    course_code = str(course.get("course_code") or "")
    if not course_code.startswith(COURSE_CODE_PREFIX):
        raise StopRepair(
            f"Course code changed: expected prefix {COURSE_CODE_PREFIX!r}, got {course_code!r}."
        )

    sections = _get_sections(client)
    by_id = {int(row["id"]): row for row in sections if "id" in row}
    if set(by_id) != {NATIVE_SECTION_ID, MERGED_SECTION_ID}:
        raise StopRepair(
            "Production section topology changed. "
            f"Expected exactly {[NATIVE_SECTION_ID, MERGED_SECTION_ID]}, got {sorted(by_id)}."
        )

    native = by_id[NATIVE_SECTION_ID]
    merged = by_id[MERGED_SECTION_ID]

    if int(native.get("course_id", -1)) != COURSE_ID:
        raise StopRepair("Native section is no longer hosted by course 74029.")
    if native.get("nonxlist_course_id") not in (None, ""):
        raise StopRepair(
            f"Native section unexpectedly has nonxlist_course_id={native.get('nonxlist_course_id')!r}."
        )

    if int(merged.get("course_id", -1)) != COURSE_ID:
        raise StopRepair("Merged online section is no longer hosted by course 74029.")
    if int(merged.get("nonxlist_course_id", -1)) != HISTORICAL_SOURCE_COURSE_ID:
        raise StopRepair(
            "Merged section provenance changed: expected nonxlist_course_id 74033, "
            f"got {merged.get('nonxlist_course_id')!r}."
        )

    return {
        "course_id": COURSE_ID,
        "course_code": course_code,
        "sections": {
            str(NATIVE_SECTION_ID): {
                "course_id": native.get("course_id"),
                "nonxlist_course_id": native.get("nonxlist_course_id"),
            },
            str(MERGED_SECTION_ID): {
                "course_id": merged.get("course_id"),
                "nonxlist_course_id": merged.get("nonxlist_course_id"),
            },
        },
    }


def _group_snapshot(groups: list[dict[str, Any]]) -> dict[int, GroupSnapshot]:
    result: dict[int, GroupSnapshot] = {}
    for group in groups:
        gid = int(group["id"])
        if gid in result:
            raise StopRepair(f"Duplicate assignment-group id returned by Canvas: {gid}")
        result[gid] = GroupSnapshot(
            id=gid,
            name=str(group.get("name") or ""),
            group_weight=float(group.get("group_weight") or 0.0),
            rules=dict(group.get("rules") or {}),
        )
    return result


def _one_group(
    groups: dict[int, GroupSnapshot], name: str, expected_weight: float
) -> GroupSnapshot:
    matches = [g for g in groups.values() if g.name == name]
    if len(matches) != 1:
        raise StopRepair(
            f"Expected exactly one assignment group {name!r}; found {len(matches)}."
        )
    group = matches[0]
    if not math.isclose(group.group_weight, expected_weight, abs_tol=1e-9):
        raise StopRepair(
            f"Assignment group {name!r} weight changed: "
            f"expected {expected_weight}, got {group.group_weight}."
        )
    return group


def _drop_lowest_names(groups: dict[int, GroupSnapshot]) -> set[str]:
    names: set[str] = set()
    for group in groups.values():
        raw = (group.rules or {}).get("drop_lowest", 0)
        try:
            drop_lowest = int(raw or 0)
        except (TypeError, ValueError) as exc:
            raise StopRepair(
                f"Unparseable drop_lowest rule on group {group.name!r}: {raw!r}"
            ) from exc
        if drop_lowest:
            if drop_lowest != 1:
                raise StopRepair(
                    f"Unexpected drop_lowest={drop_lowest} on group {group.name!r}; expected 1."
                )
            names.add(group.name)
    return names


def _prove_groups(groups_raw: list[dict[str, Any]]) -> tuple[
    dict[int, GroupSnapshot], GroupSnapshot, GroupSnapshot
]:
    groups = _group_snapshot(groups_raw)
    total_weight = sum(g.group_weight for g in groups.values())
    if not math.isclose(total_weight, 100.0, abs_tol=1e-9):
        raise StopRepair(
            f"Assignment-group weights changed: expected total 100.0, got {total_weight}."
        )

    default_group = _one_group(groups, DEFAULT_GROUP_NAME, DEFAULT_GROUP_WEIGHT)
    kickoff_group = _one_group(groups, KICKOFF_GROUP_NAME, KICKOFF_GROUP_WEIGHT)

    drop_names = _drop_lowest_names(groups)
    if drop_names != EXPECTED_DROP_LOWEST_GROUPS:
        raise StopRepair(
            "Drop-lowest contract changed. "
            f"Expected {sorted(EXPECTED_DROP_LOWEST_GROUPS)}, got {sorted(drop_names)}."
        )

    return groups, default_group, kickoff_group


def _assignment_group_map(assignments: list[dict[str, Any]]) -> dict[int, int]:
    mapping: dict[int, int] = {}
    for assignment in assignments:
        aid = int(assignment["id"])
        gid_raw = assignment.get("assignment_group_id")
        if gid_raw is None:
            raise StopRepair(f"Assignment {aid} has no assignment_group_id in Canvas readback.")
        if aid in mapping:
            raise StopRepair(f"Duplicate assignment id returned by Canvas: {aid}")
        mapping[aid] = int(gid_raw)
    return mapping


def _identify_a10(assignments: list[dict[str, Any]]) -> dict[str, Any]:
    matches = []
    for assignment in assignments:
        name = str(assignment.get("name") or "")
        normalized = name.casefold()
        if normalized.startswith("a10") and "success foundations reflection" in normalized:
            matches.append(assignment)
    if len(matches) != 1:
        candidates = [
            str(a.get("name") or "")
            for a in assignments
            if "success foundations" in str(a.get("name") or "").casefold()
            or str(a.get("name") or "").casefold().startswith("a10")
        ]
        raise StopRepair(
            f"Expected exactly one live A10 Success Foundations Reflection; found {len(matches)}. "
            f"Nearby candidates: {candidates}"
        )
    return matches[0]


def _snapshot_a10(client, assignment_stub: dict[str, Any]) -> A10Snapshot:
    from harbor.api import get_assignment

    aid = int(assignment_stub["id"])
    _, live = get_assignment(client, COURSE_ID, aid)

    try:
        points = float(live.get("points_possible"))
    except (TypeError, ValueError) as exc:
        raise StopRepair(
            f"A10 points_possible is not numeric: {live.get('points_possible')!r}"
        ) from exc

    snapshot = A10Snapshot(
        id=aid,
        name=str(live.get("name") or ""),
        assignment_group_id=int(live.get("assignment_group_id")),
        points_possible=points,
        grading_type=str(live.get("grading_type") or ""),
        submission_types=tuple(sorted(str(x) for x in (live.get("submission_types") or []))),
        omit_from_final_grade=bool(live.get("omit_from_final_grade")),
        due_at=live.get("due_at"),
        published=bool(live.get("published")),
    )

    normalized_name = snapshot.name.casefold()
    if not (
        normalized_name.startswith("a10")
        and "success foundations reflection" in normalized_name
    ):
        raise StopRepair(f"A10 identity changed after single-assignment readback: {snapshot.name!r}")
    if not math.isclose(snapshot.points_possible, 10.0, abs_tol=1e-9):
        raise StopRepair(f"A10 points changed: expected 10, got {snapshot.points_possible}.")
    if snapshot.grading_type != "points":
        raise StopRepair(
            f"A10 grading_type changed: expected 'points', got {snapshot.grading_type!r}."
        )
    if snapshot.submission_types != ("online_text_entry",):
        raise StopRepair(
            "A10 submission path changed: expected exactly ['online_text_entry'], "
            f"got {list(snapshot.submission_types)!r}."
        )
    if snapshot.omit_from_final_grade:
        raise StopRepair("A10 is unexpectedly omit_from_final_grade=true.")
    if snapshot.due_at is not None:
        raise StopRepair(
            f"A10 unexpectedly has a fixed due_at={snapshot.due_at!r}; source says no fixed due date."
        )
    if not snapshot.published:
        raise StopRepair("A10 is unexpectedly unpublished.")

    return snapshot


def _grading_contract_projection(
    groups: dict[int, GroupSnapshot],
) -> dict[int, tuple[str, float, str]]:
    """Stable fields that must not change when one assignment moves groups."""
    projected = {}
    for gid, group in groups.items():
        rules_json = json.dumps(group.rules, sort_keys=True, separators=(",", ":"))
        projected[gid] = (group.name, group.group_weight, rules_json)
    return projected


def _collect_state(client) -> dict[str, Any]:
    from harbor.api import list_assignment_groups, list_assignments

    topology = _prove_topology(client)
    groups_raw = list_assignment_groups(client, COURSE_ID)
    groups, default_group, kickoff_group = _prove_groups(groups_raw)

    assignments = list_assignments(client, COURSE_ID)
    if not assignments:
        raise StopRepair("Canvas returned zero assignments for CS1 production.")
    assignment_map = _assignment_group_map(assignments)

    a10_stub = _identify_a10(assignments)
    a10 = _snapshot_a10(client, a10_stub)
    if assignment_map.get(a10.id) != a10.assignment_group_id:
        raise StopRepair("A10 group differs between assignment list and single-object readback.")

    kickoff_members = sorted(
        aid for aid, gid in assignment_map.items() if gid == kickoff_group.id
    )
    if not kickoff_members:
        raise StopRepair("Semester kickoff week group unexpectedly has no assignments.")

    return {
        "topology": topology,
        "groups": groups,
        "default_group": default_group,
        "kickoff_group": kickoff_group,
        "assignments": assignments,
        "assignment_map": assignment_map,
        "a10": a10,
        "kickoff_members": kickoff_members,
    }


def _state_for_receipt(state: dict[str, Any]) -> dict[str, Any]:
    groups: dict[int, GroupSnapshot] = state["groups"]
    a10: A10Snapshot = state["a10"]
    return {
        "topology": state["topology"],
        "assignment_count": len(state["assignments"]),
        "assignment_group_count": len(groups),
        "total_group_weight": sum(g.group_weight for g in groups.values()),
        "drop_lowest_groups": sorted(_drop_lowest_names(groups)),
        "default_group": asdict(state["default_group"]),
        "kickoff_group": asdict(state["kickoff_group"]),
        "kickoff_member_count": len(state["kickoff_members"]),
        "a10": asdict(a10),
    }


def _write_receipt(
    cs1_root: Path,
    *,
    mode: str,
    diagnosis: str,
    source_policy: dict[str, Any],
    before: dict[str, Any],
    after: dict[str, Any] | None,
    changed_assignment_ids: list[int],
) -> Path:
    run_dir = (
        cs1_root
        / "sidecar"
        / "runs"
        / "104A_owner_repair"
        / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    )
    run_dir.mkdir(parents=True, exist_ok=False)
    path = run_dir / "a10_repair_receipt.json"
    payload = {
        "prompt": "104A",
        "mode": mode,
        "diagnosis": diagnosis,
        "target_course_id": COURSE_ID,
        "forbidden_course_id": HISTORICAL_SOURCE_COURSE_ID,
        "source_policy": source_policy,
        "before": _state_for_receipt(before),
        "after": _state_for_receipt(after) if after is not None else None,
        "changed_assignment_ids": changed_assignment_ids,
        "note": "No token, student names, enrollments, submissions, or grades are stored in this receipt.",
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _print_state(label: str, state: dict[str, Any]) -> None:
    a10: A10Snapshot = state["a10"]
    default_group: GroupSnapshot = state["default_group"]
    kickoff_group: GroupSnapshot = state["kickoff_group"]
    groups: dict[int, GroupSnapshot] = state["groups"]

    print(f"{label}:")
    print(
        f"  topology: course {COURSE_ID}, sections "
        f"{NATIVE_SECTION_ID}+{MERGED_SECTION_ID}, merged provenance {HISTORICAL_SOURCE_COURSE_ID}"
    )
    print(
        f"  groups: {len(groups)}, total weight "
        f"{sum(g.group_weight for g in groups.values()):g}%"
    )
    print(
        f"  drop-lowest groups: {len(_drop_lowest_names(groups))} "
        f"(contract exactly matched)"
    )
    print(
        f"  default group: {default_group.name!r} id={default_group.id} "
        f"weight={default_group.group_weight:g}%"
    )
    print(
        f"  kickoff group: {kickoff_group.name!r} id={kickoff_group.id} "
        f"weight={kickoff_group.group_weight:g}% members={len(state['kickoff_members'])}"
    )
    print(
        f"  A10: id={a10.id} group_id={a10.assignment_group_id} "
        f"points={a10.points_possible:g} due_at={a10.due_at!r} "
        f"submission_types={list(a10.submission_types)!r}"
    )


def _verify_after(before: dict[str, Any], after: dict[str, Any]) -> list[int]:
    before_a10: A10Snapshot = before["a10"]
    after_a10: A10Snapshot = after["a10"]
    before_default: GroupSnapshot = before["default_group"]
    after_default: GroupSnapshot = after["default_group"]

    if after_a10.id != before_a10.id:
        raise StopRepair("A10 id changed across the one-object repair.")
    if after_default.id != before_default.id:
        raise StopRepair("Default Assignments group id changed across repair.")
    if after_a10.assignment_group_id != after_default.id:
        raise StopRepair(
            "A10 did not land in the default 0%-weighted Assignments group after PUT."
        )

    before_contract = _grading_contract_projection(before["groups"])
    after_contract = _grading_contract_projection(after["groups"])
    if before_contract != after_contract:
        raise StopRepair("Assignment-group names, weights, or drop rules changed during A10 repair.")

    before_map: dict[int, int] = before["assignment_map"]
    after_map: dict[int, int] = after["assignment_map"]
    if set(before_map) != set(after_map):
        raise StopRepair("Assignment population changed during A10 repair.")

    changed = sorted(aid for aid in before_map if before_map[aid] != after_map[aid])
    if changed != [before_a10.id]:
        raise StopRepair(
            "More than A10 changed assignment groups. "
            f"Expected only {[before_a10.id]}, observed {changed}."
        )

    expected_after = dict(before_map)
    expected_after[before_a10.id] = after_default.id
    if after_map != expected_after:
        raise StopRepair("Post-write assignment-group map differs beyond the intended A10 move.")

    if len(after["kickoff_members"]) != len(before["kickoff_members"]) - 1:
        raise StopRepair(
            "Kickoff-group membership count did not decrease by exactly one after moving A10."
        )

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only by default; --apply performs one guarded A10 group move."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Permit the single A10 assignment_group_id PUT after all preflight guards pass.",
    )
    args = parser.parse_args()

    cs1_root, harbor_root, kickoff_root = _repo_paths()

    try:
        _bootstrap_harbor(harbor_root)
        source_policy = _prove_source_policy(kickoff_root)
        client = _build_client()

        before = _collect_state(client)
        _print_state("PRE-WRITE READBACK", before)

        a10: A10Snapshot = before["a10"]
        default_group: GroupSnapshot = before["default_group"]
        kickoff_group: GroupSnapshot = before["kickoff_group"]

        if a10.assignment_group_id == default_group.id:
            diagnosis = "ALREADY CORRECT"
            print("\nDIAGNOSIS: ALREADY CORRECT")
            print("A10 is already in the default 0%-weighted Assignments group. No write is needed.")
            receipt = _write_receipt(
                cs1_root,
                mode="apply-noop" if args.apply else "diagnostic",
                diagnosis=diagnosis,
                source_policy=source_policy,
                before=before,
                after=None,
                changed_assignment_ids=[],
            )
            print(f"Receipt: {receipt}")
            return 0

        if a10.assignment_group_id != kickoff_group.id:
            raise StopRepair(
                "A10 is neither in the expected wrong 5% kickoff group nor already in the "
                f"correct default group. Live group id={a10.assignment_group_id}; refusing to guess."
            )

        diagnosis = "A10 REPAIR NEEDED"
        print("\nDIAGNOSIS: A10 REPAIR NEEDED")
        print(
            f"A10 is in {KICKOFF_GROUP_NAME!r} ({kickoff_group.group_weight:g}%) "
            f"but source requires {DEFAULT_GROUP_NAME!r} ({default_group.group_weight:g}%)."
        )

        if not args.apply:
            print("\nREAD-ONLY MODE: no Canvas write was attempted.")
            print("If this output is exactly what we expected, rerun the same script with --apply.")
            receipt = _write_receipt(
                cs1_root,
                mode="diagnostic",
                diagnosis=diagnosis,
                source_policy=source_policy,
                before=before,
                after=None,
                changed_assignment_ids=[],
            )
            print(f"Receipt: {receipt}")
            return 0

        from harbor.api import update_assignment

        print("\nAPPLY MODE: all guards passed.")
        print(
            f"Writing exactly one field on assignment {a10.id}: "
            f"assignment_group_id {kickoff_group.id} -> {default_group.id}"
        )
        update_assignment(
            client,
            COURSE_ID,
            a10.id,
            {"assignment[assignment_group_id]": str(default_group.id)},
        )

        after = _collect_state(client)
        changed = _verify_after(before, after)
        _print_state("POST-WRITE READBACK", after)

        print("\nREPAIRED: A10 is now in the default 0%-weighted group.")
        print(f"Verified changed assignment ids: {changed}")
        print("Verified every other assignment-group mapping is unchanged.")
        print("Verified group weights, seven drop-lowest rules, and topology are unchanged.")

        receipt = _write_receipt(
            cs1_root,
            mode="apply",
            diagnosis="REPAIRED",
            source_policy=source_policy,
            before=before,
            after=after,
            changed_assignment_ids=changed,
        )
        print(f"Receipt: {receipt}")
        print(
            "\nNEXT READ-ONLY CHECK (separate from this script):\n"
            "  cd /mnt/brandy_nvme/jevert/git/course_foundry\n"
            "  python -m course_foundry.production_deploy dry-run --course cs1 "
            "--git-parent /mnt/brandy_nvme/jevert/git --skip-files"
        )
        return 0

    except StopRepair as exc:
        print(f"\nSTOP: {exc}", file=sys.stderr)
        print("No further action was attempted by this script.", file=sys.stderr)
        return 3
    except Exception as exc:
        print(
            f"\nSTOP: unexpected {type(exc).__name__}: {exc}\n"
            "Treat this as new evidence. Do not broaden scope or retry with weaker guards.",
            file=sys.stderr,
        )
        return 4


if __name__ == "__main__":
    raise SystemExit(main())

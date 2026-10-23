"""Checks for make_obsidian_map.py: links resolve, output is stable, the map is connected."""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAP_DIR = REPO / "_repo_map"
SCRIPT = REPO / "make_obsidian_map.py"
LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def run_script():
    subprocess.run([sys.executable, str(SCRIPT)], check=True, capture_output=True, cwd=REPO)


def snapshot_map_directory():
    return {path.name: path.read_bytes() for path in sorted(MAP_DIR.glob("*.md"))}


def link_targets(markdown_text):
    """Targets of [[target|alias]] links, with alias and #heading removed."""
    targets = []
    for raw in LINK_PATTERN.findall(markdown_text):
        targets.append(raw.split("|")[0].split("#")[0].strip())
    return targets


def target_exists(target):
    return (
        (MAP_DIR / f"{target}.md").exists()
        or (REPO / target).is_file()
        or (REPO / f"{target}.md").is_file()
    )


def test_every_link_resolves_to_an_existing_file():
    run_script()
    broken = []
    for note in sorted(MAP_DIR.glob("*.md")):
        for target in link_targets(note.read_text(encoding="utf-8")):
            if not target_exists(target):
                broken.append(f"{note.name} -> {target}")
    assert not broken, "Broken links:\n" + "\n".join(broken)


def test_running_twice_gives_identical_output():
    run_script()
    first = snapshot_map_directory()
    run_script()
    second = snapshot_map_directory()
    assert first == second


def test_course_map_links_to_every_hub():
    run_script()
    course_map = (MAP_DIR / "00_Course_Map.md").read_text(encoding="utf-8")
    linked_from_map = set(link_targets(course_map))

    all_hubs = {p.stem for p in MAP_DIR.glob("hub__*.md")}
    top_level_hubs = {name for name in all_hubs if "__" not in name[len("hub__"):]}
    assert top_level_hubs, "no folder hubs were generated"
    assert top_level_hubs <= linked_from_map, f"Course Map misses: {sorted(top_level_hubs - linked_from_map)}"

    # Nested hubs must be reachable through their parents.
    reachable = set()
    to_visit = ["00_Course_Map"]
    while to_visit:
        name = to_visit.pop()
        note = MAP_DIR / f"{name}.md"
        if name in reachable or not note.exists():
            continue
        reachable.add(name)
        to_visit.extend(link_targets(note.read_text(encoding="utf-8")))
    assert all_hubs <= reachable, f"Unreachable hubs: {sorted(all_hubs - reachable)}"

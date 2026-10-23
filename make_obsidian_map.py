"""Build a hub-and-spoke Obsidian map of this repo.

Run from anywhere:  python make_obsidian_map.py

Shape of the graph:
    00_Course_Map  ->  hub__<folder>  ->  real .md files / python notes
                                      ->  hub__<folder>__<subfolder> (nested hubs)

The vault root is the repo root, so a link like [[lessons/week09/notes]] points at the
real file lessons/week09/notes.md. Python files get a small note under _repo_map/ (tagged
#python) that records which repo files they import; that note is linked from the hub of
the folder the .py file lives in.

Only _repo_map/ is written. _repo_map/ is deleted and rebuilt on every run.
"""
import ast
import os
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent
MAP_DIR = REPO / "_repo_map"
COURSE_MAP_NAME = "00_Course_Map"

SKIP_DIRECTORY_NAMES = {
    ".git", ".obsidian", "_repo_map", "__pycache__", "venv", ".venv",
    "node_modules", ".pytest_cache",
}
SKIP_PATH_PREFIXES = ("sidecar/runs", "gpu_showdown/data")

# Folders under archive/ collapse to one hub each (no per-file links).
COLLAPSED_PARENT_FOLDER = "archive"

FEATURED_ROOT_NOTES = ["README", "START_HERE", "ROADMAP", "NAMING", "AGENTS"]

# Which color-group tag each top-level folder gets (besides #hub).
FOLDER_TAGS = {
    "lessons": "#lesson", "planning": "#lesson", "monday_moments": "#lesson",
    "function_example": "#lesson", "strings_example": "#lesson",
    "slides": "#lesson", "presentations": "#lesson",
    "assignments": "#assignment", "quizzes": "#assignment",
    "rubrics": "#assignment", "student_work": "#assignment",
    "archive": "#archive",
    "scripts": "#tooling", "tests": "#tooling", "sidecar": "#tooling",
    "gpu_showdown": "#tooling", "jobs": "#tooling", "canvas": "#tooling",
    "canvas_pages": "#tooling", "templates": "#tooling",
}

FOLDER_DESCRIPTIONS = {
    "lessons": "The instructional sequence: lesson guides, lecture notes, and the runnable example code that goes with them.",
    "planning": "Week-by-week plans for the 17-week Fall 2026 semester: focus, due items, and weekly rhythm.",
    "assignments": "Reusable student-facing assignments (A1 to A6): weekly practice, pair programming, Coding Odyssey, reflections.",
    "quizzes": "Reusable quiz drafts such as getting-to-know-you and the chapter exam.",
    "rubrics": "Grading rubrics that go with the assignments and discussions.",
    "templates": "Fill-in-the-blank starting points for assignments, rubrics, syllabi, and Canvas pages.",
    "monday_moments": "Short weekly AI-and-learning tips for beginning programmers.",
    "canvas": "Notes on how course content maps into Canvas.",
    "canvas_pages": "Page sources that get published to Canvas.",
    "slides": "Slide decks and their sources.",
    "presentations": "Presentation material for class.",
    "student_work": "Shared student examples and the code that checks them. Peers see each other's work, so no names or personal details.",
    "extras": "Optional extra material outside the main sequence.",
    "function_example": "A small worked example of functions.",
    "strings_example": "A small worked example of strings.",
    "docs": "Durable course documentation: the course ethos, curriculum maps, teaching philosophy, and analysis.",
    "prompts": "Prompts that drive curriculum development and source walks.",
    "reports": "Reports produced while building the course: audits, status snapshots, decisions applied.",
    "jobs": "Job and automation notes for course tooling.",
    "scripts": "Helper scripts for building and checking course material.",
    "tests": "Automated checks (pytest) for course code and tooling.",
    "sidecar": "Sidecar tooling and its documentation.",
    "gpu_showdown": "A GPU benchmark side project.",
    "archive": "History: Canvas snapshots from spring 2021 to spring 2026. One hub per semester keeps this a tidy branch.",
}

COURSE_DESCRIPTION = (
    "COMSC 1033, Computer Science 1: a semester-long intro to programming in Python. "
    "This repo is the source of truth for course content; Canvas is the checkpoint. "
    "Start at a hub below, then follow the links down to the real files."
)


# ---------------------------------------------------------------- finding files

def is_skipped_directory(relative_path):
    if relative_path.name in SKIP_DIRECTORY_NAMES:
        return True
    posix = relative_path.as_posix()
    return any(posix == prefix or posix.startswith(prefix + "/") for prefix in SKIP_PATH_PREFIXES)


def find_repo_files():
    """Return every .md and .py file (as repo-relative Paths), sorted, minus skipped folders."""
    found = []
    for directory, subdirectories, filenames in os.walk(REPO):
        relative_directory = Path(directory).relative_to(REPO)
        subdirectories[:] = sorted(
            name for name in subdirectories
            if not is_skipped_directory(relative_directory / name)
        )
        for filename in sorted(filenames):
            if filename.endswith((".md", ".py")):
                found.append(relative_directory / filename)
    return sorted(found)


def is_collapsed_file(relative_file):
    """True for files deep inside archive/<semester>/, which are summarised, not linked."""
    parts = relative_file.parts
    return parts[0] == COLLAPSED_PARENT_FOLDER and len(parts) >= 3


def folders_that_get_hubs(files):
    """Every folder (as repo-relative Path) that contains files, except folders nested deeper
    than archive/<semester>."""
    folders = set()
    for relative_file in files:
        folder = relative_file.parent
        while folder != Path("."):
            parts = folder.parts
            is_too_deep_in_archive = parts[0] == COLLAPSED_PARENT_FOLDER and len(parts) > 2
            if not is_too_deep_in_archive:
                folders.add(folder)
            folder = folder.parent
    return folders


# ---------------------------------------------------------------- note names

def hub_note_name(folder):
    return "hub__" + "__".join(folder.parts)


def python_note_name(relative_file):
    return "py__" + "__".join(relative_file.with_suffix("").parts)


def real_file_link(relative_file):
    """Obsidian path link to a real file. Markdown links drop the extension."""
    target = relative_file.as_posix()
    if relative_file.suffix == ".md":
        target = target[: -len(".md")]
    return f"[[{target}|{relative_file.stem}]]"


def note_link(note_name, label=None):
    return f"[[{note_name}|{label}]]" if label else f"[[{note_name}]]"


# ---------------------------------------------------------------- python imports

def read_syntax_tree(path):
    try:
        return ast.parse(path.read_text(encoding="utf-8-sig"))
    except (SyntaxError, UnicodeDecodeError, ValueError):
        return None


def imported_module_names(tree):
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[-1] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[-1])
    return names


def group_python_files_by_module_name(python_files):
    by_module = {}
    for relative_file in python_files:
        by_module.setdefault(relative_file.stem, []).append(relative_file)
    return by_module


def python_files_imported_by(relative_file, tree, by_module):
    """Repo .py files this file imports. If several files share a module name, prefer the
    one in the same folder; otherwise link all candidates."""
    if tree is None:
        return []
    imported = []
    for module_name in sorted(imported_module_names(tree)):
        candidates = [c for c in by_module.get(module_name, []) if c != relative_file]
        same_folder = [c for c in candidates if c.parent == relative_file.parent]
        imported.extend(same_folder or candidates)
    return sorted(set(imported))


# ---------------------------------------------------------------- writing notes

def write_note(note_name, lines):
    path = MAP_DIR / f"{note_name}.md"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines) + "\n")


def reset_map_directory():
    if MAP_DIR.parent != REPO or MAP_DIR.name != "_repo_map":
        raise RuntimeError(f"Refusing to delete unexpected directory: {MAP_DIR}")
    if MAP_DIR.exists():
        shutil.rmtree(MAP_DIR)
    MAP_DIR.mkdir()


def write_python_note(relative_file, tree, by_module):
    imports = python_files_imported_by(relative_file, tree, by_module)
    classes, functions = [], []
    if tree is not None:
        classes = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]
        functions = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]

    lines = [
        f"# {relative_file.name}", "", "#python", "",
        f"Source file: `{relative_file.as_posix()}`",
        f"Lives in: {note_link(hub_note_name(relative_file.parent))}" if relative_file.parent != Path(".")
        else f"Lives in: {note_link(COURSE_MAP_NAME)}",
        "", "## Imports from this repo",
    ]
    lines += [f"- {note_link(python_note_name(target))}" for target in imports] or ["- (none)"]
    lines += ["", "## Classes"] + ([f"- {name}" for name in classes] or ["- (none)"])
    lines += ["", "## Top-level functions"] + ([f"- {name}()" for name in functions] or ["- (none)"])
    write_note(python_note_name(relative_file), lines)


def count_files_under(folder, files):
    return sum(1 for f in files if folder in f.parents)


def write_hub_note(folder, files, hub_folders):
    top_level = folder.parts[0]
    tags = ["#hub"]
    if top_level in FOLDER_TAGS:
        tags.append(FOLDER_TAGS[top_level])

    is_semester_hub = folder.parts[0] == COLLAPSED_PARENT_FOLDER and len(folder.parts) == 2
    if len(folder.parts) == 1:
        description = FOLDER_DESCRIPTIONS.get(top_level, f"Files in `{folder.as_posix()}/`.")
        parent_link = note_link(COURSE_MAP_NAME)
    else:
        if is_semester_hub:
            description = (
                f"Archived Canvas material for `{folder.name}`: "
                f"{count_files_under(folder, files)} .md/.py files, summarised here instead of linked one by one."
            )
        else:
            description = f"Files in `{folder.as_posix()}/`."
        parent_link = note_link(hub_note_name(folder.parent))

    lines = [f"# {folder.as_posix()}/", "", " ".join(tags), "", description, "",
             f"Part of: {parent_link}", ""]

    sub_hubs = sorted(f for f in hub_folders if f.parent == folder)
    if sub_hubs:
        lines += ["## Subfolders"]
        lines += [f"- {note_link(hub_note_name(sub), sub.name + '/')}" for sub in sub_hubs]
        lines += [""]

    direct_files = [f for f in files if f.parent == folder and not is_collapsed_file(f)]
    markdown_files = [f for f in direct_files if f.suffix == ".md"]
    python_files = [f for f in direct_files if f.suffix == ".py"]
    if markdown_files:
        lines += ["## Markdown files"] + [f"- {real_file_link(f)}" for f in markdown_files] + [""]
    if python_files:
        lines += ["## Python files"]
        lines += [f"- {note_link(python_note_name(f), f.name)}" for f in python_files] + [""]

    write_note(hub_note_name(folder), lines)


def write_course_map(files, hub_folders):
    top_level_hubs = sorted(f for f in hub_folders if len(f.parts) == 1)
    root_files = [f for f in files if f.parent == Path(".")]
    root_markdown = [f for f in root_files if f.suffix == ".md"]
    root_python = [f for f in root_files if f.suffix == ".py"]

    featured = [f for f in root_markdown if f.stem in FEATURED_ROOT_NOTES]
    featured.sort(key=lambda f: FEATURED_ROOT_NOTES.index(f.stem))
    other_root_markdown = [f for f in root_markdown if f not in featured]

    lines = ["# Course Map", "", "#hub", "", COURSE_DESCRIPTION, "", "## Start here"]
    lines += [f"- {real_file_link(f)}" for f in featured]
    if other_root_markdown:
        lines += ["", "## Other top-level notes"] + [f"- {real_file_link(f)}" for f in other_root_markdown]
    lines += ["", "## Folder hubs"]
    lines += [f"- {note_link(hub_note_name(h), h.name + '/')}" for h in top_level_hubs]
    if root_python:
        lines += ["", "## Top-level Python files"]
        lines += [f"- {note_link(python_note_name(f), f.name)}" for f in root_python]
    write_note(COURSE_MAP_NAME, lines)


def main():
    files = find_repo_files()
    hub_folders = folders_that_get_hubs(files)
    python_files = [f for f in files if f.suffix == ".py"]
    by_module = group_python_files_by_module_name(python_files)

    reset_map_directory()
    for relative_file in python_files:
        tree = read_syntax_tree(REPO / relative_file)
        write_python_note(relative_file, tree, by_module)
    for folder in sorted(hub_folders):
        write_hub_note(folder, files, hub_folders)
    write_course_map(files, hub_folders)

    print(f"Wrote {len(hub_folders)} hub notes, {len(python_files)} python notes, "
          f"and {COURSE_MAP_NAME}.md to {MAP_DIR}")


if __name__ == "__main__":
    main()

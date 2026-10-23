"""Build an Obsidian map of a Python repo: one note per .py file and folder, linked by imports."""
import ast
import pathlib

REPO = pathlib.Path(".").resolve()
MAP_DIR = REPO / "_repo_map"
SKIP = {".git", ".obsidian", "_repo_map", "venv", ".venv", "__pycache__", "node_modules"}


def find_python_files():
    for path in sorted(REPO.rglob("*.py")):
        if not SKIP.intersection(path.relative_to(REPO).parts):
            yield path


def note_name_for_file(path):
    return "__".join(path.relative_to(REPO).with_suffix("").parts)


def note_name_for_folder(folder):
    parts = folder.relative_to(REPO).parts
    return "folder__" + ("__".join(parts) if parts else "ROOT")


def read_syntax_tree(path):
    try:
        return ast.parse(path.read_text(encoding="utf-8-sig"))
    except (SyntaxError, UnicodeDecodeError):
        return None


def imported_module_names(tree):
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[-1] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[-1])
    return names


def write_note(name, lines):
    (MAP_DIR / f"{name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    MAP_DIR.mkdir(exist_ok=True)
    python_files = list(find_python_files())
    note_for_module = {path.stem: note_name_for_file(path) for path in python_files}
    folders = set()

    for path in python_files:
        this_note = note_name_for_file(path)
        tree = read_syntax_tree(path)
        imports, classes, functions = set(), [], []
        if tree:
            imports = imported_module_names(tree)
            classes = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]
            functions = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
        links = sorted({note_for_module[m] for m in imports if m in note_for_module} - {this_note})

        lines = [f"# {path.name}", "", "#python", "",
                 f"Path: `{path.relative_to(REPO).as_posix()}`",
                 f"Lives in: [[{note_name_for_folder(path.parent)}]]", "",
                 "## Imports from this repo"]
        lines += [f"- [[{link}]]" for link in links] or ["- (none)"]
        lines += ["", "## Classes"] + ([f"- {c}" for c in classes] or ["- (none)"])
        lines += ["", "## Top-level functions"] + ([f"- {f}()" for f in functions] or ["- (none)"])
        write_note(this_note, lines)

        folder = path.parent
        while True:
            folders.add(folder)
            if folder == REPO:
                break
            folder = folder.parent

    for folder in sorted(folders):
        lines = [f"# Folder: {folder.relative_to(REPO).as_posix() or '(repo root)'}", "", "#folder", ""]
        if folder != REPO:
            lines.append(f"Inside: [[{note_name_for_folder(folder.parent)}]]")
        write_note(note_name_for_folder(folder), lines)

    print(f"Wrote {len(python_files)} file notes and {len(folders)} folder notes to {MAP_DIR}")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Generate views/semester-topic-map.canvas from the repo's actual curriculum files.

Disposable, reproducible projection — course files under docs/, planning/,
lessons/, and assignments/ remain the source of truth. Re-run this script
any time those files change; do not hand-edit the generated .canvas.

Usage: python3 scripts/views/generate_semester_topic_map.py
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
# NOTE: deliberately `views/`, not `.views/` — Obsidian hides dot-prefixed
# folders from its file explorer and index by default (no built-in setting
# reveals them, only third-party plugins), so a dot-folder here would be
# generated correctly but invisible/unopenable inside the app. Verified via
# the Obsidian forum and several "reveal hidden files" community plugins
# that exist specifically to work around this. Jeremy's call (2026-10-23):
# use a visible folder instead of installing a plugin.
OUT_PATH = REPO_ROOT / "views" / "semester-topic-map.canvas"

# Obsidian canvas preset colors: "1" red, "2" orange, "3" yellow, "4" green,
# "5" cyan, "6" purple. Week 10 (this week's focus) gets "1" to stand out.
HIGHLIGHT = "1"
ARC3_GROUP_COLOR = "4"
DRIFT_COLOR = "1"

nodes = []
edges = []
_id_counter = [0]


def nid(label):
    _id_counter[0] += 1
    return f"n{_id_counter[0]:03d}-{label}"


def file_node(path, x, y, w=320, h=90, color=None):
    node_id = nid(Path(path).stem)
    node = {
        "id": node_id,
        "type": "file",
        "file": path,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
    }
    if color:
        node["color"] = color
    nodes.append(node)
    return node_id


def text_node(text, x, y, w=340, h=120, color=None):
    node_id = nid("text")
    node = {
        "id": node_id,
        "type": "text",
        "text": text,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
    }
    if color:
        node["color"] = color
    nodes.append(node)
    return node_id


def group_node(label, x, y, w, h, color=None):
    node_id = nid("group")
    node = {
        "id": node_id,
        "type": "group",
        "label": label,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
    }
    if color:
        node["color"] = color
    nodes.append(node)
    return node_id


def edge(a, b, label=None, color=None):
    e = {"id": nid("edge"), "fromNode": a, "toNode": b,
         "fromSide": "right", "toSide": "left"}
    if label:
        e["label"] = label
    if color:
        e["color"] = color
    edges.append(e)


# ---- Title / grounding row -------------------------------------------------

title = text_node(
    "# CS1 Semester Topic Map\n"
    "Generated view — reproducible from `docs/curriculum/`, `planning/`, "
    "`lessons/`, and `assignments/`. Re-run "
    "`scripts/views/generate_semester_topic_map.py` to refresh; never hand-edit. "
    "Lives in `views/` (not `.views/`) so Obsidian's file explorer, which "
    "hides dot-prefixed folders by default, can actually show it.\n\n"
    "Arranged left-to-right by the real Fall 2026 week sequence, grouped by "
    "Coding Odyssey arc. Arrows carry the *why* — what concept the next step "
    "actually depends on, not just file adjacency.",
    x=-200, y=-520, w=900, h=180,
)
unit_map = file_node("docs/curriculum/unit-map.md", -200, -300)
course_seq = file_node("docs/curriculum/course-sequence.md", 180, -300)
arc_map = file_node("planning/coding-odyssey-arc-map.md", 560, -300)
edge(unit_map, course_seq, "durable unit list vs. full historical narrative")
edge(course_seq, arc_map, "historical sequence remapped onto real Fall 2026 weeks/arcs")

# ---- Arc 1: Foundations (Weeks 1-6) ----------------------------------------

arc1_group = group_node("Arc 1 — Foundations (Weeks 1-6)", -220, 0, 900, 260)
l01 = file_node("lessons/01-foundations-print-input.md", -180, 40, h=80)
l02 = file_node("lessons/02-variables-expressions-types.md", 180, 40, h=80)
l03 = file_node("lessons/03-branching.md", 180, 150, h=80)
l04 = file_node("lessons/04-loops.md", 540, 150, h=80)
edge(l01, l02, "print/input before values have names")
edge(l02, l03, "values enable conditions")
edge(l03, l04, "conditions repeat into loops")

# ---- Arc 2: First Real Choices (Weeks 7-9) ---------------------------------

arc2_group = group_node("Arc 2 — First Real Choices (Weeks 7-9)", 760, 0, 900, 380)
l05 = file_node("lessons/05-functions.md", 800, 40, h=80)
l06 = file_node("lessons/06-strings.md", 800, 150, h=90)
l09 = file_node("lessons/09-objects-you-use-classes-you-write.md", 1150, 260, h=100)
w09 = file_node("planning/week-09.md", 800, 260, h=90, color=DRIFT_COLOR)
edge(l04, l05, "repeated loop bodies get extracted into functions")
edge(l05, l06, "decomposition now applied to text data")
edge(l06, l09, "strings ARE objects (dot/method syntax) — first object model")
edge(w09, l09, "Week 9 plan now folds in a first custom class (2026-10-08 update)")

# ---- Arc 3: Systems That Remember Themselves (Weeks 10-14), THE FOCUS -----

arc3_group = group_node(
    "Arc 3 — Systems That Remember Themselves (Weeks 10-14) — THIS WEEK",
    -220, 440, 1900, 480, color=ARC3_GROUP_COLOR,
)
l07 = file_node("lessons/07-collections.md", -180, 480, h=90, color=HIGHLIGHT)
p_w10 = file_node("planning/week-10.md", 180, 480, h=90, color=HIGHLIGHT)
gate_w10 = file_node("assignments/odyssey_gates/week-10.md", 540, 480, h=100, color=HIGHLIGHT)
p_w11 = file_node("planning/week-11.md", 180, 620, h=90)
l08 = file_node("lessons/08-classes-and-modules.md", 900, 620, h=90)
p_w12 = file_node("planning/week-12.md", 1260, 620, h=80)
p_w13 = file_node("planning/week-13.md", 1260, 740, h=80)

edge(l09, l07, "same object idea, now TRACK MANY of them in a collection")
edge(p_w10, l07, "week's technical focus")
edge(p_w10, gate_w10, "weekly gate applies the concept to the student's own world")
edge(p_w10, p_w11, "lists first, dicts (lookup-by-key) continued next week")
edge(l07, l08, "KEY SEQUENCING DECISION: a noun already tracked in the Wk10-11 "
     "collection becomes a Wk12-13 class — collections before classes, "
     "reversed from the historical Ch.9-before-Ch.8 order")
edge(p_w11, p_w12, "dict lookup-by-name sets up the object a class will formalize")
edge(p_w12, p_w13, "Round 1 (define) -> Round 2 (objects interact)")
edge(l08, p_w12, "lesson content for both OOP rounds")

# ---- Drift note -------------------------------------------------------------

drift_note = text_node(
    "**Documentation drift (flagged, not fixed):**\n"
    "`planning/week-09.md` (committed 2026-10-08) explicitly says it "
    "*supersedes* the Week 9 framing in `planning/block-map.md` and "
    "`planning/coding-odyssey-arc-map.md` (both committed 2026-08-12), and "
    "says in its own text: 'Remapping Week 10 and later is a separate "
    "mission.' That remap has not happened yet — the arc-map/block-map "
    "still describe Week 9 as 'strings continued' with no class content. "
    "Source of truth for Week 9 right now is `week-09.md`; the arc map is "
    "stale on this one point.",
    x=760, y=950, w=700, h=260, color=DRIFT_COLOR,
)
edge(w09, drift_note, "superseded by")
edge(drift_note, arc_map, "stale framing not yet reconciled")

# ---- Arc 4/5: wrap-up (Weeks 15-17) ----------------------------------------

arc45_group = group_node("Arc 4/5 — Thanksgiving, Farkle/ML, Finals (Weeks 15-17)", 1700, 440, 620, 260)
l10 = file_node("lessons/10-farkle-ml.md", 1740, 480, h=90)
p_finals = file_node("planning/week-17-finals.md", 1740, 600, h=80)
edge(l08, l10, "ML week reuses the whole CS1 core (incl. collections/objects); no new syntax")
edge(l10, p_finals, "wrap-up and show-and-tell")
edge(p_w13, l10, "capstone build finishes before the applied fun week")

canvas = {"nodes": nodes, "edges": edges}

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUT_PATH.write_text(json.dumps(canvas, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {OUT_PATH} ({len(nodes)} nodes, {len(edges)} edges)")

#!/usr/bin/env python3
"""Geometrically validate an Obsidian .canvas file -- no Obsidian required.

Catches what structural JSON validation can't: edges whose line crosses
through an unrelated node's box, and text nodes whose content is too long
for their declared height (would need internal scrolling to read in
Obsidian, which is the "truncated card" problem). Pure stdlib -- no PIL/
cairosvg/etc., since this repo deliberately has no dependency manifest yet.

Also emits a plain-text SVG rendering (views/<name>.svg) for an actual
visual check: open it in a browser, or screenshot it via claude-in-chrome,
rather than trusting the geometry check alone.

Usage:
    python3 scripts/views/validate_canvas_layout.py [path/to/file.canvas]
"""
import json
import sys
from pathlib import Path

CHARS_PER_LINE = 45  # rough wrap estimate for the font/width this repo uses
LINE_HEIGHT = 20
PADDING = 24


def rect_of(node):
    return (node["x"], node["y"], node["x"] + node["width"], node["y"] + node["height"])


def segment_intersects_rect(p1, p2, rect):
    """True if segment p1->p2 crosses rect's interior (Liang-Barsky clip)."""
    x1, y1 = p1
    x2, y2 = p2
    rx1, ry1, rx2, ry2 = rect
    dx, dy = x2 - x1, y2 - y1
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x1 - rx1), (dx, rx2 - x1), (-dy, y1 - ry1), (dy, ry2 - y1)):
        if p == 0:
            if q < 0:
                return False
            continue
        t = q / p
        if p < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 > t1:
            return False
    # t0..t1 is the overlapping sub-segment; require a non-trivial overlap,
    # not just touching a corner/edge at t0==t1.
    return (t1 - t0) > 1e-6


def center(node):
    return (node["x"] + node["width"] / 2, node["y"] + node["height"] / 2)


def estimated_text_height(text):
    lines = text.count("\n") + 1
    wrapped = sum(max(1, (len(line) + CHARS_PER_LINE - 1) // CHARS_PER_LINE)
                   for line in text.split("\n"))
    return max(lines, wrapped) * LINE_HEIGHT + PADDING


def check(canvas_path: Path):
    data = json.loads(canvas_path.read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in data["nodes"]}
    problems = []

    for e in data["edges"]:
        a, b = nodes.get(e["fromNode"]), nodes.get(e["toNode"])
        if a is None or b is None:
            problems.append(f"edge {e['id']}: references missing node")
            continue
        p1, p2 = center(a), center(b)
        for nid, n in nodes.items():
            if nid in (e["fromNode"], e["toNode"]):
                continue
            if n["type"] == "group":
                continue  # groups are translucent background regions in
                # Obsidian; edges passing over one are normal, not a bug.
            if segment_intersects_rect(p1, p2, rect_of(n)):
                problems.append(
                    f"edge {e['fromNode']} -> {e['toNode']} crosses through "
                    f"unrelated node {nid}"
                )

    for nid, n in nodes.items():
        if n["type"] not in ("text", "file"):
            continue
        text = n.get("text", "")
        if not text:
            continue
        needed = estimated_text_height(text)
        if needed > n["height"] * 1.15:  # 15% slack before flagging
            problems.append(
                f"node {nid}: ~{needed}px of text in a {n['height']}px box "
                f"(would need scrolling to read)"
            )

    return data, problems


def render_svg(data, out_path: Path):
    nodes = data["nodes"]
    xs = [n["x"] for n in nodes] + [n["x"] + n["width"] for n in nodes]
    ys = [n["y"] for n in nodes] + [n["y"] + n["height"] for n in nodes]
    pad = 40
    minx, miny = min(xs) - pad, min(ys) - pad
    w, h = max(xs) - minx + pad, max(ys) - miny + pad

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
             f'width="{int(w)}" height="{int(h)}" font-family="sans-serif">']
    parts.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="white"/>')

    by_id = {n["id"]: n for n in nodes}
    for e in data["edges"]:
        a, b = by_id.get(e["fromNode"]), by_id.get(e["toNode"])
        if not a or not b:
            continue
        x1, y1 = a["x"] - minx + a["width"] / 2, a["y"] - miny + a["height"] / 2
        x2, y2 = b["x"] - minx + b["width"] / 2, b["y"] - miny + b["height"] / 2
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                     f'stroke="#999" stroke-width="1.5"/>')

    for n in nodes:
        x, y = n["x"] - minx, n["y"] - miny
        fill = {"1": "#ffdddd", "4": "#ddffdd"}.get(n.get("color"), "#f0f0f0")
        if n["type"] == "group":
            parts.append(f'<rect x="{x}" y="{y}" width="{n["width"]}" height="{n["height"]}" '
                         f'fill="none" stroke="#888" stroke-dasharray="4" stroke-width="2"/>')
            parts.append(f'<text x="{x+8}" y="{y+18}" font-size="13" font-weight="bold">'
                         f'{escape_xml(n.get("label",""))}</text>')
        else:
            parts.append(f'<rect x="{x}" y="{y}" width="{n["width"]}" height="{n["height"]}" '
                         f'fill="{fill}" stroke="#555"/>')
            label = n.get("file") or (n.get("text", "")[:30])
            parts.append(f'<text x="{x+6}" y="{y+16}" font-size="11">'
                         f'{escape_xml(str(label)[:40])}</text>')

    parts.append("</svg>")
    out_path.write_text("\n".join(parts), encoding="utf-8")


def escape_xml(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def main():
    canvas_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("views/semester-topic-map.canvas")
    data, problems = check(canvas_path)
    svg_path = canvas_path.with_suffix(".svg")
    render_svg(data, svg_path)

    print(f"Checked {canvas_path} ({len(data['nodes'])} nodes, {len(data['edges'])} edges)")
    print(f"SVG rendering: {svg_path} (open in a browser or screenshot to actually look)")
    if problems:
        print(f"\n{len(problems)} problem(s) found:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    else:
        print("No crossing edges or overflowing text boxes detected.")


if __name__ == "__main__":
    main()

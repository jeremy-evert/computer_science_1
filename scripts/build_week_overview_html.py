#!/usr/bin/env python3
"""Render a canvas_pages overview source to an HTML body for the weekly publish tool.

Menu slots (<!-- menu:KEY -->) are filled only from --link KEY=URL options; a
slot with no link is dropped with its label, so the page never links to
something that does not exist.
"""
import argparse, json, re
import markdown

ORDER = ["read", "listen", "watch", "deck", "quiz"]
LABELS = {"read": "Read", "listen": "Listen", "watch": "Watch", "deck": "Deck", "quiz": "Quiz"}


def render(source: str, links: dict[str, str]) -> str:
    source = re.sub(r"^# .*\n", "", source, count=1)
    source = re.sub(r"(?m)^- (Read|Listen|Watch|Deck|Quiz)\n<!-- menu:(\w+) -->\n?", "", source)
    html = markdown.markdown(source, extensions=["fenced_code", "tables"])
    items = "".join(
        f'<li><a href="{links[k]}">{LABELS[k]}</a></li>' for k in ORDER if k in links
    )
    menu = f"<ul>{items}</ul>" if items else ""
    if any(k not in links for k in ORDER):
        menu += "<p>More ways to learn this week will be added here when they are ready.</p>"
    html = re.sub(r"(<h2>Choose how you learn this</h2>)", r"\1" + menu.replace("\\", r"\\"), html, count=1)
    # "Lessons this week" is the anchor heading the walkthrough tool appends buttons after.
    return html.replace(
        "<h2>Choose how you learn this</h2>",
        "<h2>Lessons this week</h2>\n<h2>Choose how you learn this</h2>",
        1,
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--link", action="append", default=[], help="KEY=URL")
    ap.add_argument("--out-html", required=True)
    args = ap.parse_args()
    links = dict(x.split("=", 1) for x in args.link)
    unknown = sorted(set(links) - set(ORDER))
    if unknown:
        ap.error(f"unknown menu keys: {unknown}")
    html = render(open(args.source, encoding="utf-8").read(), links)
    open(args.out_html, "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    main()

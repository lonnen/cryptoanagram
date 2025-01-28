#!/usr/bin/python3

import json
import sys

USAGE = "Usage: python comics-parser.py <filename>"


def parse_comics(filename):
    try:
        with open(filename, "r") as file:
            comics = json.load(file)
            parsed = []
            for comic in comics:
                parsed.append(parse_comic(comic))
            print(json.dumps(parsed))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)


def parse_comic(comic) -> dict[str, str]:
    title, text, url, id = comic.values()
    panels = []
    metadata = []
    for panel in text.split("\n\n"):
        if panel.startswith("{{"):
            metadata.append(panel)
        else:
            panels.append(panel)
    if len(panels) != 6:
        print(
            f"Panel {id} has irregular number of panels: {len(panels)}", file=sys.stderr
        )
    return {
        "id": id,
        "title": title,
        "text": panels,
        "meta": metadata,
        "url": url
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    filename = sys.argv[1]
    parse_comics(filename)

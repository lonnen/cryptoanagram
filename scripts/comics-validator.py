#!/usr/bin/python3

import json
import sys

USAGE = """Usage: python comics-validator.py <filename>
    
    filename - the output of comics-parser.py
"""

def check_comics(filename):
    comic_id_pointer = 1
    try:
        with open(filename, "r") as file:
            comics = json.load(file)
            for comic in comics:
                id, _title, panels, metadata, _url = comic.values()
                if id > comic_id_pointer:
                    print(f"Comic {comic_id_pointer} is missing",
                        file=sys.stderr
                    )
                    comic_id_pointer=id
                elif id < comic_id_pointer:
                    print(
                        f"Comic {id} is duplicated",
                        file=sys.stderr
                    )
                    comic_id_pointer=id
                comic_id_pointer += 1
                if len(panels) != 6 and ("irregular" not in metadata):
                    print(
                        f"{id} has irregular panel count: {len(panels)}",
                        file=sys.stderr,
                    )
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    filename = sys.argv[1]
    check_comics(filename)

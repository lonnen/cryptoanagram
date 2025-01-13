#!/usr/bin/python3

import json
import sys

# take the raw_dino_comics.json file created by
# https://github.com/lonnen/dinocomics-scraper@v0.0.2 and earlier, parsing the text of
# each comic into an array of panels. This is baked into dinocomics-scraper@v0.0.3+
# and unecessary for more recent script outputs.

args = sys.argv

if len(args) < 2:
    print(f"usage:\n\n    $ ./panel-partition.py raw_dino_comics.json\n")
    sys.exit()

comics = []

with open(args[1]) as raw_file:
    data = json.load(raw_file)
    for comic in data:
        title, text, url, id = comic.values()
        panels = text.split('\n\n')
        panel_count = len(panels)
        comics.append({
            "id": id,
            "title": title,
            "text": panels,
            "url": url,
        })

print(json.dumps(comics))
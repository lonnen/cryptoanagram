#!/usr/bin/env bash

usage() {
    cat <<HELP

    Usage: $(basename "$0") raw_dino_comics.json [options] > dino_comics.txt

    Options:

      -h, --help              This message

    This transforms the output of github.com/lonnen/dinocomics-scraper by
    extracting just the text of the comics and discarding the json formatting,
    source material, and titles. The output is then sent to stdout

HELP
}


if [ "$#" -ne 1 ]; then
    usage
fi

case $1 in
    -h|--help)
        usage
        exit 0
        ;;
    *)
        # strip lines that do not contain at least one colon
        # strip lines that start
        # strip lines that are dos command prompts
        cat $1 | jq '.[].text' --raw-output | sed '/:/!d' | sed '/^{/d' | sed '/^\[/d' | sed '/^C:\\/d'
esac

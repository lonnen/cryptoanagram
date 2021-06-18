#!/usr/bin/python3

import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="fuuu up a text file")
    parser.add_argument('-n', help="how many words to a gram", type=int)
    parser.add_argument('-c', '--count', help="should ngrams be published with occurance counts",
        action='store_true')
    args = parser.parse_args()

    print(args)
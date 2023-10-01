#!/usr/bin/python3

import sys
import argparse

def positive__nonzero_int(i):
    int_i = int(i)
    if int_i < 1:
        raise ValueError("{} must be > 0".format(i))
    return int_i

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="fuuu up a text file")
    parser.add_argument('-n', help="how many words to a gram", type=positive__nonzero_int, default=1)
    parser.add_argument('-c', '--count', help="should ngrams be published with occurance counts",
        action='store_true')
    args = parser.parse_args()

    print(args)
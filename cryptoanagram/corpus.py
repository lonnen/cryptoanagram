import os

from more_itertools import windowed

from .word import Word


def ngrams(n, corpus="all_trex"):
    for line in load_lines(datadir() + "/" + corpus + ".txt"):
        words = line.split()
        for w in windowed(words, n):
            yield w


def wordset(corpus="all_trex"):
    return map(
        lambda x: Word(x[0]), [s for s in set(ngrams(1, corpus)) if s[0] is not None]
    )


def datadir():
    return os.path.join(os.path.dirname(__file__), "data")


def load_lines(filename):
    """Load a file containing a whitespace delimited list of strings"""
    with open(filename) as f:
        for line in f:
            yield line.strip()

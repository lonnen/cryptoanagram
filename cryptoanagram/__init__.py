# flake8: noqa
from .utils import datadir, load_lines

from more_itertools import windowed

from multiset import Multiset

__author__ = "Lonnen"
__email__ = "chris.lonnen@gmail.com"

# yyyymmdd
__releasedate__ = ""
# x.y.z
__version__ = "0.1.0"


QWANTZLE_LETTERS = (
    "ttttttttttttooooooooooeeeeeeeeaaaaaaallllllnnnnnnuuuuuuiiiiisssssddddd"
    + "hhhhhyyyyyIIrrrfffbbwwkcmvg:,!!"
)


def ngrams(n, corpus="all_trex"):
    for line in load_lines(datadir() + "/" + corpus + ".txt"):
        words = line.split()
        for w in windowed(words, n):
            yield w


def wordset(corpus="all_trex"):
    return map(lambda x: Word(x), set(ngrams(1, corpus)))


class Word:
    def __init__(self, ordered):
        self.ordered = ordered
        self.unordered = Multiset(ordered)


class Cryptoanagram:
    def __init__(
        self, ordered=[], unordered=QWANTZLE_LETTERS, dictionary=wordset("all_trex")
    ):
        self.unordered = Multiset(unordered)
        self.ordered = ordered
        self.dictionary = filter(
            lambda x: x.unordered.issubset(self.unordered), dictionary
        )

    def append_string(self, s):
        """append a string and subtract the letters from the pool"""
        w = Word(s)
        if w.issubset(self.unordered):
            self.ordered.append(w)
            self.unordered.difference_update(w)
            return True
        return False

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
    return set(ngrams(1, corpus))


class Cryptoanagram:
    def __init__(
        self, ordered, unordered=QWANTZLE_LETTERS, dictionary=wordset("all_trex")
    ):
        self.unordered = unordered
        self.ordered = ordered
        self.dictioary = dictionary

# flake8: noqa
from .utils import datadir, load_lines

import operator

from functools import reduce

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
    return map(lambda x: Word(x[0]), [s for s in set(ngrams(1, corpus)) if s[0] is not None])


class Word:
    def __init__(self, ordered):
        self.ordered = ordered
        self.unordered = Multiset(ordered)

    def __str__(self):
        return "Word: {}, {}".format(self.ordered, self.unordered)


class Cryptoanagram:
    def __init__(
        self, ordered, unordered=QWANTZLE_LETTERS, dictionary=wordset("all_trex")
    ):
        if isinstance(ordered, str):
            ordered = [x.strip() for x in ordered.split()]
        self.unordered = Multiset(unordered)
        self.ordered = ordered
        # super hacky, but we need the original dict for unordering words
        self._dictionary = dictionary
        self.dictionary = list(filter(self._filter, dictionary))

    def push(self, s):
        """append a string and subtract the letters from the pool"""
        w = Word(s)
        if w.unordered.issubset(self.unordered):
            return Cryptoanagram(
                self.ordered + [w.ordered],
                unordered=self.unordered.difference(w.unordered),
                dictionary=self._dictionary,
            )
        raise ValueError("Insufficient unordered letters")

    def pop(self):
        position = -1
        if len(self.ordered) == 0:
            raise IndexError("pop from empty list")
        p = self.ordered[position]
        return Cryptoanagram(
            unordered=self.unordered.union(Multiset(p)),
            ordered=self.ordered[0:position],
            dictionary=self._dictionary,
        )

    def _filter(self, word, threshold=0.5):
        probabilities = []

        probabilities.append(1.0 if word.unordered.issubset(self.unordered) else 0.0)

        # longest word is 11 letters
        probabilities.append(1.0 if len(word.ordered) < 12 else 0.0)

        # second longest word is 8 letters and is adjacent to 11
        if len(self.ordered) > 1 and len(self.ordered[-1]) == 11:
            probabilities.append(1.0 if len(word.ordered) == 8 else 0.0)

        return reduce(operator.mul, probabilities, 1.0) > 0.5

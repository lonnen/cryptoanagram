# flake8: noqa
from .corpus import datadir, load_lines, ngrams, wordset
from .word import Word

import operator

from functools import reduce

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


class Cryptoanagram:
    def __init__(
        self, ordered, unordered=QWANTZLE_LETTERS, dictionary=wordset("all_trex")
    ):
        if isinstance(ordered, str):
            ordered = [x.strip() for x in ordered.split()]
        self.ordered = ordered

        m_ordered = Multiset(ordered)
        m_unordered = Multiset(unordered)

        if not m_ordered.issubset(m_unordered):
            raise ValueError("Insufficient unordered letters")

        self.unordered = m_unordered.difference(m_ordered)
        # super hacky, but we need the original dict for unordering words
        self._dictionary = dictionary
        self.dictionary = list(filter(self._filter, dictionary))

    def push(self, s):
        """append a string and subtract the letters from the pool"""
        w = Word(s)
        return Cryptoanagram(
            self.ordered + [w.ordered],
            unordered=self.unordered,
            dictionary=self._dictionary,
        )

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

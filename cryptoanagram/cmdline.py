import sys

from . import Cryptoanagram

def run():
    s = sys.argv[1:]
    c = Cryptoanagram(" ".join(s))
    print(c.ordered)
    # unordered = Multiset(unordered)
    # ordered = ordered
    # dictionary = list(filter(self._filter, dictionary))
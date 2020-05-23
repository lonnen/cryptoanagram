import sys

from . import Cryptoanagram

def run():
    s = sys.argv[1:]
    submitted = " ".join(s)
    c = Cryptoanagram(submitted)
    print("\nCandidate: ", submitted, "\n")
    print(c.ordered)
    print(c.unordered)
    for w in c.dictionary:
        print(w.ordered)
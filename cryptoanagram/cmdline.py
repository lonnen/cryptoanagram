import sys

from . import Cryptoanagram

def run():
    s = sys.argv[1:]
    submitted = " ".join(s)
    c = Cryptoanagram(submitted)
    print("\n")
    print("Candidate: ", submitted, "\n")

    print("\n")
    print("Remaining: ", ''.join(sorted(c.unordered)), "\n")
    for w in c.dictionary:
        print(w.ordered)
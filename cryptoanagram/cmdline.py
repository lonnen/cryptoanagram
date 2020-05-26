import sys

from . import Cryptoanagram

def run():
    s = sys.argv[1:]
    submitted = " ".join(s)
    c = Cryptoanagram("")

    print("\n")
    print("Candidate: ", submitted)
    print("\n")
    print("Remaining: ", ''.join(sorted(c.unordered)))

    print("Next Words: \n")
    for w in c.dictionary:
        #print(w.ordered)
        pass
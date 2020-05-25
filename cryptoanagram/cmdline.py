import sys

from . import Cryptoanagram

def run():
    s = sys.argv[1:]
    submitted = " ".join(s)
    c = Cryptoanagram("")
    for word in s:
        c.push(word)
    print("\n")
    print("Candidate: ", submitted, "\n")

    print("\n")
    print("Remaining: ", ''.join(sorted(c.unordered)), "\n")

    print("Next Words: \n")
    for w in c._dictionary:
        print(w.ordered)
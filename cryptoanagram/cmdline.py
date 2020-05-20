import sys

from . import Cryptoanagram

def run():
    s = sys.argv[1:]
    c = Cryptoanagram(" ".join(s))
    print(c.ordered)

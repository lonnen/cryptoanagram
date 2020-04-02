import os

def datadir():
    return os.path.join(os.path.dirname(__file__), "data")

def load_words(filename):
    """Load a file containing a whitespace delimited list of strings"""
    with open(filename) as f:
        return [line.strip() for line in f]
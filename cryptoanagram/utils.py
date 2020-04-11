import os


def datadir():
    return os.path.join(os.path.dirname(__file__), "data")


def load_lines(filename):
    """Load a file containing a whitespace delimited list of strings"""
    with open(filename) as f:
        for line in f:
            yield line.strip()

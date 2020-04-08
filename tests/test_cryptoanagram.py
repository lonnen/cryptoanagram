from .context import cryptoanagram

import unittest


class TestSuite(unittest.TestCase):
    """the easiest person to fool is yourself"""

    def test_loading_data(self):
        assert cryptoanagram.load_lines(cryptoanagram.datadir() + "/all_trex.txt")


if __name__ == "__main__":
    unittest.main()

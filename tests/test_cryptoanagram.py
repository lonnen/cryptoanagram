from .context import cryptoanagram

import unittest


class TestSuite(unittest.TestCase):
    """the easiest person to fool is yourself"""

    def test_loading_data(self):
        assert cryptoanagram.load_lines(cryptoanagram.datadir() + "/all_trex.txt")

    def test_grams(self):
        tgrams = cryptoanagram.ngrams(3, corpus="test_grams")
        self.assertEqual(next(tgrams), ("I'm", 'at', 'your'))
        self.assertEqual(next(tgrams), ('at', 'your', 'house'))
        self.assertEqual(next(tgrams), ('your', 'house', 'like'))
        self.assertEqual(next(tgrams), ('Why', 'you', 'got'))
        self.assertEqual(next(tgrams), ('you', 'got', 'your'))
        self.assertEqual(next(tgrams), ('got', 'your', 'couch'))
        self.assertEqual(next(tgrams), ('your', 'couch', 'on'))
        self.assertEqual(next(tgrams), ('couch', 'on', 'my'))
        self.assertEqual(next(tgrams), ('on', 'my', 'Chucks?'))
        self.assertEqual(next(tgrams), ('Motherfucker', None, None))

if __name__ == "__main__":
    unittest.main()

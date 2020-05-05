from .context import cryptoanagram

from multiset import Multiset

import unittest


class TestSuite(unittest.TestCase):
    """the easiest person to fool is yourself"""

    def test_loading_data(self):
        assert cryptoanagram.load_lines(cryptoanagram.datadir() + "/all_trex.txt")

    def test_grams(self):
        tgrams = cryptoanagram.ngrams(3, corpus="test_grams")
        self.assertEqual(next(tgrams), ("I'm", "at", "your"))
        self.assertEqual(next(tgrams), ("at", "your", "house"))
        self.assertEqual(next(tgrams), ("your", "house", "like"))
        self.assertEqual(next(tgrams), ("Why", "you", "got"))
        self.assertEqual(next(tgrams), ("you", "got", "your"))
        self.assertEqual(next(tgrams), ("got", "your", "couch"))
        self.assertEqual(next(tgrams), ("your", "couch", "on"))
        self.assertEqual(next(tgrams), ("couch", "on", "my"))
        self.assertEqual(next(tgrams), ("on", "my", "Chucks?"))
        self.assertEqual(next(tgrams), ("Motherfucker", None, None))

    def test_wordset(self):
        self.assertEqual(
            sorted([x.ordered for x in cryptoanagram.wordset(corpus="test_grams")]),
            [
                ("Chucks?",),
                ("I'm",),
                ("Motherfucker",),
                ("Why",),
                ("at",),
                ("couch",),
                ("got",),
                ("house",),
                ("like",),
                ("my",),
                ("on",),
                ("you",),
                ("your",),
            ],
        )

    def test_word(self):
        b = cryptoanagram.Word("bears")
        s = cryptoanagram.Word("sabre")
        self.assertNotEqual(b.ordered, s.ordered)
        self.assertEqual(len(b.unordered.symmetric_difference(s.unordered)), 0)

    def test_cryptoanagram_init(self):
        c = cryptoanagram.Cryptoanagram("front bottoms")
        self.assertEqual(" ".join(c.ordered), "front bottoms")
        self.assertEqual(
            c.unordered.symmetric_difference(
                cryptoanagram.Cryptoanagram("bottomfronts").unordered
            ),
            Multiset({}),
        )

    def test_cryptoanagram_push_pop(self):
        c = cryptoanagram.Cryptoanagram("fundamental")
        d = c.push("theories")
        self.assertEqual(" ".join(d.ordered), "fundamental theories")
        self.assertEqual(
            d.unordered.symmetric_difference(c.unordered), Multiset("theories"),
        )

    def test_cryptoanagram_filter(self):
        c = cryptoanagram.Cryptoanagram("crypto")
        d = c.push("anagram")
        e = cryptoanagram.Cryptoanagram("ana crypto gram")
        self.assertEqual(
            sorted(d.dictionary, key=lambda x: x.ordered),
            sorted(e.dictionary, key=lambda x: x.ordered),
        )


if __name__ == "__main__":
    unittest.main()

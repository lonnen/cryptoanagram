from .context import cryptoanagram

from multiset import Multiset

import unittest

Cryptoanagram = cryptoanagram.Cryptoanagram
Word = cryptoanagram.Word


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
        b = Word("bears")
        s = Word("sabre")
        self.assertNotEqual(b.ordered, s.ordered)
        self.assertEqual(len(b.unordered.symmetric_difference(s.unordered)), 0)

    def test_cryptoanagram_init(self):
        c = Cryptoanagram("front bottoms")
        self.assertEqual(" ".join(c.ordered), "front bottoms")
        self.assertEqual(
            c.unordered.symmetric_difference(Cryptoanagram("bottomfronts").unordered),
            Multiset({}),
        )

    def test_cryptoanagram_push_pop(self):
        c = Cryptoanagram("fundamental")
        d = c.push("theories")
        self.assertEqual(" ".join(d.ordered), "fundamental theories")
        self.assertEqual(
            d.unordered.symmetric_difference(c.unordered), Multiset("theories"),
        )

    def test_cryptoanagram_filter(self):
        c = Cryptoanagram("crypto")
        d = c.push("anagram")
        e = Cryptoanagram("ana crypto gram")
        self.assertEqual(
            sorted(d.dictionary, key=lambda x: x.ordered),
            sorted(e.dictionary, key=lambda x: x.ordered),
        )

    def test_filter_words_we_dont_have_letters_to_spell(self):
        c = Cryptoanagram(
            "I",
            unordered="thisisnotenoughletters",
            dictionary={Word("thishouldbefiltered")},
        )
        self.assertEqual(len(c.dictionary), 0)
        self.assertEqual(len(c._dictionary), 1)

    def test_filter_words_only_words_we_dont_have_letters_to_spell(self):
        c = Cryptoanagram(
            "I",
            unordered="thisisenoughlettersforone",
            dictionary={Word("thisfits"), Word("thishouldbefiltered"),},
        )
        print([x.ordered for x in c.dictionary])
        print([x.ordered for x in c._dictionary])
        print(c.ordered)
        print(c.unordered.items())
        self.assertEqual(len(c.dictionary), 1)
        self.assertEqual(len(c._dictionary), 2)

    def test_filter_longword(self):
        c = cryptoanagram.Cryptoanagram(
            "I",
            unordered="lessthanmorethaneleven",
            dictionary={
                cryptoanagram.Word("lessthan"),
                cryptoanagram.Word("morethaneleven"),
            },
        )
        self.assertEqual(len(c.dictionary), 1)
        self.assertEqual(len(c._dictionary), 2)
        self.assertEqual(c.dictionary[0].ordered, "lessthan")


if __name__ == "__main__":
    unittest.main()

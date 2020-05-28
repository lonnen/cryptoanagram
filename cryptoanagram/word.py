from multiset import Multiset


class Word:
    def __init__(self, ordered):
        self.ordered = ordered
        self.unordered = Multiset(ordered)

    def __str__(self):
        return "Word: {}, {}".format(self.ordered, self.unordered)

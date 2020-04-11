# flake8: noqa
from .utils import *

from more_itertools import windowed

__author__ = "Lonnen"
__email__ = "chris.lonnen@gmail.com"

# yyyymmdd
__releasedate__ = ""
# x.y.z
__version__ = "0.1.0"


QWANTZLE_LETTERS = (
    "ttttttttttttooooooooooeeeeeeeeaaaaaaallllllnnnnnnuuuuuuiiiiisssssddddd"
    + "hhhhhyyyyyIIrrrfffbbwwkcmvg:,!!"
)


def ngrams(n, corpus="all_trex"):
    lines = load_lines(datadir() + "/" + corpus + ".txt")

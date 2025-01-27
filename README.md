cryptoanagram
=============

This repository hosts various data sets derived from [Dinosaur Comics](https://qwantz.com/) that has been refined to be useful in finding solutions to [Dinosaur Comics 1663](http://qwantz.com/index.php?comic=1663).

The `data` folder contains data sets. If they're sourced from outside the repo, the data will have its own folder and README explaining the origins. Any top level data in there is derived from some script in this repository. Not every data set in this folder is manipulated or created by a script in this repo - some of it is merely archival.

The `scripts` folder contains tools that manipulate the contents of the data folder. The `scripts/comics-parser.py` script is probably what you want if you're curious about how these data were derived.

This repo does not directly contain a solver of any kind, though it was created to support the solver [anagramist](https://github.com/lonnen/anagramist) and its predecessors.
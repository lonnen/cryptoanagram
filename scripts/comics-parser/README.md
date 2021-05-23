Comics Parser
---

A `Stack` based Haskell script for parsing transcriptions of Dinosaur Comics pulled from ohnorobot. These may be retrieved first with the [Dinocomics Scraper](https://github.com/lonnen/dinocomics-scraper), then by feeding the output through the `extract-text.sh` script from this repo.

In order to compile the script:

```
$ stack setup
$ stack exec -- gc ComicsParser.hs -o comicsParser
```

Then to run it:

```
$ ./comicsParser
```

Or run the file mid-development without compiling:

```
$ stack exec -- runghc Main.hs
```
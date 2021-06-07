comics-parser
---

lex and parse the extraced text of dinosaur comics, outputting them in a regularized form that is easier to work with later.

Features (it will eventually have):

- [x] remove the speaker
- [x] preserve case
- [x] preserve special characters
- [x] special characters are treated like their own word, except apostraphes
- [x] words are separated by single spaces

Turning this:

```
T-Rex: He'd certainly wish he'd stomped the soap out of the way (much as I now stomp this little house) as he passed on!
The House: oh baby i'm so glad we already live together and now are in a relationship; it's bound to make things smooth and not at all awkward.
```

Into this:
```
He'd certainly wish he'd stomped the soap out of the way ( much as I now stomp this little house ) as he passed on !
oh baby i'm so glad we already live together and now are in a relationship ; it's bound to make things smooth and not at all awkward .
```

usage:
```bash
$ cargo build; ./target/debug/comics-parser ../../data/dino_comics_extracted.txt
```
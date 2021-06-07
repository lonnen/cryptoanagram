use nom::{
    IResult,
    bytes::complete::{
        take_until,
        take_while,
        tag,
    },
    multi::fold_many0,
    sequence::{
        separated_pair,
        terminated,
    },
};

#[derive(Debug, Clone)]
pub enum LexItem {
    Speaker(String),
    Sep(char),
    Word(String),
    EOL
}

pub fn line(input: &str) -> IResult<&str, (&str, &str)> {
    separated_pair(
        take_until(":"),
        tag(":"),
        terminated(take_until("\n"), tag("\n"))
    )(input)
}

/// important: this intentionally does not include apostrophes
pub fn is_not_space_or_specific_punctuation(chr: char) -> bool {
    !" \t\n!\"#$%&()*+,-./:;<=>?@[]^_`{|}~".contains(chr)
}

/// certain punctuation marks should be treated as single-letter words
pub fn is_specific_punctuation(chr: char) -> bool {
    "!\"#$%&()*+,-./:;<=>?@[]^_`{|}~".contains(chr)
}

pub fn words(input: &str) -> IResult<&str, Vec<&str>> {
    fold_many0(
        take_while(
            is_not_space_or_specific_punctuation
        ),
        Vec::new(),
        |mut acc: Vec<_>, item| {
            acc.push(item);
            acc
        }
    )(input)
}

pub fn lex(input: &str) -> Result<Vec<LexItem>, String> {
    let mut result = Vec::new();
    let mut word = Vec::new();

    // let (input, speaker) = take_until(":")(input);

    let mut it = input.chars().peekable();
    while let Some(&c) = it.peek() {
        match c {
            '\n' => {
                it.next();
                result.push(LexItem::Word(word.clone().into_iter().collect()));
                word.clear();
                result.push(LexItem::EOL);
            },
            x if x.is_whitespace() => {
                it.next();

                if !word.is_empty() {
                    result.push(LexItem::Word(word.clone().into_iter().collect()));
                    word.clear();
                }
            },
            x if "!\"#$%&()*+,-./:;<=>?@[]^_`{|}~".contains(x) => {
                it.next();
                result.push(LexItem::Word(word.clone().into_iter().collect()));
                word.clear();

                word.push(x);
                result.push(LexItem::Word(word.clone().into_iter().collect()));
                word.clear();
            },
            x if x.is_ascii_alphanumeric() => {
                it.next();

                word.push(x);
            },
            _ => {
                return Err(format!("unexpected character {}", c));
            }
        }
    }

    Ok(result)
}

#[test]
fn test_line() {
    assert_eq!(line("professor: I can't believe it\n"), Ok(("", ("professor", " I can\'t believe it"))));
    assert_eq!(line("professor: believe me: it's bad\n"), Ok(("", ("professor", " believe me: it's bad"))))
}

#[test]
fn test_is_not_space_or_specific_punctuation() {
    assert!(is_not_space_or_specific_punctuation('a'));
    assert!(is_not_space_or_specific_punctuation('1'));
    // apostraphres are exempted but difficult to fit into function name
    assert!(is_not_space_or_specific_punctuation('\''));
    assert_eq!(is_not_space_or_specific_punctuation('['), false);
    assert_eq!(is_not_space_or_specific_punctuation(' '), false);
    assert_eq!(is_not_space_or_specific_punctuation('\t'), false);
    assert_eq!(is_not_space_or_specific_punctuation('\n'), false);
}

fn test_is_specific_punctuation() {
    assert_eq!(is_specific_punctuation('a'), false);
    assert_eq!(is_specific_punctuation('1'), false);
    assert_eq!(is_specific_punctuation('\''), false);
    assert!(is_specific_punctuation('['));
    assert!(is_specific_punctuation(' '));
    assert!(is_specific_punctuation('\t'));
    assert!(is_specific_punctuation('\n'));
}
use nom::{
    IResult,
    bytes::complete::take_until,
};

#[derive(Debug, Clone)]
pub enum LexItem {
    Speaker(String),
    Sep(char),
    Word(String),
    EOL
}

pub fn speaker(input : &str) -> IResult<&str, &str> {
    take_until(":")(input)
}

// pub fn eol(input: &str) -> IResult<&str, LexItem::EOL> {
//     take_while(is_newline)(input);
// }

pub fn lex(input: &str) -> Result<Vec<LexItem>, String> {
    let mut result = Vec::new();
    let mut word = Vec::new();

    let (input, speaker) = take_until(":")(input);

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
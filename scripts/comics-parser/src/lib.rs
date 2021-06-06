#[derive(Debug, Clone)]
pub enum LexItem {
    Word(String),
    EOL
}

pub fn is_ascii_alphanumeric_or_apostraphe(c: char) -> bool {
    c.is_ascii_alphanumeric() || c == '\''
}

pub fn lex(input: &String) -> Result<Vec<LexItem>, String> {
    let mut result = Vec::new();
    let mut word = Vec::new();

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
            x if is_ascii_alphanumeric_or_apostraphe(x) => {
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

pub struct ComicPanel {
    speaker: String,
    spoken: String
}

pub fn parse(input: Vec<LexItem>) -> ComicPanel {
    let mut speaker = Vec::new();

    let iterableInput = input.iter();

    for word in input.iter() {
        match word {

        }
    }

    Ok()
}
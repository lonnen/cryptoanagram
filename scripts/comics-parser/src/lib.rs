#[derive(Debug, Clone)]
pub enum GrammarItem {
    Speaker,
    Sep,
    Word
}

#[derive(Debug, Clone)]
pub enum LexItem {
    Speaker(String),
    Sep(char),
    Word(String),
}

fn lex(input: &String) -> Result<Vec<LexItem>, String> {
    let mut result = Vec::new();

    let mut it = input.chars().peekable();
    while let Some(&c) = it.peek() {
        match c {
            _ => {
                return Err(format!("unexpected character {}", c));
            }
        }
    }

    Ok(result)
}
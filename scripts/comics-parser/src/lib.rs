#[derive(Debug, Clone)]
pub enum LexItem {
    Word(String),
    EOL
}

pub fn is_character_word(c: char) -> bool {
    "!\"#$%&()*+,-./:;<=>?@[]^_`{|}~".contains(c)
}

pub fn expand_character_words(input: &str) -> String {
    let mut output = Vec::<char>::new();

    for c in input.chars() {
        match c {
            c if is_character_word(c) => {
                output.push(' ');
                output.push(c);
                output.push(' ');
            },
            _ => {
                output.push(c);
            }
        }
    }
    output.into_iter().collect()
}

pub fn tokenize(input: &str) -> Vec<&str> {
    input.split_whitespace().into_iter().collect()
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
            x if is_character_word(x) => {
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
fn test_expand_character_words() {
    assert_eq!(expand_character_words(""), "");
    assert_eq!(expand_character_words("a"), "a");
    assert_eq!(expand_character_words("abc"), "abc");
    assert_eq!(expand_character_words("["), " [ ");
    assert_eq!(expand_character_words("[abc]"), " [ abc ] ");
    assert_eq!(expand_character_words("can't"), "can't");
    assert_eq!(expand_character_words("can! you"), "can !  you");
}

#[test]
fn test_tokenize() {
    assert_eq!(tokenize("I can't believe it"), vec!["I", "can\'t", "believe", "it"]);
    assert_eq!(tokenize("I  can't    believe   it"), vec!["I", "can\'t", "believe", "it"]);
    assert_eq!(tokenize("I  can't    be[lie]ve   it"), vec!["I", "can\'t", "be[lie]ve", "it"]);
}

#[test]
fn test_expand_and_tokenize() {
    assert_eq!(
        tokenize(
            &expand_character_words(
                "I  can't    be[lie]ve   it")),
        vec!["I", "can\'t", "be", "[", "lie", "]", "ve", "it"]);
}
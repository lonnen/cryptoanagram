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
            }
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

pub fn parse(input: &str) -> Vec<String> {
    let expanded_words = expand_character_words(input);
    let output = tokenize(&expanded_words);
    output.into_iter().map(|w| w.into()).collect()
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
    assert_eq!(
        tokenize("I can't believe it"),
        vec!["I", "can\'t", "believe", "it"]
    );
    assert_eq!(
        tokenize("I  can't    believe   it"),
        vec!["I", "can\'t", "believe", "it"]
    );
    assert_eq!(
        tokenize("I  can't    be[lie]ve   it"),
        vec!["I", "can\'t", "be[lie]ve", "it"]
    );
}

#[test]
fn test_expand_and_tokenize() {
    assert_eq!(
        parse("I  can't    be[lie]ve   it"),
        vec!["I", "can\'t", "be", "[", "lie", "]", "ve", "it"]
    );
}

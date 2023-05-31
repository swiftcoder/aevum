#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Keyword<'a>(pub &'a str);

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Ident<'a>(pub &'a str);

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct NumericLiteral<'a>(pub &'a str);

#[derive(Debug, PartialEq, Eq, Clone, strum::Display)]
pub enum TokenType<'a> {
    Keyword(Keyword<'a>),
    Punctuation(&'a str),
    Ident(Ident<'a>),
    NumericLiteral(NumericLiteral<'a>),
    StringLiteral(&'a str),
}

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct TokenContext {
    pub line: usize,
    pub column: usize,
}

impl std::fmt::Display for TokenContext {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "line {}, column {}", self.line, self.column)
    }
}

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Token<'a> {
    pub token: TokenType<'a>,
    pub context: TokenContext,
}

impl std::fmt::Display for Token<'_> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        std::fmt::Display::fmt(&self.token, f)
    }
}

#[derive(Debug, PartialEq, Eq, thiserror::Error)]
#[error("lexer error {description} at {context:?}")]
pub struct LexError {
    pub description: String,
    pub context: TokenContext,
}

// Lexer implementation
pub fn tokenize(input: &str) -> Result<Vec<Token>, LexError> {
    let mut tokens = vec![];
    let mut line = 1;
    let mut column = 1;

    let mut chars = input.chars().peekable();

    let mut i = 0;

    while let Some(ch) = chars.next() {
        match ch {
            ' ' | '\t' => {
                column += 1;
                i += 1
            }
            '\n' => {
                line += 1;
                column = 1;
                i += 1;
            }
            '-' if chars.peek() == Some(&'>') => {
                chars.next();
                tokens.push(Token {
                    token: TokenType::Punctuation(&input[i..i+2]),
                    context: TokenContext { line, column },
                });
                i += 2;
            }
            '(' | ')' | '{' | '}' | ':' | ';' | ',' | '.' | '=' | '+' | '-' | '*' | '/' => {
                tokens.push(Token {
                    token: TokenType::Punctuation(&input[i..i + 1]),
                    context: TokenContext { line, column },
                });
                i += 1;
            }
            '0'..='9' => {
                let mut c = 0;
                while let Some('0'..='9') = chars.peek() {
                    chars.next().unwrap();
                    c += 1;
                }

                // handle decimals
                if let Some('.') = chars.peek() {
                    chars.next().unwrap();
                    c += 1;
                    while let Some('0'..='9') = chars.peek() {
                        chars.next().unwrap();
                        c += 1;
                    }
                }

                tokens.push(Token {
                    token: TokenType::NumericLiteral(NumericLiteral(&input[i..i + c])),
                    context: TokenContext { line, column },
                });
            }
            'a'..='z' | 'A'..='Z' => {
                let mut ident = ch.to_string();
                while let Some('a'..='z' | 'A'..='Z' | '0'..='9' | '_') = chars.peek() {
                    ident.push(chars.next().unwrap());
                }

                // handle any keywords
                let token_type = if ident == "fn" || ident == "struct" {
                    TokenType::Keyword(Keyword(&input[i..i + ident.len()]))
                } else {
                    TokenType::Ident(Ident(&input[i..i + ident.len()]))
                };

                tokens.push(Token {
                    token: token_type,
                    context: TokenContext { line, column },
                });
                i += ident.len();
            }
            '"' => {
                let mut text = String::new();

                let mut last_char = None;
                while let Some(c) = chars.peek() {
                    if *c == '"' && last_char != Some('\\') {
                        chars.next().unwrap();
                        break;
                    }

                    last_char = Some(*c);
                    text.push(chars.next().unwrap());
                }

                tokens.push(Token {
                    token: TokenType::StringLiteral(&input[i..i + text.len()]),
                    context: TokenContext { line, column },
                });
                i += text.len();
            }
            _ => {
                return Err(LexError {
                    description: std::format!("unknown token '{}'", ch),
                    context: TokenContext { line, column },
                })
            }
        }
    }

    Ok(tokens)
}

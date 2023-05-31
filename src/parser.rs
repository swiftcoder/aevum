use crate::{
    combinators::{
        by_ref, forward, opaque, optional, satisfy, satisfy_map, separated_by, skip_until,
        zero_or_more, Forward, Opaque, Parse, ParseExt, ParserState,
    },
    lexer::{Ident, Keyword, NumericLiteral, Token, TokenType},
};

#[derive(Debug, Clone)]
pub enum Expr {
    Atom(String),
    Add(Box<Expr>, Box<Expr>),
    Mul(Box<Expr>, Box<Expr>),
}

#[derive(Debug, Clone)]
pub struct Field {
    name: String,
    typename: String,
}

#[derive(Debug, Clone)]
pub struct Struct {
    name: String,
    fields: Vec<Field>,
}

#[derive(Debug, Clone)]
pub struct Function {
    name: String,
    return_type: Option<String>,
    arguments: Vec<Field>,
}

#[derive(Debug, Clone)]
enum ModuleItem {
    Struct(Struct),
    Function(Function),
}

#[derive(Debug, Clone)]
pub struct Module {
    structures: Vec<Struct>,
    functions: Vec<Function>,
}

#[derive(Debug, thiserror::Error)]
#[error("parser error {description}")]
pub struct ParseError {
    pub description: String,
}

pub fn parse<'a, 'b>(tokens: &'a [Token<'b>]) -> Result<Module, String> {
    let mut state = ParserState::new(tokens);

    let field_p =
        ident()
            .skip(punctuation(":"))
            .and(ident())
            .map(|(name, typename): (Ident, Ident)| Field {
                name: name.0.into(),
                typename: typename.0.into(),
            });

    let struct_p = keyword("struct")
        .with(ident())
        .skip(punctuation("{"))
        .and(separated_by(by_ref(&field_p), punctuation(",")))
        .skip(punctuation("}"))
        .map(|(name, fields): (Ident, Vec<Field>)| {
            ModuleItem::Struct(Struct {
                name: name.0.to_string(),
                fields,
            })
        });

    let expr_p = expr();

    // {
    //     let atom_p = ident().map(|i: Ident| Expr::Atom(i.0.into()));
    //     let factor_p = atom_p
    //         .skip(punctuation("+"))
    //         .and(by_ref(&expr_p))
    //         .map(|(a, b): (Expr, Expr)| Expr::Add(Box::new(a), Box::new(b)));

    //     let expr_inner = factor_p
    //         .skip(punctuation("*"))
    //         .and(by_ref(&expr_p))
    //         .map(|(a, b): (Expr, Expr)| Expr::Mul(Box::new(a), Box::new(b)));
    //     expr_p.set(Box::new(expr_inner));
    // }

    let func_p = keyword("fn")
        .with(ident())
        .skip(punctuation("("))
        .and(separated_by(by_ref(&field_p), punctuation(",")))
        .skip(punctuation(")"))
        .and(optional(punctuation("->").with(ident())))
        .skip(punctuation("{"))
        .skip(skip_until(punctuation("}")))
        .map(
            |((name, arguments), return_type): ((Ident, Vec<Field>), Option<Ident>)| {
                ModuleItem::Function(Function {
                    name: name.0.into(),
                    return_type: return_type.map(|i| i.0.into()),
                    arguments,
                })
            },
        );

    let module = zero_or_more(struct_p.or(func_p)).map(|s| {
        let mut structures = vec![];
        let mut functions = vec![];

        for i in s {
            match i {
                ModuleItem::Struct(s) => structures.push(s),
                ModuleItem::Function(f) => functions.push(f),
            }
        }

        Module {
            structures,
            functions,
        }
    });

    module.parse(&mut state)
}

fn term<'a>() -> impl Parse<'a, Token<'a>, Output = Expr> {
    opaque(|| {
        Box::new(ident().map(|i: Ident| Expr::Atom(i.0.into())))
            as Box<dyn Parse<'a, Token<'a>, Output = Expr>>
    })
}

fn factor<'a>() -> impl Parse<'a, Token<'a>, Output = Expr> {
    opaque(|| {
        Box::new(
            term()
                .skip(punctuation("+"))
                .and(expr())
                .map(|(a, b)| Expr::Add(Box::new(a), Box::new(b))),
        ) as Box<dyn Parse<'a, Token<'a>, Output = Expr>>
    })
}

fn expr<'a>() -> impl Parse<'a, Token<'a>, Output = Expr> {
    opaque(|| {
        Box::new(
            factor()
                .skip(punctuation("*"))
                .and(term())
                .map(|(a, b)| Expr::Mul(Box::new(a), Box::new(b))),
        )
    })
}

fn keyword<'a>(keyword: &'a str) -> impl Parse<'a, Token<'a>, Output = Token<'a>> {
    satisfy(|t: &Token| t.token == TokenType::Keyword(Keyword(keyword)))
}

fn punctuation<'a>(punct: &'a str) -> impl Parse<'a, Token<'a>, Output = Token<'a>> {
    satisfy(|t: &Token| t.token == TokenType::Punctuation(punct))
}

fn ident<'a>() -> impl Parse<'a, Token<'a>, Output = Ident<'a>> {
    satisfy_map(|t: &Token<'a>| {
        if let TokenType::Ident(ident) = &t.token {
            Some(ident.clone())
        } else {
            None
        }
    })
}

fn numeric_literal<'a>() -> impl Parse<'a, Token<'a>, Output = NumericLiteral<'a>> {
    satisfy_map(|t: &Token<'a>| {
        if let TokenType::NumericLiteral(num) = &t.token {
            Some(num.clone())
        } else {
            None
        }
    })
}

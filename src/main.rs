use anyhow::anyhow;

mod ast;
mod combinators;
mod lexer;
mod parser;

fn main() -> anyhow::Result<()> {
    let input = r#"
        struct Foo {
            data: u32,
        }

        struct Bar {
            data: u32,
        }

        fn add(a: u32, b: u32) -> u32 {
            a + b
        }

        fn main() {
            let foo = Foo{data: 5};

            let sum = add(foo.data, 7);

            println(sum);

            println("Hello, \"World\"!\n");
        }
    "#;

    let tokens = lexer::tokenize(input)?;

    // println!("{:?}", tokens);

    let ast = parser::parse(&tokens).map_err(|s| anyhow!(s))?;

    println!("{:#?}", ast);

    Ok(())
}

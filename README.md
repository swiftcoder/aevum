# Aevum

> **aevum** *noun*. the mean between time and eternity; the state of being of the angels in heaven.

Aevum is a playground for some programming language development ideas I have floating around. In its current state it implements a pretty rough compiler for a toy language. It uses ANTLR for parsing a lexing, python for the AST traversal, llvmlite to emit llvm IR assembly, and llvm itself to compile to native code.

## Dependencies

At a minimum you will need:

* Python - https://www.python.org/
* llvmlite - http://llvmlite.pydata.org/
* Antlr - http://www.antlr.org/
* LLVM - http://llvm.org/

## Language Features

* Functions and function calls.
* Declare and call external functions with C linkage.
* Structs.
* Variable declaration.
* Variable and member variable assignement.

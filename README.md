# Aevum

> **aevum** *noun*. the mean between time and eternity; the state of being of the angels in heaven.

Aevum is a playground for some programming language development ideas I have floating around. In its current state it implements a pretty rough compiler for a toy language. It uses ~~ANTLR~~ __PLY__ for parsing and lexing, python for the AST traversal, llvmlite to emit llvm IR assembly, and llvm itself to compile to native code.

## Dependencies

At a minimum you will need:

* Python - https://www.python.org/
* PLY - http://www.dabeaz.com/ply/
* llvmlite - http://llvmlite.pydata.org/
* LLVM - http://llvm.org/

I'd recommend installing all of the above via the Conda package manager (https://conda.io/docs/), to avoid version mismatches between LLVM and llvmlite.

## Language Features

* Functions and function calls.
* Declare and call external functions with C linkage.
* Structs.
* Variable declaration.
* Variable and member variable assignement.

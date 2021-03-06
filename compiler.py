#! /usr/bin/env python3

if __name__ == '__main__':
    import sys
    from pathlib import Path
    from parser import yacc
    from ast import Struct
    import type
    import stdlib
    from llvmlite import ir, binding
    from sorting import topological_sort
    import argparse

    parser = argparse.ArgumentParser(description='Compile Aevum source files')
    parser.add_argument('-o', dest='output_file', type=str, default='a.out', help='output file')
    parser.add_argument('intput_file', type=str, nargs='+', help='input files')
    args = parser.parse_args()

    source = Path(args.intput_file[0]).read_text()
    ast = yacc.parse(source)

    module = ir.Module(name="main")
    module.triple = binding.get_default_triple()

    dependencies = [(a, []) for a in type.builtin_types()]

    symboltable = type.builtins();
    stdlib.standard_library(symboltable, dependencies, module);

    # first populate the symbol table
    for s in ast:
        s.populate_symbol_table(symboltable)

    # gather type dependencies
    for s in ast:
        dependencies += s.dependent_types(symboltable)

    # sort it by dependency order
    ordered = topological_sort(dependencies)

    # now that we have the dependency order, check the types
    for t in ordered:
        t.typecheck(symboltable)

    for t in ordered:
        t.typecheck_body(symboltable)

    #print('\n' + '\n\n'.join(str(s) for s in ast))

    for s in ast:
        s.emit(module)

    with open(args.output_file, 'w') as output_file:
        output_file.write(str(module))

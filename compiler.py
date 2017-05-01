#! /usr/bin/env python3

if __name__ == '__main__':
    import sys
    from pathlib import Path
    from parser import yacc
    from ast import Struct
    from typemap import *
    from llvmlite import ir, binding
    from sorting import topological_sort

    source = Path(sys.argv[1]).read_text()
    ast = yacc.parse(source)

    # first populate the symbol table
    symboltable = builtins();
    for s in ast:
        s.populate_symbol_table(symboltable)

    # gather type dependencies
    dependencies = [(a, []) for a in [Int32Type, FloatType, StrType]]
    for s in ast:
        dependencies += s.dependent_types(symboltable)

    # sort it by dependency order
    ordered = topological_sort(dependencies)

    # now that we have the dependency order, check the types
    for t in ordered:
        t.typecheck(symboltable)

    #print('\n' + '\n\n'.join(str(s) for s in ast))

    module = ir.Module(name="main")
    module.triple = binding.get_default_triple()

    for s in ast:
        s.emit(module)

    print(str(module))

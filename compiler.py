#! /usr/bin/env python3

if __name__ == '__main__':
    import sys
    from pathlib import Path
    from parser import yacc, symboltable
    from ast import Struct
    from llvmlite import ir, binding

    source = Path(sys.argv[1]).read_text()
    ast = yacc.parse(source)

    # first check struct types
    for s in ast:
        if isinstance(s, Struct):
            s.typecheck(symboltable)
    # now that we have structs in the sybol table, check everything else
    for s in ast:
        if not isinstance(s, Struct):
            s.typecheck(symboltable)

    #print('\n' + '\n\n'.join(str(s) for s in ast))

    module = ir.Module(name="main")
    module.triple = binding.get_default_triple()

    for s in ast:
        s.emit(module)

    print(str(module))

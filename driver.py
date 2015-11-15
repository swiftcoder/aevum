#! /usr/bin/env python3

from antlr4 import *
from aevumLexer import aevumLexer
from aevumParser import aevumParser
from listener import Listener

def main(argv):
    input = FileStream(argv[1])
    lexer = aevumLexer(input)
    stream = CommonTokenStream(lexer)
    parser = aevumParser(stream)
    tree = parser.top_level()

    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    listener.typecheck()
    print(listener.emit())
 
if __name__ == '__main__':
	import sys
	main(sys.argv)

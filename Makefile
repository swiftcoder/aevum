
all: AevumVisitor.py

AevumVisitor.py: Aevum.g4
	antlr4 -Dlanguage=Python3 -visitor -no-listener Aevum.g4

cloc:
	cloc [^Ave]*.py *.g4

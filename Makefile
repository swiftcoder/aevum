
all: AevumVisitor.py

AevumVisitor.py: Aevum.g4
	antlr -Dlanguage=Python3 -visitor -no-listener Aevum.g4

all: AevumVisitor.py

AevumVisitor.py: Aevum.g4
	antlr -Dlanguage=Python3 -visitor -no-listener Aevum.g4

cloc:
	# ignore auto-generated files when counting lines of code
	cloc [^Ave]*.py *.g4

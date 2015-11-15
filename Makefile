
.PHONY: all test

all: aevumLexer.py aevumParser.py aevumListener.py

aevumLexer.py aevumParser.py aevumListener.py: aevum.g4
	antlr4 -Dlanguage=Python3 $<

test: a.out

a.out: out.s
	clang $<

out.s: out.ll
	 clang -Os -S $<

out.ll: example/basic.ave *.py
	./driver.py $< >$@

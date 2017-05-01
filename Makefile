
.PHONY: all test

all: test

test: build/a.out

build/a.out: build/out.s
	clang -o $@ $<

build/out.s: build/out.ll
	 clang -Os -S -o $@ $<

build/out.ll: example/basic.ave *.py
	./compiler.py $< >$@

clean:
	rm -rf build/* parser.out parsetab.py

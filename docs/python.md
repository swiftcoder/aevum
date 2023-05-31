
Aevum is a new programming language. It is a functional language with swift-like named parameters and optional lazy evaluation.

There are several built in types: void, bool, u8, i32, f32, arrays which are written `[typename]`, and closures which are written `fn(u8, u8) -> u8`.

Functions look like this:
```
// Append `item` to `array`, and return a boolean for success or failure
fn append(item: u8, to array: [u8]) -> bool {
    // code goes here
    return true;
}
```

The return type is optional, in which case it is assumed to be void.

All paramters after the first have an external name defaulting to the parameter name, however note that the `array` parameter has an overridden external name `to` specified. The caller must the external name when invoking the function, like so: `append(8, to: [1, 2, 3])` (the first parameter does not have a default external name, nor was one specified). External names can be erased by specifying an underscore in their place: `foo(bar: u32, _ baz: u32)`.

The language supports generator functions, most often used to implement iterators:
```
gen fn range(start: u32, _ end: u32) -> u32 {
    let i = start;
    while i < end {
        yield i;
        i += 1;
    }
}
```

There are a fairly standard set of control flow statements. `if condition {}` with optional `else if condition2 {}` and `else {}`. `loop {}` for infinite loops. `while condition {}` for finite loops. `for x in y {}` where y is an iterator. `break` and `continue` for breakign out of loops or skipping iterations, respectively. `return` for returning values from functions (or early-exit from void functions). `yield` for yielding values from a generator.

The following operators are supported: `&&` and `||` for boolean types, `+`, `-`, `*`, and `/` for numeric types, and the index operator `foo[5]` for array types.

Local variables are introduced via `let x = 5` statements. The `=` operator may be used to reassign a new value to the let binding.

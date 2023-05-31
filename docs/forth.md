
Aevum is a Forth-like programming language, which means that it uses RPN (Reverse-Polish Notation), and models all data as a stack. Unlike forth, function arguments and variables are explicitly declared and referenced - each function (and each statement) executes as if starting from an empty stack. It is also an expression-centric language, so most things that would be statements in another language are treated as expressions.

There are several supported literals: numeric (`10, 12.5`), string (`"hello, World!"`), booleans (`true`, `false`), and arrays (`[10, 11, 12]`). There are also built-in types: u8, u32, f32, String, arrays (written `[u32]`), and `void`.

Functions are declared in a way that matches RPN, with the function name last. Control structures are mostly inspired by functional languages, so let's look at a few:
```
fn (a: u32, b: u32) max -> u32 {
    // the < operator pops 2 values off the stack, and pushes a boolean onto the stack
    // the if expression pops 3 elements off the stack, treats the first as the condition,
    // and pushes one of the remaining arguments back 
    a b < b a if
    // whatever is on top of the stack when the function ends will be the return value
}

fn print_array {
    // use a lambda (anonymous function) to print each item in an array
    // lambdas have an argument list between pipe characters, and a body
    // between braces. the foreach loop consumes an array and a closure
    // from the stack and is a true statement - it produces no value
    [1, 2, 3] |x| {x print} foreach 
}

fn (array: [f32]) square -> [f32] {
    // map applies a closure to each item in an array,
    // and returns the result as a new array
    array |a| {a*a} map
}

fn (array: [u32]) max_item -> u32 {
    array |a, b| {a b max} reduce
}
```

Local variables are declared using the `->` (right arrow) operator.

Execution starts with the function named `main`, which may optionally take an array of strings as an argument, and may optionally return an integer.

Here's a sample program:
```
// Declare a function to find the square of elements in an array
fn (array: [f32]) square_elements -> [f32] {
    array |a| {a a *} map
}

// Declare a function to find the maximum value in an array of unsigned 32-bit integers
fn (array: [u32]) max_value -> u32 {
    array |a, b| {a b max} reduce
}

// Main function that uses square_elements and max_value
fn main {
    // Declare input array
    [2.0, 3.0, 1.0, 5.0] -> input_array

    // Call square_elements function and store the result in squared_array
    input_array square_elements -> squared_array

    // Convert squared_array to an array of u32
    squared_array |a| {a u32} map -> squared_array_u32

    // Call max_value function and store the result in max_squared_value
    squared_array_u32 max_value -> max_squared_value

    // Print the maximum squared value
    "Max squared value: " print
    max_squared_value print
}

```

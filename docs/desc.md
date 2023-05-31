Aevum is a minimalist programming language intended to compile to WASM (which can then be executed in the borwser, in a WASM interpreter, or cross-compiled to native via the wasm2c transpiler).

Data is stored in structs, and structs can be combined with the | operator to form discriminated unions:
```
struct LocalRecord {
    id: u32,
    text: String,
}

struct ExternalRecord {
    external_id: u32,
}

type Record = LocalRecord | ExternalRecord;
```

Functions look like this:
```
fn get_record_text(record: Record) -> String {
    match record {
        LocalRecord{text, ..} => text,
        ExternalRecord{external_id} => fetch_external_record_text(external_id),
    }
}

fn print_record(record: Record) {
    println(get_record_text(record));
}

fn main() {
    print_record(LocalRecord{id: 123, text: "Hello, World!"});
}
```

use std::env;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input1.txt")
        .expect("Should have been able to read the file")
        .split("\n");

    for line in contents {

    }
}

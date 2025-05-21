/*

Q: if the guessed_number itself is mutable, why does read_line need to modify the reference to the guessed_number (aka &mut)?

*/

#![allow(unused_imports)]
#![allow(unused_variables)]
use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    let secret_number = rand::rng().random_range(1..=100); 
    // println!("[debug] this is secret_number: {secret_number}");

    let mut no_tries = 0;

    loop {
        println!("guess a number");
        let mut guessed_number = String::new();
        let no_bytes = io::stdin()
            .read_line(&mut guessed_number)
            .expect("failed to read line");
        // print!("your guess: {guessed_number}");
        // println!("it has {no_bytes} bytes");

        let guessed_number : i32 = 
            match guessed_number.trim().parse() {
                Ok(num) => num,
                Err(_) => {
                    println!("type only numbers");
                    continue;
                }
            }
        ;

        no_tries = no_tries + 1;

        match guessed_number.cmp(&secret_number) {
            Ordering::Less    => { println!("too small"); }
            Ordering::Equal   => { 
                println!("you win");
                println!("took you {no_tries} tries"); 
                break;
            }
            Ordering::Greater => { println!("too big"); }
        }
    }
}

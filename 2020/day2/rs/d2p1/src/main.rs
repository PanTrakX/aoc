use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut f = File::open("../../input.txt")?;
    let mut buffer = String::new();
    f.read_to_string(&mut buffer)?;
    
    let mut valid_pass_counts: u16 = 0;
    
    for line in buffer.split("\n")
    {
        let tmp = line.replace(":", "");
        let item = tmp.split(" ").collect::<Vec<&str>>();
        let range = item[0].split("-").collect::<Vec<&str>>();
        let min: u16 = range[0].parse().unwrap();
        let max: u16 = range[1].parse().unwrap();
        let chr = item[1];
        let password = item[2];

        let mut occurs: u16 = 0;
        for c in password.chars() {
            if chr.contains(c) {
                occurs += 1;
            }
        }
        if occurs >= min && occurs <= max {
            valid_pass_counts += 1;
        }
    }
    println!("{}", valid_pass_counts);
    Ok(())
}
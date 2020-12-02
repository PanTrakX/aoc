use std::io::Read;

fn main() {
    let mut file = std::fs::File::open("../../input.txt").unwrap();
    let mut buffer = String::new();
    file.read_to_string(&mut buffer).unwrap();

    let num_split = buffer.split("\n").filter_map(|s| s.parse::<i32>().ok());
    for x in num_split.clone() {
        for y in num_split.clone() {
            for z in num_split.clone() {
                if x + y + z == 2020 {
                    println!("{}", x * y * z);
                    return
                }
            }
        }
    }
}
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

use clap::Parser;

#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
struct Cli {
    input: std::path::PathBuf,
}

fn main() -> io::Result<()> {
    let args = Cli::parse();

    let file = File::open(args.input)?;

    let reader = BufReader::new(file);

    for line in reader.lines().map(|l| l.unwrap()) {
        println!(
            "{}",
            comics_parser::parse(&line)
                .join(" ")
                .split_once(":")
                .unwrap()
                .1
                .trim()
        );
    }

    Ok(())
}

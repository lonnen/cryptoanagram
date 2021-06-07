use std::fs::File;
use std::io::{self, prelude::*, BufReader};

use structopt::StructOpt;

#[derive(StructOpt)]
struct Cli {
    #[structopt(parse(from_os_str))]
    input: std::path::PathBuf,
}


fn main() -> io::Result<()> {
    let args = Cli::from_args();

    let file = File::open(args.input)?;

    let reader = BufReader::new(file);

    for line in reader.lines().map(|l| l.unwrap()) {
        comics_parser::parse(&line)
            .iter()
            .for_each(|p| println!("{:?}", p));
    }

    Ok(())
}
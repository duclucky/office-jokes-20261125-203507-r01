from argparse import ArgumentParser
from pathlib import Path

JOKE = "I marked lunch as 'Busy' on my calendar. My boss moved it to Thursday."


def main():
    parser = ArgumentParser(description="Write a single office joke.")
    parser.add_argument(
        "--output-dir", type=Path, default=Path("/output"),
        help="directory to create if needed and write entry.txt into",
    )
    output_dir = parser.parse_args().output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()

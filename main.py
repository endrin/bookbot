import os
import sys

from stats import get_frequencies, get_num_words


def usage():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        usage()

    example = sys.argv[1]
    print_report_on(example)


def print_report_on(src: os.PathLike):
    def second_in_pair(p: tuple[str, int]) -> int:
        (_, snd) = p
        return snd

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {src}...")

    with open(src) as f:
        content = f.read()

    num_words = get_num_words(content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    freqs = get_frequencies(content)
    print("--------- Character Count -------")
    for char, amount in sorted(freqs.items(), key=second_in_pair, reverse=True):
        print(f"{char}: {amount}")

    print("============= END ===============")


main()

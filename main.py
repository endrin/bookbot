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

    print(f"--- Begin report of {src} ---")

    with open(src) as f:
        content = f.read()

    num_words = get_num_words(content)
    print(f"{num_words} words found in the document")
    print()

    freqs = get_frequencies(content)
    for char, amount in sorted(freqs.items(), key=second_in_pair, reverse=True):
        print(f"The '{char}' character was found {amount} times")

    print("--- End report ---")


main()

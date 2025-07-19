import os
import string

from collections import Counter
from stats import get_num_words


example = "books/frankenstein.txt"


def main():
    print_report_on(example)


def frequencies(line: str) -> Counter[str]:
    normalized_line = line.strip().lower()
    chars = (c for c in normalized_line if c in string.ascii_lowercase)

    return Counter(chars)


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

    freqs = frequencies(content)
    for char, amount in sorted(freqs.items(), key=second_in_pair, reverse=True):
        print(f"The '{char}' character was found {amount} times")

    print("--- End report ---")


main()

import string

from collections import Counter


def get_num_words(content: str) -> int:
    words = content.split()
    return len(words)


def get_frequencies(content: str) -> Counter[str]:
    normalized_text = content.strip().lower()
    chars = (c for c in normalized_text if c in string.ascii_lowercase)

    return Counter(chars)

""" Gain proficiency in using positive and negative lookaheads and lookbehinds to match patterns based on
what precedes or follows them. """

import re

def lookahead_lookbehind_examples():
    test_strings = [
        "I love Python programming.",
        "Python is great for data science.",
        "Java is another popular programming language.",
        "I enjoy programming with Java and Python."
    ]

    lookahead_pattern = r"Python(?= programming)"

    for string in test_strings:
        match = re.search(lookahead_pattern, string)
        if match:
            print(f"Lookahead Match in: '{string}'")
            print(f"  Match found: '{match.group()}'")

    print()

    negative_lookahead_pattern = r"Python(?! programming)"

    for string in test_strings:
        match = re.search(negative_lookahead_pattern, string)
        if match:
            print(f"Negative Lookahead Match in: '{string}'")
            print(f"  Match found: '{match.group()}'")

    print()

    positive_lookbehind_pattern = r"(?<=Python )programming"

    for string in test_strings:
        match = re.search(positive_lookbehind_pattern, string)
        if match:
            print(f"Lookbehind Match in: '{string}'")
            print(f"  Match found: '{match.group()}'")

    print()

    negative_lookbehind_pattern = r"(?<!Python )programming"

    for string in test_strings:
        match = re.search(negative_lookbehind_pattern, string)
        if match:
            print(f"Negative Lookbehind Match in: '{string}'")
            print(f"  Match found: '{match.group()}'")

lookahead_lookbehind_examples()

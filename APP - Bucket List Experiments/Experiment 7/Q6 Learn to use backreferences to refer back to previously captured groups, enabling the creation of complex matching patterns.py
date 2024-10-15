""" Learn to use backreferences to refer back to previously captured groups, enabling the creation of complex
matching patterns. """

import re

def backreference_example():
    test_strings = [
        "This is a test test string.",
        "Hello world!",
        "Python Python is great.",
        "No repetitions here.",
        "What a beautiful beautiful day!"
    ]

    pattern = r"\b(\w+)\s+\1\b"  

    for string in test_strings:
        match = re.search(pattern, string)
        if match:
            print(f"Original String: '{string}'")
            print(f"  Repeated word found: '{match.group()}'")
        else:
            print(f"Original String: '{string}'")
            print("  No repeated words found")

backreference_example()

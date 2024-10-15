""" Apply the alternation operator (|) to construct patterns that can match one of several options within a
string. """

def match_grouped_alternation():
    test_strings = [
        "I love apples and oranges.",
        "I love bananas.",
        "I love grapes and kiwis.",
        "I love pears."
    ]

    pattern = r"(apples|bananas|grapes)"

    for string in test_strings:
        match = re.search(pattern, string)
        if match:
            print(f"Original String: '{string}'")
            print(f"  Match found: '{match.group()}'")
        else:
            print(f"Original String: '{string}'")
            print("  No match found")

match_grouped_alternation()

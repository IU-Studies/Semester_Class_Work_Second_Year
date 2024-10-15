""" Implement anchors (^, $) to match the start and end of strings, and use word boundaries (\b) to find whole
words. """

import re

def regex_with_anchors_and_boundaries():
    test_strings = [
        "Hello world",
        "Hello, world!",
        "Say hello to the world",
        "cat",
        "catalog",
        "The cat sat on the mat",
        "cats are great",
        "end of the world",
        "Goodbye world"
    ]

    patterns = {
        "starts_with_hello": "^Hello",     
        "ends_with_world": "world$",        
        "whole_word_cat": r"\bcat\b",       
        "whole_word_cats": r"\bcats\b",     
    }

    for string in test_strings:
        print(f"Testing string: '{string}'")
        for description, pattern in patterns.items():
            match = re.search(pattern, string)
            if match:
                print(f"  {description}: Match found: '{match.group()}'")
            else:
                print(f"  {description}: No match")

regex_with_anchors_and_boundaries()

""" Practice using quantifiers such as *, +, ?, and {n,m} to define how many times a character or group should
occur in a string. """

import re

def regex_examples():
    test_strings = [
        "aaa",
        "aa",
        "a",
        "",
        "aaaaa",
        "b",
        "abababa",
        "abc",
        "aaaa",
    ]

    patterns = {
        "zero_or_more": "a*",   
        "one_or_more": "a+",     
        "zero_or_one": "a?",     
        "exactly_two": "a{2}",   
        "two_or_more": "a{2,}",  
        "two_to_four": "a{2,4}", 
    }

    for string in test_strings:
        print(f"Testing string: '{string}'")
        for description, pattern in patterns.items():
            matches = re.findall(pattern, string)
            print(f"  {description}: {matches}")

regex_examples()

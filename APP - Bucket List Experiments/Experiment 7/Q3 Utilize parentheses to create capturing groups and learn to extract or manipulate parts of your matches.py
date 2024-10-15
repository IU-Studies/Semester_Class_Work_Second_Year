""" Utilize parentheses to create capturing groups and learn to extract or manipulate parts of your matches. """

import re

def extract_parts_using_capturing_groups():
    test_strings = [
        "John Doe, Age: 30",
        "Alice Smith, Age: 25",
        "Bob Johnson, Age: 22"
    ]
    
    pattern = r"(\w+) (\w+), Age: (\d+)"

    for string in test_strings:
        match = re.search(pattern, string)
        if match:
            first_name = match.group(1)  
            last_name = match.group(2)   
            age = match.group(3)         
            
            print(f"Full String: '{string}'")
            print(f"  First Name: {first_name}")
            print(f"  Last Name: {last_name}")
            print(f"  Age: {age}")

extract_parts_using_capturing_groups()

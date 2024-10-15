""" Work on practical examples such as validating email addresses, phone numbers, and extracting data from
text to apply your regex skills in real scenarios. """

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return f"'{email}' is a valid email address."
    else:
        return f"'{email}' is not a valid email address."

def validate_phone_number(phone):
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    if re.match(pattern, phone):
        return f"'{phone}' is a valid phone number."
    else:
        return f"'{phone}' is not a valid phone number."

def extract_urls(text):
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

def extract_dates(text):
    pattern = r'\b(\d{1,2}/\d{1,2}/\d{4})\b'
    return re.findall(pattern, text)

def main():
    emails = [
        "test@example.com",
        "user.name+tag+sorting@example.com",
        "invalid-email@.com",
        "@missingusername.com"
    ]

    phone_numbers = [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890",
        "123-45-6789"
    ]

    sample_text = """
    Check out these websites:
    - https://www.example.com
    - http://example.org
    - Important dates: 15/04/2023 and 12/05/2024
    """

    print("Email Validation:")
    for email in emails:
        print(validate_email(email))

    print("\nPhone Number Validation:")
    for phone in phone_numbers:
        print(validate_phone_number(phone))

    print("\nExtracted URLs:")
    urls = extract_urls(sample_text)
    print(urls)

    print("\nExtracted Dates:")
    dates = extract_dates(sample_text)
    print(dates)

main()



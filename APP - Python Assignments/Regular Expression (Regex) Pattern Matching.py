import re

def find_valid_emails(text):
    specific_email_pattern = r'[a-zA-Z0-9._%+-]+@example\.com'
    emails = re.findall(specific_email_pattern, text)
    return emails

emails = """
john@example.com, jane_doe@example.in, alice@example.com,
bob.smith@example.in, carol@example.com, dave@domain.com
"""

valid_emails = find_valid_emails(emails)

for email in valid_emails:
    print(email)

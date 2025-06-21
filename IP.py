import re


def check_email(text):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    match = re.match(pattern, text)
    if match:
        print(f"Valid email: {match.group()}")
    else:
        print("Not a valid email.")


test_emails = [
    "user@example.com",
    "invalid-email@",
    "another.user@domain.co",
    "bad@domain",
    "test@domain.com"
]
for email in test_emails:
    check_email(email)

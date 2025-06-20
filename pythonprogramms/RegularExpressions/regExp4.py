import re
phone_numbers_to_start=[
    "123-456-7890",
    "1234567890",
    "123 456 7890",
    "123-456-789",
    "abc-def-ghi",
    "123-456-7890 Ext. 123"
]
for num in phone_numbers_to_start:
    if re.compile(r"((\(\d{3}\)|\d{3})[- ]?)?\d{3}[- ]?\d{4}$").fullmatch(num):
        print(f"{num} is a VALID phone number")
    else:
        print(f"{num} is Not VALID Number")


import re
phone_numbers_to_test = [
    "(123) 456-7890",
    "123-456-7890",
    "(123)456-7890",
    "1234567890"
]
for num in phone_numbers_to_test:
    if re.match(r'^(\(\d{3}\)[ -]?|\d{3}-)\d{3}-\d{4}$', num):
        print(f"{num} is a valid phone number.")
    else:
        print(f"{num} is not a valid phone number.")

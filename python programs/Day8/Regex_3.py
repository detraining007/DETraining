import re
#write python program to evaluate phone number pattern
def phone_numbers():
    return[
        "123-234-7899",
        "(098)-676-8787",
        "9898889791",
        "(576)-(572)-(8978)",
        "567-67-87898"
    ]
for number in phone_numbers():
    if re.compile(r'^(\(\d{3}\)[-]?\d{3}[-]?\d{4}|\d{3}[-]?\d{3}[-]?\d{4})$').fullmatch(number):
        print(f"{number} is a valid")
    else:
        print(f"{number} is invalid")


import re
phonenumber=["1234567890","9836 4625 5033","90101666507","939 098 3067"]
for num in phonenumber:
    if re.compile(r"^((\(\d{3}\)|\d{3})[-]?)?\d{3}[-]?\d{4}$").fullmatch(num):
       print(f"{num}")
    else:
        print(f" num is a not valid phone number")

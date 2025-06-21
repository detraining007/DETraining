import re
s = "2025 is the year we are learning regex with geekforgeeks!"

a = re.match(r"\d{4}", s)
print(a)

b = re.search(r"regex", s)
print(b)
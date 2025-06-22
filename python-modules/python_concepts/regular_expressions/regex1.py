from re import *

s = "We are using this string as input for searching"

a = match(r"We",s)

b = search(r"input", s)
# print(a)
# print(b)
s2 = "2314 is my id"

# r"\d{n} <- for n digits

c = match(r"\d{4}",s2)

# r"^[A-M] <- for starting with letters from A to M

s3 = "Hello buddy"
d = search(r"^[A-H]",s3)
# print(d)
s4 = "i'm none"
p1 = compile(r"[A-Za-z0-9]")
e = p1.search(s4)
print(e)


import re

s="regex is important in python"
x=re.match(r"regex",s)
print(x)
y=re.search(r"regex",s)
print(y)

res=re.match(r"\d{4}","2025 is the year")
print(res)

res=re.search(r"\d{4}","shj2025 is the year")
print(res)

res1=re.match(r"^[A-Z]","Hello World")
print(res1)


def is_allowed_specific_char(string):
    charRe=re.compile(r"[a-zA-Z0-9]") #[^a-zA-Z0-9] these char doesn't check
    return charRe.search(string)
    # return not bool(string)

print(is_allowed_specific_char("ABCDabcdf12345"))
print(is_allowed_specific_char("&*%$##@()"))



ip="216.0096.647.7373"
string=re.sub('\.[0]*','.',ip)
print(string)

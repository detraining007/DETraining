from re import *


def text_match(pattern, string):
    if pattern.search(string):
        return "Found a match"
    else:
        return "No match found"

p1 = compile(r"ab*")  # one 'a' followed by any no of b's from 0,  for ab+ 1 to many b's after a
s1 = "absdf"
s2 = "aete"

# print(text_match(p1,s1))

p2 = compile(r"ab{2,4}")
s3 = "aby"



p3 = compile('a.*k$')  # $ start with a and end with k (k$ for end with k)
s4 = "alink"
# print(text_match(p3,s4))

# To remove 0's occuring after '.'
st = '\.[0]*'
ip = "250.003450530.405.08"
ans = sub(st,'.',ip)
# print(ans)

# 

s5 = "The quick brown fox jumps over the lazy dog"

# write a program to extract date from url


# program to validate phone numbers
phoneNums = ["123-456-7890",
             "1234567890",
             "123 456 7890",
             "123-456-789",
             "abc-def-ghij",
             "123-456-7890 Ext. 123"]
for phn in phoneNums:
    if compile(r"^((\(\d{3}\)|\d{3})[- ]?)?\d{3}[- ]?\d{4}$").fullmatch(phn):
        print(f"'{phn}' is a VALID phone number.")
    else:
        print(f"'{phn}' is NOT a VALID phone number.")



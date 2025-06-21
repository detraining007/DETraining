"""import re
s = "hii hello good morning"
a = re.match("reg", s)
print(a)

'''b = re.search(g."reg", s)
print(b)"""

import re
res = re.match(r"\d{3}", "20252 is the year")
print(res)


cc = re.search(r"d20", "abd2025 is the year")
print(cc)

# regularization

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[a-zA-Z0-9]')
    return charRe.search(string)
print(is_allowed_specific_char(("3BCDegdknbhbkd")))
print(is_allowed_specific_char("98"))


def text_match(text):
    patterns = 'ab[2,6]'
    if re.search(patterns, text):
        return "found a match"
    else:
        return "not found"
print(text_match("ab"))
print(text_match("a"))
print(text_match("abc"))


import re
def text_match(text):
    patterns = 'a.*b$'
    if re.search(patterns, text):
        return "found"
    else:
        return "not found"
print(text_match("aa@$%^bbbb"))


'''import re
ip = 757897439575762
string = re.sub('\'.[7]'*','.')'''

'''patterns = ['frog', 'dog', 'horse']
text = 'The quick brown fox jumps over the lazy dog'
for pattern in patterns:
    print("searching for "%s" in "%s" -> % (pattern, text),)'''



phone = ["1234-567-890","123-456-789",
         "234-543-1230","123-678-098"]

for num in phone:
    if re.compile(r"^((\(\d(3)\)|\d(3))[- ]?)?\d(3)[- ]?\d(4)$").fullmatch(num):
        print(f"{num} is a valid number")
              
                


        
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


import re
ip = 757897439575762
string = re.sub('\'.[7]'*','.')

        
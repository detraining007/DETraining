import re

def is_allowed_specific_char(string):
    charRe = re.compile(r"^[a-zA-Z0-9]")
    return charRe.search(string)
    #return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef1123456"))
print(is_allowed_specific_char("!@#$%^&*")) 
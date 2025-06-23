import re

# s ="We are learning regex expressions in python regex is useful for pattern matching"
#
# # match for search for begining of string
# a = re.match("regex",s)
# print(a)
# # search will check first occurence
# b = re.search("regex",s)
# print(b)
#
# # r"\{}" regex matching expression
# res = re.match(r"\d{2}","s2025 june")
# print(res)
#
# # r"\{}" regex matching expression
# ress = re.search(r"\d{4}","s2025 june")
# print(ress)
#
# a = re.match(r"^[A-Z]","Ramu Miriyala")
# print(a)

# def is_allow_specific(string):
#     charRe = re.compile(r'[a-zA-Z0-9.][^y]')
#     # return charRe.search(string)
#     return bool(charRe.search(string))
#
# print(is_allow_specific("ayBCGCDHGdghdfvgh538746."))
# print(is_allow_specific("$#%&*()#@"))

# pattern checking exactly three more than three b's
# def pattern_match(text):
#     pattern = "ab{3}?"
#     if re.search(pattern,text):
#         return "match found"
#     else:
#         return "match not found"
# print(pattern_match("vhdvbbabb"))
# print(pattern_match("abbbbcd"))
# print(pattern_match("abb"))
# print(pattern_match("babbbb"))

# pattern checking for "ab+"
# def pattern_match(text):
#     pattern = "ab+"
#     if re.search(pattern,text):
#         return "match found"
#     else:
#         return "match not found"
# print(pattern_match("vhdv"))
# print(pattern_match("abbbbcd"))
# print(pattern_match("ab"))
# print(pattern_match("babbbb"))

# pattern checking for range
def pattern_match(text):
    pattern = "ab{2,6}"
    if re.search(pattern,text):
        return "match found"
    else:
        return "match not found"
print(pattern_match("vhdv "))
print(pattern_match("abbbbcd"))
print(pattern_match("ab"))
print(pattern_match("babbbbbbbb"))
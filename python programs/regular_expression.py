# import re 
# s='''we are leraning regex with greek for greeks 
# regex is very useful regex for string matching'''
# a= re.match(r"regex",s)
# print(a)
# b=re.search(r"regex",s)
# print(b)




# res= re.match(r"\d{4}", "2025 is the year")
# print(res)





# res= re.search(r"\d{4}", "s2025 is the year")
# print(res)





# res= re.match(r"^[A-Z]", "Hello World")
# print(res)


# import re
# def is_allowed_specific_char(string):
#     charRe = re.compile(r'^[a-zA-Z0-9.]')
#     return charRe.search(string)
#     # return not bool(string)
# print(is_allowed_specific_char("ABCDEFabcdef123450"))
# print(is_allowed_specific_char("*&%@#!}{"))



# import re
# def text_match(text):
#     pattern='a.*?bbbbbb$'
#     if re.search(pattern,text):
#         return "found a match"
#     else:
#         return "not matched"
# print(text_match("c"))
# print(text_match("a"))
# print(text_match("abc"))
# print(text_match("ab@#$#$%^&bbbbbb"))




# import re
# ip = "2106.34.08.0094.196" 
# string = re.sub('\.[0]*','.',ip)
# print(string)


import re
phone_number_to_test=[
    "123-456-7890",
    "123456789",
    "123 456 7890",
    "123-456-789",
    "abc-def-ghij",
    "123-456-7890 Ext. 123"
]
for num in phone_number_to_test:
    if re.compile(r"^((\(\d{3}\)|\d{3})[- ]?)?\d{3}[- ]?\d{4}$").fullmatch(num):
        print(f"'{num}' is a VALID phone number.")
    else:
        print(f"'{num}'is not VALID phone number.")

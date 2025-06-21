# from re import *
# def is_allowed_specific_char(string):
#     c =compile(r'[^a-zA-Z0-9]')
#     return not bool(c.search(string))
# print(is_allowed_specific_char("a$BCDEFabcdef123456"))
# print(is_allowed_specific_char("&%$#@}{"))
# import re 
# def data(text):
#     patterns ='ab{2,7}?'
#     if re.search(patterns,text):
#          return 'found a match'
#     else:
#          return'not matched'
# print(data("c"))
# print(data("a"))
# print(data("abbbbbbbbc"))
# print(data("abbbbb"))
# print(data("aabbc"))
# import re 
# def data(text):
#     patterns="a.*b$"
#     if re.search(patterns,text):
#        return 'found a match'
#     else:
#         return('not matched')
# print(data('abbc'))
# print(data('abbbbb'))
# print(data('cb'))
# import re
# def data(text):
#      patterns ='^[a-zA-Z0-9_]'
#      if re.search(patterns,text):
#           return 'found a match'
#      else:
#           return'not matched'
# print(data("c"))
# print(data("a"))
# print(data("abbbbbbbbc"))
# print(data("abbbbb"))
# print(data("aabbc"))
# import re
# ip="233.234.33.456"
# s=re.sub('\.[2].*','.',ip)
# print(s)
import re
patterns=['fox','dog','cat','pig']
s='this is a fox and pig are runing cat will tide'
for patterns

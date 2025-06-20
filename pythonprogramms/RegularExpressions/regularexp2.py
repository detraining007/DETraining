#Write a programm that matches a strig that has an a followed by zero or more b's
import re
def text_search(text):
    # pattern="ab*"
     # pattern="ab+"   # *=>means 0 to many,,+ => means atleast one
    # pattern="ab{3}?"
    # pattern="ab{2,6}?"
    # pattern="{a-z}?_{A-Z}?"
    # pattern="a.*b$"
    pattern="^\w+"
    if re.search(pattern,text):
        return "Found a match"
    else:
        return "Not Matched!"
    
# print(text_search("c"))
# print(text_search("ab"))
# print(text_search("abc"))
# print(text_search("a"))
    
# print(text_search("abbb"))
# print(text_search("abbcd"))
    
# print(text_search("ab"))
# print(text_search("abbbb"))
    
# print(text_search("ABCefdg"))
    
# print(text_search("a$##%%bbbbFEDb"))
# print(text_search("aaabAbbbc"))
# print(text_search("ahbdhbhdb"))
    
print(text_search("The Quick brown fox jumps over the lazy dog"))






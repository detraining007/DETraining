import re
s = '''We are learning regex course
    regex is very useful''' 
a= re.search(r"regex",s)
print(a)
b = re.match(r"We",s)
print(b)
res = re.match(r"\w{2}","hello is a new year")
print(res)
res1 = re.match(r"[A-Z]","Hello World")
print(res1)

def is_allowed_specific_char(string):
    charRE = re.compile(r'[A-Za-z0-9.]')
    string = charRE.search(string)
    return  bool(string)

print(is_allowed_specific_char("ABCDEabcde01234"))
print(is_allowed_specific_char("ab"))
print(is_allowed_specific_char("&(@#$%)"))

def is_there(text):
    pattern = "ab*?"
    if re.search(pattern,text):
        return "found a match"
    else:
        return "not found a match"

print(is_there("a"))
print(is_there("ac"))
print(is_there("abbc"))

def min(text):
    pattern = "a{3}b{3}"
    if re.search(pattern,text):
        return "found a match"
    else:
        return "not found a match"

print(min("aaabbbc"))
print(min("abbbc"))
print(min("abbbb"))

def text_match(text):
    pattern = "ab{2,5}"
    if re.search(pattern,text):
        return "found a match"
    else:
        return "not found a match"

print(text_match("abb"))
print(text_match("abbbbbb"))

def lower_case(text):
    pattern = "^[a-z]*+_[a-z]*$"
    if re.search(pattern,text):
        return "found a match"
    else:
        return "not found a match"
    
print(lower_case("Abccdc_acacaa"))
print(lower_case("asasbsma_asasA"))

ip = "216.08.00904.196"
string = re.sub('\.[0]*',".",ip)
print(string)

phone_numbers_to_test=  [
    "123-456-7890",
    "1234567890",
    "123 456 789",
    "123-456-789",
    "abc-def-ghij",
    "123-456-7890 Ext.123"
]

for num in phone_numbers_to_test:
    if re.compile(r'^((\d{3}\)|\d{3})[- ]?)?\d{3}[- ]?\d{4}$').fullmatch(num):
        print(f'{num} is a valid phone number')
    else:
        print(f"{num} is not a valid number")



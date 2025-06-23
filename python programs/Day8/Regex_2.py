import re

#pattern checking first and last letters
# def text_match(text):
#     pattern = 'a.*b$' # meaning string should strat with 'a' and end with 'b'
#     if re.search(pattern,text):
#          return "match found"
#     else:
#         return "match not found"
#
# print(text_match("abkjbjb")) #string start with 'a' and end 'b'
# print(text_match("avhva"))

def text_match(text):
    pattern = r'^[a-zA-Z0-9_\s]*$' # meaning string should strat with 'a' and end with 'b'
    if re.search(pattern,text):
         return "match found"
    else:
        return "match not found"

print(text_match("abkjbjbbkjbsdkbkjn")) #string start with 'a' and end 'b'
print(text_match("@avhva6876876"))

ip="9849.9480.084.0098"
string=re.sub(r'\.[0]*','.',ip) #removes zero after dot
print(string)

patterns =['fox','dog','horse']
text ="The quick brown fox jumps over the lazy dog"
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern,text),)
    if re.search(pattern,text):
        print("matched")
    else:
        print("not matched")

def exract_date(url):
    pattern =r'/(\d{4})/(\d{1,2})/(\d{1,2})/'
    if re.search(pattern,url): #findall also can take
        return "matched"
    else:
        return "not match"
print(exract_date("http://www.gvjgjb/vhvcv/2025/09/6/ghjvcjh.com")) #matched
print(exract_date("http://www.gvjgjb/vhvcv/202/09/6/ghjvcjh.com"))  #not matched

def phone_number_match():
    return[
    "123-155-7686",
    "(452)-678-7893",
    "561-66-87387",
    "8898789879"
        ]
for num in phone_number_match():
    if re.compile(r'^(\(\d{3}\)[-]?\d{3}[-]?\d{4}|\d{3}[-]?\d{3}[-]?\d{4})$').fullmatch(num):
        print(f"{num} is a valid number")
    else:
        print(f"{num} not a valid number")


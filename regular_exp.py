import re
s='''hello world, this is python code 
 in vs'''
print(dir(re))#methods in re
a=re.match(r"hello",s)#checks whether hello is present at begining and gives pos
print(a)
b=re.search(r"vs",s)#gives pos of vs of first occurence
print(b)
c=re.match(r"\d{4}","1234 this is chetan")#checks the first 4 element are digits are not
print(c)
d=re.search(r"\d{2}","hi 23 chetan ")
print(d)
e=re.search(r"^[A-Z]","Hello world")
print(e)
#checking a first character in string only contains a-z,A-Z,0-9
def check(string):
    c=re.compile(r'^[a-zA-Z0-9.]')#[^a-zA-Z0-9.]opposite ga work avutundhi 
    return c.search(string)
print(check("ABCEabc012"))
print(check("&%@#!"))
print(check("@abcABC012"))
#checks in string whether a followed by atleast 1 b , ab+ = ab,abb,abbb,abbbbb,....
def text_match(text):
    patterns='ab+'
    if re.search(patterns,text):
        return 'found a match'
    else:
        return 'not matched'
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
print(text_match("bab"))
print(text_match("b"))
#a followed by atleast 3b's abbb,abbbb,abbbbb,abbbbbbb,...
print("a followed by atleast 3b's")
def text_match(text):
    patterns='ab{3}'
    if re.search(patterns,text):
        return 'found a match'
    else:
        return 'not matched'

print(text_match("abb"))
print(text_match("abbbbb"))
print(text_match("abbb"))
print("starting with a, between anything, ending with b")
def text_match(text):
    patterns='a.*b$'
    if re.search(patterns,text):
        return 'found a match'
    else:
        return 'not matched'
print(text_match("a#cdjfdsg8965_b"))
print(text_match("abbc"))
print(text_match("ab"))
print("starting with word accept else not accept")
def text_match(text):
    patterns='^\w+'
    if re.search(patterns,text):
        return 'found a match'
    else:
        return 'not matched'
print(text_match(" ab"))
print(text_match("abb"))
print("a-zA-Z0-9 ey udali")
def text_match(text):
    patterns='^[a-zA-Z0-9_]*$'#\s for checking space
    if re.search(patterns,text):
        return 'found a match'
    else:
        return 'not matched'
print(text_match("the ab"))
print(text_match("theabAB_12"))

print("removes 0 zeros from string which are comming after .")
ip="20016.08.0023.03.20003.10"
s=re.sub('\.[0]*','.',ip)
print(s)

patterns=['fox','dog','horse']
text='The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s"->' %(pattern,text))
    if re.search(pattern, text):
        print("Matched!")
    else:
        print("Not Matched!")

phone_numbers=["123 234-3453",
               "342-456-6543",
               "1234567890",
               "234-234-234",
               "cg2-344-1234"]
for num in phone_numbers:
    if re.compile(r"^((\(\d{3}\)|\d{3})[-]?)?\d{3}[-]?\d[4]$").fullmatch(num):
        print(f"{num} is valid number")
    else:
        print(f"{num} is not a valid number")



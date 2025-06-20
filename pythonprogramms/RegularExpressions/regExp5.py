import re
def match_num(string):
    text=re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))

print("-----Date Extraction-----")
def extract_date(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/',url)
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))

print("--Convert date Formate-----")
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',dt)
dt1="2026-01-02"
print("Original date in YYYY-MM-DD Format:",dt1)
print("New date in DD-MM-YYYY",change_date_format(dt1))

print("---Separate and print numbers-----")
text="Ten 10,Twenty 20,Thirty 30"
result=re.split("\D+",text)
for element in result:
    print(element)

print("---if email address valid or not---")

regex=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
def check(email):
    if(re.fullmatch(regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")

if __name__=='__main__':
    email="pushpa987@gmail.com"
    check(email)
    email="my.ownsite@our-earth.org"
    check(email)
    email="pushpa.com"
    check(email)
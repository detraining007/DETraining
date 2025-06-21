import re
s = "We are kearning regex with geekforgeeks regex is very useful regex for !"

a = re.match(r"regex", s)
print(a)

b = re.search(r"regex", s)
print(b)
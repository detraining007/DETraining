from re import *

# Match function -> returns match object if given pattern is present at start of given string

p1 = r"my"
s1 = "my name is ...."
o1 = match(p1,s1)
# print(o1)

# Search -> same as match, but for any position
# only first match is identified and returned
o2 = search("name",s1)
# print(o2)

# split -> splits the string at occurances of given pattern and returns a list of substrings generated
s2 = "My name is Akanksh my age is 23"
p2 = "Akanksh"
o3 = split(p2,s2)
# print(o3)

# sub -> replaces / substitutes , one with another string
s3 = "Apple and Apple Pie, Apple Cake"
p3 = "Orange"
o4 = sub("Apple","Orange",s3)
print(o4)
import re
'''' RegExpression is a sequences of character that firm a search pattern'''

# re.compile() is used to compile a regular expression pattern into a regex object

# 1. Searching for a pattern in a string
txt="The season in Spain is vey hot and Cold"

pattern=re.search("hot",txt) #Using search
print(pattern)

pattern=re.match("hot",txt)  #Using match 
print(pattern)

pattern=re.findall("hot",txt) #Using findall
print(pattern)

#2.Checking if a string starts with a number
pattern=(re.match(r"\d{4}", "2025 is the year"))
print(pattern)

#3.Matching a string that starts with a capital letter

pattern =(re.match(r"[A-Z]", "The Data is Integrated"))
print(pattern)

#4.  Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

def Name(String):
    pattern = re.compile(r"^[a-zA-Z0-9.]+$")
    if pattern.fullmatch(String):
        return "MatchFound"
    else:
        return "MatchNotFound"
    
String = "asasdcjkfpvrg12343"
print(Name(String))

#5. Write a Python program that matches a string that has an a followed by zero or more b's

def Name(String):
    pattern = 'ab*?'
    if re.search(pattern,String):
        return "Found Match"
    else:
        return "Not Found Match"
    
String="abbabsba"
print(Name(String))

#6 . Program that matches a string that has an a followed by 3 b's

def Name(String):
    pattern='ab{3}?'
    if re.search(pattern,String):
        return "Found Match"
    else:
        return "Not Found Match"
    
String="abbbabs"
print(Name(String))


#7.Range of b's

def Name(String):
    pattern='ab{2,7}?'
    if re.search(pattern,String):
        return "Found Match"
    else:
        return "Not Found Match"
    
String="aabbbbbc"
print(Name(String))


#8. Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
def Object(String):
    pattern= r'^[a-z]+_[a-z]+$'
    if re.search(pattern,String):
        return "Found"
    else:
        return "Not Found"
        
String="asastgy_asfcvr"
print(Object(String))


#9. Write a Python program that matches a word at the beginning of a string.aq 
import re
def Data(String):
    pattern= r"[^\w]"
    if re.match(pattern,String):
        return "Found"
    else:
        return "Not Found"
        
String="ijojnveo"
print(Data(String))

#10.Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

import re
def Data(Example):
    pattern=r"a?b$"
    if re.search(pattern,Example):
        return "Found a Match"
    else:
        return "Not Found"
        
Example="aabAbbbc"
print(Data(Example))
        
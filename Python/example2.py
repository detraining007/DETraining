str = "This is a python training class"
str_list = str.split(" ")
dic = {}

for ch in str_list:
    dic[ch] = len(ch)

max = float("-inf")

for x in dic:
    if dic[x] > max:
        keys = x
        max = dic[x]
        
print(f"{keys} {max}")

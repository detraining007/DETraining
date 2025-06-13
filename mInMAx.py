# min / max element in a given list
list = [2,4,6,8,10]
min = list[0]
max = list[0]
for i in list:
    if(i < min):
        min = i
    if(i > max):
        max = i
print(min)
print(max)
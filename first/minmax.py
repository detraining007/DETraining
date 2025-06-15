# To Find min and max elements in a list

li = [2,4,1,0,45,-3,6,-53,47]
min = 1000
max = -1000
for i in li:
    if(min > i):
        min = i
    if(max < i):
        max = i
print("minimum : ", min, " maximum : ", max)

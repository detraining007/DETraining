#Bubble Sort without any bulitin functions

li=[12,3,34,44,5,6,7,8,9,10,11,13,14,15]
length=len(li)
for num in range(length-1):
    for val in range(length-num-1):
        if li[val]> li[val+1]:
            #If condition statisfies then swap the numbers
            li[val],li[val+1]=li[val+1],li[val]
print(li)

                            
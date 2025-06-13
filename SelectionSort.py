#Selectional Sort
li=[12,3,34,44,5,6,7,8,9,10,11,13,14,15]
length=len(li)
for num in range(length-1):
    min_val=num
    #We are finding the minimum from the unsorted list
    for val in range(num+1,length):
        if li[val]<li[min_val]:
            min_val=val
    li[num],li[min_val]=li[min_val],li[num]
print(li)
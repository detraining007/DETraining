#Minimum and Maximum element in the list
lst = [2,4,1,-3,5]
min1=lst[0]
max1=lst[0]
for i in range(len(lst)):
    if lst[i]<min1:
        min1=lst[i]
    else:
        max1=lst[i]

print("Minimum num is",min1,"and Maximum number is",max1)
    

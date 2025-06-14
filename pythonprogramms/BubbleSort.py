def Bubble_sort(list):
    n=len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
            
list=[8,10,9,7,21,1,19]
print(Bubble_sort(list))

    
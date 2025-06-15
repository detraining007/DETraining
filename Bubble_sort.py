def Bubble_sort(list):
    n=len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[2,4,3,35,23,12,30]
print(Bubble_sort(list))
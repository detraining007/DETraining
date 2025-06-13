# Bubble Sort

def bubbleSort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(n-1-i):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


# Selection Sort

def minId(list,s):
    minIdx = s
    min = list[minIdx]
    for i in range(s,len(list)):
        if(list[i] < min):
            min = list[i]
            minIdx = i
    return minIdx

def selectionSort(list):
    n = len(list)
    for i in range(n):
        minIdx = minId(list,i)
        list[i],list[minIdx] = list[minIdx],list[i]


list1 = [3,1,6,9,2,0,4]
print(list1)
selectionSort(list1)
print(list1)
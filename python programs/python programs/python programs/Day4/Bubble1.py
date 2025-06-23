import random
import time
from Selection_Sort import selection_Sort


def bubble(arr):
    size = len(arr)

    for i in range(size-1,0,-1):
        flag = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1],arr[j]
            flag = True

        if not flag:
            break
num = int(input("Enter number"))
arr =[]
for i in range(num):
    arr.append(random.randint(1,100))
start = time.time()
bubble(arr)
end = time.time()
buble_time = end - start
starts = time.time()
selection_Sort(arr)
ends = time.time()
select_time = ends - starts
print(arr)
print("total time for bubble sort:",end - start)
print("total time for Selection sort:",ends - starts)
if select_time > buble_time:
    print("Select sort takes more time than " , select_time-buble_time )
else:
    print("Bubble sort takes more time than ", buble_time-select_time)
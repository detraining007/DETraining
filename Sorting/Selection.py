numList = [44,8,5,6,4,7,2,6,11,0]

def SelectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

print(SelectionSort(numList))
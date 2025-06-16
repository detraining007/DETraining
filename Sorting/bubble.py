list = [2,5,6,8,7,2,0,7]


def bubble_sort(arr):
    n = len(arr)
    for i in range (n-1):
        if arr[i]> arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print("Unsorted list:", list)
sorted_list = bubble_sort(list)
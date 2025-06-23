def selection_Sort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if arr[min_index] > arr[j]:
                arr[min_index] , arr[j] = arr[j] , arr[min_index]

arr = [20,4,55,7,11,89,0,-246]
selection_Sort(arr)
# print(arr)

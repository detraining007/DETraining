def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i
        # Find the index of the minimum element in the rest of the list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap if a smaller element was found
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


data = eval(input("Enter a list : "))
sorted_data = selection_sort(data)
print("Sorted array:", sorted_data)

'''
Output:

Enter a list : [3,6,9,4,6,3,9,5,7,19,8]
Sorted array: [3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 19]

'''
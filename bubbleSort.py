def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


data = eval(input("Enter a list : "))
print("Bubble Sorted:", bubble_sort(data))

'''
Outpout:

Enter a list : [2,9,3,8,4,7,5,6]
Bubble Sorted: [2, 3, 4, 5, 6, 7, 8, 9]

'''
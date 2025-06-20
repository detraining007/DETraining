#To implement bubble sort without using built in functions

def bubble_sort(arr):
    n = len(arr)
    for num in range(n):  
        for index in range(0, n-num-1):  # Last i elements are already in place
            if arr[index] > arr[index+1]:
                # Swap
                temp = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = temp


#arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Enter the numbers with spaces: ")
arr1=list(map(int,input().split()))
bubble_sort(arr1)
print("Bubble Sorted array:", arr1)

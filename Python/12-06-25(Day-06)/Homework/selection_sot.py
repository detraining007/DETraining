#To implement selection sort without using built in functions

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

# Example usage
#arr2 = [64, 25, 12, 22, 11]
print("Enter the numbers with spaces: ")
arr1=list(map(int,input().split()))
selection_sort(arr1)
print("Selection Sorted array:", arr1)

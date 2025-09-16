def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example
data = [64, 34, 25, 12, 22, 11, 90]
print("Quick Sort:", quick_sort(data))

def bubble_sort(row):
    n = len(row)
    for i in range(n):
        for j in range(0, n-i-1):
            if row[j] > row[j+1]:
                row[j], row[j+1] = row[j+1], row[j]
    return row

matrix = [[3, 1, 2], [9, 5, 6], [7, 8, 4]]

print("Original matrix:")
for row in matrix:
    print(row)

sorted_matrix = [bubble_sort(row[:]) for row in matrix]

print("\nSorted matrix (row-wise):")
for row in sorted_matrix:
    print(row)
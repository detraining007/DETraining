matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTranspose of the matrix:")
for row in transpose:
    print(row)
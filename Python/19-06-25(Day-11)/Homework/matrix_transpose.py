#To implement
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Find the number of rows and columns
rows = len(matrix)
cols = len(matrix[0])

# Create an empty matrix for the transpose
transpose = []
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)


print("Transpose of the matrix:")
for row in transpose:
    print(row)

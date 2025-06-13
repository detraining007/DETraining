def matrix_multiplication(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication is not possible! Number of columns in A must match rows in B.")
        return

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_matrix = matrix_multiplication(matrix_A, matrix_B)

if result_matrix:
    for row in result_matrix:
        print(row)
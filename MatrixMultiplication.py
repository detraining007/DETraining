# Basic program to print matrix multiplication

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))

def matrix_multiplication(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print("Matrix A:")
print_matrix(A)
print("\nMatrix B:")
print_matrix(B)

result = matrix_multiplication(A, B)
print("\nResult of A x B:")
print_matrix(result)
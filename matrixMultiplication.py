# Function to multiply two matrices A and B
def matrix_multiply(A, B):
    rows_A = len(A) # p
    cols_A = len(A[0]) # n
    rows_B = len(B) # n_b
    cols_B = len(B[0]) # q

    if cols_A != rows_B: # (if n!=n_B)
        raise ValueError("no of cols in A must equal no of rows in B")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)] 

    for i in range(rows_A): # p
        for j in range(cols_B): # q
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Input matrix A --- p*n
rows_A = int(input("Enter rows for Matrix A: "))
cols_A = int(input("Enter cols for Matrix A: "))
print("Enter elements of Matrix A :")
A = []
for i in range(rows_A):
    row = [int(x) for x in input().split()]
    if len(row) != cols_A:
        raise ValueError("Row does not have the correct no of columns.")
    A.append(row)

# Input matrix B --- n*q
rows_B = int(input("Enter rows for Matrix B: "))
cols_B = int(input("Enter cols for Matrix B: "))
print("Enter elements of Matrix B :")
B = []
for j in range(rows_B):
    row = [int(x) for x in input().split()]
    if len(row) != cols_B:
        raise ValueError("Row does not have the correct no of columns.")
    B.append(row)

# Multiply and print result
try:
    result = matrix_multiply(A, B)
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
except ValueError as e:
    print("Error:", e)

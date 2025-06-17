import random

def matrix_create(i,j):
  matrix = [[random.randint(1, 10) for _ in range(j)] for _ in range(i)]
  return matrix

i1= int(input("Enter no. of rows in matrix_1"))
j1 = int(input("Enter no.of columns in matrix_2"))
A = matrix_create(i1,j1)
for i in A:
  print(i)
i2= int(input("Enter no. of rows in matrix_1"))
j2= int(input("Enter no.of columns in matrix_2"))
B = matrix_create(i2,j2)
for i in B:
  print(i)

if(j1==i2 or i1==j2):
    # Initialize result matrix with zeros
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]

    # Matrix Multiplication Logic
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    print("Matrix Multiplication of A and B")
    for row in result:
      print(row)
else:
  print("Matrix multiplication not possible")




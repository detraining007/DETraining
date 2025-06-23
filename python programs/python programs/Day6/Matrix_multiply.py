def create_matrix(row,column):
    # empty matrix
    matrix =[]
    k = 1
    for i in range(row):
        ls=[]
        for j in range(column):
            ls.append(int(input(f"Enter element{k}")))
            k += 1
        matrix.append(ls)

    return matrix

# function for matrix multiplication
def matrix_multiply(matrix1 , matrix2):
    if column_1 == row_2:
       #Initializing result matrix with zeros
       rows_1, cols_1 = len(matrix1), len(matrix1[0])
       rows_2, cols_2 = len(matrix2), len(matrix2[0])
       # example i*j matrix i1*j1 matrix multiplied then formation new matrix is i*j1 matrix
       result = [[0] * cols_2 for _ in range(rows_1)]
       print("multiplication of matrix1 and matrix2")
       # Matrix Multiplication Logic
       for i in range(rows_1):
           for j in range(cols_2):
               for k in range(cols_1):
                   result[i][j] += matrix1[i][k] * matrix2[k][j]
       return result
    else:
         return "matrix multiplication not possible"


#Asking input for first matrix
row_1 = int(input("Enter no of rows in matrix1"))
column_1 = int(input("Enter no of columns in matrix1"))

# calling create_matrix function
matrix1 = create_matrix(row_1, column_1)

#Asking input for 2nd matrix
row_2 = int(input("Enter no of rows in matrix2"))
column_2 = int(input("Enter no of columns in matrix2"))

#Calling create_matrix function for 2nd matrix
matrix2 = create_matrix(row_2, column_2)

print("matrix1 you entered")
for row in matrix1:
    print(row)
print("matrix2 you entered")
for row in matrix2:
    print(row)

result = matrix_multiply(matrix1,matrix2)
if isinstance(result, str):
    print(result)
else:
    for row in result:
        print(row)
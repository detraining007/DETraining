#Transpose
import numpy as np
row_1=int(input("Enter the Number of rows: "))
col_1=int(input("Enter the Number of Cols:  "))
matrix_01=[]
matrix_02=[]


for i in range(row_1):
    row = list(map(int, input(f"Enter the elements in row {i+1}: ").split()))
    if len(row) != col_1:
        print(f"Error: You must enter exactly {col_1} elements.")
        exit()
    matrix_01.append(row)
print("matrix_01:", matrix_01)

#Transpose of Matrix
matrix_02=np.array(matrix_01)
print("Transpose of matrix: \n",matrix_02.T)

"""matrix_02 = []
for j in range(col_1):
    transposed_row = []
    for i in range(row_1):
        transposed_row.append(matrix_01[i][j])
    matrix_02.append(transposed_row)

print("\nTransposed matrix (matrix_02):")
for row in matrix_02:
    print(row)"""

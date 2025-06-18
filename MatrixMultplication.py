print("Matrix-01")
row_1 = int(input("Enter the Number of rows: "))
col_1 = int(input("Enter the number of columns: "))
matrix_01 = []

for i in range(row_1):
    row = list(map(int, input(f"Enter the elements in row {i+1}: ").split()))
    if len(row) != col_1:
        print(f"Error: You must enter exactly {col_1} elements.")
        exit()
    matrix_01.append(row)
print("matrix_01:", matrix_01)

print("Matrix-02")
row_2 = int(input("Enter the Number of rows: "))
col_2 = int(input("Enter the number of columns: "))
matrix_02 = []

for i in range(row_2):
    row = list(map(int, input(f"Enter the elements in row {i+1}: ").split()))
    if len(row) != col_2:
        print(f"Error: You must enter exactly {col_2} elements.")
        exit()
    matrix_02.append(row)
print("matrix_02:", matrix_02)

# Matrix multiplication
if col_1 != row_2:
    print("Matrix multiplication not possible: columns of Matrix 01 must equal rows of Matrix 02.")
else:
    result = []
    for i in range(row_1):
        result_row = []
        for j in range(col_2):
            sum_product = 0
            for k in range(col_1):
                sum_product += matrix_01[i][k] * matrix_02[k][j]
            result_row.append(sum_product)
        result.append(result_row)
    print("Resultant Matrix after multiplication:")   
    for val in result:
        print(list(val))

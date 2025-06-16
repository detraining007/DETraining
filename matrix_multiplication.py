rows=int(input("Enter Number of rows of first Matrix:"))
cols=int(input("Enter Number of cols of first matrix:"))
rows1=int(input("Enter Number of rows of second matrix:"))
cols1=int(input("ENter Number of cols of Second matrix:"))

A=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input(f"A[{i}][{j}]:")))
    A.append(row)

for row in A:
    print(row)

B=[]
for i in range(rows1):
    row=[]
    for j in range(cols1):
        row.append(int(input(f"B[{i}][{j}]:")))
    B.append(row)

for row in B:
    print(row)

print("The Multiplication of matrix")
C=[]
for i in range(rows):
    row=[]
    for j in range(cols1):
        product=0
        for k in range(cols):
            product+=A[i][k]*B[k][j]
        row.append(product)
    C.append(row)

for row in C:
    print(row)
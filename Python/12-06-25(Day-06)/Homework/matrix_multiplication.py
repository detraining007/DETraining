#To implement matrix multiplication of two matrices

# matrix1=[[1,2,3],[4,5,6],[7,8,9]]
# matrix2=[[2,4,6],[8,1,3],[5,7,9]]

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result=[[0,0],[0,0]]


for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]


for row in result:
    print(row)

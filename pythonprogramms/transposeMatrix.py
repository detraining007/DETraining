def Transpose(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

if __name__=="__main__":
    matrix=[[1,4,7],
            [2,5,8],
            [3,6,9]]
    print("Original Matrix")
    for row in matrix:
        print(row)
    Transpose(matrix)
    print("Transpose of above Matrix")
    for row in matrix:
        print(row)

   
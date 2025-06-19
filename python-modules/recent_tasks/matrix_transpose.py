
mat1 = [[2,1,5]]

def transposeMatrix(matrix):
    ncolst = len(matrix)
    nrowst = len(matrix[0])
    matrixt = [[None for _ in range(ncolst)] for _ in range(nrowst)]
    for col in range(nrowst):
        for row in range(ncolst):
            matrixt[col][row] = matrix[row][col]
    for row in matrixt:
        print(row)

transposeMatrix(mat1)
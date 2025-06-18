mat1 = [[2,4,6],
        [1,2,3],
        [5,6,7]]

mat2 = [[3,6,1],
        [5,2,8],
        [8,0,4]]


def multiplyMatrices(mat1, mat2):
    # if m1 is m x n and m2 is n x p then their product will be of order m x p
    mat3 = [[None for j in range(len(mat2[0]))] for i in range(len(mat1))]
    # row _m1 corresponds to row of matrix 1, similarly col_m2 as column of matrix 2

    # outer loop for traversing rows in mat1
    for row_m1 in range(len(mat1)):
        # for each row in mat1, we need to traverse each column of mat2, this mid loop serves that purpose
        for col_m2 in range(len(mat2[0])):
            sum = 0
            # for accessing corresponding elements in mat1 and mat2, we use for multiplying
            for col_m1 in range(len(mat1[0])):
                sum += mat1[row_m1][col_m1] * mat2[col_m1][col_m2]
            # storing evaluated value in corresponding position of matrix 3
            mat3[row_m1][col_m2] = sum
    for row in mat3:
        print(row)

if __name__ == "__main__":
    multiplyMatrices(mat1, mat2)

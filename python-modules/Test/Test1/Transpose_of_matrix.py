
def transpose(matrix):
    rlen = len(matrix)
    clen = len(matrix[0])
    res = [[None for _ in range(rlen)] for _ in range(clen)]

    for r in range(rlen):
        for c in range(clen):
            res[c][r] = matrix[r][c]

    return res


m1 = [[2,5,1,6],
      [3,6,9,0]]

for row in m1:
    print(row)

tm1 = transpose(m1)
print("Transposed matrix : ")
for row in tm1:
    print(row)
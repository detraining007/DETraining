
n = 3
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[0,0,0] for _ in range(n)]
print(m2)


for i in range(n):
    for j in range(n):
        # print(i,j,end=" ")
        # print("|",end=" ")
        # print(j,i)
        m2[i][j] = m1[j][i]
print(m2)
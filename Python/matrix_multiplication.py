m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l = len(m1)
result = [[0] * l for _ in range(l)] 

for i in range(l):
    # index = i
    for j in range(l):
        print((i,j),end = " ")
        # print(m1[i][j])
        print(j,i)
        for k in range(l):
            result[i][j] += m1[i][k] * m2[k][j]
print(result)
        
        # for k in range(3):
        #     # mul = m1[i][j] * m2[j][index]
        #     print(j,i)
        #     # ele+=mul
        #     index += 3
        # index = 0
        # print(ele)



m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = len(m1)
result = [[0] * l for _ in range(l)] 


for i in range(l):

    for j in range(l):
        print((i,j), end = " ")
        
        print(j,i)
        for k in range(l):
            result[i][j] += m1[i][k] * m2[k][j]
print(result)
        


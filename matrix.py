a=[[2, 4, 5],
[4, 5, 3],
[7, 8, 9]]
b=[[7, 8, 9],
[2, 4, 5],
[4, 5, 3]]
result=[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
for i in range(len(a)):
 for j in range (len(b[0])):
  for k in range(len(b)):
    result[i][j]+=a[i][k]*b[k][j]
for k in result:
    print(k)



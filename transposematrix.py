A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
transpose=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(A[j][i])
    transpose.append(row)
for row in transpose:
    print(row)
    

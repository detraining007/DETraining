# matrix
n = [[1,2],[3,4]]
b=[[0,0],[0,0]]
for rows in n:
    for columns in n:
        b[rows][columns]= n[columns][rows]
print(b)
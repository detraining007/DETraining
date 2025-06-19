def sort_matrix(matrix):
    mat_list=[]
    for row in matrix:
        for col in row:
            mat_list.append(col)

    n=len(mat_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if mat_list[j]>mat_list[j+1]:
                mat_list[j],mat_list[j+1]=mat_list[j+1],mat_list[j]
   
    row=len(matrix)
    col=len(matrix)
    c=[]
    index=0
    for i in range(row):
        row=[]
        for j in range(col):
            row.append(mat_list[index])
            index+=1
        c.append(row)
    print("Sorted Matrix")
    for row in c:
        print(row)

if __name__=="__main__":
    matrix=[[5,6,1],
            [2,9,4],
            [7,3,8]]
    print("Original Matrix")
    for row in matrix:
        print(row)
sort_matrix(matrix)
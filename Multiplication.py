mat1=[[1,3,5],
      [7,9,11],
      [13,15,17]]
mat2=[[2,4,6],
      [8,10,12],
      [14,16,18]]
def multliplication():
        result=[[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        if len(mat1)!=len(mat2):
            print("multiplication not possible")
        else:
            for i in range(len(mat1)):
                 for j in range(len(mat2[0])):
                      for k in range(len(mat2)):
                           result[i][j] +=mat1[i][k]*mat2[k][j]
            print(result)
multliplication()
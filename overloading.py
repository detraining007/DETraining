class overloading:
    def __add__(self,x):
        return 10

obj1=overloading()
obj2=overloading()

print(obj1+obj2)

matrix_A=[[1,2],[3,4]]
matrix_B=[[4,5],[6,7]]
empty=[[],[]]
for i in range(len(matrix_A)):
    for j in range(len(matrix_A)):
        for k in range(len(matrix_A)):
            empty[i][i]+=[matrix_A[i][j] * matrix_B[j][i]]
       


num1 = [[1,12],
        [3,24]]
num2 = [[22,4],
        [45,2]]

new_list=[]
  


result=[[0,0],
        [0,0]]
for i in range(len(num1)):
    for j in range(len(num2[0])):
        for k in range(len(num2)):
            result[i][j] += num1[i][j]*num2[k][j] # [0][0] *


for row in result:
    print (row)
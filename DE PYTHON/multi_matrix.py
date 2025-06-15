i1=int(input("enter the no of rows 1: "))
j1=int(input("enter the no of columns 1: "))
i2=int(input("enter the no of rows 2: "))
j2=int(input("enter the no of columns 2: "))

if i2==j1 :
    m1 = eval(input("enter the nested list as matrix 1: "))
    m2 = eval(input("enter the nested list as matrix 2: "))

    result = [[] * j2 for _  in range(i1)] 
    for l in range(i1):
        for m in range(j1):
              for k in range(j1):
                result[l][m] += m1[l][k] * m2[k][m]
    
    print(result)

elif i2!=j1:
    print("mulitiplication not possible")





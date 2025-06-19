
def B_Sort(x):
    sorted_flag = True
    while sorted_flag:
        sorted_flag = False
        for i in range(len(x)-1):
            # print((i,i+1))
            if x[i] > x[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
                sorted_flag = True
    return x



x = [6,3,2,8,1,0]
print(B_Sort(x))



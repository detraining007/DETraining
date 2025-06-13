x = [6,3,2,8,1,0]
sorted_list = []

for i in range(len(x)):
    min_ele = x[i]
    for j in range(i,len(x)):
        if x[j] < min_ele:
            min_ele = x[j]
        x[j] = x[i]
        x[i] = min_ele
print(x) 



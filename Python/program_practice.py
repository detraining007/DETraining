li = [4,5,6,0,8,2]
result = []

for i in range(len(li)):
    if i % 2 == 0:
        result.append(li[i]+1)
    elif i % 2 !=0:
        result.append(li[i]-1)

print(result)
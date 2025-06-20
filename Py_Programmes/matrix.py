data =[[63,54,17],
       [50,54,94],
       [70,55,88]]

value =[]
for i in data:
    value+=i
print(value)

def sorting(value):
    for i in range(len(value)):

        for j in range(len(value)-1):
            if value[j]>value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]
    
    return value

value1 = sorting(value)
print(value)

data1 = [value1[i*3:(i+1)*3] for i in range(3)]
print(data1)
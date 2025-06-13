# val = lambda x :x+10
# print(val(20))

listData = [1,2,3,4,5,6]

even = lambda x : x % 2 == 0

for i in listData:
    if even(i):
        print(i)

data = [x for x in listData if even(x)]

print(data)




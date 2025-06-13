# import math
# from functools import reduce
# #cmb = lambda n,r:math.comb(n,r)
# fac3 = lambda x:x%3==0
# m3 = lambda x,y : x*y
# list1 = [3,7,4,8,9,1,27,18,66]
# list2 = list(filter(fac3,list1))
# # print(list2)

# #print(filter(fac3,list1))

# ls = reduce(m3,list1)
# print(ls)
# print(m3(2,5))

def generator(n):
    for i in range(1,n):
        yield i

for i in range(3):
    generator1 = generator(i)
    print(generator1.__next__)

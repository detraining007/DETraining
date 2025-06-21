
n=[1,3,4,5,7,6]
l1=list(filter(lambda x:x%2!=0,n))
print(l1)
from functools import reduce
l2=reduce(lambda x,y:x+y,n)
print(l2)
l3=list(map(lambda x:x+10,n))

n=[1,3,4,5,7,6]
l1=list(filter(lambda x:x%2!=0,n))
print(l1)
from functools import reduce
l2=reduce(lambda x,y:x+y,n)
print(l2)
l3=list(map(lambda x:x+10,n))
95904fb3354e403a37a876779019fbdd2e0d26f6
print(l3)
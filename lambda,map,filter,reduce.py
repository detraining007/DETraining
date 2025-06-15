n=[1,3,4,5,7,6]
l1=list(filter(lambda x:x%2!=0,n))
print(l1)
from functools import reduce
l2=reduce(lambda x,y:x+y,n)
print(l2)
l3=list(map(lambda x:x+10,n))
print(l3)
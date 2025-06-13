n=[1,3,4,5,7,9]
list1=(filter(lambda x:x%2!=0,n))
print(list1)
from functools import reduce
list2=(reduce(lambda x,y:x+y,n))
print(list2)
list3=(map(lambda x:x+10,n))
print(list3)
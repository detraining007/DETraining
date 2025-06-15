
from functools import reduce
boys=[3,4,5,6,7]
good=reduce(lambda x,y : x*y, boys)
print(good)
from functools import reduce

lst = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66]
fil = list(filter(lambda X : X%2==0,lst))
print(fil)

# data = reduce
mapData = list(map(lambda x : x*x,lst ))
print(mapData)

reduceData = reduce(lambda x,y:x+y,lst)
print(reduceData)
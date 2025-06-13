from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=reduce(lambda x,y:x+y, numbers)
print(odd_numbers)

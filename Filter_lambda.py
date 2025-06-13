'''
num=[1,2,3,4,5,6,7,8,9]
odd_num=list(filter(lambda x:x%2!=0,num))
print(odd_num)
'''
'''
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10]
Z=reduce(lambda x,y:x+y,numbers)
print(Z)
'''
'''
sqrlst=[1,2,3,4,5]
Y=list(map(lambda item:item*item,sqrlst))
print(Y)
'''
def gen(n):
	for i in range(1,n):
		N=n*i
		yield N
d=gen(9)
print(next(d))
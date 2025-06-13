'''num=[2,3,4,5,6,7,8,9,34,56]
lop=list(filter(lambda y : y%3==0, num))
print(lop)
'''
'''
from functools import reduce
num=[2,3,4,5,6,7,8,9,34,56]
lop=reduce(lambda x,y : x*y, num)
print(lop)
'''
'''
num=[2,3,4,5,6,7,8,9,34,56]
lop=list(map(lambda x : x-6, num))
print(lop)
'''

def joy(num):
	for mem in range(1,num+1):
		yield str(mem) +" "+"Family member"
if __name__=="__main__":
	num=int(input("enter the number: " ))
	for family in joy(num):
		print(family)







#generators

def generatoritem(n):
	new_list = []
	for i in range(n):
		yield(i)
new_list = list(generatoritem(6))
print(new_list)

'''

def generatoritem(n):
	new_list = []
	for i in range(n):
		yield(i)
new_list = list(generatoritem(6))
print(new_list)
print(next(new_list))
print(new_list.__next__())
print(next(new_list))


def gen(n):
	for i in range(1,n):
		N = n*1
	yield N
d = gen(9)
print(next(d))


'''
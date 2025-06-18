class test(object):
	def function1(self):
		print("Test function1")
	def __init__(self):
		print("Test init")

class test_child(test):
	def function1(Self):
		print("child function1")
	def __init__(self):
		print("Child init")

obj = test()
obj1 = test_child()
print(obj.function1())
print(obj1.function1())

'''
output:

Test init
Child init
Test function1
None
child function1
None
'''
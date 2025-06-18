class test(object):
	def __new__(cls): # overriding the new to know what is happening in new
		print("I am in new")
		return super().__new__(cls) # if there is no return then AttributeError: 'NoneType' object has no attribute 'setter'
		#return 10.8 # AttributeError: 'float' object has no attribute 'setter'
	def __init__(self):
		print("I am in init")
		self.x = 10
		self.y = 20
	def setter(self,x1,y1):
		self.x = x1
		self.y = y1
	def getter(self):
		return self.x , self.y

if __name__=="__main__":
	obj = test()
	print(obj.getter())
	obj.setter(3,4)
	print(obj.getter())


'''
Output:

I am in new
I am in init
(10, 20)
(3, 4)

'''
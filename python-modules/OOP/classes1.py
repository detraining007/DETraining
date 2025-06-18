# class DE:
#     def __init__(self):
#         x = 2
#         y = 3
#     def setVal(self,x,y):
#         self.x = x
#         self.y = y
#     def getVal(self):
#         return self.x,self.y

# obj1 = DE()
# obj1.setVal(54,"variable")
# print(obj1.getVal())

class MyClass(object):
    def __new__(cls):
        
        print("i'm in new")
        return super().__new__(cls)
    def __init__(self):
        print("Im in init")
        self.x = 9
    
cls2 = MyClass()
print(cls2.x)


'''
__new__ is constructor it returns object
__init__ is initializer for initializing data
'''
class Test(object):
    def __init__(self):
        self.x=20
        self.y=30

    def __add__(self,a): #__add__ is built-in function 
        return self.x+self.y
    
obj1=Test()
obj2=Test()
print(obj1 + obj2) #Here + operand calls the __add__ Method
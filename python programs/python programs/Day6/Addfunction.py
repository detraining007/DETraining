class Test(object):
    def __init__(self,x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x
obj = Test(10)
obj1 = Test(20)
obj2 = Test(30)
obj3 = obj +obj1
print(obj3 + obj2)
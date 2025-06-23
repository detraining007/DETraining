class Test(object):
    def add(self):
        self.x=10
        self.y=23
        self.z=self.x+self.y
        return (self.z)
    def __init__(self,a):
        self.a = a
    def __add__(self, other):
        return self.a + other.a
obj = Test(5)
obj1 = Test(10)
print(obj.add())
print(obj.add() + obj1.add())
print(obj + obj1)
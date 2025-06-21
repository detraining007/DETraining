class Test(object):
    def __add__(self):
        self.x = 10
        self.y = 20
        self.z=self.x+self.y
        return(self.z)

def __init__(self,a):
    self.a = a
    def __add__(self,other):
        return(self.x + other.a)
    obj1 = Test(2)
    obj2 = Test(30)
    print(obj1.ad() + obj2.add())
    print(obj1+ obj2)  
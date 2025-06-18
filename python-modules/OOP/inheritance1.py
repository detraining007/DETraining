class Base:
    
    def __init__(self,name,s):
        super().__init__
        self.name = name
        self.s = s
    def func(self):
        print(self.name, self.s)
        print("func from Base")
    
class Derived1(Base):

    def func(self):
        print(self.name, self.s)
        print("func from Derived1")

class Derived2(Base):
    
    def func(self):
        print(self.name, self.s)
        print("func from Derived2")


obj1 = Base("Base",5)
obj1.func()
obj2 = Derived1("Derived1",6)
obj2.func()
obj3 = Derived2("Derived2",7)
print(obj3.name, obj3.s)
obj3.func()

class Child(Derived2,Derived1):
    def funcChild(self):
        print("From funcChild")

cobj = Child("child",8)
cobj.func()
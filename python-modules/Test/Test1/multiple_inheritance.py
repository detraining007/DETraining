class Base(object):
    def fun(self):
        print("i'm in Base Class")

class Derived(Base):
    def fun(self):
        print("I'm in Derived Class")

class Child(Derived,Base):
    def __init__(self):
        super().__init__()

b1 = Base()
d1 = Derived()
c1 = Child()

c1.fun()
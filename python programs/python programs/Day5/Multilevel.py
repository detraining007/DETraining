class Parent(object):
    def __init__(self):
       self.land = 2
       self.house =1
       self.total = self.land + self.house
       print("Parent class properties",self.total)
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.vehicles = 2
        self.plots =1
        self.totalChild = self.plots+self.vehicles+self.total
        print("Child class properties",self.totalChild)
class GrandChild(Child):
    def __init__(self):
        super().__init__()
        self.gold = 10
        self.bitcoin = 3
        self.totalGrandChild = self.totalChild+self.total+self.gold+self.bitcoin
        print("Grand Child properties",self.totalGrandChild)
obj = Parent()
# obj1 = Child()
obj2 = GrandChild()
print(obj2.bitcoin,obj2.land)
print(obj.land)
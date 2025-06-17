class Parent(object):
    def properties(self):
        self.land=4
        self.house=1
        self.total = self.land + self.house
        return self.total
class Child(Parent):
    def properties(self):
        super().properties()
        self.vehicles=2
        self.plots=1
        self.total_child = self.vehicles + self.plots +self.total
        return self.total_child
class Grand_child(Child):
    def properties(self):
        super().properties()
        self.gold = 10
        self.bitcoin =4
        return  self.total_child + self.gold +self.bitcoin



obj = Parent()
obj1 = Child()
obj2 = Grand_child()
print("Parent class properties",obj.properties())
print("Child class properties",obj1.properties())
print("Grand Child class properties",obj2.properties())
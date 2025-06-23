class Parent(object):
    def __add__(self, other):
        self.x=10
        self.y=29
        return self.x +self.y
class Child(Parent):
    def add(self):
        obj = Parent()
        obj1 = Parent()
        return obj + obj1
obj2 = Child()
print(obj2.add())
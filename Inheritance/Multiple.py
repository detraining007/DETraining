class Base(object):
    def __init__(self,val1,val2):
        self.val1 =val1
        self.val2 = val2
        print("This is Base class")
    def operation(self):
        return self.val1 + self.val2
        
class Child1(Base):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)
        print("This is child class 1,also contains Base class")
    def operation(self):
        return self.val1-self.val2
    
class Child2(Child1):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)
        print("This is child class 2,also contains child class 1 and Base class")
    def operation(self):
        print("Calling child1 operation",super().operation())
        print("Calling Base operation",Base.operation(self))
        return self.val1*self.val2
        
    

if __name__ == "__main__":
    obj2 = Child2(10,20)
    print(obj2.operation())
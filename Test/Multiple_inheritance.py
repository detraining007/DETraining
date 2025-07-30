class A(object):
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        print("This is Base class 1")
    def operation(self):
         return self.val1+self.val2

class B(object):
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        print("This is Base class 2")
    def operation(self):
        return self.val1 - self.val2


class C(A,B):
    def __init__(self, val1, val2):
        super().__init__(val1, val2)
        print("This is child class and takes A class print statement because of MRO")
    def operation(self):
        return super().operation()
    


if __name__ == "__main__":
    obj1 = C(1,2)
    print(obj1.operation())
    
        
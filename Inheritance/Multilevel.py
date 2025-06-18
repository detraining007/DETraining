class Base1(object):
    def __init__(self):
        print("This is Base class 1")
    def operation(self):
        print("operation in Base class 1")

class Base2(object):
    def __init__(self):
        print("This is Base class 2")
    def operation(self):
        print("operation in Base class 2")

class Child1(Base1,Base2):
    def __init__(self):
        super().__init__()
        print("This is child class")
    def operation(self):
        return super().operation()




if __name__ == "__main__":
    obj1 = Child1()
    obj1.operation()
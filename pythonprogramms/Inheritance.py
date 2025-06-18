class Baseclass():
    def __init__(self):
        self.p1=20
        print("Base class")
    def fun(self):
        print("Base class")
class Derivedclass1(Baseclass):
    def p2(self):
        print("Derived class 1")
class Derivedclass2(Baseclass):
    def p3(self):
        print("Derived class 2")
class childclass(Derivedclass1,Derivedclass2):
    def p4(self):
        print("this is child class")

if __name__=="__main__":
    obj=childclass()
    obj.p2()
    obj.fun()
    # obj1=Baseclass()

class parent:
    def parent(self):
        print("this is parent class")
class class1(parent):
    def parent(self):
        print("overriding parent class method from child class 1")
    def cls1(self):
        print("this is class 1")
class class2(parent):
    def cls2(self):
        print("this is class 2")
class class3(class1,class2):
    def cls3(self):
        print("this is class 3")
obj=class3()
obj.cls1()
obj.cls2()
obj.cls3()
obj.parent()
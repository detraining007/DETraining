class parent():
    def parent(self):
        print("this is parent class")
class child1(parent):
    def child1(self):
        print("this is child 1 class")
class child2(child1):
    def child2(self):
        print("tihs is child 2 class")
obj=child2()
obj.child2()
obj.child1()
obj.parent()
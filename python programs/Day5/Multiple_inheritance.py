class Father(object):
    def family(self):
        self.wife = "Bhagya"
        self.child1 = "Mamatha"
        self.child2 ="Ram"

        return self.wife , self.child1,self.child2
class Child1(Father):
    def family(self):
        wife,child1,child2=super().family()
        self.husband = "venkatesh"
        self.child1 = "Tanusree"
        self.child2 ="Advith"
        return self.husband,self.child1,self.child2 , wife
class Child2(Father):
    def family(self):
        husband,child1,child2,wife =super().family()
        self.age = 24
        return self.age,wife
class GrandChild(Child2,Child1):
    def family(self):
        wife , age= super().family()
        return wife,age
obj = GrandChild()
print(obj.family())

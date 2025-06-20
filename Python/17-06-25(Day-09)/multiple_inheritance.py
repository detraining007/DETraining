#To implement Multiple inheritance

class base:
    def __init__(self):
        self.x=10
        self.y=3

class child1(base):
    def add(self):
        self.z= self.x+self.y
        return self.z

class child2(base):
    def sub(self):
        self.z=self.x-self.y
        return self.z

if __name__=="__main__":
    test1=child1()
    print("addition of values given in base class: ",test1.add())
    test2=child2()
    print("subtraction of values given in base class: ",test2.sub())
    print(test2.add())

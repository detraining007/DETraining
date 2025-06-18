class parent:
    def __init__(self,x):
        self.x=x
        
    def __add__(self,other):#overrites the defualt add method
        return self.x+other.x
    def value(self):
        return self.x
obj3=parent(4)
obj4=parent(7)
obj5=parent(10)
x=obj3+obj4
print(obj3+obj4)
print(x+obj5.value())
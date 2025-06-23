class parent:
    def __init__(self,x):
        self.x=x
    def __add__(self,y):
        return self.x + y.x  
obj1=parent(6)
obj2=parent(8)
print(obj1 + obj2)
        
         
class Name:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    
obj=Name(10,20)
addition=obj.add()
print(addition)
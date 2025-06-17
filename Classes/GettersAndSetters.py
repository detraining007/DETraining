class Name:
    def __init__(self,x=10,y=30):
        self.x=x
        self.y=y



    def get_x(self): #Getter method
        return self.x,self.y
    
    def set_x(self,x,y):  #Setter Method
        self.x=x
        self.y=y
    
obj=Name()
print(obj.set_x(50,60))
print(obj.get_x())
class Name:

    def __new__(cls,x=10,y=30):
        print("I am in new method")
        return super().__new__(cls)


    def __init__(self,x=10,y=30):
        self.x=x
        self.y=y
    

    def get_x(self): #Getter method
        return self.x,self.y
    
    def set_x(self,x,y):  #Setter Method
        self.x=x
        self.y=y
        return self.x,self.y
    
obj=Name()
print(obj.set_x(50,60))
print(obj.get_x())
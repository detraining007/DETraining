#To implement classes and objects

class add():
    def __init__(self):
        self.x=3
        self.y=5

    def getter(self):
        return self.z
    
    def setter(self):
        self.x=int(input("enter x value: "))
        self.y=int(input("Enter y value: "))
        self.z=self.x+self.y
    
if __name__=="__main__":
    test1=add()
    print(test1.x,test1.y)
    setter1=test1.setter()
    val=test1.getter()
    print(val)
    

    
   

    
    
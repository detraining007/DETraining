# Classes and Objects 
class DE(object):
    def __init__(self):
        self.x=10
        self.y=20
    def __new__(cls):
        print("I am New")
        return super().__new__(cls)
    def getter(self): #get the values
        return self.x,self.y
    def setter(self): # to set the values
        self.x=20
        return self.x
if __name__=="__main__":
    obj=DE()
    print(obj.getter())
    print(obj.x,obj.y)
    print(obj.setter())
    

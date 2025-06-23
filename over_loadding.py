class Test(object):
    def __init__(self):
        self.x=12
        self.y=13
    def __add__(self,x,y):  
        print 
    def __add__(self,x):
        return "nikhil"
obj1=Test()
obj2=Test()
print(obj1+obj2)        


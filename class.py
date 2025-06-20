class test(object):
    def __init__(self):
        self.x=2
        self.y=8
    def getter(self):
        return self.x,self.y
    def setter(self):
        self.x=5 
        self.y=14
        return self.x,self.y
if __name__=="__main__":
    obj1=test()
    print(obj1.x,obj1.y)
    val1=obj1.setter()
    print(val1)
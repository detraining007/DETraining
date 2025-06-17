class DE(object):
    def __init__(self):
        print("init constructor")
        self.x=5
        self.y=10
    def __new__(cls):
        print("I am new")
        return super().__new__(cls)
    def set(self,x,y):
        self.x=x
        self.y=y
    def getter(self):
        return self.x,self.y
if __name__=="__main__":
        obj = DE()
        obj.set(10, 20)
        print(obj.getter())


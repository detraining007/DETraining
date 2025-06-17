class Test(object):
    def __init__(self):
        print("init constructor")
    def set(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return self.x,self.y
if __name__=="__main__":
        obj = Test()
        obj.set(20, 30)
        print(obj.get())
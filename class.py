class DE(object):
    def __init__(self):
        self.x=5
        self.y=10
    def set(self,x,y):
        self.x=x
        self.y=y
    def getter(self):
        return self.x,self.y
if __name__=="__main__":
        obj = DE()
        obj.set(10, 20)
        print(obj.getter())               
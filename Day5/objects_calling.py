class DE(object):
    def __init__(self):
        print("init constructor")
        self.x=10
        self.y=9
    def __new__(cls):
        print("new constructor")
        # return "Ram"
        return super().__new__(cls)

    def set(self,x,y):
        self.x=x
        self.y=y
    def getter(self):
        return self.x +self.y

if __name__ == "__main__":
   obj = DE()
   # print(obj.x)
   obj.set(20,30)
   print(obj.getter())




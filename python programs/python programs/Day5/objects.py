class Test(object):
    def __init__(self):
        print("Init constructor called")
        self.x=10
        self.y=8
    def set(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return self.x , self.y

    def __new__(cls):
        print("new constructor called")
        return super().__new__(cls)


obj = Test()
obj.set(256,78)
print(obj.get())
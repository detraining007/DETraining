class py(object):
    def __new__(cls):
        print("i am in new")
        #return "dd"
        return super().__new__(cls)
    def __init__(self):
        print("i am in init")
        self.x=12
        self.y=5
    def set1(self,x1,y1):
        self.x=x1
        self.y=y1
    def get1(self):
        return self.x,self.y
if __name__=="__main__":
    obj=py()
    print(obj.x,obj.y)
    obj.set1(3,4)
    print(obj.get1())
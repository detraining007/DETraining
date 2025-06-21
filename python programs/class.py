class test(object):
    def __new__(self):
        print("iam in new")
        # return super().__new__(self)
        
    def __init__(self):
        self.x = 12
        self.y = 23

    def setter(self, x1, y1):
        self.x = x1
        self.y = y1

    def getter(self):
        return (self.x, self.y)
if __name__ == "__main__":
    obj = test()           
    # print(obj.getter())     
    
    # obj.setter(100, 200)    
    # print(obj.getter())     

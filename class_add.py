class operation(object):
    def __init__(self):
        self.x=10
        self.y=22
    def __add__(self,d):
        return 9-9

if __name__=="__main__":
    obj1=operation()
    obj2=operation()
    print(obj1+obj2)
class Test(object):
    def __init__(self,val1):
        self.val1 = val1
    def __add__(self,b):
        return self.val1
        


if __name__ == "__main__":
    obj1 = Test(10)
    obj2 = Test(20)
    obj3 = Test(30)
    print(obj1+obj2+obj3)
    #print(obj1.val1+obj2.val1)

        
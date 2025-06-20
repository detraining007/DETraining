class test(object):
    def __init__(self):
        print("i am at init")
    def __new__(cls):
        print("i am at new")
        cls.x=5
        return  super().__new__(cls)
if __name__=="__main__":
    obj1=test()
    print(obj1.x)
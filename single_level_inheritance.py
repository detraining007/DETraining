class Test(object):
    def n1(self):
        print("Test n1 constructor")
    def __init__(self):
        print("Test init constructor")
class Test_child(object):
    def n1(self):
        print("Test child n1 constructor")
    def __init__(self):
        print("Test child init constructor")
if __name__=="__main__":
        obj = Test()
        obj1 = Test_child()
        print(obj.n1())
        print(obj1.n1())                
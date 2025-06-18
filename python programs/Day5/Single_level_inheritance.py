class Test(object):

    def m1(self):
        print("Test m1 function")
        return "Ram"
    def __init__(self):
        print("Test init constructor")

class Test_Child(Test):
    # def __new__(cls):
    #     print('msg')
    #     return super(Test_Child,cls).__new__(cls)
    def m1(self):
        print("child m1 function")
        return "R"
    def __init__(self):
        print("child init constructor")

obj = Test()
obj1 = Test_Child()
print(obj.m1())
print(obj1.m1())


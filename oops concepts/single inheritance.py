class pen:
    def func1(self):
        print("this function is in pen class")

class cap(pen):
    def func2(self):
        print("this function is in cap class")

obj = cap()
obj.func1()
obj.func2()

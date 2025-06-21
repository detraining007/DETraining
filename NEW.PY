class test(object):
    def __new__(cls):
        print("i am in new")
        return super().__new__(cls)
    def __init__(self):
        print("i am in init")
        self.x = 10
        self.y = 20
    def setter(self, a, b):
        self.x = a
        self.y = b
    def getter(self):
        return self.x, self.y

if __name__ == "__main__":
    obj = test()
    print(obj.getter())
    obj.setter(100, 200)
    print(obj.getter())
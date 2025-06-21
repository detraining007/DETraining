class test:
    def __init__(self):
        self.x = 10
        self.y = 20

    def setter(self, a, b):
        self.x = a
        self.y = b

    def getter(self):
        return self.x, self.y

    def reset(self):
        self.x = None
        self.y = None

if __name__ == "__main__":
    obj = test()
    print(obj.getter())  
    obj.setter(30, 40)
    print(obj.getter())  
    obj.reset()
    print(obj.getter())  
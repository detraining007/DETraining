class test:
    def __init__(self):
        self.x = 10
        self.y = 20

    def setter(self, a , b):
        self.x = a
        self.y = b

    def getter(self):
        return self. x, self. y
    
if __name__ == "__main__":
    obj = test()
    print(obj.getter())
    obj.setter(30,40)
    print(obj.getter())
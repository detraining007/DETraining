class parent(object):
    def __init__(self):
        self.a=19
        self.b=20
    def add(self):
        return self.a+self.b
class child(parent):
    def __init__(self):
        super().__init__()
        self.b=30
    def add(self):
        return self.a+self.b
obj=parent()
print(obj.add())
obj1=child()
print(obj1.add())
        
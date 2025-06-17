class parent(object):
    def __init__(self):
        self.x=10
        self.y=20
    def add(self):
        return self.x+self.y
class child(parent):
    def __init__(self):
        super().__init__()
        self.y=30
    def add(self):
        return self.x+self.y
ob1=parent()
print(ob1.add())
ob2=child()
print(ob2.add())
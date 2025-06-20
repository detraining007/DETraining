class parent:
    def __init__(self):
        self.x=20
        self.y=30
    def __private(self):
        return self.x+self.y
    def _protected(self):
        print(self.__private())# private and protected members can be aceesible witin class and subclass
        return self.y-self.x
obj=parent()
# obj.__add() will raise attribute exception
print(obj._parent__private())
#print(obj._protected()) ,,
print(obj._protected())
    
#To implement single inheritance 

class Base:
    def __init__(self):
        self.x="Im from base class"
        self.y=2

class child(Base):
    def base1(self):
        self.z=1
        self.w=15

if __name__=="__main__":
    test1=child()
    print(test1.x)  
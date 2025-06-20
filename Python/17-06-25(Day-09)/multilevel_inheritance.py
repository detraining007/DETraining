#To implement multi-level inheritance

#defining base class
class rectangle:
    def __init__(self):
        self.x=13
        self.y=4

class perimeter(rectangle):
    def perimeter1(self):
        self.peri1=self.x+self.y
        return self.peri1
    
class area(perimeter):
    def area1(self):
        self.area2=self.x*self.y
        return self.area2
    
if __name__=="__main__":
    test1=area()
    print("Area of the rectangle is: ",test1.area1())
    print("Perimeter of the rectangle is: ",test1.perimeter1())
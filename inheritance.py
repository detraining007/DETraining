class shape:
    def __init__(self,length,breadth=0):
        self.length=length
        self.breadth=breadth
        print('Any area or any shape')

class rectangle(shape):
    def area_rectangle(self):
        return self.length * self.breadth
    
class square(shape):
    def area_square(self):
        return self.length * self.length

class triangle(shape):
    def area_triangle(self):
        return 0.5*(self.length * self.breadth)

obj_1=rectangle(7,8)
obj_2=square(4)
obj_3=triangle(7,8)
print(obj_1.area_rectangle())
print(obj_2.area_square())
print(obj_3.area_triangle())
        

class addition:
    def sum(self,x,y):
        return x+y
    
class subtraction(addition):
    def sub(self,x,y):
        return x-y

class multiplication(subtraction):
    def mult(slef,x,y):
        return x*y

obj=multiplication()
print(obj.mult(10,20))
print(obj.sum(10,20))
print(obj.sub(30,40))
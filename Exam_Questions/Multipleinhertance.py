#Multiple Inhertiance
class addition:
    def sum(self,x,y):
        return x+y
    
class subtraction(addition):
    def sub(self,x,y):
        return x-y

class multiplication(addition):
    def mult(self,x,y):
        return x*y
class Name_01(subtraction,multiplication):
    def rem(self,x,y):
        return x % y

obj=Name_01()
print(obj.mult(10,20))
print(obj.sum(10,20))
print(obj.sub(30,40))
print(obj.rem(30,40))






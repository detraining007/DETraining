class data(object):
    def __init__(self,a):
        self.a=a
    def __add__(self, self1):
          return self.a+self1.a
obj1=data(2)
obj2=data(3)
obj3=data(4)
print(obj1+obj2)
x=obj1+obj2
print(x+obj3 .value())



        
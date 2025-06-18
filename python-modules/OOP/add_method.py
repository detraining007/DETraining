class Mem1(object):
    def __init__(self,num1):
        self.num1 = num1
    def __add__(self,x):
        return 5

class Mem2(object):
    def __init__(self):
        var1 = 2
objm1 = Mem1(6)
objm2 = Mem1(2)
print(objm1+objm2)

'''
if we try to add two objects, __add__(only with two args) method is called if we have defined it
else trows an error (unsupported operand type for + className and className)
'''



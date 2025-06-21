class name:
    def __init__(self, val):
        self.val = val

    def __add__(self,val2,val3):
        #self.val2 = val2
        return val2.val+self.val+val3.val

obj1 = name(30)
obj2 = name(20)
obj3=  name(40)
obj4 = obj1 + obj2  +obj3
print(obj4)


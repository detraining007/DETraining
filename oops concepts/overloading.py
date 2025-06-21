class my_class(object):

    def add(self, a, b):
        return float(a + b)
    def add (self , a, b, c):
        return int(a+b+c)
obj = my_class()
print(obj.add(1,2,3))
# print(obj.add (1,2))
#print(obj.add (1))

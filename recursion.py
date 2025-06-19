class recursion(object):
    def factorial(self,x):
        if (x==0):
            return 1
        else:
            return x*self.factorial(x-1)
obj1=recursion()
result=obj1.factorial(6)
print(result)
    

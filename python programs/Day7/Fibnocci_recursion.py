class Fibnocci_Recursion(object):
    def fib(self,number):
        a=0
        b=1
        if number <= 1:
           return number
        else:
            return self.fib(number-1) + self.fib(number-2)
obj = Fibnocci_Recursion()
print(obj.fib(8))
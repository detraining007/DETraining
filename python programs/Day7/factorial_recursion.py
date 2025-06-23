class Factorial_Recursion(object):
    def fact(self,number):
        if number ==0:
            return 1
        else:
            return number * self.fact(number-1)
obj = Factorial_Recursion()
number = int(input("enter number"))
print(obj.fact(number))
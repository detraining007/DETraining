si=float(input("enter the simple intrest amount: "))
r=float(input("enter the rate of intrest: "))
t=float(input("enter the time period: "))
if t > 10:
    raise Exception("Time cannot be greater than 10")
try:
    p=si*100/(t*r)
    print(p)
except ZeroDivisionError:
    print("error:can't divided by zero")





#This program is to find principle amount using try and except blocks and ducking it
#DUCKING Program

simple_interest=int(input("Enter simple interest: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the total time: "))

try:
    p=(simple_interest*100)/(r*t)
    print("Principle amount is equal to: ",p)

except ZeroDivisionError:
    print("Its a zero division exception. Rate(r) and time(t) cannot be zero")

#This program is to find simple interest using try and catch blocks

simple_interest=int(input("Enter simple interest: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the total time: "))

try:
    p=(simple_interest*100)/(r*t)
    print("Principle amount is equal to: ",p)

except:
    print("Its a zero division exception")
    if r==0:
        r=simple_interest
    else:
        t=simple_interest
    p=(simple_interest*100)/(r*t)
    print("Principle amount is equal to: ",p)

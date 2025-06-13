#swapping two numbers without using temp variable

n1=int(input("Enter the number n1: "))
n2=int(input("Enter the number n2: "))
print("berfore Swapping \nn1=",n1,"n2=",n2)

n1=n1+n2
n2=n1-n2
n1=n1-n2

print("After swapping \nn1=", n1, "n2=", n2)

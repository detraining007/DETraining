#Prime Numbers
num = int(input("Enter the number : " ))
c=0
for i in range(2,num):
    if num%i==0:
        c=c+1
if c>0:
    print(num, " is not a Prime number")
else:
    print(num, "is a prime number")

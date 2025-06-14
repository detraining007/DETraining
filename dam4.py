gitx=2
while x<20:
    x*=3
print(x)

n=10
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end= "")
    for cols in range(1,2 * rows):
        print("*",end="" )
    print()

    n=10
for i in range(1,n+1):
    for spaces in range(1,n-i+1):
        print("",end=" ")
    for j in range(1,i):
        print("*",end="")
    print()

    num= int(input("enter  a number :"))
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        break
else:
    print("is a prime number")

    num= [2,3,44,55,66,77]
for i in range(0,num):
    if num%i==0:
        print("not a prime number")
        break
else:
    print("is a prime number")
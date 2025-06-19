#fibanocci
a=0
b=1
n=int(input("Enter the number:"))
for i in range(0,n):
    c=a+b
    print(c)
    a,b=b,c

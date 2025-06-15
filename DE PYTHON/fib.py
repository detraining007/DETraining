n=int(input("enter the number: "))
c=0
d=1
if n==2:
    print(c,d,end="\n")
elif n==1:
    print(c)
elif n>2:
    for i in range(n):
        print(c)
        temp=c
        c=d
        d=c+temp
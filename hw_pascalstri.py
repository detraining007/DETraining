'''Pascals Triangle'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def comb(n,r):
    n=n-1
    r=r-1
    numerator=fact(n)
    x1=fact(n-r)
    x2=fact(r)
    denominator=x1*x2
    return numerator//denominator

n=int(input("enter a number :"))
for i in range(0,n):
    for k in range(n-i,0,-1):
        print(" ",end="")
    c=1
    for j in range(1,2*(i)+2):
        if j%2==0:
            print(" ",end="")
        else:
            print(comb(i+1,c),end="")
            c+=1
            
    print("\n")

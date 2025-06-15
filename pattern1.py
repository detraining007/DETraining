n=int(input("enter a number"))
for i in range(0,n-1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(1,2*(i)+2):
        print("*", end=" ")
    print("\n")
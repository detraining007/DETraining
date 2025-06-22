Num=int(input("Enter the value : "))
for i in range(Num-1,-1,-1):
    print(" "*(Num-i),end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,Num):
    print(" "*(Num-i),end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
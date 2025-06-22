Num=int(input("Enter the Range of Number: "))
for i in range(2,Num):
    k=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            k+=1
    if k==0:
        print(i,end=" ")


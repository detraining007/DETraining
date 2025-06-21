
import math
n=int(input("enter a number"))
c=3
s=2*(n//2)+1-2
for i in range(0,n):
    if i<=n//2:
        for j in range(math.ceil(n//2),i-1,-1):
            print(" ",end=" ")
    
        for k in range(1,2*(i)+2):
            print("*",end=" ")
    else:
        for j in range(1,c):
            print(" ",end=" ")
        c+=1
        for k in range(0,s):
            print("*",end=" ")
        s-=2

import math
n=int(input("enter a number"))
c=3
s=2*(n//2)+1-2
for i in range(0,n):
    if i<=n//2:
        for j in range(math.ceil(n//2),i-1,-1):
            print(" ",end=" ")
    
        for k in range(1,2*(i)+2):
            print("*",end=" ")
    else:
        for j in range(1,c):
            print(" ",end=" ")
        c+=1
        for k in range(0,s):
            print("*",end=" ")
        s-=2
95904fb3354e403a37a876779019fbdd2e0d26f6
print("\n")
<<<<<<< HEAD
n=int(input("enter a number"))
try:
    if n>26:
        raise ValueError("value of n cannot be greater than 26")
except ValueError as e:
    print(f"ERRROR: {e}")
if n<=25:
    m=n
    s=1
    for i in range(1,n+1):
        x1=65
        x2=65+n-i
        for j in range(1,2*(n)):
            if j<=m:
                print(f"{chr(x1)}",end="")
                x1+=1
        if i==1:
            for p in range(x2-1,64,-1):
                print(f"{chr(p)}",end="")
        if i>=2:
            for i in range(0,s):
                print(" ",end="")
            s+=2
            for k in range(x2,64,-1):
                print(f"{chr(k)}",end="")
        m-=1
=======
n=int(input("enter a number"))
try:
    if n>26:
        raise ValueError("value of n cannot be greater than 26")
except ValueError as e:
    print(f"ERRROR: {e}")
if n<=25:
    m=n
    s=1
    for i in range(1,n+1):
        x1=65
        x2=65+n-i
        for j in range(1,2*(n)):
            if j<=m:
                print(f"{chr(x1)}",end="")
                x1+=1
        if i==1:
            for p in range(x2-1,64,-1):
                print(f"{chr(p)}",end="")
        if i>=2:
            for i in range(0,s):
                print(" ",end="")
            s+=2
            for k in range(x2,64,-1):
                print(f"{chr(k)}",end="")
        m-=1
>>>>>>> 95904fb3354e403a37a876779019fbdd2e0d26f6
        print("\n")
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end="")
    for colm in range(1,2*rows):
        print("*",end="")
    print()
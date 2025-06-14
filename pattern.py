num = int(input ("enter the number of rows:"))
for i in range(0,-1):
    for j in range(0, num-1):
        print(end = " ")
        for j in range(0,i):
            print("*" , end=" ")
            print()

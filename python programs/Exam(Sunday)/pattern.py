def pattern(number):
    for row in range(number,0,-1):
        space = " "*(number-row)
        print(space ,end="")
        for column in range (row):
            print("*" , end=" ")
        print()
    for row in range(1,number):
        space =" "*(number-(row+1))
        print(space,end="")
        for column in range(row+1):
            print("*",end=" ")
        print()
number = int(input("Enter number"))
pattern(number)
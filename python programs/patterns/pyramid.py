number = int(input("Enter a number"))

for vertical in range (1,number+1):
    for space in range(number-vertical):
        print(" ", end=" ")
    for lefthorizontal in range(vertical):
        print("*",end=" ")
    for righthorizontal in range(vertical-1):
         print("*", end=" ")
    print()

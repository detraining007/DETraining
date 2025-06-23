number = int(input("Enter a number to build Rhombus pyramid"))

for vertical in range(1,number+1):
    #creating left spaces to get pyramid structure
    for spaces in range(number-vertical):
        print(" ",end=" ")
    #print left side pyrmid first
    for lefthorizontal in range(vertical):
        print("*",end=" ")
    #printing right side pyramid
    for righthorizontal in range(vertical-1):
        print("*",end=" ")
    print()

#printing bottom side pyramid
for bottom in range(number-1,0,-1):
    #creating spaces
    for spaces in range(number-bottom):
        print(" ",end=" ")
    #bottom left pyramid
    for lefthorizontal in range(bottom):
        print("*",end=" ")
    #bottom right pyramid
    for righthorinzontal in range(bottom-1):
        print("*",end=" ")
    print()
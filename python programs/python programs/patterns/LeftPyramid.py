def left_pyramid(number):
    for i in range(number):
        print(" "*(number-(i+1)),end="")
        for j in range(i+1):
            print(i,end="")
        print()

number = int(input("Enter a number"))
left_pyramid(number)
number = int(input("Enter a number"))

for vertical in range(1,number+1):
    # for left in range(vertical):
        print("* "* vertical, end="")
    # for space in range(number):
        space = (number - vertical)*2
        print(" "* space,end="")
    # for right in range(vertical):
        print("* "*vertical)
        print()

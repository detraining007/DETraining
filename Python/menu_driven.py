from menu_driven_lib import Addition,Subtraction,Multiplication,Division

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

do_you_continue = "Y"

while do_you_continue == "Y":
    operation = int(input("\nFor Addition Enter :1\n" \
                    "For Subtraction Enter :2\n" \
                    "For Multiplication Enter :3\n" \
                    "For division Enter :4\n "))
    if operation == 1:
        print(Addition(num1,num2))
    elif operation == 2:
        print(Subtraction(num1,num2))
    elif operation ==3:
        print(Multiplication(num1,num2))
    elif operation == 4:
        print(Division(num1,num2))
    else:
        print("Please Enter a valid number")
        do_you_continue = input("Please Enter Y to continue\n" \
        "Please Enter N to stop\n").upper()
    
    if do_you_continue == "N":
        print("You entered N\nThe program has terminated")

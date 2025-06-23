from libraryfunctions import add, subtraction,multiply,division

if __name__ == "__main__":

    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))

    opinion = "yes"v


    while opinion == "yes":

        choice = int(input("Enter your choice from 1(Add), 2(Subtraction), 3(Multiply), 4(Division)"))

        if choice < 5 and choice > 0:
            if choice == 1:
                add(num1, num2)
                break
            elif choice == 2:
                subtraction(num1, num2)
                break
            elif choice == 3:
                multiply(num1, num2)
                break
            elif choice == 4:
                division(num1, num2)
                break
        else:
            print("You must choose your choice between given numbers 1,2,3,4")
        opinion = input("Do you want continue ? Type yes/no").lower()

        if opinion=="no":
            print("You have selected to no option , then we are ending program here")



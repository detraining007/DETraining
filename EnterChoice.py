from functions import MenuDriven
if __name__ == "__main__":
      
    while True:
        try:
            n1 = int(input("Enter a number n1: "))
            n2 = int(input("Enter a number n2: "))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    while True:
        try:
            choice = int(input("Enter choice (1 -addition /2 -subtraction /3 -Multiplication /4 -division): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Invalid choice")

            preference = input("Do you want to continue? Enter yes/no: ")
            if preference != "yes":  
                print("You have entered no Soo EXITING")
                exit()
            
    if choice == 1:
        print(MenuDriven.add(n1, n2))
    elif choice == 2:
        print(MenuDriven.sub(n1, n2))
    elif choice == 3:
        print(MenuDriven.mul(n1, n2))
    elif choice == 4:
        try:
            print(MenuDriven.div(n1, n2))
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
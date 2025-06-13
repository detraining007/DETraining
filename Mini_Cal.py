def add_(n1,n2):
    return n1+n2
def sub_(n1,n2):
    return n1-n2
def product_(n1,n2):
    return n1*n2
def div_(n1,n2):
    return n1//n2
if __name__ == "__main__":
    while True:
        n1 = int(input("enter first number:"))
        n2 = int(input("enter second number:"))
        ch = int(input("enter your choice from 1 to 4:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nYour choice:"))
        if ch == 1:
            result = add_(n1,n2)
            print("sum of these n1,n2 is:", result)
        elif ch == 2:
            result = sub_(n1,n2)
            print("sub of these n1,n2 is:", result)
        elif ch == 3:
            result = product_(n1,n2)
            print("product of these n1,n2 is:", result)
        elif ch == 4:
            if n2 != 0:
                result = div_(n1,n2)
                print("div of these n1,n2 is:", result)
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("your choice is not belongs to the above four")
        
        cont = input("Do you want to try again? (yes/no): ")
        if cont.lower() != "yes":
            print("Exiting the program.")
            break
 
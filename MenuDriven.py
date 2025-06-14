def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

if __name__ == "__main__":
      
    n1 = int(input("Enter a number n1: "))
    n2 = int(input("Enter a number n2: "))
        
    while True:
        choice = int(input("Enter choice (1/2/3/4): "))
            
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Invalid choice")
            preference = input("Do you want to continue? Enter yes/no: ")
            if preference!= "yes":  
                print("EXIT")
                break
                
    if choice == 1:
        print(add(n1, n2))
    elif choice == 2:
        print(sub(n1, n2))
    elif choice == 3:
        print(mul(n1, n2))
    elif choice == 4:
        print(div(n1, n2))


def add(n1,n2):
    return n1+ n2

def sub(n1, n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div (n1, n2):
    return n1/n2

if __name__ == "__main__": 

    choice = int(input("enter choice(1/2/3/4)"))
    n1 = int(input("enter a number n1: "))
    n2 = int(input("enter a number n2: "))

    if choice == 1:
        print(add(n1,n2))
    if choice == 2:
        print(sub(n1,n2))
    elif choice == 3:
        print(mul(n1,n2))
    elif choice == 4:
        print(div(n1,n2))
    else:
        print("invalid choice")

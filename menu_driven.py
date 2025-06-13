#defining functions with operations
def add(n1, n2):
    print(n1+n2)
def sub(n1, n2):
    print(n1-n2)
def mul(n1, n2):
    print(n1*n2)
def div(n1, n2):
    print(n1/n2)
def mod(n1, n2):
    print(n1%n2)

decision = "yes"
while(decision == "yes"):
    #taking inputs inside the loop
    n1=int(input("enter n1: "))
    n2=int(input("enter n2: "))
    choice=int(input("enter your choice from 1 to 5: "))
    
    if choice == 1:
        add(n1, n2)
    elif choice == 2:
        sub(n1, n2)
    elif choice == 3:
        mul(n1, n2)
    elif choice == 4:
        div(n1, n2)
    elif choice == 5:
        mod(n1, n2)
    else:
        print("enter choice from 1 to 5")
    
    decision = input("Do u want to continue? yes or no: ")
print("Thank you for using the caluculator!")    #if decision == no
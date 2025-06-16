def calculator(n1,n2,operator):
    if(operator == '+'):
        add(n1,n2)
        return
    elif(operator == '-'):
        subtract(n1,n2)
        return
    elif(operator == '*'):
        multiply(n1,n2)
        return
    elif(operator == '/'):
        divide(n1,n2)
        return
    else:
        print("Only +, -, *, / operators are accepted")

def add(n1,n2):
    print(n1,'+',n2,"=",n1+n2)
    return
def subtract(n1,n2):
    print(n1,'-',n2,"=",n1-n2)
    return
def multiply(n1,n2):
    print(n1,'*',n2,"=",n1*n2)
    return
def divide(n1,n2):
    if(n2 == 0):
        print("n2 cannot be 0")
        return
    print(n1,'/',n2,"=",n1/n2)
    return

if(__name__ == '__main__'):
    choice = "y"
    while(choice == "y"):
        n1 = int(input("Enter n1 : "))
        n2 = int(input("Enter n2 : "))
        operator = input("Enter operator : ")
        calculator(n1,n2,operator)
        choice = input("Enter y to go once again or any other key to end : ")
    
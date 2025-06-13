def Add(num1,num2):
    return num1 + num2

def Sub(num1,num2):
    return num1 - num2

def Div(num1,num2):
    return num1 / num2

def Mul(num1,num2):
    return num1 * num2

if __name__ == "__main__":
    num1 = int(input("enter first numnber "))
    num2 = int(input("enter first numnber "))
    print("enter your choice\n 0 is for add \n 1 is for Sub \n 2 is for Div \n 3 is for Mul")
    choice = int(input("Enter your choice "))


while():
    if(choice == 0):
        print(Add(num1,num2))
    elif(choice ==1):
       print(Sub(num1,num2))
    elif(choice ==1):
        print(Div(num1,num2))
    elif(choice ==1):
        print(Mul(num1,num2))
    else:
        print("please enter the valid choice")

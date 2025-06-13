#Creating a calculator called menu driven using functions 
def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

if __name__=="__main__":
    num1=int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))
    choice=int(input("Enter your choice: "))

    if choice==1:
        add=addition(num1,num2)
        print("The Addition of",num1,"and",num2,"is: ",add)
    elif choice==2:
        sub=subtraction(num1,num2)
        print("The subtraction of",num1,"and",num2,"is: ",sub)
    elif choice==3:
        mul=multiplication(num1,num2)
        print("The multiplication of",num1,"and",num2,"is: ",mul)
    elif choice==4:
        div=division(num1,num2)
        print("The divisin of",num1,"and",num2,"is: ",div)
    else:
        print("Enter a proper choice from '1' to '4'")



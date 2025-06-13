from Calculator_methods import Add,Sub,Mul,Div

if __name__ == "__main__":
     a='y'
while(a == 'y'):
    num1 = int(input("enter first numnber "))
    num2 = int(input("enter first numnber "))
    print("enter your choice\n 0 is for add \n 1 is for Sub \n 2 is for Div \n 3 is for Mul")
    choice = int(input("Enter your choice "))


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
    val = input("do you want to continue Y/N")
    if(val == "y"):
        continue
    else:
        print("Terminated")
        break
    



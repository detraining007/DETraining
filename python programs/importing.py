import menu
decision="yes"    
while(decision=="yes"):
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second number: "))
    choice=int(input("enter your choice 1,2,3,4"))
    if choice==1:
       print(add(num1,num2))
    elif choice==2:
       print(sub(num1,num2))
    elif choice==3:
       print(mul(num1,num2))
    elif choice==4:
       print(div(num1,num2))
    else:
        print("enter correct choice? ")
    decision=input("do you want to continue yes or no!")    
print("thank you for using the calculator")        
        
        

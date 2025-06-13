from calculator import *
choice="Yes"
while choice=="Yes":
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    c=int(input("enter the operation you want to perform"))
    if c==1:
        print(f"the sum is:{add(n1,n2)}")
    elif c==2:
        print(f"the substraction result : {sub(n1,n2)}")
    elif c==3:
        print(f"the multiplication  result:{mul(n1,n2)}")
    elif c==4:
        print(f"the division result:{div(n1,n2)}")
    else:
        print(f"invalid chocie")
    choice=input(f"do you want to continue? Yes or No")
if choice=="No":
    print("***the program is terminated***")
    

    

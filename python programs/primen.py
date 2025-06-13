def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1%num2
if __name__=="__main__":

    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    choice=int(input("enter your choice 1,2,3,4"))
    if choice==1:
       print( add(num1,num2))
    elif choice==2:
       print(sub(num1,num2))
    elif choice==3:
       print( mul(num1,num2))
    elif choice==4:
       print(div(num1,num2))
    else:
        print("enter correct choice")



    

    

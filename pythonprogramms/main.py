# from function import add,sub
from function import *

if __name__=="__main__":
        n1=int(input("Enter n1:"))
        n2=int(input("Enter n2:"))
        print("1.Addition \n 2.Multiplication \n 3.Subtraction \n 4.Division ")
        c=int(input("Enter your choice:"))
        while True:
            if c==1:
                print(add(n1,n2))
                break
            elif c==2:
                print(mul(n1,n2))
                break
            elif c==3:
                print(sub(n1,n2))
                break
            elif c==4:
                print(div(n1,n2))
                break
            else:
                print("Invalid choice")
                c=int(input("Enter correct choice"))
                ch=input("do you want to continue ? Enter Yes or No:")
            if ch!="yes":
                continue
            else:
                 print("You entered No so,the program is terminated")
                 


from methods import *

if __name__ == "__main__":
    userchoice = "Yes"
    while(userchoice == "Yes"):
      number1 = int(input("Enter Number 1 : "))
      number2 = int(input("Enter Number 2 : "))
      print("The choice has to be in between 1 to 4 which means addition,subtraction,multiplication,divison")
      choice = int(input("Enter your choice: "))
      if(choice== 1 or 2 or 3 or 4):
           if(choice==1):
             print(f'The sum of {number1} and {number2} is {add(number1,number2)}')
           elif(choice==2):
             print(f'The difference of {number1} and {number2} is {sub(number1,number2)}')
           elif(choice==3):
             print(f'The product of {number1} and {number2} is {mul(number1,number2)}')
           elif(choice==4):
             print(f'The divison of {number1} and {number2} is {div(number1,number2)}')
           else:
             print("You have entered wrong number")
           while True:
             userchoice = input("Do you want to continue or not(Yes/No?)")
             if(userchoice == "No"):
                break
             elif(userchoice == "Yes"):
                break
             else:
               print("The userchoice must be either Yes or No!")
    
        

# sum = 0
# subt = 0
# product = 0
# divison = 0

from methods  import *




if __name__ == "__main__":
    number1 = int(input("Please enter number 1: "))
    number2 = int(input("Please enter number 2: "))
    choice = int(input("Please enter your choice : "))
    if choice == 1:
        # add(number1,number2)
        print(f'sum of numbers {number1} and {number2} is {add(number1,number2)}')    
    elif choice == 2:
           #sub(number1,number2)
           print(f'subtraction of numbers {number1} and {number2} is {sub(number1,number2)}')
    elif choice == 3:
           #mul(number1,number2)
           print(f'multiplication of numbers {number1} and {number2} is {mul(number1,number2)}')
    elif choice == 4:
           #div(number1,number2)
           print(f'divison of numbers {number1} and {number2} is {div(number1,number2)}')
    else:
           print("You have entered the wrong choice")

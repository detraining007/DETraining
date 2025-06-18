#import MultiDrivenCalulator
#from MultiDrivenCalulator import add , mul
from MultiDrivenCalulator import *

if __name__ == "__main__":
	while True:
		num1 = int(input("Enter number1: "))
		num2 = int(input("Enter number2: "))
		choice = int(input("Enter choice (1-Add, 2-Sub, 3-Mul, 4-Div): "))

		if choice == 1:
			print(add(num1, num2))
		elif choice == 2:
			print(sub(num1, num2))
		elif choice == 3:
			print(mul(num1, num2))
		elif choice == 4:
			print(div(num1, num2))
		else:
			print("Enter a valid choice.")
		cont = input("Do you want to continue? (yes/no): ")
		if cont != "yes":
			print("Thank you!")
			break

'''
Output:

Enter number1: 4
Enter number2: 5
Enter choice (1-Add, 2-Sub, 3-Mul, 4-Div): 3
20
Do you want to continue? (yes/no): yes
Enter number1: 4
Enter number2: 5
Enter choice (1-Add, 2-Sub, 3-Mul, 4-Div): 1
9
Do you want to continue? (yes/no): yes
Enter number1: 4
Enter number2: 5
Enter choice (1-Add, 2-Sub, 3-Mul, 4-Div): 2
-1
Do you want to continue? (yes/no): yes
Enter number1: 4
Enter number2: 5
Enter choice (1-Add, 2-Sub, 3-Mul, 4-Div): 4
0
Do you want to continue? (yes/no): no
Thank you!

'''
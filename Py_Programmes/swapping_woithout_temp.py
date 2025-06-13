#Without Using temp variable
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swap: num1 = {num1} num2 = {num2}")

num1 = num1+num2
num2=num1-num2
num1=num1-num2

print(f"After swap: num1= {num1} num2 = {num2}")




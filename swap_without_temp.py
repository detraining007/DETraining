a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))


print(f"Before swapping num1:{a} num2:{b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping a:{a}  b:{b}")

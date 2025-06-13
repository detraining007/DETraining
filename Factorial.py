number = int(input("Enter a number"))
factorial = 1
for i in range(number):
    factorial = factorial * number
    number = number-1
print(f'factorial of a  number  = {factorial}')
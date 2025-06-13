number = int(input("How many terms? "))

number1, number2 = 0, 1

count = 0

if number <= 0:
    print("Please enter a positive number.")
elif number == 1:
    print("Fibonacci sequence up to 1 term:")
else:
    print("Fibonacci sequence:")
    while count < number:
        print(number1, end=' ')
        number1, number2 = number2, number1 + number2
        count += 1


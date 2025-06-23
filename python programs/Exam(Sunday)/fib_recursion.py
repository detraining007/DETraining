def fib_rec(number):
    if number == 0:
        return 1
    else:
        return number * fib_rec(number-1)
number = int(input("Enter number"))
result = fib_rec(number)
print(result)
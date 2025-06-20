# factorial

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
factorial = 6
print(fact(factorial))



# fibonacci

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fib = 8
print(fibonacci(fib))
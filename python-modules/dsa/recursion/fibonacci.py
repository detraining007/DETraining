
def fib(n):
    # ls = [None for _ in range(n)]

    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
# print(fib(6))


    
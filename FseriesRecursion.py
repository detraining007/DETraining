def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    num = int(input("Enter a number of terms: "))
    print("Fibonacci Series:")
    for i in range(num):
        print(fibonacci(i), end=" ")

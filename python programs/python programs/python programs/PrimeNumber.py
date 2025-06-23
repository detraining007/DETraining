def prime(number):
    count = 0  # Initialize count to 0
    for num in range(1, number + 1):
        if number % num == 0:
            count += 1  # Count divisors
    return count == 2  # Prime numbers have exactly 2 divisors

number = int(input("Enter a number: "))

if prime(number):
    print("It is a prime number")
else:
    print("Not a prime number")
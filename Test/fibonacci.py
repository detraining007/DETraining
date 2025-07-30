def fibonacci_series(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fibonacci_series(number-1) + fibonacci_series(number-2)
    







if __name__ == "__main__":
    number = int(input("Enter the element u want"))
    print(fibonacci_series(number))
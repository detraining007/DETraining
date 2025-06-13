def PrimeNumber(number):
    count = 1
    if number == 1:
        return True
    for value in range(1,number):
        if number%value == 0:
            count += 1
    if count==2:
         return True
    
    return False

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    prime = PrimeNumber(num)
    if prime == True:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
    
    
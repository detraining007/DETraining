# prime using function

def PrimeNumber(number):
    count = 1
    for i in range(1 , number):
        if number % i == 0:
            count = count + 1
    if count > 2:
        return False
    return True 

if __name__ == "__main__":
    number = int(input("enter a number :"))
    prime = PrimeNumber(number)
    if prime:
        print(number , " is a prime")
    else:
        print(number , "not a prime")

'''
Output:

enter a number : 9
9 not a prime

'''
def primeNumberCheck(n):
    if(n < 1):
        print(n,"is not a prime number")
        return
    for i in range(2,int(n/2)):
        if(n % i == 0 and n != i):
            print(n,"is not a prime number")
            return
    print(n,"is a prime number")

primeNumberCheck(454)

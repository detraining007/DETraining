def PrimeNumber(n):
    count=0
    if n < 1:
        return False
    if n == 1:
        return True
    for i in range(2, int(n-1)):
        if n % i == 0:
            count = count+1
            
    if count == 2:
        return True
    return False     
    

if __name__ == "__main__":
    number = int(input("Enter any number"))
    if (PrimeNumber(number)):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    






    
    




#Finding prime numbers using function with return as boolean value
#Function definition
def PrimeNumber(num):
    count=0
    for i in range(2,num):
        if num%i==0:
            count=count+1
    if count>0:
        return True
    else:
        return False
    
#Function invocation
if __name__=="__main__":

    number=int(input("Enter a number: "))
    prime_number=PrimeNumber(number)
    if prime_number:
        print(number,"is not a Prime Number")
    else:
        print(number,"is a prime number")



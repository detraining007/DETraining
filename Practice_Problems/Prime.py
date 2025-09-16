def isPrime(number):
    prime = []
    non_prime = []
    for val in range(2,number+1):
        count = 0
        for val2 in range(1,val+1):
            if val%val2==0:
              count += 1
        if(count==2):
            prime.append(val)
        else:
            non_prime.append(val)
    
    print("Prime Numbers in the range: ",prime)
    print("Non Prime numbers in the range: ",non_prime)
    




number = int(input('Enter a range to know its prime or not: '))
isPrime(number)

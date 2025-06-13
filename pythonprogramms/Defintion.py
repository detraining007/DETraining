def PrimeNumber(number):
    n=0
    for i in range(1,number):
        if number%i==0:
            n+=1
           
    if n==1:
        return 'True'
    else:
        return 'False'
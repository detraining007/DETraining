def prime(number):
    if number<=1:
        return False
    flag=True
    for num in range(2, number):
        if number%num==0:
            flag=False
            break
        return flag
number=int(input("enter a number"))
result=prime(number)
if(result):
    print("it is a prime number")
else:
    print("it is not prime number")
    

    

            
    
            

    
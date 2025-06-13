n=5
N=int(input("enter the number:"))
count=0
for i in range (1,N+1):
 if num % i == 0:
     count+=1
     if count == 2:
         print("it is a prime number")
else:
            print("it is not a prime number")

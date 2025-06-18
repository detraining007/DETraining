num = input("Enter a number :")
num = int(num)

count =1

for i in range(1,num):
    if(num%i==0):
        count=count+1

if(count > 2):
    print("Not a prime number")
else:
    print("Prime number")

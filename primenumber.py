num = int(input("Enter the number:"))
count = 1
for i in range(1,num):
    if(num%i==0):
       count = count+1
if(count>2):
    print("not a prime number")
else:
    print("prime number")
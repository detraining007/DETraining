num = int(input("Enter a number: "))
count = 1

if num == 1:
    count = 0
if num > 1 :
    for i in range(1,num//2):
        if num % 2 == 0:
            count += 1
    

if count == 2 or count == 1:
    print(num,"it is a prime number")
else:
    print(num, "it is not a prime number")
Num=int(input("Enter the Val: "))
sum=0
x=Num
while Num>0:
    rem=Num%10
    sum=sum+rem**3
    Num=Num//10
print(sum)
if sum==x:
    print("Amstong")
else:
    print("Not a Amstrong")


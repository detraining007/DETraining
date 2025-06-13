#Factorial program
num=int(input("Enter the number: "))
fac=1
#for i in range(1,num+1):
for i in range(num,0,-1):
    fac=fac*i
print("Factorial of the",num,"=",fac)

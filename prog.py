
ord=int(input("enter the number"))
dig=int(input("enter the number"))
dig2=int(input("enter the number"))

listo=[(n1,n2,n3) for n1 in range(ord)  for n2 in range(dig)  for n3 in range(dig2) ]
print(listo)

'''
digits=eval(input("enter the list of numbers : "))
odd=lambda num : num%2==0
even=lambda num : num%2==1
print("Odd numbers are:")
for num in digits:
    if odd(num):
        print(num, end=" ")
print()
print("Even numbers are:")
for num in digits:
    if even(num):
        print(num, end=" ")
print()
'''






digits=eval(input("enter the list of numbers : "))
odd=lambda num : num%2==0
even=lambda num : num%2==1
evenli=[]
oddli=[]
print("Odd numbers are:")
for num in digits:
    if odd(num):
        oddli.append(num)   
print(oddli)
print("Even numbers are:")
for num in digits:
    if even(num):
        evenli.append(num) 
print(evenli)

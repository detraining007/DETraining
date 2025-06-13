#Apply lambda to list to do even number and odd number segregation
print("Even numbers using lambda")
even_list=list(filter(lambda i:i%2==0,[1,2,3,4,5,6,7,8,9,10]))
print(even_list)

print("Odd numbers using lambda")
odd_list=list(filter(lambda i:i%2!=0,[1,2,3,4,5,6,7,8,9,10]))
print(odd_list)
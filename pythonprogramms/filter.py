#filter
numbers=[1,2,3,4,5,6,7,8,9,10]
odd=list(filter(lambda x:x%2!=0,numbers))
print(odd)

print("Even numbers using lambda")
even_list=list(filter(lambda i:i%2==0,[1,2,3,4,88,9,10,6]))
print(even_list)


print("Odd Numbers using lambda")
odd_list=list(filter(lambda i:i%2!=0,[1,2,3,4,88,9,10,6]))
print(odd_list)

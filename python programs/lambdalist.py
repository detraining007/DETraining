n=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,n))
odd_numbers=list(filter(lambda x:x%2!=0,n))
print("even numbers",even_numbers)
print("odd numbers",odd_numbers)

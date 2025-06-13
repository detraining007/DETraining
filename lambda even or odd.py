
num =[1,2,3,4,5,6,7,8,9]
print("original list of number:")
print(num)
print("even numbers form the list :")
even_num = list (filter(lambda x:x%2==0,num))
print(even_num)
print("odd numbers form the list :")
odd_num =list(filter (lambda x:x%2!=0,num))
print(odd_num)

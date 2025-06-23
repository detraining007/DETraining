numbers =[1,2,3,4,5,6,7,8,9]
odd_num = list(filter(lambda x: x%2!=0 , numbers))
even_num = list(filter(lambda x: x%2==0 , numbers))

print(odd_num)
print(even_num)

c="chetan"
print(type(c[0]))
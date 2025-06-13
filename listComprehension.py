# list comprehension
even = [num for num in [2,3,4,5,6,7,8] if num%2==0]
print("Even numbers:", even)
odd = [num for num in [2,3,4,5,6,7,8] if num%2==1]
print("Odd numbers:", odd)
list = [num+10 for num in [2,3,4,5,6,7,8]]
print("After adding 10 to given list:" , list)
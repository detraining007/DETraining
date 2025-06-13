num = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x : x % 2 != 0 , num))
even_numbers = list(filter(lambda x : x % 2 == 0 , num))
print("Odd numbers : " , odd_numbers)
print("Even numbers : " , even_numbers)

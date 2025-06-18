# swapping of two numbers
a = 5
b = 10

temp = a
a = b
b = temp
print(a , b) # 10 , 5

a , b = b, a
print(a , b) # 5 , 10

'''
Output:

10 5
5 10

'''
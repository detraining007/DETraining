'''
# ------------------------------------------------------------ swapping of two numbers
a = 5
b = 10

temp = a
a = b
b = temp
print(a , b)

a , b = b, a
print(a , b)


# ------------------------------------------------------------ sum of all the numbers in a given list
list = [1, 2, 3, 4, 5]
total = 0
for i in list:
    total += i
print(total)


# ------------------------------------------------------------ factorial
num = int(input("enter a number : "))
fact = 1
for i in range(1 , num+1):
        fact = fact * i
print(fact)


# ------------------------------------------------------------ min / max element in a given list
list = [2,4,6,8,10]
min = list[0]
max = list[0]
for i in list:
    if(i < min):
        min = i
    if(i > max):
        max = i
print(min)
print(max)


# ------------------------------------------------------------ fibonnaci series
list = [0,1,1,2,3,5]
sum = list[0]
n1 = 0
n2 = 1
for i in list:
    sum = n1 + n2
    n1 = n2
    n2 = sum
print(sum)


# ------------------------------------------------------------ prime using function

def PrimeNumber(number):
    count = 1
    for i in range(1 , number):
        if number % i == 0:
            count = count + 1
    if count > 2:
        return False
    return True 

if __name__ == "__main__":
    number = int(input("enter a number :"))
    prime = PrimeNumber(number)
    if prime:
        print(number , " is a prime")
    else:
        print(number , "not a prime")


# ------------------------------------------------------------ multi driven cal program

def add(num1 , num2):
    return num1+num2
def sub(num1 , num2):
    return num1-num2
def mul(num1 , num2):
    return num1 * num2
def div(num1 , num2):
	if num2 != 0:
		return num1 // num2
	else:
		return "Cannot divide by zero."

if __name__ == "__main__":
	while True:
		num1 = int(input("Enter number1: "))
		num2 = int(input("Enter number2: "))
		choice = int(input("Enter choice (1-Add, 2-Sub, 3-Mul, 4-Div): "))

		if choice == 1:
			print(add(num1, num2))
		elif choice == 2:
			print(sub(num1, num2))
		elif choice == 3:
			print(mul(num1, num2))
		elif choice == 4:
			print(div(num1, num2))
		else:
			print("Enter a valid choice.")
		cont = input("Do you want to continue? (yes/no): ")
		if cont != "yes":
			print("Thank you for using the calculator.")
			break



# ------------------------------------------------------------ generate pyramid sequence

def PyramidPattern(number_of_rows):
    # Top half including middle row
    for row_number in range(1, number_of_rows + 1): # for range we use +1
        spaces = '  ' * (number_of_rows - row_number) # number of rows - row number : gives spaces before the first star prints in that row
        stars = ' *  ' * row_number # prints stars as per row number
        print(spaces + stars)

    # Bottom half
    for row_number in range(number_of_rows - 1, 0, -1): # to decrease the range in steps of 1
        spaces = '  ' * (number_of_rows - row_number) # number of rows - row number : gives spaces before the first star prints in that row
        stars = ' *  ' * row_number # prints stars as per row number
        print(spaces + stars) 

number_rows = int(input("Enter the number of rows : "))
PyramidPattern(number_rows)



# ------------------------------------------------------------ ptr exception

try:
	P = float(input('enter the principle :'))
	I = float(input('enter the simple interest : '))
	R = float(input('enter the rate of interest : '))
	T = I*100/P*R
	print(T)
except Exception as error:
	print(' P or R cannot be zero')
	if P==0 or R==0:
		raise Exception('Denominator cannot be zero')
finally:
	print('try again')


# ------------------------------------------------------------ list comprehension
even = [num for num in [2,3,4,5,6,7,8] if num%2==0]
print("Even numbers:", even)
odd = [num for num in [2,3,4,5,6,7,8] if num%2==1]
print("Odd numbers:", odd)
list = [num+10 for num in [2,3,4,5,6,7,8]]
print(list)


# ------------------------------------------------------------ pascal triangle
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

if __name__ == "__main__":
    n = int(input('How many lines? : '))
    width = 2  # Column width per number

    for i in range(n):
        # Print leading spaces to center the row
        print(' ' * width * (n - i - 1), end='')

        for j in range(i + 1):
            print(f"{ncr(i, j):^{width}}", end='')
        print()


# ------------------------------------------------------------ Apply lambda to list to do even number , odd number segregation

numbers = [2, 3, 4, 5, 6, 7, 8]

even = [num for num in numbers if (lambda x: x % 2 == 0)(num)]
odd  = [num for num in numbers if (lambda x: x % 2 == 1)(num)]

print("Even numbers:", even)
print("Odd numbers:", odd)


# ------------------------------------------------------------ filter , reduce , map
# FILTER :

num = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x : x % 2 != 0 , num))
even_numbers = list(filter(lambda x : x % 2 == 0 , num))
print("Odd numbers : " , odd_numbers)
print("Even numbers : " , even_numbers)

# REDUCE :
	
from functools import reduce
number = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = reduce(lambda x , y: x + y , number)
print(odd_numbers)

# MAP :

sqr = [1,2,3,4,5]
sqr_lst = list(map(lambda item : item*item , sqr))
print(sqr_lst)



# ------------------------------------------------------------ generators

def generatoritem(n):
	new_list = []
	for i in range(n):
		yield(i)
new_list = list(generatoritem(6))
print(new_list)
print(next(new_list))
print(new_list.__next__())
print(next(new_list))


def gen(n):
	for i in range(1,n):
		N = n*1
	yield N
d = gen(9)
print(next(d))
-------------------------------------------------------------------

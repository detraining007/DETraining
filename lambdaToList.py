# Apply lambda to list to do even number , odd number segregation

numbers = [2, 3, 4, 5, 6, 7, 8]

even = [num for num in numbers if (lambda x: x % 2 == 0)(num)]
odd  = [num for num in numbers if (lambda x: x % 2 == 1)(num)]

print("Even numbers:", even)
print("Odd numbers:", odd)

# list comprehension using multiple loops

list = lambda: [(x + y) for x in range(3) for y in range(3)]
print(list())

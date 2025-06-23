lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, lst))
odd = list(filter(lambda x: x % 2 != 0, lst))

print("Even numbers:", even)
print("Odd numbers:", odd)
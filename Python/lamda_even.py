l = [1, 2, 3, 4, 5, 6, 7]

# even_numbers = list(filter(lambda x: x % 2 == 0, l))
# odd_numbers = list(filter(lambda x: x % 2 != 0, l))



even_numbers = list(lambda x: x % 2 == 0, l)
odd_numbers = list(lambda x: x % 2 != 0, l)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
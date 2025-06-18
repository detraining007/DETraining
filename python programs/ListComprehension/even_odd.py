list1 = [4,5,6,11,78,8,9,3,232,2,43,45,466,13,1]

even_nums = [even for even in list1 if even%2==0]
odd_nums = [odd for odd in list1 if odd%2!=0]
prime_nums = [prime for prime in list1 if prime > 1 and all(prime % i != 0 for i in range(2, int(prime**0.5) + 1))]
even_Square = [even**2 for even in list1 if even%2==0]
odd_Square = [odd**2 for odd in list1 if odd%2!=0]

print(even_nums)
print(odd_nums)
print(prime_nums)
print(even_Square)
print(odd_Square)

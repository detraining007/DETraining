#List comprehension
print("Even numbers")
even_list=[i for i in [1,2,3,4,88,9,10,6] if i%2==0]
print(even_list)

print("Odd Numbers")
odd_list=[i for i in [1,2,3,4,88,9,10,6] if i%2!=0]
print(odd_list)

print("Adding 10")
new_list=[i+10 for i in [1,2,3,4,88,9,10,6]]
print(new_list)


# List comprehension with multiple loops
print("Sum of two lists")
sum_list=[(n1+n2) for n1 in range(1,10) for n2 in range(11,20)]
print(sum_list)

print("Mul of two lists")
mul_list=[(n1*n2) for n1 in range(1,10) for n2 in range(11,20)]
print(mul_list)







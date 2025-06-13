# List Comprehension with multiple loops
print("Sum of two lists")
sum_list=[(n1+n2) for n1 in range(1,10) for n2 in range(11,20)]
print(sum_list)

print("mul of two lists")
mul_list=[(n1*n2) for n1 in range(1,10) for n2 in range(11,20)]
print(mul_list)
#printing even values
even_val = [val for val in range(0,10) if val%2==0]
print(even_val)
#printing odd values
odd_val = [val for val in [29,56,47,23,44,78,91,73,88,81] if val%2!=0] 
print(odd_val)
#printing adding values to range of numbers
add_val = [val+10 for val in range(0,10)]
print(add_val)
#printing pairs of numbers
pairs = [(i+j) for i in [1,2,3] for j in [2,3,4]]
print(pairs)
# even number
NewValue = [i for i in [1,2,3,4,5,6,7] if i % 2 == 0]
print(NewValue)

SecondVal = [i for i in range(1,5) if i % 2 == 0 ]
print(SecondVal)

# Odd number

OddValue = [i for i in [11,2,3,42,4,2,12,134,97,5,7] if i % 2!=0]
print(OddValue)

# Adding additional number to an list
AddingVal = [ i+10 for i in range(0,10)]

print(AddingVal)

# matrix = [numbers[i*2:(i+1)*2] for i in range(2)]
# print(matrix)

# data = [(x,Y) for i in [1,2,3] for j in [1,2,3]]
# print(data)
pairs = [(i+ j) for i in [1, 2, 3] for j in [4, 5, 6]]
print(pairs)  

numbers = [1,2,4,5]

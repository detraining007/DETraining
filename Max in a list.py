lst = [20,47,88,2,1,7]
Minimum = 1
Maximum = 0
for value in range(len(lst)):
    if Minimum >= lst[value]:
        Minimum = lst[value]
    if Maximum <= lst[value]:
        Maximum = lst[value]
print(f'The Maximum number in the list is {Maximum}')
print(f'The Minimum number in the list is {Minimum}')
l = [1,2,3,4,5,6,99]

max = float("-inf")
for i in l:
    if i > max:
        max=i
print(max)

min = float("inf")
for i in l:
    if i < min:
        min=i
print(min)
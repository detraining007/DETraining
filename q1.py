# amstrong
n = [1,6,3,4]
z = int(input())
sum = 0
x = [i**z for i in n]
for i in x:
    sum += i
print(sum)
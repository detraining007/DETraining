# fibonnaci series
list = [0,1,1,2,3,5]
sum = list[0]
n1 = 0
n2 = 1
for i in list:
    sum = n1 + n2
    n1 = n2
    n2 = sum
print(sum)
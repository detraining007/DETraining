first= 0
second = 1
value = 0
series = []
sum=0
while(value<10):
    series.append(first)
    sum = first + second
    first = second
    second = sum
    value += 1
print(f'The first  10 fibonacci series numbers sum is {series}')



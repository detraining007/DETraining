def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(10))

def ncr(n,r):
    return factorial(n)/(factorial(r)*factorial((n-r)))

print(ncr(2,0))
length = 5

for i in range(length):
    print(" " * (length -i), end="")
    for j in range(i+1):
        print(int(ncr(i,j)),end=" ")
    print()
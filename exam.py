
# fibonacci

def fib(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
num = int(input())
print(fib(num))


# matrix

'''n = [[1,2],[3,4]]
b=[[0,0],[0,0]]
for rows in n:
    for columns in n:
        b[i][j]=a[j][i]
print(b)'''

# patterns

n = int(input())
for i in range(n):
    for j in range(n-1):
        print("*")

# number conversion

def factorial(n):
    result = 1
    for val in range(1,n+1):
        result = result * val
    return result

def ncr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

length = 7
for val in range(length):
    print(" "*(length-val),end = "")
    for val2 in range(val+1):
        print(int(ncr(val,val2)),end = " ")
    print()







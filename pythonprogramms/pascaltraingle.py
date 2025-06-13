from math import  factorial
rows=int(input("Enter number of rows:"))

for n in range(rows):
    for space in range(rows-n):
        print(end=" ")
    for r in range(n+1):
        ncr=factorial(n)//(factorial(n-r)*factorial(r))
        print(ncr,end=" ")
    print()
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
def ncr(n,r):
    return factorial(n)// (factorial(r) * factorial(n-r))
if __name__=="__main__":
    n=int(input("no. of line :"))
    width=2
    for i in range(n):
        print(' '*width*(n-i-1), end='')
        for j in range(i+1):
            print(f"{ncr(i,j):^{width}}", end='')
        print()
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
if __name__=="__main__":
    n=int(input("Enter the Value of n: "))
    x=factorial(10)
    print(x)
def fibonacci(n):
    if n==1 or n==0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__=="__main__":
    n=int(input("Enter number:"))
    x=fibonacci(n)
    print(f"fibonacci number is:",x)

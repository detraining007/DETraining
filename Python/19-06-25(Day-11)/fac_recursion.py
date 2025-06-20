#Factorial Recursion

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

if __name__=="__main__":
    n=int(input("Enter the number to which you wanna find out factorial: "))
    fac=factorial(n)
    print("The factorial of ",n,"is: ",fac)
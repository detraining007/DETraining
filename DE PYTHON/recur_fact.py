
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
try:
        n = int(input("Enter the number for factorial: "))
        print(f"Factorial of {n} is {fact(n)}")
except RecursionError:
        print("Recursion limit reached. Try a smaller number.")
except ValueError:
        print("Invalid input. Please enter an integer.")
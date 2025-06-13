# factorial

num = int(input("enter a number : "))
fact = 1
for i in range(1 , num+1):
        fact = fact * i
print(fact)


'''
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = fact(num)
    print(f"Factorial of {num} is {result}")
'''
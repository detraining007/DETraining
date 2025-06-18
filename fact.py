# factorial

num = int(input("enter a number : "))
fact = 1
for i in range(1 , num+1):
        fact = fact * i
print(fact)

'''
Output:

enter a number : 6
720

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
Output:

Enter a number: 9
Factorial of 9 is 362880

'''


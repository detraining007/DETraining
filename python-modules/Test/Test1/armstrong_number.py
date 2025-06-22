# on 22-06-2025
def armstrong():
    n = input("Enter a number : ")
    l = len(n)
    res = 0
    num = int(n)
    num2 = int(n)
    while(num > 0):
        r = num % 10
        res += r**l
        num //= 10
    print(num2,"is armstrong number") if num2 == res else print(num2,"is not armstrong number")

armstrong()
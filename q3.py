# prime

def is_prime(n):
    if n <= 1:
        return 0
    else:
        for i in range(2, n):
            if i % 2 != 0:
                return i
            print(i, end = " ")
num = int(input())
print(is_prime(num))
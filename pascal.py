def print_pascal_triangle(n):
    for line in range(1, n+1):
        num = 1
        for i in range(1, line+1):
            print(num, end=" ")
            num = num * (line - i) // i
        print()

print_pascal_triangle(5)

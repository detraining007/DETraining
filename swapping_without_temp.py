def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

x, y = 5, 10
x, y = swap(x, y)
print("x:", x, "y:", y)

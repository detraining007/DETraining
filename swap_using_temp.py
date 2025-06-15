def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x, y = 5, 10
x, y = swap(x, y)
print("x:", x, "y:", y)

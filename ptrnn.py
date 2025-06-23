n = 5  # height of the top half

# Upper inverted triangle
for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))

# Lower normal triangle
for i in range(1, n):
    print(" " * (n - i - 1 + 1) + "*" * (2 * i + 1))


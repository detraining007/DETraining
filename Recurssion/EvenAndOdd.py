def is_even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    elif n > 1:
        return is_even(n - 2)
    else:  # Handle negative numbers
        return is_even(n + 2)

print(is_even(10))
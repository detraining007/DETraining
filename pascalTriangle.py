def factorial(n):
    result = 1
    for i in range(1, n + 1): # Loop from 1 to n
        result *= i # Multiply result by i at each step
    return result # Return factorial


def ncr(n, r): # function for (nCr) with factorial
    return factorial(n) // (factorial(r) * factorial(n - r))

if __name__ == "__main__":
    n = int(input("How many lines? : "))
    width = 4  # Width per number slot (adjust for spacing)

    total_width = width * n + (width - 1) * (n - 1)  # Full width of bottom row

    for i in range(n):
        row = ""
        for j in range(i + 1): # For each number in the current row, compute nCr
            row += f"{ncr(i, j):^{width}}" # Add each number to the row string, centered within `width` characters
        print(row.center(total_width))

'''
Output:

How many lines? : 5
               1
             1   1
           1   2   1
         1   3   3   1
       1   4   6   4   1

'''
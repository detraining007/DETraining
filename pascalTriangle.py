def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

if __name__ == "__main__":
    n = int(input("How many lines? : "))
    width = 4  # Width per number slot (adjust for spacing)

    total_width = width * n + (width - 1) * (n - 1)  # Full width of bottom row

    for i in range(n):
        row = ""
        for j in range(i + 1):
            row += f"{ncr(i, j):^{width}}"
        print(row.center(total_width))




'''
# Function to compute factorial of a number n
def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
        result *= i           # Multiply result by i at each step
    return result              # Return the computed factorial

# Function to compute "n choose r" (nCr) using the factorial formula
def ncr(n, r):
    # nCr = n! / (r! * (n - r)!)
    return factorial(n) // (factorial(r) * factorial(n - r))

# Main block of the program
if __name__ == "__main__":
    # Prompt the user for the number of lines (height of Pascal's Triangle)
    n = int(input("How many lines? : "))

    width = 4  # Fixed width per number to control spacing in each row

    # Calculate total width of the bottom row to use for centering rows
    # This ensures all rows are centered according to the last row's width
    total_width = width * n + (width - 1) * (n - 1)
    # Explanation:
    # - width * n ? max number of numbers in the last row, each taking `width` characters
    # - (width - 1) * (n - 1) ? total spaces between numbers in the last row

    # Loop through each row of the triangle
    for i in range(n):
        row = ""  # Start with an empty string to build the current row

        # For each number in the current row, compute nCr and format it
        for j in range(i + 1):
            # Add each number to the row string, centered within `width` characters
            row += f"{ncr(i, j):^{width}}"

        # Print the full row string, centered within the total triangle width
        print(row.center(total_width))
'''
list = ['A', 'B', 'C', 'D', 'E']

for rows in range(len(list),0,-1):
    # Print the left side
    for column in range(rows):
        print(list[column], end=" ")

    # Print spaces in between
    spaces = (len(list) - rows) * 4  # Adjust space scaling
    print(" " * spaces, end="")

    # Print the right side
    for column in range(rows):
        print(list[-(column+1)], end=" ")

    print()
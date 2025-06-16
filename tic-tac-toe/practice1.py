import random

# # Generate a 3x3 matrix with random unsorted numbers between 1 and 99
# matrix = [[for i in range(1, 10) for _ in range(3)] for _ in range(3)]

# for row in matrix:
#     print(row).

# 2x2 matrix with zeros
# matrix = [[0 for _ in range(2)] for _ in range(2)]
# print(matrix)
# for row in matrix:
#     print(row)

# import random

# numbers = random.sample(range(1, 5), 3)
# print(numbers)
# matrix = [numbers[i*2:(i+1)*2] for i in range(2)]

# for row in matrix:
#     print(row)
# matrix[1][0]=5
# print(matrix)

import random

# Generate a 2x2 matrix with unique numbers from 1 to 4
numbers = random.sample(range(1, 5), 4)
matrix = [numbers[i*2:(i+1)*2] for i in range(2)]

for row in matrix:
    print(row)

# Insert a value at [1][1]
matrix[0][0] = 0  # Let's use 0 as the movable element (like a blank in a puzzle)
print("\nInitial matrix with 0 at [1][1]:")
for row in matrix:
    print(row)

# Function to move the 0 (blank) in the matrix
def move(matrix, direction):
    # Find the position of 0
    for i in range(2):
        for j in range(2):
            if matrix[i][j] == 0:
                x, y = i, j #
    # Move logic
    if direction == "up" and x > 0:
        matrix[x][y], matrix[x-1][y] = matrix[x-1][y], matrix[x][y]
    elif direction == "down" and x < 1:
        matrix[x][y], matrix[x+1][y] = matrix[x+1][y], matrix[x][y]
    elif direction == "left" and y > 0:
        matrix[x][y], matrix[x][y-1] = matrix[x][y-1], matrix[x][y]
    elif direction == "right" and y < 1:
        matrix[x][y], matrix[x][y+1] = matrix[x][y+1], matrix[x][y]
    else:
        print("Move not possible!")
    return matrix

# Example move
user_move = input("Enter move (up/down/left/right): ").strip().lower()
matrix = move(matrix, user_move)

print("\nMatrix after move:")
for row in matrix:
    print(row)
# Initial scrambled matrix
matrix = [[2, 8, 3],
          [1, 6, 4],
          [7, 0, 5]]  # 0 is the empty space

# Goal matrix (sorted)
goal_matrix = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]

n = len(matrix)

def print_matrix(mat):
    for row in mat:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

# Main game loop
while True:
    print_matrix(matrix)

    if matrix == goal_matrix:
        print("🎉 Matrix sorted! You did it.")
        break

    try:
        num = int(input("Enter number to move (0 to exit): "))
    except ValueError:
        print("❌ Invalid input. Enter a number.")
        continue

    if num == 0:
        print("Game exited.")
        break

    # Find position of number and blank (0)
    num_pos = None
    zero_pos = None
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == num:
                num_pos = (i, j)
            if matrix[i][j] == 0:
                zero_pos = (i, j)

    if not num_pos:
        print("❌ Number not found.")
        continue

    x, y = num_pos
    zx, zy = zero_pos

    # Only allow swap if the number is next to the 0
    if (abs(x - zx) == 1 and y == zy) or (abs(y - zy) == 1 and x == zx):
        matrix[zx][zy], matrix[x][y] = matrix[x][y], matrix[zx][zy]
    else:
        print("⚠️ You can only move a number next to the empty space.")

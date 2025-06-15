
matrix = [ [2, 8, 3],[1, 6, 4],[7, 5, 9]]
n=len(matrix)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

goal_matrix=[ [1, 2, 3],[4, 5, 6],[7, 8, 9]]

while True:
    if matrix == goal_matrix:
        print("🎉 Matrix sorted! You did it.")
        break

    num = int(input("Enter number to move (0 to exit): "))
    if num == 0:
        break

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == num:
                x = i
                y = j
                break
        else:
            continue
        break
    else:
        print("Number not found")
        continue
        
    move = input("Move where? (u = up, d = down, l = left, r = right): ")

    if move == 'u':
        if x > 0:
            matrix[x][y], matrix[x-1][y] = matrix[x-1][y], matrix[x][y]
        else:
            print("Can't move up")
    elif move == 'd':
        if x < 2:
            matrix[x][y], matrix[x+1][y] = matrix[x+1][y], matrix[x][y]
        else:
            print("Can't move down")
    elif move == 'l':
        if y > 0:
            matrix[x][y], matrix[x][y-1] = matrix[x][y-1], matrix[x][y]
        else:
            print("Can't move left")
    elif move == 'r':
        if y < 2:
            matrix[x][y], matrix[x][y+1] = matrix[x][y+1], matrix[x][y]
        else:
            print("Can't move right")
    else:
        print("Invalid move key")

    # Show the matrix after move
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()

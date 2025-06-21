def print_puzzle(puzzle):
    for row in puzzle:
        for val in row:
            if val == 0:
                print('  ', end=' ')  
            else:
                print(f'{val:2}', end=' ')
        print()
    print()

def find_zero(puzzle):
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0:
                return i, j

def possible_moves(x, y):
    moves = []
    if x > 0: moves.append('up')
    if x < 3: moves.append('down')
    if y > 0: moves.append('left')
    if y < 3: moves.append('right')
    return moves

def make_move(puzzle, move):
    x, y = find_zero(puzzle)
    if move == 'up':
        puzzle[x][y], puzzle[x-1][y] = puzzle[x-1][y], puzzle[x][y]
    elif move == 'down':
        puzzle[x][y], puzzle[x+1][y] = puzzle[x+1][y], puzzle[x][y]
    elif move == 'left':
        puzzle[x][y], puzzle[x][y-1] = puzzle[x][y-1], puzzle[x][y]
    elif move == 'right':
        puzzle[x][y], puzzle[x][y+1] = puzzle[x][y+1], puzzle[x][y]


puzzle = [
    [1, 2, 3, 4],
    [5, 6, 0, 8],
    [9, 10, 7, 12],
    [13, 14, 11, 15]
]

while True:
    print_puzzle(puzzle)
    x, y = find_zero(puzzle)
    moves = possible_moves(x, y)
    print("Possible moves:", moves)
    move = input("Enter move (up/down/left/right or 'exit' to quit): ").lower()
    if move == 'exit':
        break
    if move in moves:
        make_move(puzzle, move)
    else:
        print("Invalid move! Try again.")

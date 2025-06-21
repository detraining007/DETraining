import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print("--+---+--")

def check_win(player):
    win_pos = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6]           
    ]
    for pos in win_pos:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_full():
    return all(cell != " " for cell in board)

player = "X"
while True:
    print_board()
    move = int(input(f"Player {player}, enter position (1-9): ")) - 1
    if board[move] == " ":
        board[move] = player
        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("That spot is taken. Try again.")
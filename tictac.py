def create_board():
    board=[['' for _ in range(3)] for _ in range(3)]
    return board
def display_board(board):
    for row in board:
        print('|'.join (row))
        print('_'* 5)
board=create_board()
display_board(board)
      
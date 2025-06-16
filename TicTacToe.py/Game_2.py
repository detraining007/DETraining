import numpy as np

def initialize_players():
    while True:
        print("User_1 : 0\nUser_2 : 1")
        choice = input("Choose starting player (0/1): ").strip()
        
        if choice == "0":
            print("Starting with User_1: 0")
            return 0
        elif choice == "1":
            print("Starting with User_2: 1")
            return 1
        print("Invalid input! Choose 0 or 1\n")

def create_board():
    """Creating 3x3 game"""
    return np.full((3, 3), -1, dtype=int)

def display_board(board):
    print("\nCurrent Board:")
    for row in board:
        print("|", end="")
        for cell in row:
            symbol = ' ' if cell == -1 else str(cell)
            print(f" {symbol} |", end="")
        print("\n-------------")

def get_move(player):
    while True:
        try:
            pos = int(input(f"Player {player+1} ({player}), enter position (0-8): "))
            row, col = divmod(pos, 3)
            if 0 <= pos <= 8:
                return row, col
            print("Invalid position! Try 0-8")
        except ValueError:
            print("Numbers only please!")

def check_win(board, player):
    return (any(np.all(board == player, axis=1)) or 
            any(np.all(board == player, axis=0)) or  # Columns
            np.all(np.diag(board) == player) or      # Main diagonal
            np.all(np.diag(np.fliplr(board)) == player))  # Anti-diagonal

def play_game():
    current_player = initialize_players()
    board = create_board()
    # Maximum 9 moves
    for _ in range(9):
        display_board(board)
        
        # Geting a valid move
        while True:
            row, col = get_move(current_player)
            if board[row, col] == -1:
                break
            print("Position already occupied!")
        
        # Updated board matrix
        board[row, col] = current_player
        
        # Check wining using matrix patterns
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player+1} wins!")
            return
        current_player = 1 - current_player
    
    # Draw condition
    display_board(board)
    print("Game draw!")

if __name__ == "__main__":
    play_game()

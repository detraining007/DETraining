import random

def print_board(board):
    for row in board:
        print(' '.join(f'{num:2}' for num in row))
    print()

def find_position(board, num):
    for i in range(4):
        for j in range(4):
            if board[i][j] == num:
                return i, j
    return None

def move_selected(board, num, direction):
    num_pos = find_position(board, num)
    zero_pos = find_position(board, 0)

    if not num_pos:
        print(f"Number {num} not found on the board!")
        return
    
    num_i, num_j = num_pos
    zero_i, zero_j = zero_pos

    if direction == "up" and num_i > 0 and num_i - 1 == zero_i and num_j == zero_j:
        board[num_i][num_j], board[zero_i][zero_j] = board[zero_i][zero_j], board[num_i][num_j]
        print(f"Moved {num} up.\n")
    elif direction == "down" and num_i < 3 and num_i + 1 == zero_i and num_j == zero_j:
        board[num_i][num_j], board[zero_i][zero_j] = board[zero_i][zero_j], board[num_i][num_j]
        print(f"Moved {num} down.\n")
    elif direction == "left" and num_j > 0 and num_j - 1 == zero_j and num_i == zero_i:
        board[num_i][num_j], board[zero_i][zero_j] = board[zero_i][zero_j], board[num_i][num_j]
        print(f"Moved {num} left.\n")
    elif direction == "right" and num_j < 3 and num_j + 1 == zero_j and num_i == zero_i:
        board[num_i][num_j], board[zero_i][zero_j] = board[zero_i][zero_j], board[num_i][num_j]
        print(f"Moved {num} right.\n")
    else:
        print(f"Invalid move! {num} cannot move {direction}.\n")

def main():
    nums = list(range(16))
    random.shuffle(nums)
    board = [nums[i*4:(i+1)*4] for i in range(4)]

    print("Welcome to the 15 Puzzle Game!")
    print("Arrange the numbers from 1 to 15 in order.")
    print("First, select a number adjacent to the empty space.")
    print("Then, choose a direction (up/down/left/right) to move it.\n")

    while True:
        print_board(board)
        
        try:
            selected_num = int(input("Enter a number (1-15) to move, or -1 to exit: "))
            if selected_num == -1:
                print("Exiting the game. Thanks for playing!")
                break

            direction = input("Enter move direction (up/down/left/right): ").lower()
            move_selected(board, selected_num, direction)

        except ValueError:
            print("Invalid input! Please enter a number.\n")

if __name__ == "__main__":
    main()
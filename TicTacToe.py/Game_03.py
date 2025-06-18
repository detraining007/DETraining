import numpy as np

# --- User Selection --- 
User_1 = 0
User_2 = 1
while True:
    try:
        print("User_1 : 0")
        print("User_2 : 1")
        Select = input("Choose the User_1 or User_2: ")
        if Select == "0":
            print("You have chosen the User_1:", User_1)
            current_player = User_1
            break
        elif Select == "1":
            print("You have chosen the User_2:", User_2)
            current_player = User_2
            break
        else:
            raise ValueError(f"Choose only User_1 or User_2 ({User_1},{User_2}).")
    except ValueError as e:
        print('Invalid_Input:', e)

# --- Correct Board Initialization ---
matrix = np.full((3, 3), -1, dtype=int)  # -1 = empty
print("Initial Matrix:")
for row in matrix:
    print(row)

# --- Game Loop ---
moves_made = 0
while moves_made < 9:
    try:
        print(f"\nPlayer {current_player}'s turn")
        row = int(input("Enter row index (0-2): "))
        col = int(input("Enter column index (0-2): "))

        if row not in range(3) or col not in range(3):
            print("Invalid position! Row/column must be 0-2.")
            continue
        if matrix[row][col] != -1:
            print("Position already occupied!")
            continue
    
        matrix[row][col] = current_player
        moves_made += 1
        print(f"\nUpdated Matrix (Move {moves_made}):")
        for row_disp in matrix:
            print(row_disp)

        win = False
        # Check rows/columns
        for i in range(3):
            if np.all(matrix[i, :] == current_player) or np.all(matrix[:, i] == current_player):
                print(f"Player {current_player} wins!")
                win = True
                break
        # Check diagonals
        if not win:
            if np.all(np.diag(matrix) == current_player) or np.all(np.diag(np.fliplr(matrix)) == current_player):
                print(f"Player {current_player} wins!")
                win = True
        
        if win:
            break
            
        current_player = User_2 if current_player == User_1 else User_1

    except Exception as e:
        print("Invalid input. Please enter integers for row and column.")

if not win and moves_made == 9:
    print("It's a draw!")
  
# --- Correct Restart Logic ---
print("\nDo you want to start the game again? (yes/No)")
ans = input().strip().lower()
if ans == "yes":
    matrix = np.full((3, 3), -1, dtype=int)  # Maintain -1 initialization
    print("\nGame restarted. Initial Matrix:")
    for row_disp in matrix:
        print(row_disp)
else:
    print("Game Over.")

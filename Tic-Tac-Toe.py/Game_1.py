import numpy as np

User_1 = 0
User_2 = 1

# --- User Selection ---
while True:
    try:
        print("User_1 : 0")
        print("User_2 : 1")
        Select = input("Choose the User_1 or User_2: ")
        if Select == "0":
            print("You have chosen the User_1:", User_1)
            player = User_1
            break
        elif Select == "1":
            print("You have chosen the User_2:", User_2)
            player = User_2
            break
        else:
            raise ValueError(f"Choose only User_1 or User_2 ({User_1},{User_2}).")
    except ValueError as e:
        print('Invalid_Input:', e)

# --- Board Initialization ---
matrix = np.zeros((3, 3), dtype=int)
print("Initial Matrix:")
for row in matrix:
    print(row)

# --- Game Loop ---
chances = 0
while chances < 3:
    try:
        row = int(input("Enter row index (0-2): "))
        col = int(input("Enter column index (0-2): "))
        value = int(input("Enter the new value (0 or 1): "))
        if row not in range(3) or col not in range(3) or value not in (0, 1):
            print("Invalid input. Row and column must be 0, 1, or 2; value must be 0 or 1.")
            continue
        matrix[row][col] = value
        chances += 1
        print(f"\nUpdated Matrix (Chance {chances}):")
        for row_disp in matrix:
            print(row_disp)
    except Exception as e:
        print("Invalid input. Please enter integers for row, column, and value.")

    if chances == 3:
        win = False
        # Check rows and columns
        for i in range(3):
            if np.all(matrix[i, :] == 0) or np.all(matrix[:, i] == 0):
                print("User_1 wins!")
                win = True
                break
            if np.all(matrix[i, :] == 1) or np.all(matrix[:, i] == 1):
                print("User_2 wins!")
                win = True
                break
        # Check diagonals
        if not win:
            if np.all(np.diag(matrix) == 0) or np.all(np.diag(np.fliplr(matrix)) == 0):
                print("User_1 wins!")
                win = True
            elif np.all(np.diag(matrix) == 1) or np.all(np.diag(np.fliplr(matrix)) == 1):
                print("User_2 wins!")
                win = True

        if not win:
            print("No winner. Do you want to start the game again? (yes/No)")
            ans = input().strip().lower()
            if ans == "yes":
                matrix = np.zeros((3, 3), dtype=int)
                chances = 0
                print("\nGame restarted. Initial Matrix:")
                for row_disp in matrix:
                    print(row_disp)
            else:
                print("Game Over.")
                break
        else:
            break

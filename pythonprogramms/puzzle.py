import random
#print the random puzzle
def print_puzzle(puzzle):
    for i in range(0, len(puzzle), 3):
        print(f"{puzzle[i]}|{puzzle[i+1]}|{puzzle[i+2]}")
    print()
#to Move the number
def move_number(puzzle, number, direction):
    if direction not in ["up", "down", "left", "right"]:
        print("Invalid direction.")
        return False
    elif direction in ["up", "down", "left", "right"]:
        position = puzzle.index(number) #find the position of the number and that position will change into row,col beloww
    else:
        print("Number not found.")
        return False

    row, col = divmod(position, 3)

    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    d_row, d_col = moves[direction]
    new_row, new_col = row + d_row, col + d_col

    if 0 <= new_row < 3 and 0 <= new_col < 3:
        new_pos = new_row * 3 + new_col
        puzzle[position], puzzle[new_pos] = puzzle[new_pos], puzzle[position]
        return True
    else:
        print("Move out of bounds!")
        return False

def main():
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(puzzle)

    while True:
        print_puzzle(puzzle)
        if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Puzzle solved")
            break
        elif puzzle!= [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            number = int(input("Choose number to move: "))
            direction = input("Direction (up/down/left/right): ").lower()
            moved = move_number(puzzle, number, direction)

            if not moved:
                print("Try a valid direction:")
            else:
                print("enter a valid number:")

main()

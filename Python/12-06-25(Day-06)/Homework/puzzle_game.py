#To design a puzzle game where we try to rearrange the numbers in an order in the matrix


matrix=[[1,2,3],[4,5,6],[7,8,9]]


def print_func():
    print("The matrix is: ")
    for i in range(3):
        for j in range(3):
            print(matrix[i][j],end=" ")
        print()

if __name__=="__main__":

    print_func() 
    

    r=int(input("Enter row index: "))
    c=int(input("Enter column index: "))
    print("You are at the number: ",matrix[r][c])
    print("To swap element with the above element choose:  u\n" \
    "To swap element with the below element choose:  b\n" \
    "To swap element with the left element choose:   l\n" \
    "To swap element with the right element choose:  r\n" \
    "To stop the session enetr choice             :  end")
    while True:
        choice = input("Enter your choice: ")
        if choice == "u":
            if r > 0:
                matrix[r][c], matrix[r-1][c] = matrix[r-1][c], matrix[r][c]
                r -= 1  # update position
                print_func()
            else:
                print("Move not possible. You're at the top edge.")
        elif choice == "b":
            if r < 2:
                matrix[r][c], matrix[r+1][c] = matrix[r+1][c], matrix[r][c]
                r += 1
                print_func()
            else:
                print("Move not possible. You're at the bottom edge.")
        elif choice == "l":
            if c > 0:
                matrix[r][c], matrix[r][c-1] = matrix[r][c-1], matrix[r][c]
                c -= 1
                print_func()
            else:
                print("Move not possible. You're at the left edge.")
        elif choice == "r":
            if c < 2:
                matrix[r][c], matrix[r][c+1] = matrix[r][c+1], matrix[r][c]
                c += 1
                print_func()
            else:
                print("Move not possible. You're at the right edge.")
        elif choice.lower()=="end":
            print("You have ended your session")
            break
        else:
            print("You have entered a wrong choice.")
            choice2 = input("Would you like to choose again? Type yes/no: ")
            if choice2.lower() != "yes":
                print("You have selected to end your session.")
                break




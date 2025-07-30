def mat_transpose(size):
    total_size = size*size
    Elements = (input(f'Enter the {total_size} values for {size}*{size}'))
    El_list = list(map(int,Elements.split()))
    if(len(El_list)==total_size):
        print("Correct input")
    else:
        print(f'For {size}*{size} matrix the elements should be  exactly {total_size}')
    mat_values = [El_list[val:val+size] for val in range(0,total_size,size)]
    print(mat_values)
    print("Matrix before tranpose:")
    for row in range(len(mat_values[0])):
        for col in range(len(mat_values[row])):
            print(mat_values[row][col],end = ' ')
        print()
    
    print("Matrix after tranpose:")
    for row in range(len(mat_values[0])):
        for col in range(len(mat_values[row])):
            if(row<col):
                mat_values[row][col],mat_values[col][row] = mat_values[col][row],mat_values[row][col]
            print(mat_values[row][col],end = " ")
        print()
    




if __name__ == "__main__":
    size = int(input("Enter the matrix of any size"))
    print(mat_transpose(size))


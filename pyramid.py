# generate pyramid sequence
def PyramidPattern(number_of_rows):
    # Top half including middle row
    for row_number in range(1, number_of_rows + 1): # for range we use +1
        spaces = '  ' * (number_of_rows - row_number) # number of rows - row number : gives spaces before the first star prints in that row
        stars = ' *  ' * row_number # prints stars as per row number
        print(spaces + stars)

    # Bottom half
    for row_number in range(number_of_rows - 1, 0, -1): # to decrease the range in steps of 1
        spaces = '  ' * (number_of_rows - row_number) # number of rows - row number : gives spaces before the first star prints in that row
        stars = ' *  ' * row_number # prints stars as per row number
        print(spaces + stars) 

number_rows = int(input("Enter the number of rows : "))
PyramidPattern(number_rows)
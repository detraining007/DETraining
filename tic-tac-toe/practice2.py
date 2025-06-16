num = [3,2,0,1] # so this an 2*2 matrix

matrix=[num[i*2:(i+1)*2]for i in range(2)]

print(matrix)

for i in matrix:
    print(i)
 
flage = False
# while
while flage == False:
    def move(matrix, direction):
        for i in range(2):
            for j in range(2):
                if matrix[i][j] == 0:
                    x,y = i,j
        
        # Move logic

        if direction == "up" and x > 0:
            matrix[x][y], matrix[x-1][y] = matrix[x-1][y], matrix[x][y]
        elif direction == "down" and x < 1:
            matrix[x][y], matrix[x+1][y] = matrix[x+1][y], matrix[x][y]
        elif direction == "left" and y > 0: # if it is 0 means we can move

            matrix[x][y] , matrix[x][y-1] = matrix[x][y-1],matrix[x][y]
        elif direction == "right" and y<1:
            matrix[x][y], matrix[x][y+1] = matrix[x][y+1],matrix[x][y]
        else:
            print("move not posible")
        return matrix
    user_move = input("Enter move (up/down/left/right): ").strip().lower()
    matrix = move(matrix, user_move)

    print(matrix)

    print("\nMatrix after move:")
    for row in matrix:
        print(row)

    def sort_matrix(matrix):
        single_list = matrix[0] + matrix[1] 
        return single_list == sorted(single_list)
    
    if sort_matrix(matrix):
        print("The matrix is sorted.")
        flage = False
        
    print(sort_matrix(matrix))















# matrix = []

# for i in num:
#     print (i)
# matrix = [num[i*2:(i+1)*2] for i in range(2)]
# print(num[0:2])



# for i in range(0,2):
#     for j in range(0,2):
#         matrix[i]

    
    
        

# a[0][0]
# a[0][1]
# a[1][0]
# a[1][1]
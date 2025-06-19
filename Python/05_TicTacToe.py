
matrix = [[2,3,5],[1,8,4],[6,7,9]]
sorted_matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j],end=" ")
    print()

# print("Enter the indexes of element")
# index1 = int(input("Enter index1: "))
# index2 = int(input("Enter index2: "))

print("Enter the indexes of element")
index1 = int(input("Enter index1: "))
index2 = int(input("Enter index2: "))
print("You are at ",matrix[index1][index2])
while matrix != sorted_matrix:


    choice = input("To move upward Enter                   :w\n" \
                    "To move downward Enter                 :s\n" \
                    "To move to the left side Enter         :a\n" \
                    "To move to the right side Enter        :d\n").lower()

    if choice == "w" and index1>0:
        temp = matrix[index1][index2]
        matrix[index1][index2] = matrix[index1-1][index2]
        matrix[index1-1][index2] = temp
        index1,index2 = index1-1,index2
        
    elif choice == "s" and index1 <2:
        temp = matrix[index1][index2]
        matrix[index1][index2] = matrix[index1+1][index2]
        matrix[index1+1][index2] = temp
        index1,index2 = index1+1,index2
    elif choice == "a" and index2 > 0: 
        temp = matrix[index1][index2]
        matrix[index1][index2] = matrix[index1][index2-1]
        matrix[index1][index2-1] = temp
        index1,index2 = index1,index2-1
    elif choice == "d" and index2 < 2 :
        temp = matrix[index1][index2]
        matrix[index1][index2] = matrix[index1][index2+1]
        matrix[index1][index2+1] = temp
        index1,index2 = index1,index2+1
    else:
        print("Please enter the right choice")

    print("The matrix after swapping")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j],end=" ")
        print()

    next_location = input("Enter Y to goto next location\n" \
                            "Enter N to continue with the current location").lower()
    if next_location == "y" and  matrix != sorted_matrix:
            print("Enter the indexes of element")
            index1 = int(input("Enter index1: "))
            index2 = int(input("Enter index2: "))
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    print(matrix[i][j],end=" ")
                print()
            print("You are at ",matrix[index1][index2])
    elif next_location == "n":
        continue
 
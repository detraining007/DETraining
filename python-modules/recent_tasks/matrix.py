# Tic Tac Toe

matrix = [[17,10,16,14],
          [13,12,24,25],
          [11,23,20,18],
          [19,15,13,21]]

def isSorted(list2d):
    rows = len(list2d)
    cols = len(list2d[0])
    for row in range(rows):
        for col in range(cols):
            if col < cols-1 and list2d[row][col] > list2d[row][col+1]:
                return False
            if row < rows-1 and list2d[row][col] > list2d[row+1][col]:
                return False
    return True

def swap(list2d,idx1,idx2):
    temp = list2d[idx1[0]][idx1[1]]
    list2d[idx1[0]][idx1[1]] = list2d[idx2[0]][idx2[1]]
    list2d[idx2[0]][idx2[1]] = temp


inValue = 'a'
idx = [0,0]
while(isSorted(matrix) != True):
    inValue = input("Enter input to proceed : ")
    if inValue == 'x':
        print("You have chosen to end program")
        break
    rows = len(matrix)
    cols = len(matrix[0])
    if inValue == 'u':
        idxs = [idx[0]-1,idx[1]]
        if(idx[0] < 1):
            print("We are on first row, Cannot move up")
            continue
        swap(matrix,idx,idxs)
        idx = idxs
        for a in range(rows):
            print(matrix[a])
        print("Now we are at : ",matrix[idxs[0]][idxs[1]])
    elif inValue == 'd':
        idxs = [idx[0]+1,idx[1]]
        if(idx[0] >= rows-1):
            print("We are on last row, Cannot move down")
            continue
        swap(matrix,idx,idxs)
        idx = idxs
        for a in range(rows):
            print(matrix[a])
        print("Now we are at : ",matrix[idxs[0]][idxs[1]])
    elif inValue == 'l':
        idxs = [idx[0],idx[1]-1]
        if(idx[1] < 1):
            print("We are on left most column, Cannot move left")
            continue
        swap(matrix,idx,idxs)
        idx = idxs
        for a in range(rows):
            print(matrix[a])
        print("Now we are at : ",matrix[idxs[0]][idxs[1]])
    elif inValue == 'r':
        idxs = [idx[0],idx[1]+1]
        if(idx[1] >= cols-1):
            print("We are on right most column, Cannot move right")
            continue
        swap(matrix,idx,idxs)
        idx = idxs
        for a in range(rows):
            print(matrix[a])
        print("Now we are at : ",matrix[idxs[0]][idxs[1]])
    else:
        print("Entered input not in - u, d, l, r \n Please enter one of them")

# flaw - position is sticked to one value throughout the program
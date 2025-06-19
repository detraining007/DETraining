m1 = [[22,45,41,17,64,-45,56],
      [16,10,75,-2,23,-4,74],
      [18,34,5,11,71,-32,0],
      [43,78,12,-67,23,31,18]]

def columnSort(matrix):
    isSwapped = False
    nrows = len(matrix)
    ncols = len(matrix[0])
    # Bubble sort for each column
    for c in range(ncols):
        for i in range(nrows - 1):
            for j in range(nrows - 1 - i):
                if(matrix[j][c] > matrix[j + 1][c]):
                    matrix[j][c], matrix[j + 1][c] = matrix[j + 1][c], matrix[j][c]
                    isSwapped = True
    return isSwapped

def rowSort(matrix):
    isSwapped = False
    nrows = len(matrix)
    ncols = len(matrix[0])
    # Bubble sort for each row
    for r in range(nrows):
        for i in range(ncols - 1):
            for j in range(ncols - 1 - i):
                if(matrix[r][j] > matrix[r][j + 1]):
                    matrix[r][j], matrix[r][j + 1] = matrix[r][j + 1], matrix[r][j]
                    isSwapped = True
    return isSwapped

def eSort(matrix):
    isSwapped = False
    nrows = len(matrix)
    ncols = len(matrix[0])
    for r in range(nrows - 1):
        if(matrix[r][ncols - 1] > matrix[r + 1][0]):
            matrix[r][ncols - 1], matrix[r + 1][0] = matrix[r + 1][0], matrix[r][ncols - 1]
            isSwapped = True
    return isSwapped

def sortMatrix(matrix):
    rowSwap = rowSort(matrix)
    colSwap = columnSort(matrix)
    eSwap = eSort(matrix)
    while(rowSwap == True or colSwap == True or eSwap == True):
        rowSwap = rowSort(matrix)
        colSwap = columnSort(matrix)
        eSwap = eSort(matrix)

if __name__ == "__main__":
    sortMatrix(m1)
    for row in m1:
        print(row)

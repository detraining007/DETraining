def transpose(matrix,n,m):
    print("Given Matrix:")
    for row in matrix:
        print(row)
    out = []
    for x in range(m):         
        new_row = []           
        for y in range(n):     
            new_row.append(matrix[y][x])
        out.append(new_row)

    print("Transposed Matrix:")
    for row in out:
        print(row)
        return out

if __name__ == '__main__':
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of columns: "))
    matrix = eval(input("Enter matrix as nested list (like: [[1,2,3..],[4,5,6]...]): "))

    trans = transpose(matrix,n,m)

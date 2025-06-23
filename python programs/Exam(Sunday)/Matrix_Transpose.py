def create_matrix(row,column):
    matrix =[]
    k = 1

    for i in range(row):
        lst =[]
        for j in range(column):
            lst.append(int(input(f"Enter element {k} ")))
            k +=1
        matrix.append(lst)
    return matrix
def transpose_matrix(result):
    single_list = []
    for i in result:
        for j in i:
            single_list.append(j)
    matrix =[]
    k =0
    for row in range(len(result[0])):
        lst =[]
        for column in range(len(result)):
            lst.append(single_list[k])
            k +=1
        matrix.append(lst)
    return matrix


row = int(input("Enter number of rows in matrix"))
column = int(input("Enter number of columns in matrix"))
result = create_matrix(row,column)
print("Your Matrix")
for row in result:
    print(row)
transpose = transpose_matrix(result)
print("Transposed matrix")
for i in transpose:
    print(i)


from selection import selection_sort
def mat_list(matrix):
    list = []
    for row in matrix:
        for item in row:
            list.append(item)
    return list
def  mat(list):
    for row in list:
        print(*row)

def list_mat(list,c):
    nested = []
    for i in range(0, len(list), c):
        row = []
        for j in range(i, min(i + c, len(list))):
            row.append(list[j])
        nested.append(row)
    print("\nMatrix form:")
    for row in nested:
        print(*row)
    return nested

if __name__ == '__main__':

    matrix= eval(input("Enter nested list: "))
    c=len(matrix[0])
    see=mat(matrix)
    unsort=mat_list(matrix)
    after_sort=selection_sort(unsort)
    final=list_mat(after_sort,c)

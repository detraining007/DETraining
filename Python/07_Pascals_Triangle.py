n = 6

triangle = []

for i in range(n):
    row = [1]


    if i > 0:
        last_row = triangle[-1]
        # print(last_row)

        for j in range(1,i):
            ele = last_row[j-1] + last_row[j]
            # print(last_row[j])
            # print(last_row[j-1])
            row.append(ele)
        row.append(1)

    triangle.append(row)


spaces = n - 1
for i in triangle:

    for k in range(spaces):
        print(" ",end="")
    for j in i:
        print(j,end=" ")
    spaces-=1
    print()

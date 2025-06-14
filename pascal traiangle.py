

def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]  
        if i > 0:
            last_row = triangle[-1]
            for j in range(1,i):
                ele = last_row[j] + last_row[j-1]
                row.append(ele)
            row.append(1)  
        triangle.append(row)
 
    print("the triangle")
    for row in triangle:
        print(' '.join(map(str, row)))



# def pascal_triangle(n):
#     triangle = []

#     for i in range(n):
#         row = [1]
#         if i > 0:
#             for j in range(1,i):
#                 row.append(triangle[i-1][j-1] + triangle[i-1][j])
#             row.append(1)
#         triangle.append(row)

#     print("the triangle")
#     for row in triangle:
#         print(' '.join(map(str, row)))


# pairs = [(x, y) for x in range(1, 4) for y in range(4, 7)]
# print(pairs)



pascal_triangle(4)


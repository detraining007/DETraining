# n=5
# for rows in range(1, n + 1):
#     for space in range(1,n-rows+1):
#         print(" ", end= "")
#     for colms in range(1,2 *rows):
#         if colms<=rows:
#             print(colms, end= "")
#         else:
#             print( 2*rows-colms,end="")
#     print()
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end="")
    for colm in range(1,2*rows):
        if colm<=rows:
            print(colm,end="")
        else:
            print(2*rows-colm,end="")
    print()
#To print a * pattern. The pattern should look like top half of a rhombus with 5 rows.
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *   


# num=6
# for row in range(num):
#     print(end=(num-row)*" ")
#     for col in range(row):
#         print("*",end=" ")
#     print("\n")


num=6
for row in range(num):
    print(" "*(num-row-1),end=" ")
    for col in range(row):
        print("*",end=" ")
    print("\n")


# n=5
# for i in range(n):
#     #Print leading spaces
#     print(' ' * (n - i - 1), end='')
#     # Print stars with spaces
#     print('* ' * (i + 1))
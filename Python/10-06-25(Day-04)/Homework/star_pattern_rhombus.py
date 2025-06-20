#To print a * pattern. The pattern should look like top half of a rhombus with 5 rows.
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *  
#   * * * * 
#    * * *
#     * *
#      *

num=6
for row in range(num):
    print(" "*(num-row-1),end=" ")
    for col in range(row):
        print("*",end=" ")
    print("\n")

num2=5
for row in range(num2):
    print(" "*row,end=" ")
    for col in range(num2-row):
        print("*",end=" ")
    print("\n")


# n=5
# for i in range(n):
#     #Print leading spaces
#     print(' ' * (n - i - 1), end='')
#     # Print stars with spaces
#     print('* ' * (i + 1))

# for i in range(4):
#     print(' '*i,end=" ")
#     print('* '*(4-i))
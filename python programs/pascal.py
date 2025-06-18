def pascal_triangle(number):
    for row in range(number):
     print(" " * (number-row),end="  ")
     num = 1
     for col in range(row+1):
         print(num,end=" ")
         num =int( num * (row - col)/(col+1))
     print()

number = int(input("Enter length of pascal triangle"))
pascal_triangle(number)


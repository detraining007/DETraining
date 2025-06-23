def pascal_triangle(number):
    for row in range(number):
        spaces = " "*(number-(row+1))
        print(spaces,end="")
        num=1
        for column in range(row+1):
            print(num,end=" ")
            num = int(num * (row - column)/(column+1))
        print()

number = int(input("Enter length of pascal triangle"))
pascal_triangle(number)


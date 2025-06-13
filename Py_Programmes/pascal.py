rows = int(input("Enter number of rows: "))

for i in range(rows):
    number = 1
    print(" " * (rows - i), end="")

    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)

    print()  

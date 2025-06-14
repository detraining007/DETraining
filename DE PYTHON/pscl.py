def pascal_triangle(n):
    print("\nPascal's Triangle:\n")
    for i in range(n):
        print(" " * (n - i), end="")  
        val = 1  
        for j in range(i + 1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1)  
        print()
    print("\nPascal's Triangle Completed.")

rows = int(input("Enter number of rows for Pascal's Triangle: "))
pascal_triangle(rows)

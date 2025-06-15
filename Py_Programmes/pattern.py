n = 6  
for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    spaces = 2 * i - 1
    print("  " * spaces, end="")  

    for j in range(n - i - 1, -1, -1):
        if i == 0 and j == n - i - 1:
            continue 
        print(chr(65 + j), end=" ")

    print()  

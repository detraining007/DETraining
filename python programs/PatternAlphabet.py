n = 6  
for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end=' ')
    space_count = 2 * i - 1
   
    if space_count > 0:
        print('  ' * space_count, end='')
    if i>=1:
        for j in range(n - i - 1, -1, -1):
            print(chr(65 + j), end=' ')
    print()  

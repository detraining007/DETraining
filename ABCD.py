'''
def print_pattern():
    n = 6  
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(n):
        
        left_part = [alphabets[j] for j in range(n - i)]

        
        right_part = left_part[:-1][::-1]  


        spaces = "  " * (2 * i - 1) if i != 0 else ""

        
        if i == 0:
        
            line = ' '.join(left_part + right_part)
        else:
            line = ' '.join(left_part) + spaces + ' '.join(right_part)

        print(line)

print_pattern()


'''



def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)

    print("The triangle:")
    for row in triangle:
        print(' '.join(map(str, row)))



pascal_triangle(5)

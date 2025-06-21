def print_pattern(n):
    for i in range (n):
        for j in range (n-i):
            print(chr(65+j),end = "")
            spaces = 2*i-1
            print(" ",*spaces, end = " ")
            for j in range (n-i)

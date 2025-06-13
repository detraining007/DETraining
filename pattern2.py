def rhombus_pattern(lines):
    for Upper_Triangle in range(lines-1):
        for spaces in range(Upper_Triangle,lines):
            print(" ",end = "  ")
        for left_stars in range(Upper_Triangle):
            print("*",end = "  ")
        for right_stars in range(Upper_Triangle+1):
            print("*",end = "  ")
        print("\n")
    for lower_triangle in range(lines):
        for spaces in range(lower_triangle+1):
            print(" ",end = "  ")
        for left_stars in range(lower_triangle,lines-1):
            print("*",end = "  ")
        for  right_stars in range(lower_triangle,lines):
            print("*",end = "  ")
        print("\n")






if __name__ == "__main__":
    lin = int(input("Enter the no of lines you want: "))
    print(rhombus_pattern(lin))
     
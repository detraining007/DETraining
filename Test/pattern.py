def pat(size):
    for upper_triangle in range(size):
        for left_space in range(upper_triangle+1):
            print(" ",end = "")
        for triangle in range(upper_triangle,size):
            print("*",end = " ")
        for right_space in range(upper_triangle+1):
            print(" ",end = " ")
        print()
    for lower_triangle in range(size-1):
        for left_space in range(lower_triangle,size):
            print(" ",end = "")
        for triangle in range(lower_triangle+1):
            print("*",end = " ")
        for right_space in range(lower_triangle,size):
            print(" ",end = " ")
        print()
    







if __name__ == "__main__":
    size = int(input("Enter the size of pattern"))
    print(pat(size))

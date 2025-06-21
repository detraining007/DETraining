def transpose(size):
    total_size = size*size
    while True:
        User_input = input(f"Enter {total_size} elements for {size}*{size} matrix: ")
        Elements = list(map(int,User_input.split()))
        if(len(Elements)==total_size):
            print("Correct no of elements")
            break
        else:
            print(f'Wrong no of elements entered,for{size}*{size} matrix elements must be exactly {total_size}')
    Mat_Values = [Elements[val:val+size] for val in range(0,total_size,size)]
    print(Mat_Values)
    print("Array before getting sorted:")
    for row in range(len(Mat_Values[0])):
        for col in range(len(Mat_Values[row])):
            print(Mat_Values[row][col],end = " ")
        print()
    print("We are transposing the matrix i.e rows and columns will be interchanged")
    for row in range(len(Mat_Values[0])):
        for col in range(len(Mat_Values[row])):
            if(row < col):
               Mat_Values[row][col],Mat_Values[col][row] = Mat_Values[col][row],Mat_Values[row][col]
            print(Mat_Values[row][col],end = " ")
        print()
    print("This is transposed matrix with rows and columns inter changed")
                













if __name__ == "__main__":
    size = int(input("Enter the size of matrix: "))
    print(transpose(size))
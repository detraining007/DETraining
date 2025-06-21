def Matrix_Sort(size):
    total_size = size*size
    while True:
        User_input = input(f"Enter {total_size} elements for {size}*{size} matrix")
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
    print("Array after getting sorted:")
    for row in range(len(Elements)-1):
        min = Elements[row]
        index = row
        for col in range(row+1,len(Elements)):
            if(Elements[col]<min):
                min = Elements[col]
                index = col
        Elements[index] = Elements[row]
        Elements[row] = min
    Mat_Values2 = [Elements[val:val+size] for val in range(0,total_size,size)]
    for row in range(len(Mat_Values2[0])):
        for col in range(len(Mat_Values2[row])):
            print(Mat_Values2[row][col],end = " ")
        print()

    
    
            
            
        
    
    
    










if __name__ == "__main__":
    size = int(input("Enter the size of matrix: "))
    print(Matrix_Sort(size))
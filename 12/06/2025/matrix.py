def matrix_multiply(mat1,mat2):
    # this is second matrix
    size1 = mat1
    total_size1 = mat1*mat1
    user_input1 = input(f'For {size1} size Please enter the matrix values of {total_size1}: ')
    mat1_val = list(map(int,user_input1.split()))
    if len(mat1_val) != total_size1:
      print(f'You entered wrong size for {mat1_val},it must be in the range of { total_size1} only')
    Matrix1 = [mat1_val[val1:val1+size1] for val1 in range(0,total_size1,size1)]
    

    # this is second matrix
    size2 = mat2
    total_size2 = mat2*mat2
    user_input2 = input(f'For {size2} size Please enter the matrix values of {total_size2}: ')
    mat2_val = list(map(int,user_input2.split()))
    if len(mat2_val) != total_size2:
      print(f'You entered wrong size for {mat2_val},it must be in the range of { total_size2} only')
    Matrix2 = [mat2_val[val2:val2+size1] for val2 in range(0,total_size2,size2)]
   
    #now,we will do mutliplication i.e Matrix1 * Matrix2
    Matrix3 = [[0*size1 for el in range(size1)] for el1 in range(size2)]
    
    
    
    for i in range(size1):
       for j in range(size2):
          for k in range(size2):
           Matrix3[i][j] += Matrix1[i][k]*Matrix2[k][j] 
    print("1st matrix is:") 
    for row in Matrix1: 
        print(row)   
    print("2nd matrix is:")
    for row in Matrix2: 
        print(row)  
    print("result of 1st matrix and 2nd matrix is :")
    for row in Matrix3: 
        print(row) 
    print(f'The product of {Matrix1}*{Matrix2} is {Matrix3}')


       
    
              
   






if __name__ == "__main__":
    mat1 = int(input("Please enter the first matrix limit: "))
    mat2 = int(input("Please enter the second matrix limit: "))
    print(matrix_multiply(mat1,mat2))

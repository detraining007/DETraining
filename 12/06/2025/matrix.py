def matrix_multiply(mat1,mat2):
    # this is second matrix
    size1 = mat1
    total_size1 = mat1*mat1
    user_input1 = input(f'For {size1} size Please enter the matrix values of {total_size1}: ')
    mat1_val = list(map(int,user_input1.split()))
    if len(mat1_val) != total_size1:
      print(f'You entered wrong size for {mat1_val},it must be in the range of { total_size1} only')
    Matrix1 = [mat1_val[val1:val1+size1] for val1 in range(0,total_size1,size1)]
    for row in Matrix1: 
        print(row)

    # this is second matrix
    size2 = mat2
    total_size2 = mat2*mat2
    user_input2 = input(f'For {size2} size Please enter the matrix values of {total_size2}: ')
    mat2_val = list(map(int,user_input2.split()))
    if len(mat2_val) != total_size2:
      print(f'You entered wrong size for {mat2_val},it must be in the range of { total_size2} only')
    Matrix2 = [mat1_val[val2:val2+size1] for val2 in range(0,total_size1,size1)]
    for row in Matrix2: 
        print(row)   

    #now,we will do mutliplication i.e Matrix1 * Matrix2
    Matrix3 = []
    final_matrix = 0
    
    for i in Matrix1:
       for j in i:
          Matrix3 = Matrix1[i][j]*Matrix2[j][i] 
          final_matrix += Matrix3
          j +=1
       i += 1
       
    
              
   






if __name__ == "__main__":
    mat1 = int(input("Please enter the first matrix limit: "))
    mat2 = int(input("Please enter the second matrix limit: "))
    print(matrix_multiply(2,0))

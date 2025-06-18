def game(size):
    total_size = size*size
    while True:
     user_input = input(f"Please enter {total_size} elements for matrix size {size}: ")
     Matrix = list(map(int,user_input.split()))
     if(len(Matrix)== total_size):
        print("Correct input")
        break
     else:
      print(f'wrong no of elements,for {size} matrix elements must be {total_size},not less or more')
    
    Mat_values =[ [Matrix[val:val+size] for val in range(0,total_size,size)]]
    for row in range(len(Mat_values[0])):
       for col in  range(len(Mat_values[0][row])): 
         print(Mat_values[0][row][col],end = ' ')
       print()
       
    choice = "yes"
    i = int(input("Enter row value "))
    j = int(input("Enter column value"))
    element = [Mat_values[0][i][j]]
    print(f'You are at {Mat_values[0][i][j]}')
    correct= True
    while(choice == "yes"):
      while correct:
         user_choice = input("Enter your choice between up,left,right,down:")
         if user_choice not in ["up", "down" , "left" , "right"]:
            print("choice must be either up,down,left,right")
         else:
           print("correct choice")
           break
      new_i,new_j = i,j
      if(user_choice=="up" and i>0):
         new_i -= 1
      elif(user_choice=="down" and i<size-1):
         new_i += 1
      elif(user_choice=="left" and j>0):
         new_j -= 1
      elif(user_choice=="right" and j<size-1):
         new_j += 1
      else:
         print("Wrong user choice,user choice must be either up or down or left or right or move is not possible")
         continue
      
      #updating matrix
      Mat_values[0][i][j],Mat_values[0][new_i][new_j] = Mat_values[0][new_i][new_j],Mat_values[0][i][j]
      i,j = new_i,new_j

      #printing updated matrix
      print("Updated matrix:")
      for row in range(len(Mat_values[0])):
         for col in range(len(Mat_values[0][row])):
            print(Mat_values[0][row][col],end= ' ')
         print()
      print(f'You are at {Mat_values[0][i][j]}')
      
      choice = input("Do you want to continue,Type yes or no: ")
        
        
         




      


if __name__ == "__main__":
    size = int(input("Enter the matrix size you want: "))
    print(game(size))
    
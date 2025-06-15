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
    for row in range(len(Mat_values)):
       for col in  range(len(Mat_values[row])): 
        print(Mat_values[row][col])
    choice = "yes"
    i = 0
    j = 0
    element = Mat_values[0][i][j]
    cursor = [0][i][j]
    correct= True
    while(choice == "yes"):
      while(correct == True):
         user_choice = input("Enter your choice between up,left,right,down:")
         if(user_choice != "up" or "down" or "left" or "right"):
            print("choice must be either up,down,left,right")
         else:
           print("correct choice")
           break
      if(user_choice=="right"):
         cursor = [0][i-1][j]
         Mat_values[0][i-1][j] = element
         Mat_values[0][i][j] = Mat_values[cursor]
    for row in range(len(Mat_values)):
       for col in range(len(Mat_values[row])):
          print[col]
         




      


if __name__ == "__main__":
    size = int(input("Enter the matrix size you want: "))
    print(game(size))
    
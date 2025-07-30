class Stack_Menu:
    def __init__(self,option,Elements):
       self.option= option
       self.Elements = Elements
    def Menu(self):
       another_try = True
       option = self.option
       Elements= self.Elements
       while(another_try):
        if(option==1):
          add=int(input("Enter element to add: "))
          Elements.append(add)
        elif(option==2):
          if(len(Elements)==0):
             print("Stack is empty,cannot pop")
          else:
           Elements.pop()
        elif(option==3):
            if(len(Elements)==0):
               print("Stack is empty,top value cannot be printed")
            else:
              print("Top Element",Elements[-1])
        elif(option==4):
          if(len(Elements)==0):
             print("Stack is Empty")
          else:
             print("Stack Elements:",Elements)
        elif(option==5):
          print("Size of stack",len(Elements))
        else:
           print("Invalid input")
        further= input("Do you want to continue? Type yes or no: ")
        if(further.lower()=="yes"):
          option = int(input("Enter the option again:"))
        elif(further.lower()=="no"):
            print("Thank you for playing")
            another_try = False
        else:
          print("wrong text,enter only yes or no")
       

        
          
       
        




 
    











if __name__ == "__main__":
    print("Welcome to Stack Menu")
    listed = input("Please enter your elements:")
    Elements = list(map(int,listed.split()))
    print("In stack you can perform 5 operations,please enter the following number for following operation:" )
    print("1:Push()-Add an element to end")
    print("2:Pop()-Remove an element from the end")
    print("3:peek()/top()-the last element")
    print("4:isEmpty()-checks if stack is empty")
    print("5:size()-to know the size")
    option= 0
    val = True
    while(val):
      choice = int(input("Enter your choice between 1 and 5: "))
      if(choice>5):
         print("Your choice is greater than 6,please enter choice between 1 and 6!")
      elif(choice<=5):
        print("Correct Choice")
        val = False
        option = choice
    obj1 = Stack_Menu(option,Elements)
    obj1.Menu()




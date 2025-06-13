from Menu_lib import *

if __name__=="__main__":
  while(True):
    try:
      Num_1=int(input("Enter the Num_1 value: "))
      Num_2=int(input("Enter the Num_2 value: "))
    except ValueError:
      print("Invalid Numbers! Enter the correct digits")
      continue

    print("Choose the Method to be perform Operations")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Remainder")

    try:
      Operation = int(input("Choose the Operation Number: "))
      if Operation>5 or Operation<1:
        raise ValueError(f"Invalid Operation Number :{Operation}. Enter the Operation Number Between 1 to 5")
        break
    except ValueError as e:
      print(e)
      continue

    if (Operation ==1):
      print("Result:",add(Num_1,Num_2))

    elif (Operation ==2):
      print("Result:",sub(Num_1,Num_2))


    elif(Operation==3):
      print("Result:",Multi(Num_1,Num_2))


    elif(Operation==4):
      print("Result: ",Div(Num_1,Num_2))

    elif(Operation==5):
      print("Result: ",Remainder(Num_1,Num_2))

    """else:
      print("You had Entered the Wrong Operation Method!")
      time.sleep(1)
      restart=input("Do you want to start the program again(yes/No): ").strip().lower()
      if restart .lower()!= "yes":
        print("Exiting the Program")
        break
      else:
        continue"""

    #After the successful Completion of program
    Again=input("\nDo you want to start the program Again ?(yes/No): ")
    if Again.lower()!="yes":
      print("Iam Exiting the Program")
      print("Thank You!")
      break

def read_file():
    with open("example.txt","r") as file:
        content= file.read()
        print(content)
def write_file():
    with open("example.txt","w") as file:
        file.write("i am doing work")
        print("content written successfully")
def append_to_file():
    with open("example.txt","a") as file:
        file.write("\n this is new lines")
        print("content append successfully")
decision = "yes"
while decision.lower()=="yes":
    print("\nmenu:\n1:.read\n.write\n2.append\n3.append to file:")
    choice=int(input("enter the choice (1 to 3):"))

    if choice==1:
        read_file()
    elif choice==2:
        write_file()
    elif choice==3:
        append_to_file()
    else:
        print("please enter valid choice (1 to 3):")
    decision=input("do you want to continue? (yes/no):")
print("thank you for using txt files")


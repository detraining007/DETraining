# #To implement file operations using the menu driven method

#To create a new file
with open('test.txt',"w") as file:
    info=file.write("Im writing into the file")
    print("Creating file is done")
with open('test.txt',"r") as file:
    context0=file.read()
    print(context0)

#To write information to the file
with open('example.txt',"w") as file:
    context=file.write("Hello world")
    print("The writing operation is done")

#To read information from the file
with open('example.txt',"r") as file:
    context1=file.read()
    print(context1)

#To append information to the file
with open('example.txt',"a") as file:
    context2=file.write("This is DD")
    print("Append operation is done")
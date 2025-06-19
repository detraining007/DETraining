try:
    with open("C:\\test\\DETraining\\python-modules\\python_concepts\\files\\test2.txt","r") as file:
        line = file.read()
        print(line)
except FileNotFoundError:
    with open("C:\\test\\DETraining\\python-modules\\python_concepts\\files\\test2.txt","w") as file:
        file.write("EXCEPT ... This is first line of test2 file")
        file.close()

with open("C:\\test\\DETraining\\python-modules\\python_concepts\\files\\test1.txt","w+") as file:
    file.write("Hello, this is test1 file")
    content = file.read()
    print(content)
    file.close()


# with open("C:\\test\\DETraining\\python-modules\\python_concepts\\files\\test1.txt","a+") as file:
#     file.write("\nThis line is added through append mode")
#     content = file.read()
#     print(content)

# with open("C:\\test\\DETraining\\python-modules\\python_concepts\\files\\test1.txt","r") as file:
#     content  = file.read()
#     print(content)

'''
path from current dir
absolute path
reading a file

'''
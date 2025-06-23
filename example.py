with open("C:\\Users\\vishveshwar\\OneDrive\\New Folder\\python.py\\example.txt","w") as file:
    file.write("hello world")

with open("C:\\Users\\vishveshwar\\OneDrive\\New Folder\\python.py\\example.txt","r") as file:
    content = file.read()
    print(content)

with open("C:\\Users\\vishveshwar\\OneDrive\\New Folder\\python.py\\example.txt","a+") as file:
    file.write("\nthis is my new file to append a file")
    content = file.read()
    print(content)


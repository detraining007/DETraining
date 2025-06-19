def create_file(filename):
    with open(filename,"w") as file:
        file.write("This is a New File.")
        file.close()

def read_file(filename):
    try:
        with open(filename,"r") as file:
            content=file.read()
            print(content)
            file.close()
    except FileNotFoundError:
        print("File Not Found")

def append_to_file(filename,content):
    with open(filename,"a") as file:
        file.write("This is a New line.")
        file.close()
c=['create','read','append']
# n=input("Enter which Mode do you want..(create/read/append):")
while True:
        n=input("Enter which Mode do you want..(create/read/append/exit):")
        if n=="create":   
            create_file("example.txt")  
        elif n=="read":
            read_file("example.txt")
        elif n=="append":
            append_to_file("example.txt","\n This is new line ")
        elif n=="exit":
            print("Exit the programm")
            break
        else:
            print("Invalid Mode,Enter correct Mode")
            
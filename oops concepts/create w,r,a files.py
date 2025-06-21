
def create_file(filename):
    with open(filename, "w") as file:
        file.write("this is new file")

def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
    

def write_file(filename):
    with open(filename, "w") as file:
        file.write("this is new file")


def append_file(filename):
    with open(filename, "a") as file:
        file.write("this is new file") 

if __name__ == "__main__": 
    while True:
        print("1. create file")
        print("2. read file")
        print("3. write file")
        print("4. append file")
        print("5. exit")
        choice= input("enter your choice(1/2/3/4/5):")
        if choice == "1":
            filename = input("enter file name:")
            create_file(filename)
        elif choice == "2":
            filename = input("eneter file name to read:")
            read_file(filename)
        elif choice == "3":
            filename = input("eneter file name to write:")
            write_file(filename)
        elif choice == "4":
            filename = input("enter file name to append:")
            append_file(filename)
        elif choice == "5":
            print("exiting.")
            break
        else:
            print("invalid choice, please try again.")

        
            




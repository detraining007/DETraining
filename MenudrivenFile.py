def write():
    text = input("Enter text to write: ")
    with open("class.txt", "w") as file:
        file.write(text)
            
def append():
    text = input("Enter text to append: ")
    with open("class.txt", "a") as file:
        file.write("\n" + text)
    
def read():
    with open("class.txt", "r") as file:
        content = file.read()
        print(content)
    
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Read file")
        print("2. Write")
        print("3. Append")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            read()
        elif choice == '2':
            write()
        elif choice == '3':
            append()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


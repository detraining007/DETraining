def read_file():
    try:
        with open("exam.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_file():
    try:
        with open("exam.txt", "w") as file:
            file.write("I am doing work")
            print("Content written successfully.")
    except Exception as e:
        print(f"An error occurred while writing: {e}")

def append_to_file():
    try:
        with open("exam.txt", "a") as file:
            file.write("\nThis is a new line")
            print("Content appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending: {e}")

decision = "yes"

while decision.lower() == "yes":
    print("\nMenu:\n1. Read File\n2. Write to File\n3. Append to File")
    try:
        choice = int(input("Enter your choice (1 to 3): "))
        if choice == 1:
            read_file()
        elif choice == 2:
            write_file()
        elif choice == 3:
            append_to_file()
        else:
            print("Please enter a valid choice (1 to 3).")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 3.")

    decision = input("Do you want to continue? (yes/no): ")

print("Thank you for using txt files!")

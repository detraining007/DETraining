def create(n, r):
    with open(r, 'w') as file:
        file.write(n)

def read(r):
    try:
        with open(r, 'r') as file:
            content = file.read()
            print("File Content:", content)
    except FileNotFoundError:
        with open(r, 'w') as file:
            file.write(n)
        

def append(r, n):
    with open(r, 'a') as file:
        file.write(n)

if __name__ == '__main__':
    while True:
        o = input("Enter option: create (c), read (r), append (a), or exit (e): ").lower()
        
        if o == 'c':
            r = input("Enter the filename with extension (e.g., file.txt): ")
            n = input("Enter the content: ")
            create(n, r)
            read(r)
        
        elif o == 'r':
            r = input("Enter the filename with extension: ")
            read(r)
        
        elif o == 'a':
            r = input("Enter the filename with extension: ")
            n = input("Enter the content to append: ")
            append(r, n)
            read(r)
        
        elif o == 'e':
            print("Program ended.")
            break
        
        else:
            print("Invalid option. Try again.")

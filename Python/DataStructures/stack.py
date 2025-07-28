def push_stack():
    n = int(input("Enter a number you want to push"))
    stack.append(n) 
    print("----------------Push in process----------------------------\n" \
    "--------------------Successfully Pushed into Stack-----------------------")
    print("The Stack after pushing:",stack)

def pop_stack():
    stack.pop()
    print("----------------Pop in process----------------------------\n" \
    "--------------------Successfully Poped From the Stack-----------------------")
    print("The Stack after poping the element:",stack)


stack = []

print('''
  ____  _             _              ____            _        ______             
 / ___|| |_ __ _  ___| | __         |  _ \ _   _ ___| |__    / |  _ \ ___  _ __  
 \___ \| __/ _` |/ __| |/ /  _____  | |_) | | | / __| '_ \  / /| |_) / _ \| '_ \ 
  ___) | || (_| | (__|   <  |_____| |  __/| |_| \__ | | | |/ / |  __| (_) | |_) |
 |____/ \__\__,_|\___|_|\_\         |_|    \__,_|___|_| |_/_/  |_|   \___/| .__/ 
                                                                          |_|    
          ''')
if not stack:
    print("Stack is empty")
else:
    print("Stack is:",stack)    

while True:
    choice = int(input("Do you want to push/pop to the stack \n" \
    "Enter 1 for push\n" \
    "Enter 2 for pop:\n"))

    if choice == 1:
        push_stack()
    elif choice == 2:
        pop_stack()
    else:
        print("Enter Right choice")

    still_continue = input("Do you want to continue Y/N").lower()
    if still_continue == "n":
        break
    elif still_continue == "y":
        pass
    else:
        print("Wrong choice!")
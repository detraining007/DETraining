def enqueue_queue():
    n = int(input("Enter a number you want to push"))
    queue.append(n)
    print("----------------Push in process----------------------------\n" \
    "--------------------Successfully Pushed into queue-----------------------")
    print("The queue after pushing:",queue)

def dequeue_queue():
    queue.pop(0)
    print("----------------dequeue in process----------------------------\n" \
    "--------------------Successfully removed From the queue-----------------------")
    print("The queue after removing the element:",queue)


queue = []

print('''
   ___                                                                                                 
 .'   `.                                                                                               
/  .-.  \  __   _   .---.  __   _   .---.                                                              
| |   | | [  | | | / /__\\[  | | | / /__\\                                                             
\  `-'  \_ | \_/ |,| \__., | \_/ |,| \__.,                                                             
 `.___.\__|'.__.'_/ '.__.' '.__.'_/ '.__.'                                                             
 ______           _           ______    _                           _                                  
|_   _ `.        / |_       .' ____ \  / |_                        / |_                                
  | | `. \ ,--. `| |-',--.  | (___ \_|`| |-'_ .--.  __   _   .---.`| |-'__   _   _ .--.  .---.  .--.   
  | |  | |`'_\ : | | `'_\ :  _.____`.  | | [ `/'`\][  | | | / /'`\]| | [  | | | [ `/'`\]/ /__\\( (`\]  
 _| |_.' /// | |,| |,// | |,| \____) | | |, | |     | \_/ |,| \__. | |, | \_/ |, | |    | \__., `'.'.  
|______.' \'-;__/\__/\'-;__/ \______.' \__/[___]    '.__.'_/'.___.'\__/ '.__.'_/[___]    '.__.'[\__) ) 
                                                                                                       
    
          ''')

if not queue:
    print("queue is empty")
else:
    print("queue is:",queue)    

while True:
    choice = int(input("Do you want to push/dequeue to the queue \n" \
    "Enter 1 for push\n" \
    "Enter 2 for dequeue:\n"))

    if choice == 1:
        enqueue_queue()
    elif choice == 2:
        dequeue_queue()
    else:
        print("Enter Right choice")

    still_continue = input("Do you want to continue Y/N").lower()
    if still_continue == "n":
        print("---------------------------------------------------------------------------------------------------")
        print(queue)
        break
    elif still_continue == "y":
        pass
    else:
        print("Wrong choice!")


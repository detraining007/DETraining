class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, key, data):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Key not found.")

    def delete_node(self, key):
        temp = self.head
        if not temp:
            print("List is empty.")
            return

        if temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
        else:
            print("Key not found.")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Found: {key}")
                return
            temp = temp.next
        print("Not found.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Menu-driven part
def menu():
    sll = SinglyLinkedList()
    while True:
        print("\n--- Singly Linked List Menu ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert After Element")
        print("4. Delete Node")
        print("5. Search Element")
        print("6. Display List")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            val = int(input("Enter value to insert at beginning: "))
            sll.insert_at_beginning(val)
        elif choice == '2':
            val = int(input("Enter value to insert at end: "))
            sll.insert_at_end(val)
        elif choice == '3':
            key = int(input("Enter the element after which to insert: "))
            val = int(input("Enter value to insert: "))
            sll.insert_after(key, val)
        elif choice == '4':
            key = int(input("Enter value to delete: "))
            sll.delete_node(key)
        elif choice == '5':
            key = int(input("Enter value to search: "))
            sll.search(key)
        elif choice == '6':
            sll.display()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1-7.")


# Run the menu
menu()

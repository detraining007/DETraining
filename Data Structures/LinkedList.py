class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


class LinkedList(Node):
    def __init__(self, data, next,head,null):
        super().__init__(data, next)
        self.head = head
        self.null = null

      
        







if __name__ == "__main__":
    print("Welcome to linked list Menu")
    linked = input("Please enter the elements: ")
    elements = list(map(int,linked.split()))
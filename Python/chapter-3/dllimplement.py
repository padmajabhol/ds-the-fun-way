class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<-->")
            temp = temp.next
        print("NULL")

dll = DoublyLinkedList()
dll.insertAtTail(1)
dll.insertAtTail(2)
dll.insertAtTail(3)
dll.display()



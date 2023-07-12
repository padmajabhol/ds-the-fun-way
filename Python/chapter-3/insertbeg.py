:class Node():
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class SingleLinkedList():

    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

L = SingleLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4

L.insert_beginning(5)
L.insert_beginning(2)
L.display()






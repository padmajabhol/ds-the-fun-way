class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class SingleLinkedList():
    def __init__(self):
        self.head: Node | None = None

    def insertend(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne


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

L.insertend(60)
L.display()


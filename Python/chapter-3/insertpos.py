class Node():

    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class SingleLinkedList():

    def __init__(self):
        self.head: Node | None = None

    def insert_pos(self, pos, data):
        np = Node(data)
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
        #np.data = data
        np.next = temp.next
        temp.next = np

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
L.insert_pos(2, 24)
L.display()

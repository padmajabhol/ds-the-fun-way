class Node():
    def __init__(self, data):
        self.data: Node | None = data
        self.prev: Node | None = None
        self.next: Node | None = None

class DLL:
    def __init__(self):
        self.head: Node | None = None

    def insertionB(self, data):
        n = Node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

    def insertionE(self, data):
        n = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        n.prev = temp
        temp.next = n

    def insertionPOS(self, pos, data):
        n = Node(data)
        temp = self.head
        for _ in range(1, pos - 1):
            temp = temp.next
        n.next = temp.next
        n.prev = temp
        temp.next = n
        temp.next.prev = n


    def display(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end="")
                temp = temp.next

L = DLL()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n2.prev = n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3
n4 = Node(40)
n3.next = n4
n4.prev = n3
L.insertionB(5)
L.insertionE(50)
L.insertionPOS(4, 35)
L.display()

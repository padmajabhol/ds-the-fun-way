class Node():
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class SLL():
    def __init__(self):
        self.head: Node | None = None

    def insertBeg(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def insertEnd(self, data):
        n = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n

    def insertPOS(self, pos, data):
        n = Node(data)
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
        n.next = temp.next
        temp.next = n

    def deleteB(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def deleteE(self):
        temp = self.head.next
        prev = self.head
        while temp.next:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def deletePOS(self, pos):
        temp = self.head.next
        prev = self.head
        for _ in range(0, pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next


L = SLL()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
L.insertBeg(5)
L.insertPOS(3, 35)
L.insertEnd(40)
L.deleteB()
L.deleteE()
L.deletePOS(2)
L.display()


class Node():
    def __init__(self, data):
        self.data: Node | None = data
        self.prev: Node | None = None
        self.next: Node | None = None

class DLL:
    def __init__(self):
        self.head: Node | None = None

    def deleteB(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def deleteE(self):
        temp = self.head.next
        before = self.head
        while temp.next:
            temp = temp.next
            before = before.next
        temp.prev = None
        before.next = None

    def deletePOS(self, pos):
        temp = self.head.next
        before = self.head
        for _ in range(1, pos - 1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None

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
n5 = Node(50)
n4.next = n5
n5.prev = n4
#L.deleteB()
#L.deleteE()
L.deletePOS(3)
L.display()

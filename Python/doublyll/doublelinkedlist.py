class Node():
    def __init__(self, data):
        self.data: Node | None = data
        self.prev: Node | None = None
        self.next: Node | None = None

class DLL:
    def __init__(self):
        self.head: Node | None = None

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
n4.prev = n3
n3.next = n4
L.display()

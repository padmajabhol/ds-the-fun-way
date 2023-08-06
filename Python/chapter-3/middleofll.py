import math
class Node():
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class SingleLinkedList():

    def __init__(self):
        self.head: Node | None = None

    def middle(self):
        length = 0
        temp = self.head

        while temp:
            length = length + 1
            temp = temp.next

        mid_idx = math.ceil(length/2)

        if length % 2 == 0:
            mid_idx = mid_idx + 1

        mid_node = self.head

        for _ in range(mid_idx - 1):
            mid_node = mid_node.next
        return mid_node.data

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
L.display()
print(L.middle())


class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class LinkedList():

    def __init__(self):
        self.head: Node | None = None
    
    def delete_b(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
    
    def delete_e(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delete_pos(self, pos):
        temp = self.head.next
        prev = self.head
        for _ in range(0, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def display(self):
        if self.head is None:
            print("LL is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next


L = LinkedList()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5
n6 = Node(60)
n5.next = n6
#L.delete_b()
#L.delete_e()
L.delete_pos(3)
L.display()

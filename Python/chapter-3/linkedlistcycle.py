class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class LinkedList:

    def __init__(self):
        self.head: Node | None = None

    def cycle(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


L = LinkedList()
n1 = Node(20)
L.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n4.next = n2

print(L.cycle())

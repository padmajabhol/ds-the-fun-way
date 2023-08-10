class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def Solution(self, l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data > l2.data:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next

        if not l1:
            tail.next = l2
        else:
            tail.next = l1

        self.head = dummy.next


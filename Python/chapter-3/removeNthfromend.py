class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def Solution(self, n):
        slow, fast = self.head, self.head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return self.head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next


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
L.Solution(2)
L.display()


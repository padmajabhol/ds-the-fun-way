class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

#node1 = Node(10)
#print(node1)

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def display(self):
        if self.head == None:
            print("LinkedList is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next


l = LinkedList()
n = Node(10)
l.head = n
n1 = Node(20)
l.head.next = n1
l.display()

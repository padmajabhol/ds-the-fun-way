class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

def deleteNode(n):
    n.data = n.next.data
    n.next = n.next.next

def display(head):
    curr = head

    while curr:
        print(curr.data, "-->", end=" ")
        curr = curr.next
    print("None")

node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node6 = Node(7)
node1.next = node3
node3.next = node5
node5.next = node6

new_ll = deleteNode(node3)

display(node1)


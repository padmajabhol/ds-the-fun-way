class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

def mergeTwoSortedList(l1, l2):
    dummy = Node(None)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if not l1:
        tail.next = l2
    else:
        tail.next = l1

    return dummy.next

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node1.next = node3
node3.next = node5

# List 2: 2 -> 4 -> 6
node2 = Node(2)
node4 = Node(4)
node6 = Node(6)
node2.next = node4
node4.next = node6

# Merge and print merged sorted linked list
merged_head = mergeTwoSortedList(node1, node2)
print("Merged sorted linked list:")
display(merged_head)

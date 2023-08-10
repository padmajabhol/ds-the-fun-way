class Node:
    def __init__(self, value):
        self.value: Node | None = value
        self.next: Node | None = None

def find_intersection(head1, head2):
    visited = set()
    
    # Traverse the first linked list and add nodes to the set
    current = head1
    while current:
        visited.add(current)
        current = current.next
    
    # Traverse the second linked list and check for intersection
    current = head2
    while current:
        if current in visited:
            return current.value
        current = current.next
    
    return None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

# List 2: 7 -> 8 -> 3
node7 = Node(7)
node8 = Node(8)
node7.next = node8
node8.next = node3

# Find intersection and print common value
intersection = find_intersection(node1, node7)
if intersection is not None:
    print("Intersection found at:", intersection)
else:
    print("No intersection found.")

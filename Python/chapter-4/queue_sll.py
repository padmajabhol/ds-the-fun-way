class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class Queue:
    def __init__(self):
        self.front: Node | None = None
        self.rear: Node | None = None
    def enqueu(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeu(self):
        if self.front is None:
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def front_peek(self):
        return self.front.data if self.front else None

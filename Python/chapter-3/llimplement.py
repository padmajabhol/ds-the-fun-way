class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, data):
        current = self.head
        while current:
            if data == current.data:
                return True
            current = current.next
        return False

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_pos(self, data, pos):
        new_node = Node(data)
        if not self.head:
            if pos == 1:
                self.head = new_node
                return
            return
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_beginning(self):
        if not self.head:
            return
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head.next
        prev = self.head
        while curr.next is not None:
            curr = curr.next
            prev = prev.next
        prev.next = None

    def delete_pos(self, pos):
        if not self.head:
            return
        if not self.head.next:
            return
        prev = self.head
        curr = self.head.next
        for _ in range(pos - 1):
            curr = curr.next
            prev = prev.next
        prev.next = curr.next
        curr.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, "-->", end=" ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.insert_beginning(0)
linked_list.insert_pos(2.5, 3)
linked_list.insert_end(5)
linked_list.delete_beginning()
linked_list.delete_end()
linked_list.display()
print(linked_list.search(2))

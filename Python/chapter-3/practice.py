class Node():
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_b(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_e(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_pos(self, data, pos):
        np = Node(data)
        temp =self.head
        for _ in range(pos - 1):
            temp = temp.next
        np.next = temp.next
        temp.next = np
       
    def del_b(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def del_e(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def del_pos(self, pos):
        temp = self.head.next
        prev = self.head
        for _ in range(0, pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def display(self):
        if self.head == None:
            print("None")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

l = LinkedList()
n = Node(10)
l.head = n
n2 = Node(20)
n.next = n2
n3 = Node(30)
n2.next = n3
l.display()



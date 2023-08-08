class BSTN:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add in left node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTN(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTN(data)

    def in_order_traversal(self):
        elements = []
        
        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    root = BSTN(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = build_tree(numbers)
print(numbers_tree.in_order_traversal())


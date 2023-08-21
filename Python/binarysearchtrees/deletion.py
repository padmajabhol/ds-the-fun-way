class BSTN:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
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
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            self.right.find_max()

    
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            self.left.find_min()

    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            min_val = self.right.find_min()
            #put min_val in current node
            self.data = min_val
            #delete min val
            self.right = self.right.delete_node(min_val)
        
def build_tree(elements):
    root = BSTN(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
numbers_tree.delete_node(20)
print(numbers_tree.in_order_traversal())

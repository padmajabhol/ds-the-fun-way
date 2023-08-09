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

    def post_order(self):
        elements = []

        #visit left node
        if self.left:
            elements += self.left.post_order()

        #visit right node
        if self.right:
            elements += self.right.post_order()

        elements.append(self.data)

        return elements

    def pre_order(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        return elements

def build_tree(elements):
    root = BSTN(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = build_tree(numbers)
print(numbers_tree.pre_order())
print(numbers_tree.post_order())

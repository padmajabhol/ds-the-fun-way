class BSTN: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #left node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTN(data)
        else:
            #right node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTN(data)

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def buildTree(elements):
    root = BSTN(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = buildTree(numbers)
print(numbers_tree.search(9))

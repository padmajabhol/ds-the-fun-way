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

    def cal_sum(self):
        if self.left is None:
            left_sum = 0
        else:
            left_sum = self.left.cal_sum()

        if self.right is None:
            right_sum = 0
        else:
            right_sum = self.right.cal_sum()

        return self.data + right_sum + left_sum

def build_tree(elements):
    root = BSTN(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = build_tree(numbers)

print(numbers_tree.cal_sum())

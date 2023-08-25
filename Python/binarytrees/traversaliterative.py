class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None

def pre_order(root):
    if root is None:
        return

    stack = []
    result = []
    stack.append(root)

    while stack:
        root = stack.pop()
        result.append(root.val)

        if root.right is not None:
            stack.append(root.right)

        if root.left is not None:
            stack.append(root.left)

    return result

def in_order(root):
    if root is None:
        return None

    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def post_order(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        root = stack1.pop()
        stack2.append(root)

        if root.left is not None:
            stack1.append(root.left)
        if root.right is not None:
            stack1.append(root.right)

    result = []
    while stack2:
        result.append(stack2.pop().val)
    return result



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(pre_order(root))
print(in_order(root))
print(post_order(root))

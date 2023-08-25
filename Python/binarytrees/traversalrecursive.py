class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

def preorder_traversal(node):
    if node is not None:
        print(node.val, end=" ")  
        preorder_traversal(node.left)  
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.right)
        postorder_traversal(node.left)
        print(node.val, end=" ")

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Preorder traversal:")
preorder_traversal(root)

print("In-order traversal:")
inorder_traversal(root)

print("Post-order traversal:")
postorder_traversal(root)

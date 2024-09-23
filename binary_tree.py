class TreeNode:

    def __init__(self, data: int):
        self.data = data
        self.right = None
        self.left = None


# Inorder traversal
def inorder_traversal(root: TreeNode):
    if root is not None:
        inorder_traversal(root.left)
        print(f'{root.data}')
        inorder_traversal(root)

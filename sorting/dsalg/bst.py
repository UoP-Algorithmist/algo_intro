"""
Binary Search Tree
"""


class BinarySearchTree:

    def __init__(self):
        self.node = None

    def insert(self, node):
        pass

    def insert_helper(self, root, node):
        data : int = node.data
        if root == None:
            root = node
            return root
        pass

    def display(self):
        pass

    def display_helper(self, root):
        pass

    def search(self, data: int):
        pass

    def search_helper(self, root):
        pass

    def remove(self, data: int):
        pass

    def remove_helper(self, root, data):
        return None

    def successor(self, root):
        return 0

    def predecessor(self, root):
        pass


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
